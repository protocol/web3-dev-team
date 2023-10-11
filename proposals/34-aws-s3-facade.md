# AWS S3 Facade to Filecoin

Authors: [@alanshaw](https://github.com/alanshaw)

Initial PR: https://github.com/protocol/web3-dev-team/pull/34

Problem Addressed: New developers have to spend too much time and money to go through a simple storage/retrieval workflow. (P1)

> Instead of the whole world switching to Filecoin. Why doesn't AWS and Google make the switch instead? Would that be easier?
> 
> An AWS S3 API facade to a Lotus.

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

There are many companies, organizations and individuals (entities) that use AWS S3 in their applications. Using Filecoin to store data could yield a cost saving, but perhaps cannot be justified because of the amount of work that would be involved to refactor code to interface with a different storage provider.

In this document we propose a facade to AWS S3 that would allow entities to simply and easily switch to using Filecoin for storage, with minimal code changes to their applications.

#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->

* AWS S3 is used by many entities.
* Filecoin is a cheaper alternative to S3.
* Entities are amenable to switching to using a different storage provider.
* It will be easier to switch to using Filecoin if large codebase refactors do not have to take place.

#### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->

There are two envisaged possibilities for how the solution is implemented:

1. As a backend service. It would allow ALL S3 clients in ALL languages to talk to it. Developers would simply need to update their S3 API URL and credentials in their apps to begin using it. The downside is that it comes with additional infrastructure to setup and run. Developers would need to deploy the service or alternatively there could be a S3<->FIL bridge as-a-service where the developer could 1-click deploy for a minimal fee.
    * The service would need to be periodically "charged" with FIL to allow it to make storage deals.
    * The service could optionally act as a caching proxy to avoid some retrieval charges.
2. As a client library. The disadvantage being that this would have to be implemented for each language but it would not need additional infrastructure to be setup. Developers would need to switch dependencies from the S3 client library they're using and add some configuration and plumbing to allow the client to be "charged" with FIL in order to interact with the market. Aside from that no further changes would be necessary to app code.

#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

<!--
Explain how this addresses known challenges or opportunities.
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

* AWS S3 has a large user base. This lowers the barrier to entry for those users and provides means for them to experiment and evaluate Filecoin with lower commitment and risk.
* Has potential to demonstrate to Amazon that they should switch to Filecoin behind the scenes for significant operational cost savings.
* Could hugely increase the amount of data actually stored on the Filecoin network.
* We could dogfood the solution internally where we're using S3 to store data.
* Abstracting automated deal making logic will be useful in other projects.
* This project would likely expose issues with deal making that we can resolve.

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

<!--
Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

* A successful switch to using Filecoin as a storage provider in existing applications will increase the likelyhood for developers to use Filecoin directly in new projects.
* Furure projects could re-use and improve the deal making logic. The library would be a good OSS project that would not only be useful to PL but to many other dapp developers.

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

<!--Explain why this rating-->

Med-Low

It's common knowledge that AWS S3 is one of the largest storage providers in the world. Switching providers to save on cost is commonly known to be something that everyone from individuals to large corporations do. There even exist companies that are built explicitly to enable switching e.g. insurance, gas/water/electricity utilities, bank accounts. I know from experience that it's not always easy to get go ahead to refactor code in existing applications when confidence in the change is low or unknown. This is especially true in larger companies.

## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

Assuming we'd opt for the backend service solution:

1. Create API endpoints compatible with AWS S3.
1. Define and build (or use if exists) automated deal maker logic.
1. Deploy demonstration servers.
1. Verify with demos in multiple languages.
1. Dogfood with some real PL projects (if exists?).

Optionally:

1. Create and deploy a S3<->FIL bridge as-a-service application.

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

* A PoC exists that can be used to store and retrieve data via ANY S3 client.

####  What does success look like?
_Success means impact. How will we know we did the right thing?_

<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

1. 10 projects that use AWS S3 make the switch.
1. 1 or more projects publicly report their month on month cost saving by switching.
1. Automated deal maker lib has 5 external contributors.
1. A successful switch causes developers from an entity to use Filecoin directly in a new project.

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

The success of this project hindges on the deal making process working well. It needs to be fast and should not fail.

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

* Facade to Google Cloud Storage/other big storage provider instead.

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

* 1-2 developers with golang experience
