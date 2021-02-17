# [outcome or objective here] 

Authors: @aschmahmann

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

Currently the process of performing a go-ipfs release is tedious and is a barrier to having smaller more frequent releases. Having a more automated release process would allow us to iterate faster.

Additionally, it would be great if our release process was such that we felt comfortable having an option for go-ipfs to automatically update on start instead of making users update. This would also be a step towards removing user barriers with package managers like `snap` which are not CLI tool friendly.

#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->
- Doing go-ipfs releases manually must impede release cycle time in a way that impacts project velocity, or
- The way in which users currently update go-ipfs is sufficiently an impediment that either it causes users to have a bad experience with the stack (e.g. by running into bugs which have long been fixed), or it significantly harms development velocity by needing to take into account old non-upgraded nodes

#### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->

A go-ipfs maintainer could run a script or GitHub action that would automatically perform a release from a given branch instead of manually performing the release.

A go-ipfs user would be able to set an option in their config file such that on boot they would be able to automatically update the software they were running. Additionally, package managers with restrictive environments could just distribute shims around go-ipfs and the shim would be able to update and maintain itself.

#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

<!--
Explain how this addresses known challenges or opportunities.
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

Users having up to date versions of go-ipfs will give them a better experience resulting in fewer complaints about long solved issues, lower ecosystem burden and an easier time updating protocols.

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

<!--
Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

Future projects would make it to users faster and there would be less time from developers distracted by release process.

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

<!--Explain why this rating-->


## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

It takes less than 1hr to do a go-ipfs release from when the release is ready to be tagged, and users can automatically update to the latest version of go-ipfs.

####  What does success look like?
_Success means impact. How will we know we did the right thing?_

<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

- There are external factors slowing down releases other than the process itself
- It takes too much effort to automate the release process

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

- go-ipfs engineer
- infra engineer