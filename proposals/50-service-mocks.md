# Mock implementations for our key services

Authors: @rvagg, @vasco-santos

Initial PR: https://github.com/protocol/web3-dev-team/pull/50

## Purpose &amp; impact 

#### Background &amp; intent

_Describe the desired state of the world after this project? Why does that matter?_

Filecoin and IPFS aim to become the foundation for a decentralized Internet. This is a complex mission, and consequently is composed of several complex systems with different characteristics and extensibility angles. The web3/dweb community are thrilled to build on top of these technologies, but need to focus on the application layer rather than on all the services and infrastructure around the web3 stack to run.

Web3 app developers should have access to quality and up-to-date mock implementations of our key, and complex services that can be used for fast integration and unit testing.

IPFS, libp2p, and Lotus (miner and node?) are services that can be complicated to set up for test environments, or, as in the case of Lotus, require a full-time running live instance to perform integration testing against.

We should offer simple, efficient, accurate and up-to-date mock versions of our key services. Prioritising the most complex ones first. This would rapidly speed up the development velocity for web3 developers creating applications against our stack, create efficient CI pathways, and increase _developer joy_.

#### Assumptions &amp; hypotheses

_What must be true for this project to matter?_

 * Testing against our stack is complex and is likely avoided until the very last step, or actively replaced with mocks and stubs managed by users who may not be in the best position to maintain up-to-date and accurate replacements
 * Testing against our stack is expensive. Lotus nodes require an expensive machine

#### User workflow example

_How would a developer or user use this new capability?_

App developer would install and start, or integrate, our mock services when performing unit and integration testing. Projects could also have mock services integrated into CI testing pipelines where fast mocked verification is acceptable.

#### Impact

_How would this directly contribute to web3 dev stack product-market fit?_

#### Leverage

_How much would nailing this project improve our knowledge and ability to execute future projects?_

#### Confidence

_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

## Project definition

#### Brief plan of attack

 1. Mock

#### What does done look like?

_What specific deliverables should completed to consider this project done?_

We have complete, verified, lightweight and accessible mocks that suit typical developer environments and can be used to cover the typical workflows that application developers need from our stack.

####  What does success look like?

_Success means impact. How will we know we did the right thing?_

Our mocks show up in web3 app stacks (where we have visibility)

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

Medium - Large depending on the scope we choose (just one service, or all the things? do we want full API coverage? do we cover many workflows?)

#### Roles / skills needed

<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->

 * Understanding of our key API endpoints and their nuances
 * (probably) JavaScript development for mock services and libraries
 * (maybe) Go development for mock libraries
