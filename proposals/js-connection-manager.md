# js active connection management

Authors: @vasco-santos <!-- List authors' GitHub or other handles -->

Initial PR: https://github.com/protocol/web3-dev-team/pull/81 <!-- Reference the PR first proposing this document. Oooh, self-reference! -->

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

With the existing protocols in libp2p, as well as IPFS subsystems built on top of libp2p, such as Pubsub and the DHT, the need for a connection manager overhaul becomes an import work stream, so that these protocols operate as expected by the users, i.e. out of the box solution.

Currently, js nodes have a reactive connection manager that can be decoupled into two parts: establishing new connections and trimming connections. The former relies on an `autoDial` approach, where each time a new node is discovered it will try to establish a connection with that peer. The later consists on blindly trimming connections when reaching a configurable threshold.

From the current solution, there is a lot of space for improvement with tremendous value for the users. Either evolving the current connection manager to the state of the go-implementation or implementing a fully fledged [Connection Manager v2](https://github.com/libp2p/specs/pull/161) (+ [more notes](https://github.com/libp2p/notes/issues/13)).

With the connection manager overhaul in JS we aim to:
- Find our closest peers on the network, and attempt to stay connected to n to them
- Finding, connecting to and protecting our gossipsub peers (same topics search)
- Finding and binding to relays with AutoRelay
- Finding and binding to application protocol peers (as needed via MulticodecTopology) -- We should clarify what libp2p will handle intrinsically and what users need to do

All the above scenarios need proper setups from our users at the moment, which means they need to manually find the nodes they want to connect and connect to them, as libp2p connection manager will not be actively looking at meaningful connection to establish.

An active connection manager will enable out of the box creation of meaningful overlay networks, as well as enable browser nodes to bind to AutoRelay nodes, so that they can be dialed from other nodes in the network. Moreover, JS nodes keep the discovered peers stored in the PeerStore. On subsequent node starts, these nodes should prioritize their previous established topology over the bootstrap nodes if possible.

#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->

- Web3 developers want to have a reliable pubsub topology out of the box without relying on star servers
- Web3 developers want to find and connect to other peers in a given scope
- Browser developers want to have their nodes reachable via more transports than `webrtcSTAR` out of the box
- PL wants to decrease the load on bootstrap nodes

#### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->

Out of the box usage with sane defaults. However, the developer should be enabled to configure the proactive dial strategies  (power users)

#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

<!--
Explain how this addresses known challenges or opportunities.
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

This solves (together with browsers being able to dial go nodes) most of the common issues of our users when trying to use features like IPNS and Pubsub and hitting problems.

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

<!--
Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

<!--Explain why this rating-->


## Project definition
#### Brief plan of attack
<!--Briefly describe the milestones/steps/work needed for this project-->

There is a proposal already for a [full connection manager overhaul](https://github.com/libp2p/js-libp2p/issues/744). There are a few items that should not be considered into this scope. Connection Gating, Retries and Disconnect are good candidates for a follow up proposal. Decaying tags might have their value, but depend on how far we aim to reach as a first step. Proactive dial, Trim connections, Keep Alive and being able to protect important connections are essential for the scope of this proposal.

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

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
