# JavaScript libraries are trim and modular

Authors: @rvagg @achingbrain @vasco-santos

Initial PR: https://github.com/protocol/web3-dev-team/pull/47

## Purpose &amp; impact 

#### Background &amp; intent

_Describe the desired state of the world after this project? Why does that matter?_

Using IPFS with JavaScript requires installing and loading a _lot_ of code and you end up with a monolith. Using js-ipfs necessitates it being _the primary thing_ in your application stack because of its size and complexity.

1. There are a _lot_ of dependencies
   1. Takes a long time to install
   2. Assumes the user wants _all the things_
2. The total weight of code is very large
   1. Related to the _all the things_ accumulative design of the stack
   2. Crypto libraries mostly to blame
3. The API surface area is very large
   1. Related to the projection of the CLI API up into the browser API and exposing _all the things_
   2. The complexity of the entire stack means there's a lot of different ways to achieve things using different APIs and configuring them separately, but you still get _all the things_

The goal of this project is to initial exploration, design and planning of a suite of JavaScript libraries that can be composed according to user / application needs, with minimal inclusion of features and functionality that are out of bounds for those needs.

Actual development within this project would be exploratory / experimental only. Outcomes would be further scoped proposals for more work to do actual implementation of parts, or all of the proposed suite.

#### Assumptions &amp; hypotheses

_What must be true for this project to matter?_

 * Interacting with IPFS in JavaScript is something that users want to do
 * Current js-ipfs is too monolithic and causing barriers to entry

#### User workflow example

_How would a developer or user use this new capability?_

Developers would be able to choose the level of interaction with our web3 stack in JavaScript:

 * IPLD ("I just want to make CIDs for DAG-CBOR thanks")
 * libp2p ("I just want to chat bitswap with known peers and handle everything else myself thanks")
 * UnixFS ("I want to wrap up this in-browser video recording into DAG-PB in a CAR file and let the user download it, thanks")
 * CIDs ("I want to make this thing into an NFT and would like to know the CID before I submit it to `<IPFS, Filecoin, service, etc.>`")
 * etc.

Some of these kinds of use-cases are either impossible or very difficult with the current incarnation of the JavaScript stack.

#### Impact

_How would this directly contribute to web3 dev stack product-market fit?_

Reach JavaScript developers at their level of comfort. 

Surveys like [the one conducted annually by StackOverflow](https://insights.stackoverflow.com/survey/2019/#most-popular-technologies), suggest that there are nearly an order of magnitude more developers who know Javascript (67%) than who know Go (8%). But our JavaScript offering is not friendly for general consumption and we usually end up pushing them to use go-ipfs (and friends) and build wrappers around it. Many use-cases are much simpler than requiring the entire js-ipfs stack as it currently exists and we're not serving those (well).

#### Leverage

_How much would nailing this project improve our knowledge and ability to execute future projects?_

#### Confidence

_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.


## Project definition

#### Brief plan of attack

  1. Account for our current JavaScript stack - write up a full list of components, both included in js-ipfs and outside of it (including newer incarnations of pieces, such as the recent IPLD re-implementations).
  2. Create list of user-stories that would describe discrete verticals within our JavaScript stack.
  3. Map out a path to a suite of separate libraries that can be easily combined to support those verticals
     1. Likely also includes replacement or re-writing of some dependencies where their weight is a problem (e.g. crypto libraries which currently occupy a bit too much of the dependency tree)

Care will need to be paid to problems like versioning, compatibility, documentation, maintainence, etc.

#### What does done look like?

_What specific deliverables should completed to consider this project done?_

A plan of attack for _actual_ implementation.

####  What does success look like?

_Success means impact. How will we know we did the right thing?_

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

Small - Medium

#### Roles / skills needed

<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->

 * js-ipfs expertise
 * js-libp2p expertise
 * js-ipld expertise
