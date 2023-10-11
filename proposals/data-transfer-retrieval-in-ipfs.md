# Arbitrary Retrieval In IPFS via Data Transfer

Authors: @hannahhoward

Initial PR: https://github.com/protocol/web3-dev-team/pull/57

Problems Addressed:

- Data that has been stored successfully is not guaranteed to be retrievable. (P1)

## Purpose &amp; impact 

#### Background &amp; intent
_Describe the desired state of the world after this project? Why does that matter?_

This proposal describes a comprehensive solution to allow IPFS users to retrieve data from Filecoin and other external services in IPFS. The initial project would support free retrievals but would include extensable interfaces for paid retrievals via Filecoin retrieval protocol or other 3rd party protocols.

It has 3 primary technical components:
- The ability to add records to the IPFS DHT that specify retrievals that must be fetched through other protocols such as Filecoin retrieval
- The [data transfer module](https://github.com/filecoin-project/go-data-transfer) inside of IPFS is used to support retrieval protocols other than existing IPFS bitswap fetch.
- An RPC API (HTTP? JSON-RPC? tbd.) to generate data transfer vouchers to power a paid retrieval in the future. 

The proposal is an alternative to [Proposal: Free retrieval via IPFS ](https://github.com/protocol/web3-dev-team/pull/52). This design supports a much wider set of use cases, but at the same time requires some breaking changes (modifying the IPFS DHT or creating a new one) and may require greater additional cost to develop (in time and resources)

#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->

- Miners that want to allow free retrieval of content are MORE likely to make it available to the IPFS network if doing so requires minimal changes to their existing operations

- IPFS users would like to retrieve from Filecoin ideally without ever leaving IPFS or running any Filecoin software on their computer

- The primary existing customers for retrieval of data ARE IPFS users. IPFS users don't want a seperate discovery mechanism for Filecoin retrieval -- they want to use what already exists

- There is a market for paid retrieval within IPFS eventually and we should have a path to support this.

#### User workflow example
_How would a developer or user use this new capability?_

Example: Retrieval via go-data-transfer for free retrievals

1. I negotiate an agreement to put data in a external service such as Filecoin outside of IPFS. I complete a deal to store the data

2. The external service, upon completion, posts a record in the IPFS DHT for the CID of pinned data that contains both the peer address where the data is stored, a flag indicating this is "generic free retrieval", and a data transfer voucher needed to initiate a free retrieval via `go-data-transfer`

3. For retrieval, upon querying the DHT, the IPFS client sees the the record has a 'generic free retrieval' data transfer voucher, and instead of using standard bitswap fetching, initiates a transfer via the data transfer protocol, and fetches data this way.

Future Example: Paid Filecoin retrieval with IPFS & Lotus Lite client on same computer

1. I make a deal with a miner through my lotus lite client to store some data. When my deal is done, the miner OR client can advertise the peer address and retrieval parameters in the IPFS dht 

2. IPFS clients allow other software to register as providers for different types of paid retrievals. Each provider must offer an RPC endpoint that satisfys an API specification to generate data transfer vouchers for a paid retrieval. Lotus Lite is registered as the provider for paid retrievals via Filecoin.

3. The IPFS Client sees a record for paid Filecoin retrieval in the DHT. IPFS communicates with Lotus Lite via RPC to generate parameters for a paid retrieval deal. The IPFS client then initiates a data transfer request. As needed, further RPC calls are made to Lotus Lite to generate additional vouchers.

Future example: Custom paid retrieval via any paid retrieval format

1. I negotiate and store data with a custom retrieval provider with their own designated retrieval protocol. (note: do we need to establish a global table of some sort?)

2. I run my custom providers software which offers an RPC endpoint that satisfys the API specification to generate data transfer vouchers for a paid retrieval. The software registers itself with IPFS as the provider for the custom protocol

3. The IPFS Client sees a record for paid custom protocol in the DHT. IPFS communicates with the providers software via RPC to generate parameters for a paid retrieval deal. The IPFS client then initiates a data transfer request. As needed, further RPC calls are made to providers software to generate additional vouchers.

#### Impact
_How directly important is the outcome to web3 dev stack product-market fit?_

🔥🔥🔥

This would provide a clear and comprehensive story for bridging Filecoin -> IPFS. It would do so without forcing existing miners to make any changes to their operations, other than posting records in a DHT. 

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

🎯🎯🎯

While the initial project would only aim to support only the free-retrieval use case, there's a clear path to all kinds of paid retrievals. It would help us flesh out key issues around discovery for retrievals. (for example extending what goes in the IPFS DHT, learning how to decide between free or paid retrieval).

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

High

We know multiple companies that wish to use Filecoin as the storage provider for IPFS data. We know that many have been unsuccessful so far in bridging the gap.

## Project definition
#### Brief plan of attack

1. We work with libp2p & IPFS stewards to come up with design for how we put filecoin retrieval records in the DHT. Note: I have used language so far that assumes these records will go in the IPFS DHT itself, but it may make sense to first work on composable content routing so that records might come from somewhere other than the DHT.

2. We work out a way to get these DHT records posted as part of the deal making process. (this might be the miner directly, or dealbots posting to the DHT via Hydra)

3. We add the data transfer module to IPFS.

4. We implement a negotiation mechanism for deciding between retrieval via data transfer vs traditional bitswap in IPFS (note: this requires significant design)

5. We design the data transfer RPC API in concert with those who are looking at providing alternate mechanisms of paid retrieval

<!--Briefly describe the milestones/steps/work needed for this project-->

#### What does done look like?
_What specific deliverables should completed to consider this project done?_
Done is when you can complete retrieval from Filecoin in IPFS and a spec exists for building future paid retrievals

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
