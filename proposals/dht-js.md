# Effective content and service discovery in JS

Authors: @jacobheun

Initial PR: TBD

## Purpose &amp; impact
#### Background &amp; intent
_Describe the desired state of the world after this project? Why does that matter?_
<!--
Outline the status quo, including any relevant context on the problem you’re seeing that this project should solve. Wherever possible, include pains or problems that you’ve seen users experience to help motivate why solving this problem works towards top-line objectives.
-->

**Current State**
- JS projects rely on delegate and preload nodes to be able to interact with the live network
- PL hosted delegate/preload nodes are often overloaded negatively impact performance of projects

#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->

TODO

#### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->

TODO

#### Impact
TODO

<!--
Explain why you have chosen this rating
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

#### Leverage
TODO

<!-- Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

<!--Explain why this rating-->


## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

The focus of this effort is to build the DHT to function solely in Node.js. Running a DHT in browser is not currently viable.

- Week 0 - Complete the DHT specification (DHT protocol expertise)
- Create a test plan in Testground to evaluate query performance
- Implement DHT routing table construction and refresh
- Implement the improved query logic
- Implement Peer Eviction logic


**Assumptions**
- Routing table diversity is not criticial and can be implemented later
- We can start with "Client Mode" only support to minimize the surface area of the solution

#### What does done look like?

- js-ipfs in Node.js ships with the DHT enabled in client mode by default
- js DHT query times are comparable to Go over TCP/Noise connections

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

Being able to effectively find content and services on the network unlocks core functionality of IPFS for the JS ecosystem that removes more of its reliance on a paired Go IPFS node. This will enable more JS engineers to build Full Stack solutions on top of the web3 stack.

## Required resources

#### Effort estimate

- Medium, 3-5 weeks

This should be reasonable to do within a 5 week period given that the DHT protocol is well known. A concerted effort should be made within the first week, owned by DHT protocol experts, to produce a specification for the JS engineers to continue working off of.

#### Roles / skills needed

- DHT protocol expertise; Ideally this would result in a finished specification for the existing state of the libp2p DHT.
- js-libp2p expertise; 2-3 JS Engineers to implememnt the DHT spec
- Testground expertise for scale testing
