# Integrate IPLD Prime into go-ipfs

Authors: @acruikshank, @gammazero, @hannahhoward, @mvdan, @willscott
Point Of Contact: @willscott

Initial PR: https://github.com/protocol/web3-dev-team/pull/25

## What work was done?

### Phase 1: introduction of IPLD-Prime under go-merkledag

https://github.com/ipfs/go-ipld-legacy introduces a [implementation](https://github.com/ipfs/go-ipld-legacy/blob/master/node.go#L225) of 
a [`UniversalNode`](https://github.com/ipfs/go-ipld-legacy/blob/master/decode.go#L16) which can serve as a shim satisfying both the old and
new interfaces.

Note: a `format` Node and a `prime` Node doe not map 1:1 - a format node represents the full dag held in one IPFS Block, while prime Nodes are
finer grain.

### Phase 2: [`go-merkledag`](https://github.com/ipfs/go-merkledag/pull/67) is re-factored to internally be powered by IPLD-Prime.

IPLD format nodes and their interaction make common use of the `dagpb` format. This is used within merkledag, and to translate it to
IPLD prime this work finished [go-codec-dagpb](https://github.com/ipld/go-codec-dagpb) to fully represent the semantics of protobufs
used by IPFS.

We then consider what actually happens in go-merkledag.

Merkledag encapsulates 3 distinct interfaces:

* Fetching IPLD nodes by CID, potentially from a local blockstore, or potentially from the network.
* Interaction with the local blockstore - adding, and removing blocks from the store.
* Modification of IPLD nodes, to add files to directories, or change structured data.

These 3 are split into distinct interfaces.

* Fetching is now handled by [go-fetcher](https://github.com/ipfs/go-fetcher)
* Interaction with the local blockstore is now handled by [go-dagwriter](https://github.com/ipfs/go-dagwriter)
* Modification is either done natively through IPLD prime, or continues to occur as before against format nodes through the legacy shim.

### Phase 3: Prime propagates into go-ipfs

* Pathing (how we navigate a DAG to traverse folders) is [updated](https://github.com/ipfs/go-path/pull/34) to directly use the fetcher, rather than the legacy shim.
  * To represent these paths, the UnixFS semantics are interpreted for IPLD-Prime using [go-unixfsnode](https://github.com/ipfs/go-unixfsnode)
* the `ipfs dag put` [command](https://github.com/ipfs/go-ipfs/pull/7995) is updated to use ipld-prime codecs, rather than an unloved registry of `inputenc` encodings
  * This introduces a breaking change in names of codec. `json` and `cbor` previously meant `dag-json` and `dag-cbor` respectively, but htose are now the respective non-dag variants, conforming to expected multicodec registry naming.
* "ipld plugins" for IPFS which previously registered additional `inputenc`'s are removed, and instead this functionality can be achieved by registering an additional ipld-prime codec, which will automatically become available.
* The `api.Dag()` [interface](https://github.com/ipfs/interface-go-ipfs-core/blob/master/coreapi.go#L23) is updated to include direct access to `go-fetcher` access to prime data.

## What work would happen next?

A number of unixfs libraries remain using the legacy shim, and also at some point can transition to the prime interface.
These include:

* https://github.com/ipfs/go-unixfs
* github.com/ipfs/go-ipfs-pinner
* https://github.com/ipfs/go-ipfs-posinfo
* github.com/ipfs/go-ipfs-provider
* github.com/ipfs/go-mfs

They also involve several packages (e.g `fuse`, `tar`, and some of the `core` APIs) within go-ipfs directly.

This work was consiously "out-of-scoped" as it would be beneficial to coordinate it with updates to any semantic changes we hope to introduce to UnixFS,
and to understand if we want to update any of the filesystem interfaces to better work with the recently released golang 1.16 filesystem interfaces.


## What was learned?

### Mutation events could use centralizations

The main mutator seems to be go-unixfs.
go-mfs does use ProtoNodes, but does not seem to mutate them directly.
Note that go-mfs does use the Directory interface.

* [dagutils.Editor](https://pkg.go.dev/github.com/ipfs/go-merkledag/dagutils#Editor)
  * Same operations as those on ProtoNode, but across blocks
  * go-ipfs uses it to import a tar archive into a ProtoNode; [link](https://github.com/ipfs/go-ipfs/blob/8e6358a4fac40577950260d0c7a7a5d57f4e90a9/tar/format.go)
      * Will mentions we could do a tar ipld-prime codec instead?
  * go-ipfs uses it for the Object API's "add link" and "remove link" on ProtoNodes; [link](https://github.com/ipfs/go-ipfs/blob/895b340e08b9473699179d006eb0bd54bfc951f9/core/coreapi/object.go)
  * Seems to not be used anywhere else in all of IPFS?

* [ProtoNode.AddNodeLink](https://pkg.go.dev/github.com/ipfs/go-merkledag#ProtoNode.AddNodeLink)
    * go-unixfs uses it to implement Directory.AddChild; [link](https://github.com/ipfs/go-unixfs/blob/68c015a6f317ed5e21a4870f7c423a4b38b90a96/importer/helpers/dagbuilder.go#L330)
* [ProtoNode.UpdateNodeLink](https://pkg.go.dev/github.com/ipfs/go-merkledag#ProtoNode.UpdateNodeLink)
    * Used nowhere in the ipfs org?
* [ProtoNode.RemoveNodeLink](https://pkg.go.dev/github.com/ipfs/go-merkledag#ProtoNode.RemoveNodeLink)
    * go-unixfs uses it in a Directory.AddChild implementation right before AddNodeLink; [link](https://github.com/ipfs/go-unixfs/blob/68c015a6f317ed5e21a4870f7c423a4b38b90a96/io/directory.go#L146)
        * We could make this redundant
* [ProtoNode.SetLinks](https://pkg.go.dev/github.com/ipfs/go-merkledag#ProtoNode.SetLinks)
    * Initially not part of the plan, but also called directly by some bits of code
    * go-unixfs uses it to implement Directory, as a "remove link by index"; [link](https://github.com/ipfs/go-unixfs/blob/68c015a6f317ed5e21a4870f7c423a4b38b90a96/importer/helpers/dagbuilder.go#L343)


### Translations needed for IPLD Prime
* Accessing data in a node
    * old: go-ipld-format.Node
    * new: go-ipld-prime.Node
    * important discrepancies/distinctions: node in old IPLS = whole block, node in new IPLD = atomic point in data structure
    * compatibility layer: go-ipld-legacy.UniversalNode
* Deserializing data
    * old: go-ipld-format.DecodeNode + go-ipld-format.Register + piecemeal functions (DecodeProtobuf)
    * new: go-ipld-prime.Link.Load + go-ipld-prime.RegisterMulticodecDecoder
    * important discrepency: the Decoder in go-ipld-format defines the typ of node built build, where the decoder in IPLD prime takes a nodeAssembler that determines the node type
    * compatibility layer: go-ipld-legacy.DecodeNode & go-ipld-legacy.RegisterCodec
* Serializing data
    * old: piecemeal functions (go-merkledag.ProtoNode.EncodeProtobuf / go-merkle-dag.ProtoNode.Marshall / go-ipld-cbor.DumpObject)
    * new: go-ipld-prime.LinkBuilder.Build + go-ipld-prime.RegisterMulticodecEncoder
* Special handling of DagPB + Raw
    * old: go-merkledag.ProtoNode + go-merkledag.RawNode
    * new: go-ipld-prime-proto
    * important discrepency: all codecs have specialized node types in old library. Only proto&raw have this in go-ipld-prime proto
    * compatibility layer: see https://github.com/ipfs/go-merkledag/pull/64
* Mutating data
    * old: go-merkleDag.ProtoNode mutation methods (Add/Remove/Update links), go-merkledag.dagutils.Editor (hardcoded to ProtoNode type)
    * new: go-ipld-prime FocusTransform. More work likely needed 
    * *Needs design*
    * important discrepency: all mutation is hard coded to node type (ProtoNode), aiming to keep mutation in ipld-prime generalized
* Building New Nodes
    * old: create blank nodes, use mutation methods
    * new: go-ipld-prime.NodeBuilder/go-ipld-prime.NodeAssembler -- mutation is built on top of NodeBuilder, which is a node creation tool (i.e. functional copy-on-modification approach)
* Storage/Persistence
    * old: go-merkledag.DagService - only implementation of go-ipld-format.DAGService. Confusing because Get Methods are also network transport abstraction
    * new: go-ipld-prime.Loader / go-ipld-prime.Storer -- very lightweight methods for converting ipld.Link -> io.reader/io.writer
* Network fetching high level API
    * old: go-merkledag.DagService.Get, go-merkledag.DagService.GetMany, go-merkledag.NewSession() (for grouping get requests)
    * new: TBD, *needs design*
    * compatbility layer: see https://github.com/ipfs/go-merkledag/pull/64
* Network fetching / local loading abstraction
    * old: go-merkledag.DagService.Get, go-merkledag.DagService.GetMany, go-merkledag.NewSession() (for grouping get requests)
    * new: TBD, *needs design* **Possibly eliminate**
    * compatbility layer: see https://github.com/ipfs/go-merkledag/pull/64
* Network fetching protocols
    * old: none -- bitswap works with blocks without any IPLD knowledge
    * new: graphsync - go implementation hardcoded to ipld-prime
* Graph Traversal
    * old: go-merkledag.FetchGraph / go-merkledag.Walk (whole graph only, supports serial/parallel, implied network fetch for missing local data)
    * new: go-ipld-prime.Focus / go-ipld-prime.Walk (supports selectors, partial traversal, serial only, loader implementation determines network fetch, if any)
    * *Needs Design* parallel traversal? 

