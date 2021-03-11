# Wrap up rendezvous implementation and deployment

Authors:
- @vasco-santos
- @gozala

Initial PR: #67 <!-- Reference the PR first proposing this document. Oooh, self-reference! -->

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

##### Problem Statement

During the lifetime of a libp2p node, particularly during its startup, establishing connections with other peers will be crucial to create a network topology able to fulfill the needs of the node.

Each connection to a different peer might have different outcomes. Accordingly, each peer will need to find peers providing a given service or playing a given role over time, so that they can operate more efficiently. These services and roles can range from circuit relays to enable connectivity between restricted nodes, subscribers of a given pubsub topic, or even application specific routing.

Currently the JS stack (only?) does not offer this out of the box. It is expected that the users understand the infrastucture pieces they will need to configure and deploy, as well as get their nodes connected to this infrastructure. This proposal aims to mitigate this entrance barrier, which is one of the main points discussed in most of the meetings with collabs and users of our stack.

Moreover, nodes in some environments (Ex: browser) cannot have a big number of connections open at the same time. Consequently, we need them to find and connect to the most meaningful peers.

One of the possible ways to register and discover certain roles/services is using the [rendezvous protocol](https://github.com/libp2p/specs/tree/master/rendezvous). Shortly, libp2p Rendezvous is a lightweight mechanism for generalized peer discovery. It can be used for bootstrap purposes, real time peer discovery, application specific routing, and so on.

##### Current state

We have a working implementation of the rendezvous protocol (Server and client) in JS ready for review and an outdated PR with the implementation in Go (needs Signed Peer Records). We also need to decide wether we need [Rendezvous message signing](https://github.com/libp2p/specs/issues/303) and get it implemented if so.

#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->

- Dapps need to be able to find relays to bind, in order to accept incoming connections
- Dapp developers want to easily discover all the peers running their dapp 
- Developers want out of the box meaningful connections to establish reliable overlay networks
- We want alternatives for service discovery 
- We want to extend the number of bootstrap nodes with community deployed nodes that can be discovered via Rendezvous

#### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->

Rendezvous can offer a wide range of scenarios.

1. A developer will start a `js-ipfs` node in the browser (pubsub is enabled by default) and behind the scenes the node will be able to discover and connect to nodes that share the same interestes (pubsub subscriptions)
2. A developer will start a `js-ipfs` node in the browser and the node will try to find available relays out of the box, so that it can use them to receive incoming dials.
3. A developer can use the Rendezvous API to register peers under a given namespace, so that other nodes can easily find them. Example: Discover all the peers running in the dapp scope. A real use case would be Slate, which has this requirement.


#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

<!--
Explain how this addresses known challenges or opportunities.
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

🔥🔥🔥 This would allow nodes to become more self sufficient (or at least would be a first step towards that), instead of requiring users to have all the knowledge about the infrastructure needs of a node to operate efficiently.


#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

<!--
Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

🎯🎯🎯 - This would enable the users of our stack to focus on their products, rather than understanding all the pieces behind the scenes that need to exist and be configured.

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

<!--Explain why this rating-->


## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

- Both GO and JS stacks have Rendezvous clients merged and released
- We have a set of Rendezvous servers deployed
- We have 

####  What does success look like?
_Success means impact. How will we know we did the right thing?_

<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

- JS and GO nodes can out of the box establish meaningful connections to enable its subsystems to properly work
  - Nodes are connected to 6 pubsub nodes
  - Nodes are connected to X closest peers
  - Browser nodes are always advertising a multiaddr through a relay
  - Browser nodes are dialed from go nodes (through a relay)

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

- Rendezvous Servers cannot handle all the expected load

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

We have an efficient and reliable way of performing DHT queries on every single runtime (or an efficient way of delegating them).

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

Part of the [Connection Manager Overhaul](https://github.com/libp2p/js-libp2p/issues/744) (future project pitch) will be essential to achieve all the magic out of the box connections. With this Project, both are users and the dev team will be able to discover meaningful peers in an efficient fashion. Consequently, we can make the connection manager more intelligent to trigger queries and establish connections with the important peers.

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

- 1 js-libp2p engineer
- 1 go-libp2p engineer
- 1 infrastructure engineer
