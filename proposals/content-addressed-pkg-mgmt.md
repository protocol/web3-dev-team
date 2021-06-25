# Content Addressed Package Management

Authors: [@andrew](https://github.com/andrew)

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

Package management is an excellent use case for IPFS and Filecoin, as was [explored a couple of years ago](https://github.com/ipfs-inactive/package-managers),
but has yet to see major adoption within any large package managers.

Package management has been plagued with reproducibility problems over the past few years, with the same mistakes often made by different package manager servers and clients because there's no documented standards for designing and building package managers, even less so for content addressed/decentralized package managers.

Making package managers content addressable would unlock the ability for the data within package management registries to become more portable,
opening it up to much needed innovation in areas such as transport protocols, storage backends and network topologies.

A documented set of basic standards for how to implement a content address package management system will enable new languages/communities to quickly produce reliable and secure implementations. 

To enable this a specification for a protocol for content addressed package management would be written, along with a [working implementation](https://github.com/forestpm/forest), that outlines a standardized way for consumers, publishers and maintainers to share package management data that allows people to opt-in to various levels of decentralization without sacrificing existing usability, performance and security.

#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->
* package management data is content addressable
* package manager users care about the verifiablity of their software supply chain

#### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->
* Developers can quickly and safetly fetch packages directly from other developers, falling back to upstream registry
* Develoeprs can easily onboard onto content addressed package management without high commitment costs
* IT teams can easily mirror packages within an internal network with low infrastructure costs
* Third-parties can co-host packages from a registry in a trustless, permissionless way

#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

<!--
Explain how this addresses known challenges or opportunities.
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

Past attempts at decentralizing packagement have attempted to import whole registries into IPFS but come with a very high commitment cost and painful onboarding UX, as such have had low adoption so far.

In taking a slightly different approach, focusing on content addressing data from registries, we allow each user to co-host the packages that they use, unlocking resiliance and performance gains without requiring significant infrastructure or upfront buy-in from upstream registry maintainers.

Almost every software developer uses package management in some form, reducing the commitment costs of switching to content addressed packagement could unlock the data from large centralized registries and enable significant innovation in the package management space, enabling innovations like blockchain-based solutions that work seemlessly with existing centralized infrastructure.


#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

<!--
Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->
Formalizing the existing patterns in packagement in content addressed terminology will enable other projects and contributors to build on top of those formats in an open form.

Brand new package managers will be able to directly implement the best practices as well as reducing their infrastructure overheads by adhering to a content addressed package management protocol.

Documenting the architecture pattern of how we content addressed and decentralized package management can then be used as a blueprint for other similar internet infrastructure projects.

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

<!--Explain why this rating-->
- TODO

## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

- Research and document various package manager metadata formats, api endpoints and processes to extract requirements for spec
- Initial draft of data model and formats for spec
- Refactor core data model of https://github.com/forestpm/forest to implement draft spec
- Deploy analytics service for monitoring DHT for package usage
- Build and deploy marketing website for https://github.com/forestpm/forest and onboard early adopters
- Reach out to key stakeholders in package management for early thoughts, feedback and requirements
- Refine and document spec + implementation
- Publish v1 of https://github.com/forestpm/forest
- Publish specification

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

- A published draft of a v0.1 of the content addressed package management protocol specification
- A functional implementation of the specification with support for multiple package managers
- Documented discussion of protocol and process with a selection of package manager maintainers, publishers and consumers

####  What does success look like?
_Success means impact. How will we know we did the right thing?_

<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->
- Increasing number of users sharing packages on the dht
- Projects and package managers adopting and building on the protocol
- Increased discussion around content addressing in software development and tooling

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

- Content discovery and publishing on the IPFS DHT of millions of packages may affect growth once a certain level of adoption is reached
- If the user experience is poor or switching costs are too high, reaching critical levels of adoption will be difficult
- There may be incentives for some package management infrastructure organizations to retain centralized control and choose to avoid adoption

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

- [Valist](https://github.com/valist-io/valist) is an alternative project, although it appears to be closely tied to Ethereum.

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

- Whilst not directly dependent on, https://github.com/protocol/beyond-bitswap/pull/29 can help ease onboarding 

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->
A standardized package metadata format can enable the development of:
- a content addressable, public transparency log for all package managers, similar to the ]certificate transparency project](https://certificate.transparency.dev/)
- package maintainers could publish signed nfts of each release of their packages, enabling alternative sources of funding for open source

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

- Large, 6-10 weeks

#### Roles / skills needed
<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->

- package management knowledge
- javascript development
- ipfs experience
- protocol design/specification writing experience
