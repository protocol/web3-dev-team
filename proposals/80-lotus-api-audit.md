# Lotus / Filecoin RPC and Library Audit

Authors: @rvagg

Initial PR: https://github.com/protocol/web3-dev-team/pull/80

## Purpose &amp; impact 

#### Background &amp; intent

_Describe the desired state of the world after this project? Why does that matter?_

The Lotus RPC and its associated JavaScript libraries would be catalogued, their feature set and deficiencies would be well understood, and this information is available for the production of better documentation and other educational materials for users.

Production of documentation and other educational materials is not specifically part of the scope of this project but it may be expanded to include this as a collaboration with the individuals who own / specialise in this area (i.e. this likely turns into a collaboration with the Dev Adoption & Onboarding team).

There currently exists a small but sprawling and poorly documented, ecosystem of JavaScript libraries interact with the Lotus RPC API. There are also some known deficiencies with the API (e.g. the external wallet problem) that are not documented, just known by people who have bumped into the particular problem(s).

This project aims to do a mini audit of the landscape of libraries and the abilities offered by the Lotus RPC API to developers interacting with Lotus from the outside—for any purpose, including simple wallet/send actions, general message crafting and submitting, deal-making, etc.

Outputs of this project includes:

* A catalog of existing libraries used to interact with the Lotus RPC API, including (currently known to be roughly within this category):
  * Those in [filecoin-shipyard](https://github.com/filecoin-shipyard)
  * Those currently published under the [@glif npm namespace](https://github.com/glifio/modules/tree/primary/packages/)
  * Those maintained for/by the [Truffle suite](https://github.com/trufflesuite/ganache-filecoin-alpha-cli)
* An indication of quality or status and a recommendation for action; smaller-scope actions may be taken as part of this project. Such actions may include:
  * Further documentation in specific areas
  * Deprecation / archival
  * Improvements and feature additions
* Key information required to create/improve higher-level documentation containing recommendations for users seeking to interact with the Lotus RPC (production of / contribution to is not a necessary part of this project, but generating the resources and/or knowledge to do so it part of this project).
* A catalog of areas for high-value improvement, including the creation of new project proposals or the provision of more details to existing project proposals, for:
  * The Lotus RPC
  * Relevant JS libraries

#### Assumptions &amp; hypotheses

_What must be true for this project to matter?_

That developers want to be able to interact with Lotus, and Filecoin more broadly, via JavaScript and that the path to doing this is currently via RPC APIs.

#### User workflow example

_How would a developer or user use this new capability?_

#### Impact

_How would this directly contribute to web3 dev stack product-market fit?_

Maturity of Filecoin depends on a developer ecosystem building layer 1 (and beyond) technologies to serve users. As with IPFS, it is expected that a large portion (possibly a majority) will be leaning on JavaScript application stacks, and dapp developers will be leaning on the browser JavaScript environment. It is critical that we provide a solid foundation for building libraries to interact with Filecoin and the current technical focus for this is Lotus and its RPC. This will evolve over time but the current state suggests high-value will be derived from basic investment in the landscape of JavaScript libraries that interact with (and above) Lotus, and the Lotus RPC itself.

#### Leverage

_How much would nailing this project improve our knowledge and ability to execute future projects?_

This project will serve as a foundation for additional investment in the JS (and general API) layer above Filecoin to unlock additional web3 developer opportunities. Being able to know _what we have_ and what the status of it is critical to understanding where to invest.

#### Confidence

_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

## Project definition

#### Brief plan of attack

Executing this project would include:

 * Seeking input on the current status and future plans of individuals / teams involved in maintaining or authoring relevant libraries, including (but not limited to):
   * Jim Pick (ecosystem / grantee, ex-PL)
   * Alan Shaw (PL)
   * Glif.io / Infinite Scroll
   * Truffle / Ganache contributors (initially via Jim Pick)
   * Other PL staff who may have an interest in, or experience with these libraries and the RPC itself
 * Attemtping to use the libraries as they currently exist, and possibly the Lotus RPC directly and documenting the process to contribute to the project outputs listed above

#### What does done look like?

_What specific deliverables should completed to consider this project done?_

* A clear map of the currently available JavaScript libraries available for interacting with Filecoin (RPC API and other)
* A clear, and generally complete, pre-documentation catalog of the functionality available:
  * in those JavaScript libraries
  * via the Lotus RPC
  * _Note that producing actual documentation is a further extension of this project to be scoped accordingly._
* A clear, shared understanding of the quality and state of these libraries and the scope of their utility for achieving basic tasks with Filecoin (wallet transactions, state inspection, deal making, etc.) (i.e. "shared" because it is critical that this is communicated and understood by relevant parties))
  * An ideal outcome of this would be further project proposals to undertake improvements.
* Sufficient clarity to be able to rate (and priority sort) proposals for further work on relevant libraries (or non-existing libraries) to interact with Filecoin, and the Lotus RPC itself with regards to its affordances for external users.

####  What does success look like?

_Success means impact. How will we know we did the right thing?_

A clearer path to the improvement of external Lotus interaction

#### Counterpoints &amp; pre-mortem

_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

#### Alternatives

_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

#### Dependencies/prerequisites

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

Small for 3-5 FTEs (i.e. lower for smaller investment, as available to Sudo at the time of writing)

#### Roles / skills needed

<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->

* JavaScript
* TypeScript
* Lotus (some Go)
* Basic Filecoin understanding
