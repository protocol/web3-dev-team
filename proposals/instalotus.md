# Project Pitch: Instalotus

##### (very rough early proposal) A PoC of an ephemeral fully-validating lotus instance in 500 seconds.

Authors: @ribasushi

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

The Filecoin blockchain is complex. This translates directly into a rather arduous and error prone initialization of a trustless node. This hampers adoption and work on multiple fronts: internal and external QA, curious devs, curious users, etc

The aim of this proposal is to attempt to build a "hack-week-quality" PoC on top of the RDBMS-backed blockstore coming online imminently ( week of Feb 15th ). Upon completion, provided no current assumptions are invalidated, a user will be able to stand up a full node in less than 10 minutes.

<!--
Outline the status quo, including any relevant context on the problem you’re seeing that this project should solve. Wherever possible, include pains or problems that you’ve seen users experience to help motivate why solving this problem works towards top-line objectives.
-->

#### Assumptions &amp; hypotheses

- Existence of privacy/decentralization/self-reliance conscious users, who for various reasons do not want to rely on a 3rd party service
- Increasing difficulty of spinning up mainnet "seeding nodes" ( think filecoin-hydras )
<!--(bullet list)-->

#### User workflow example

- Get a box with ~32G ram / sufficiently fast ( ~512 mbps ) network
- Clone a small git repo
- Run an entry script ( assuming availability of docker )
- Wait 500 seconds or less
- Enjoy API access to an ephemeral yet fully-validating node

#### Impact

- Lower the barrier to entry to the filecoin mainnet
- Provide further datapoints of what needs attention in lotus if one "ignores badger"

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

- Lack of a "democratized lotus experience" at present is a relatively serious bottleneck to a number of projects and experiments (this is my subjective experience, seen through the lens of being on the receiving end of "I need a node: I will ask riba").

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

🤷 / TODO: Could not quickly determine from a skim of the article how to come up with realistic ICE score


## Project definition
#### Brief plan of attack

- Blockstore replica(s) are available for consumption ( already in flight from previous projects, ETA Feb 19th )
- A branch of lotus combining a memrepo with a secondary pg-based repo ( reusing the already existing mechanism of `LOTUS_ENABLE_CHAINSTORE_FALLBACK` )
- Tuning/tuning/tuning

#### What does done look like?
- The "User workflow example" above is a reality OR is disproven as "this isn't possible due to reasons X,Y,Z"

####  What does success look like?
- This is a PoC, the lessons learned in either case of "done" are a success in themselves

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

- 🤷 / unsure

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

- 🤷 / unsure

#### Dependencies/prerequisites

- Nothing aside from the listed already-ongoing-nearly-finished work

#### Future opportunities

- 🤷 / unsure what to add besides the user-enablement items listed earlier

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

- small ( 2 riba-weeks )

#### Roles / skills needed
<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->

- Go, Postgresql, Filecoin / above average ability to pinpoint and reason through system/networking bottlenecks