# Lotus Light Mode

Authors: @magik6k

Initial PR: TBD <!-- Reference the PR first proposing this document. Oooh, self-reference! -->

## Purpose &amp; impact
#### Background &amp; intent

Currently, running lotus nodes requires dedicating lots of resources. Users should
be able to talk to the blockchain without validating it fully

#### Assumptions &amp; hypotheses
* Filecoin chain can be followed just by validating blockheaders with bits of previous state safely
* Bitswap is fast enough to support this

#### User workflow example
Instead of syncing a full node from a snapshot (big, ~90G), the client would
start a light node, which would trust state in blockheaders, and follow the chain
just by running basic validation on blockheaders (checking miner power/signatures
using older state we already trust)

#### Impact
Lotus would be much easier to run for non-miner users

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

<!--
Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

<!--Explain why this rating-->


## Project definition
#### Brief plan of attack
* Research what is the secure way to follow the filecoin chain without computing state
* Add a lotus mode which doesn't compute state during sync
* Don't subscribe to pubsub messages
* Identify areas of lotus which may trigger state computation, try to get rid of those

#### What does done look like?
Clients can start interacting with the chain without having to download tens of
gigabytes of data, and having to dedicate significant resources for the node

####  What does success look like?
_Success means impact. How will we know we did the right thing?_

<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

#### Counterpoints &amp; pre-mortem
* Even basic validation of the chain, pulling the state over Bitswap might still be very resource intensive

#### Alternatives
* Other operation modes where we delegate more trust to other nodes

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->

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

Medium

#### Roles / skills needed
<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->

* 1-2 engineers familiar with lotus chain subsystem
* Filecoin consensus knowledge