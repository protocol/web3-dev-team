# IPFS Gateway can use an external index 

Authors: @willscott

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

Right now the ipfs gateways recieve a bunch of requests for CIDs. some they have cached locally. Others, they use the IPFS content routing system for discovery to attempt to locate based on the request.

#### Assumptions &amp; hypotheses

* We expect the options for where content may be found to continue evolving.
* We expect these temporary points of centralization may need different solutions than a normal ipfs node - e.g. if they want to effectively be a gateway they may need a larger cache / knowledge of where content is than a normal node.
* we want to run these gateways with reasonably high availability as we iterate this index.

#### User workflow example

* incoming requests come to gateway for data in ipfs. gateway returns data
* incoming requests come for data in a pinning service. gateway returns data (or 302's to an http provided by pinning service)
* incoming requests come for data in filecoin. data returns data.

#### Impact

High. retreaval is part of the story.

#### Leverage

Medium. helps reduce complexity of development in this space to allow more experimentation.

#### Confidence

~1.0. we know the overall problem is important. it is supposition that this is an important component for it. 


## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

#### What does done look like?

We add a parallel content routing api to dht / pubsub whereby gateways can make a direct request to one or a few 'external indexes', which may be able to resolve content.

####  What does success look like?

gateways offload some of their index to an external index. This will not happen from this project, but after a subsequent project creating such a complementary example of such an external index.

#### Counterpoints &amp; pre-mortem

We could lean on the pubsub mechanism directly for this
 * that would potentially mean all CIDs not resolved directly by the gateway can be easily monitored by anyone
 * that would increase complexity, bandwidth, and latency compared to this solution.

#### Alternatives

Could ignore gateway pain and work directly towards helping IPFS nodes succed.

#### Dependencies/prerequisites

none

#### Future opportunities

* can make a program miners can run to provide content to ipfs via the gateway / this api
* can make a cache program that makes deals with miners and provides it to ipfs via the gateway / this api

## Required resources

#### Effort estimate

small

#### Roles / skills needed

* stewardship from gateway/bifrost
* go development
