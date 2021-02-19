# Free Retreival via IPFS

Authors: [@alanshaw](https://github.com/alanshaw)

Initial PR: https://github.com/protocol/web3-dev-team/pull/52

Problems Addressed:

* Data that has been stored successfully is not guaranteed to be retrievable. (P1)
* IPFS users can’t pin their data to Filecoin. (P1)

<!--
This template is for a proposal/brief/pitch for a significant project to be undertaken by a Web3 Dev project team.
The goal of project proposals is to help us decide which work to take on, which things are more valuable than other things.
-->
<!--
A proposal should contain enough detail for others to understand how this project contributes to our team’s mission of product-market fit
for our unified stack of protocols, what is included in scope of the project, where to get started if a project team were to take this on,
and any other information relevant for prioritizing this project against others.
It does not need to describe the work in much detail. Most technical design and planning would take place after a proposal is adopted.
Good project scope aims for ~3-5 engineers for 1-3 months (though feel free to suggest larger-scoped projects anyway). 
Projects do not include regular day-to-day maintenance and improvement work, e.g. on testing, tooling, validation, code clarity, refactors for future capability, etc.
-->
<!--
For ease of discussion in PRs, consider breaking lines after every sentence or long phrase.
-->

## Purpose &amp; impact 
#### Background &amp; intent
_Describe the desired state of the world after this project? Why does that matter?_
<!--
Outline the status quo, including any relevant context on the problem you’re seeing that this project should solve. Wherever possible, include pains or problems that you’ve seen users experience to help motivate why solving this problem works towards top-line objectives. 
-->

Miners that want to allow free retrieval of content make it available to IPFS nodes.

Currently in Filecoin, users can make deals of 0-n FIL for _storing_ data on a miner. _Retrieving_ data from the miner costs 0-n FIL per retrieval at the miner's discretion.

This project caters for the situation where miners wish to earn exclusively from storage deals or wish to offer storage _and_ retrieval **for free**, without having to setup or run additional infrastructure.

Since Lotus is built on libp2p, there should be no issue enabling protocols that IPFS uses to allow exchange of data deemed as free to access.

Distributing data stored on Filecoin via IPFS is preferable for many reasons.

#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->

* Miners are currently able to allow free retrievals.
* Miners exist that want to allow free retrievals.
* IPFS is a desired means for retrieving data stored in Filecoin.

#### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->

A miner would add a configuration option to their Lotus node that allows any data stored to be accessible via IPFS if the retrieval cost for that data is 0 FIL. It would be sent to `true` by default.

For a possible stage 2, this could be in the deal contract i.e. the miner _must_ allow access for free and it _must_ be made available to IPFS nodes.

As a proof-of-concept, we'd like to be able to open a bitswap session with a Lotus node and exchange data from a current deal.

#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

<!--
Explain how this addresses known challenges or opportunities.
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

This would bridge the Filecoin -> IPFS use case for free-to-retrieve data in a simple way.

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

<!--
Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

Ideally this would unblock retrieval problems for companies (pinning services) wishing to store IPFS data on Filecoin.

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

<!--Explain why this rating-->

High

We know multiple companies that wish to use Filecoin as the storage provider for IPFS data. We know that many have been unsuccessful so far in bridging the gap.

## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

Scoped here is a possible proof-of-concept that can be taken forward if proven to be useful.

1. Enable Bitswap protocol used by IPFS in Lotus.
1. Add data from deals to a separate blockstore used by bitswap.
1. When bitswap sessions are established, check cost of retrieval for CID and allow bitswapping if free.
1. (Optional) When deal expires, unpin the root CID from the blockstore.
1. Demonstrate to everyone.

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

* PoC is available.
* Demonstration recorded.

####  What does success look like?
_Success means impact. How will we know we did the right thing?_

<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

* PoC is accepted and a robust solution is added to Lotus and released.
* 1 or more collabs run Lotus with this option enabled.

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

* Enabling bitswap on a Lotus node might increase memory/CPU usage to the extent that it would affect it's normal operations.

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

Attacking this from the other angle and upgrading IPFS with abilities to store and retrieve from Filecoin. e.g. [myel.network](https://myel.network/).

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

None.

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->

Publishing CIDs on the DHT.

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

Small

#### Roles / skills needed
<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->

* 1-2 developers with golang experience
