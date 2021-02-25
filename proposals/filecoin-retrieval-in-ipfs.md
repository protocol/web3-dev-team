# Filecoin Retrieval In IPFS

Authors: @hannahhoward

Initial PR: https://github.com/protocol/web3-dev-team/pull/57

Problems Addressed:

- Data that has been stored successfully is not guaranteed to be retrievable. (P1)
- IPFS users can’t pin their data to Filecoin. (P1)

## Purpose &amp; impact 

#### Background &amp; intent
_Describe the desired state of the world after this project? Why does that matter?_

This proposal describes a comprehensive solution to allow IPFS users to pin data in filecoin and make it available for retrieval. The initial project would support free retrievals via Filecoin retrieval protocol but would include extensable interfaces for paid retrievals via default Filecoin retrieval protocol or 3rd party protocols.

It has 4 primary technical components, one existing and 3 new:
- The IPFS remote pinning API (existing)
- The ability to add records to the IPFS DHT that specify retrievals that must be fetched through other protocols such as Filecoin retrieval
- The [data transfer module](https://github.com/filecoin-project/go-data-transfer) inside of IPFS is used to support retrieval protocols other than existing IPFS bitswap fetch. Non-chain based Filecoin retrieval code from go-fil-markets is part of IPFS to support free retrieval.
- A plugin system to generate data transfer vouchers to power a paid retrieval in the future. 

The proposal is an alternative to [Proposal: Free retrieval via IPFS ](https://github.com/protocol/web3-dev-team/pull/52). This design supports a much wider set of use cases, but at the same time requires some breaking changes (modifying the IPFS DHT or creating a new one) and may require greater additional cost to develop (in time and resources)

#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->

- Miners that want to allow free retrieval of content are MORE likely to make it available to the IPFS network if doing so requires minimal changes to their existing operations

- IPFS users would like to pin content and retrieve from Filecoin ideally without ever leaving IPFS or running any Filecoin software on their computer

- The primary existing customers for retrieval of data ARE IPFS users. IPFS users don't want a seperate discovery mechanism for Filecoin retrieval -- they want to use what already exists

- There is a market for paid retrieval within IPFS eventually and we should have a path to support this

#### User workflow example
_How would a developer or user use this new capability?_

Example: IPFS pinning with Filecoin, using remote pinning API and free retrieval

1. As an IPFS user who wants to pin data with filecoin, I negotiate an agreement to pin data in Filecoin with a pinning service out of band in exchange for an access token (i.e. I pay them through their website for X GB of filecoin pinning at Y Price). 

2. I use the remote pinning API from the IPFS command line to pin some data with them.

3. The pinning service initiates and completes a filecoin deal to store the data

4. The pinning service, upon completion posts a record in the IPFS DHT for the CID of pinned data that contains both the peer address for the miner and also flag to indicate it requires filecoin retrieval (and potentially also includes the PieceCID?).

5. For retrieval, upon querying the DHT, the IPFS client sees the the record is a filecoin retrieval record, and instead of using standard bitswap fetching, switches over to proposing a free retrieval via the data transfer protocol to the miner, and completes the retrieval this way.

Future Example: Paid retrieval with IPFS & Lotus Lite client on same computer

1. I make a deal with a miner through my lotus lite client to store some data. When my deal is done, the miner OR client can advertise the peer address and retrieval parameters in the IPFS dht 

2. The IPFS Client sees a record for paid Filecoin retrieval in the DHT and uses the paid Filecoin retrieval plugin to talk to the Lotus Lite HTTP api to generate parameters for a paid retrieval deal. The IPFS client then initiates a data transfer request. As needed, the plugin calls out to Lotus Lite HTTP API to generate additional vouchers.

Future example: Custom retrieval payment system for a "retrieval miner" using a custom payment system

1. I negotiate out of band with a custom paid retrieval provider an agreement to retrieve data.

2. I use the IPFS Pinning API to request to pin data. The miner stores the data in Filecoin as backup, and to prove it's being stored, but then distributes several copies to it's CDN pinning network and advertises all records in the IPFS DHT as paid retrievals that use its custom protocol.

3. To retrieve, I use the information in the DHT and a plugin supplied by the provider to generate vouchers for a data transfer with one of their miners close to me. 

#### Impact
_How directly important is the outcome to web3 dev stack product-market fit?_

🔥🔥🔥

This would provide a clear and comprehensive story for bridging Filecoin -> IPFS. It would do so without forcing existing miners to make any changes to their operations, other than posting records in a DHT. 

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

🎯🎯🎯

While the initial project would only aim to support only the free-retrieval use case, there's a clear path to all kinds of paid retrievals. It would help us flesh out key issues around discovery for retrievals. (for example extending what goes in the IPFS DHT, learning how to decide between free or paid retrieval). It should at minimum make things easier for pinning services who want to use Filecoin.

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

High

We know multiple companies that wish to use Filecoin as the storage provider for IPFS data. We know that many have been unsuccessful so far in bridging the gap.

## Project definition
#### Brief plan of attack

1. We work with libp2p & IPFS stewards to come up with design for how we put filecoin retrieval records in the DHT. Note: I have used language so far that assumes these records will go in the IPFS DHT itself, but it may make sense to explore putting them in a seperate DHT that IPFS also has access too.

2. We work out a way in Lotus to get these DHT records posted as part of the deal making process.

3. We add the data transfer module to IPFS and the retrieval portion of go-fil-markets backed by a node interface that errors on chain based requests.

4. We implement a negotiation mechanism for deciding between Filecoin retrieval via data transfer vs traditional bitswap in IPFS (note: this requires significant design). This negotiation happens in the [currently-in-development rewritten go-ipfs fetcher](https://github.com/ipfs/go-fetcher). Alternatively, perhaps data transfer itself becomes the top level interface above the fetcher? 

5. We work with select pinning providers (eg Pinata) to verify we've provided the components for roundtrip pinning to Filecoin from IPFS

6. We design the data transfer plugin API in concert with those who are looking at providing alternate mechanisms of retrieval (note: it's not clear to me if this should be a local plugin system or an HTTP API -- a local plugin can do any kind of custom HTTP communication, but is also harder to install and configure)

<!--Briefly describe the milestones/steps/work needed for this project-->

#### What does done look like?
_What specific deliverables should completed to consider this project done?_
Done is when you can complete a roundtrip pinning / retrieval to Filecoin from IPFS and a spec exists for building future paid retrievals

####  What does success look like?
_Success means impact. How will we know we did the right thing?_
- Well known pinning services begin offering Filecoin based pinning
- Accelerator projects around new kinds of retrieval begin building plugins for paid retrieval

<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_
- A DHT change discussion is a big design discussion, and could take a long time or hit roadblocks. It also could involve breaking changes to the content routing API in Libp2p, which might cause a lot of headaches
- It may turn out to be quite difficult to make smart decisions about when to use Filecoin retrieval vs regular Bitswap. The simple case where data is pinned ONLY in Filecoin and not IPFS is easy to decide on. When its in both, how we decide what to use is not totally clear.
- The long term future of Filecoin retrieval protocol in general is dependent on improvements to proofs that enable faster unsealing or reliable systems for gauranteeing unsealed copies. (i.e. Filecoin Plus)

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

See [Proposal: Free retrieval via IPFS ](https://github.com/protocol/web3-dev-team/pull/52). If all of that proposal's assumptions turn out to be true and it is possible to just have miners throw data in a bitswap accessible blockstore, it is probably the fastest path to baseline filecoin retrieval in IPFS. 

There are as mentioned various variations within this proposal -- building a seperate DHT for Filecoin retrievals as opposed to extending the IPFS DHT, having a data transfer voucher HTTP API Spec as opposed to a local plugin system, etc.

#### Dependencies/prerequisites

This project should commence after the currently in-progress [IPLD in IPFS project](https://github.com/protocol/web3-dev-team/pull/25) as they are hard to do simultaneously.

<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->

- See future examples of workflows for Lotus Lite and custom retrieval

## Required resources

#### Effort estimate

Because of cross-cutting concerns, this is a large project
<!--T-shirt size rating of the size of the project. If the project might require external collaborators/teams, please note in the roles/skills section below). 
For a team of 3-5 people with the appropriate skills:
- Small, 1-2 weeks
- Medium, 3-5 weeks
- Large, 6-10 weeks
- XLarge, >10 weeks
Describe any choices and uncertainty in this scope estimate. (E.g. Uncertainty in the scope until design work is complete, low uncertainty in execution thereafter.)
-->

#### Roles / skills needed

- 1-2 developers work 1 Libp2p steward to design and implement changes to the DHT
- 1 developer working with 1 lotus steward to design and implement optionally posting records to the DHT as part of the Lotus deal making process.
- 2 developers with knowledge of both IPFS transfer, the data transfer module, and go-fil-markets designing and implementing free filecoin retrieval via data transfer in IPFS. Ideally, they would work closely with an IPFS steward.

<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->
