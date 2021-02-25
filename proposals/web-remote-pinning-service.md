# Pinning Services API in JS-IPFS

Authors:
- @gozala

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

go-ipfs 0.8.0 and [IPFS HTTP Client][] have shipped support for [remote pinning services][]. [Pinata][] is implementing support and [Textile is commited][] to doing it as well. This enables users to persist and ensure their data is available without having to invest into own infrastructure. 

Support has not been implemented in js-ipfs making this feature unavailable for web nodes, so teams building web3 products will need to contiune providing persistence through a backend as opposed to letting their users choose where their data gets persisted.

By implemnting support in js-ipfs we can enable ecosystem of web applications in which product users are empowered to choose where their data is persisted with almost no effort on teams building them.

[remote pinning services]:https://ipfs.github.io/pinning-services-api-spec/
[pinata]:https://pinata.cloud
[Textile is commited]:https://twitter.com/textileio/status/1363896959073804288?s=20
[IPFS HTTP Client]:https://www.npmjs.com/package/ipfs-http-client

#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->

- Teams building products would like an ability of not having to build persistence layer.
- Pinning services will deploy support for this API.

#### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->

App delevloper will have a choice to not build their own storage, instead allowing a user connect app with their pinata, textile or any other pinning service account _(with a flow similar to login with twitter/facebook/google)_ to register remote pininng service into app embedded IPFS node.

This would allow application to pin data at  pinning service of users choosing with a built-in remote pinning API.

#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

<!--
Explain how this addresses known challenges or opportunities.
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

- Web3 is all about making users in charge of their data. This makes it possible out of the box without any additional effort.
- Enables a class of web3 applications that run all of the business logic at the edge to be backend free (app is deployed as a static bundle of html+js, users bring their data storage through pinning services).
- Creates a potential to grow user base of pinning services by making them viable option for end users.

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

<!--
Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

- Unlocks whole class of web applications not possible today.
- Creates a cowpath for web applications that empower users to choose or even bring their storage.
- Developer teams can save time spend on building infrastructure for content persistence.

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

<!--Explain why this rating-->

Level 3 - Apps already use pinnig services through proprietary APIs making it difficult to support multiple different services as each one requires additional development. Enabling them to use single API to support all existing and future pinning services creates a high value / low risk proposition.


## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

- Just implement & land it.

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

- Version of js-ipfs is shipped with remote pinning API.

####  What does success look like?
_Success means impact. How will we know we did the right thing?_

<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

- Web applications are leveraging remote pinnig API to solve persistence. 

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

- Products choose not to allow users to connect pinning services (in house pinning is what they charge users for).
- Pinning services do not ship support.
- Pinning service connection flow is to complicated.

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

- 🤷‍♂️

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

- none

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->

- Template for building 0-backend web applications on IPFS.
- Sets a precedence of types of applications that empower users to choose where their data lives.
- 0-config IPFS Desktop support, enabling web-apps to pin into IPFS Desktop.

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

- Medium

#### Roles / skills needed
<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->

- JS-IPFS contributor
- JS-IPFS maintainer (to do a review)
