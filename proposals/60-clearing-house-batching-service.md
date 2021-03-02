# Filecoin Clearing House / Batching Service protocol

Authors: @rvagg

Initial PR: https://github.com/protocol/web3-dev-team/pull/60

## Purpose &amp; impact 

#### Background &amp; intent

_Describe the desired state of the world after this project? Why does that matter?_

* Small deals are hard, and economically unattractive for miners; anecdotally, with current costs, attractive deals are in the order of 16 GiB for standard and 4 GiB for FIL+
* Many use cases involve parties with _only_ small deals to make and little opportunity to batch their own data
* Dealing with fr32 padding combined with needing to have deals be power-of-two sized will generally lead to waste on the client side (e.g. [see this table for optimal deal sizes](https://github.com/filecoin-project/filecoin-docs/issues/705#issuecomment-787618483))
* The deal-making latency is quite large, in the order of 12-24 hours for many deals to be completed and sealed
* Deals require relationships with miners, the overhead of acquiring and maintaining relationships is a negative for developers building on Filecoin
* The overhead of managing redundancy, monitoring deal-lifecycle, renewing deals, etc. is a negative for developers building on Filecoin

Batching deals to achieve optimal deal size for miners should enable a better matching of incentives between client and miner. Batching can either be done at the application layer, or it could be done as a service, aggregated across many applications. A batching service **"protocol"** could define a standard API and workflow that could be adopted by layer 1 ecosystem partners and present a common interface to application developers and a simpler set of concerns and rules required to store assets on Filecoin.

This proposal is for developing a protocol and an operational reference implementation.

* The batching service is responsible for making the deals direct with miners. Deals would be large in size, ideally 16 GiB or 32 GiB and would be FIL+.
* Users of the service only need to establish a relationship with the batching service, not with miners (for storage, retrieval is out of scope for this initial proposal).
* Users make **micro-deals** via the batching service, depositing FIL with the service in batches to be consumed in small amounts for each deal.
* Users submit data via an API or IPFS (or other means) and the data is placed in a queue.
* The batching service aggregates enough data to fit into an optimal deal size, pre-determined for the service, perhaps with a compromise where it will make smaller deals when it hasn't received enough data in a certain number of hours.
* The same process is repeated for all micro-deals in the queue, repeating for each micro-deal until the number of replicas is satisfied.
* The deal cost is deducted pro-rata from each micro-deal's FIL balance.

The aggregated data will need to be packed into a complete DAG. So an IPLD data structure (such as [Vector](https://specs.ipld.io/data-structures/vector.html)) will need to address it all. For each storage deal with a miner, each micro-deal could be addressed by a deal ID (piece CID?) and a selector to their data. Retrieval will depend on being able to retrieve by CID+Selector ([depends on #22](https://github.com/protocol/web3-dev-team/pull/22)). Replicas will have different CID+Selector due to different Piece CID & packing structure.

Some deployment options:

* The service could be used for a single-user, where it's an in-house service standing between an application and Filecoin, not needing to aggregate data with other users but simply batching up local data and storing it without needing that logic in the application itself.
* The service could be deployed as a profit-making exercise for the hoster who takes a small % of the FIL.

This proposal should be initially scoped to include only an MVP, which could be limited to:

* Submission of data via API - no user identification or FIL required - service responds with a micro-deal identifier
* Deal batching & packing (no replicas)
* Deal making
* Keeping track of deals & their constituent micro-deals so the user can request status & storage details

The MVP would prove the concept with a concrete implementation that we can host and allow us to shape the API and workflow for the beginings of a protocol spec.

#### Assumptions &amp; hypotheses

_What must be true for this project to matter?_

* The web3 stack (Filecoin in particular) would be well served by a well defined protocol for batching services that are able to aggregate data and make deals on behalf of end users/developers
* That definition of such a protocol and reference implementation(s) is not going to cause channel-conflict with existing ecosystem partners who are working in this area (e.g. Powergate) but may enhance their offerings by standardising an interface and workflow for batching

#### User workflow example

_How would a developer or user use this new capability?_

* Create relationship with batching service - signup using DID of some form - get an API key
* Deposit FIL with the service to be consumed over micro-deals made
* Submit micro-deals via an API
  * Either uploading data directly or via IPFS CID
  * Set maximum FIL for the micro-deal (or accept what the service needs to use)
  * Set initial replica count
  * Receive an identifier for the micro-deal to use for later reference
* Check micro-deal status via API

An MVP would trim this down to remove user identification, FIL handling and replicas.

#### Impact

_How would this directly contribute to web3 dev stack product-market fit?_

#### Leverage

_How much would nailing this project improve our knowledge and ability to execute future projects?_

#### Confidence

_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

## Project definition

#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

#### What does done look like?

_What specific deliverables should completed to consider this project done?_

####  What does success look like?

_Success means impact. How will we know we did the right thing?_

#### Counterpoints &amp; pre-mortem

_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

* This places an intermediate layer between miner and client which introduces potential safety and reputational concerns. A miner can't do a plain filter by CID in this mechanism since the actual data CID will be buried inside the deal (unless Lotus looks for filtered CIDs deep inside the DAG?). A batching service instance would have to have a relationship with its miners and would offload some of the filtering requirements. So miners needing baseline guarantees about content would need to ensure the batching service they deal with imposes that on clients.
* There may be concerns with adjacent content inside single deals if your content is places next to objectionable content. I'm not sure how this plays out, but CID+selector where you manually adjusting the selector slightly gives you someone else's content might have unfortunate side-effects?

#### Alternatives

_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

#### Dependencies/prerequisites

* [#22](https://github.com/protocol/web3-dev-team/pull/22) for retrieval of small DAG subset by selector

#### Future opportunities

## Required resources

#### Effort estimate

<!--T-shirt size rating of the size of the project. If the project might require external collaborators/teams, please note in the roles/skills section below). 
For a team of 3-5 people with the appropriate skills:
- Small, 1-2 weeks
- Medium, 3-5 weeks
- Large, 6-10 weeks
- XLarge, >10 weeks
Describe any choices and uncertainty in this scope estimate. (E.g. Uncertainty in the scope until design work is complete, low uncertainty in execution thereafter.)
-->

#### Roles / skills needed

<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->
