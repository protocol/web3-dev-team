# DeDHT - a DHT for Filecoin Deals

Authors: [@alanshaw](https://github.com/alanshaw)

Initial PR: TBD <!-- Reference the PR first proposing this document. Oooh, self-reference! -->

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

**Discovery of content providers on the Filecoin network without centralized indexes.**

There is currently an unsolved problem of knowing which miner is storing which content. If you have a CID, which miner do you retrieve the content from?

Maintaining a global index of which miner has which content will be difficult (in terms of keeping up to date, it's size, the running costs etc.) and is inherently centralized.

This project proposes that miners keep an index of the content that they are storing themselves (including of deals made up of batches/aggregations of content) such that they can be asked if content for a CID can be retrieved from them.

Miners also register themselves on the "DeDHT", a DHT where deals are made with miners that are "closest" to the CID of the content. There is no guarantee that deals are actually made with CIDs that are "close" to the miner's ID but there is incentive to do so if the creator wants the content to be found efficiently by others.

Leveraging a DHT avoids the need for a centralized index of all the content and allows miners to only have to keep track of the things they have agreed to store.

Note that a file is made up of many CIDs. The recommendation could be that whole files reside on a single miner, it is just the root CID that is "close" to the miner. The same can apply for directories.

One issue is aggregations, which will be slower to accumulate because content will need to be aggregated in multiple "buckets" of "close" CIDs.

On the surface Sybil attacks appear to be a problem. The more places in the DHT your miners are in the more deals they will receive. However if we mandate that participants in this DHT must be active miners registered in the Filecoin blockchain the barrier to entry to becoming a miner should be deterrent enough to prevent this.

#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->

* Users want to discover which Filecoin miner is storing their data.
* We don't really want to keep a central index of where the CIDs are stored.

#### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->

A content owner would calculate the CID for a given file, and then interrogate the DeDHT for the closest miner(s) to that CID. Once a list of miners is received they negotiate one or more deals with them.

A content consumer would obtain the CID, interrogate the DeDHT for the closest miner(s), and connect to each one in order by "closeness" and query them to see if they are storing the content for the CID. If yes, then they can start retrieval.

#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

<!--
Explain how this addresses known challenges or opportunities.
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

Nodes operating on the mainstream IPFS network will be able to bridge any content stored on Filecoin miners without having to maintain a global index or restrict available content to known deals.

#### Internal leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

<!--
Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

<!--Explain why this rating-->

Medium-Low

## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

TBD

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

####  What does success look like?
_Success means impact. How will we know we did the right thing?_

<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

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

#### Roles / skills needed
<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->
