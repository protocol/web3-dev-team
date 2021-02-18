# Integrate IPLD Prime into go-ipfs

Authors: @hannahhoward, template edit by @mvdan

Initial PR: https://github.com/protocol/web3-dev-team/pull/25

## Purpose &amp; impact 
#### Background &amp; intent
_Describe the desired state of the world after this project? Why does that matter?_

IPLD is the core data model for content addressed data used in our technologies.
It has a [very well defined specification](https://github.com/ipld/specs).
However, only a single library in go -- [go-ipld-prime](https://github.com/ipld/go-ipld-prime) -- implements most major portions of this specification.
Meanwhile a hodge podge of technologies and libraries, many of them officially "deprecated", are actually used to work with IPLD in IPFS and Filecoin, both in Javascript and in Go.
This limits certain use cases of IPFS, and perhaps more importantly, it blocks implementation of a number of capabilities across the web 3 stack due to the limitations of legacy libraries.
Longer writeup of the current state of the IPLD world.

This project aims to integrate go-ipld-prime into go-ipfs, as a first step toward standardizing IPLD usage across the PL stack.

#### Assumptions &amp; hypotheses

* As the foundational data model for our technology stack, the quality of our libraries and technologies for working with IPLD affect the entire web3 stack.
* We’d like to have access to IPLD Selectors or other IPLD querying capabilities across the web3 stack for our own and others development efforts, because they enable a natural representation for addressing individual pieces of data.
* There are external developers who would like to work directly with structured data in our stack, as opposed to serializing to flat files prior to import. Support for structured data in IPFS is immediately useful for them.
* go-ipld-prime is sufficiently mature to be integrated through major portions of the web 3 stack, and remaining sharp edges are most easily ironed out through integration.

#### User workflow example

I am a developer.
I have a set of structured JSON data.
Or, perhaps I have an existing Web2 JSON API.
I want to import that data directly into IPFS.

I can run:

    ipfs dag import users.json

Or perhaps even:

    ipfs dag import  https://api.spacexdata.com/v4/launches/latest

This returns a CID for the data, encoded in a block in CBOR.
I can fetch said block and output as JSON.

Let’s say the CID for our SpaceX json is `QMABCDEF`.
Soon, on another node, I should be able to fetch that data from the CID reference (note that selector pathing is not fully encompassed in this project):

    ipfs dag get QMABCDEF/links/flickr/original/0
    
And per the sample response [here](https://github.com/r-spacex/SpaceX-API),
I’d get back the text `https://live.staticflickr.com/65535/49927519643_b43c6d4c44_o.jpg`.

Eventually, we might choose to recognize http links, download the results, and convert them to MerkleDAG data (either more CBOR data for json or UnixFS for HTML/Gif/PNG).
Now the same query gets back `QMGHIJKL` -- a CID to download the image above of a space shuttle launch!

#### Impact

We have a number of existing users who have structured data they want to put in IPFS.
Currently, they are expending effort to take that data and put it in flat files before importing into IPFS, with almost no query capabilities. 

#### Leverage

This a project whose greatest impact may be unblocking other projects. Among them:

* Faster data transfer in IPFS (we can integrate bitswap and graphsync to speed up transfer, we cannot in the current stack)
* Unlocking greater capabilities in the stack through use of selectors, including to-be-written selectors
* IPLD based databases and graph querying as optimization mechanism
* Standardizing IPLD across the stack including Filecoin (see meta doc above)
* Coherent IPFS and Filecoin retrieval patterns (also needs Filecoin retrieval improvements)
* Almost any effort to support dApps that work with non-static or non-file data

#### Confidence

On the scale: 1 -- Low

Impact: 1 -- We have anecdotal examples of users who are frustrated with their inability to put semantic data into IPFS (todo: collect examples from Eric Myhre, Adin Schmahmann)

Impact 3: Top user request: https://github.com/ipfs/go-ipfs/issues/7909

## Project definition
#### Brief plan of attack

go-IPFS primarily uses legacy IPLD libraries -- go-ipld-format -- in the context of working primarily with UnixFS v1.
Use of IPLD primarily flows through the [`DAGService`](https://github.com/ipfs/go-ipld-format/blob/master/merkledag.go), which sits on the BlockService, which is hardcoded to fetch through Bitswap, among other things.

Several things sit on top of `DAGService` -- most prominently UnixFS.

The first goal here is to get to a go-ipld-prime based `DAGService`, as close in interface to the existing DAGService, so that libraries dependent on this service would require only minimal changes.

A first step is proposing an ipld-prime interface for this revamp’d DAG service, and to write a minimal scaffold translating from that interface to the current implementation.

At that point, two people will continue working within the `dag service -> block service -> bitswap` and plumb through IPLD in that direction, while others will add more IPLD commands to the IPFS command line and handle propagating it to the various top level interfaces.

We can also decide if we want to pursue updating some services that sit on top of `DAGService`.

#### What does done look like?

* P0: I can build IPFS without go-ipld-format
* P1: I can import structured data (following links of generic codecs) directly from the IPFS command line
* P1: structured data is importable and can be queried over the IPFS HTTP API 
* P2: I can query structured data directly from the IPFS command line

####  What does success look like?

* People who have structured data or are looking at dynamic dApps do not leave the web3 ecosystem.
  We see less new custom serialization code into IPFS files.
* We see a growing percentage of gateway & DHT cid activity representing non-unixfs multicodec data.
* We see less community frustration on inability to integrate DAG-JOSE
* People who are considering dynamic dAPPs considers our stack
* Filecoin is open to integrating go-ipld-prime in their codebase

#### Counterpoints &amp; pre-mortem

* People are struggling with static files, particularly in Filecoin, could leave before we can offer these services
* We could find selectors or graphsync are not ultimately that useful a technology for working with structured data, or don’t unlock speed improvements
* The impact of IPLD standardization will be felt strongest when we use go-ipld-prime across the stack.
  We might finish our work in IPFS, but efforts to standardize in Filecoin could get delayed indefinitely by other project priorities.
  This would leave standardization in a slightly better, but still incomplete state.
* We may discover design issues in go-ipld-prime that require significant additional work to make it truly useful

#### Alternatives

* It’s possible we can just provide utilities in IPFS to import structured data and serialize to flat files?
* It’s possible we can unlock some (thought not all) of the blocked projects without porting go-ipfs to go-ipld-prime

#### Dependencies/prerequisites

None, for the time being

#### Future opportunities

* We can continue to develop and expand data querying capabilities with improved selectors, and an effort to serialize selectors for command lines
* We can move go-ipld-prime into the Filecoin stack and VM and reach IPLD standardization across the stack
* See all blocked projects

## Required resources

#### Effort estimate

Large; 6-9 weeks.

#### Roles / skills needed

* Initial 3-weeks: 1-2 developers with IPFS & IPLD knowledge creating the ipld-prime DAG Service and translation layer
* Second 3-weeks: 3-4 developers,
  one group (1-2 devs) plumbing down (integrating in bitswap and go-graphsync),
  one group (1-3 devs) plumbing up (moving UnixFS, IPFS command lines over to new interfaces
* Remaining time: add new IPFS commands to work with structured data
