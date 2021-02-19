# PubSub enabled by default

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
Outline the status quo, including any relevant context on the problem you’re seeing that this project should solve.
Wherever possible, include pains or problems that you’ve seen users experience to help motivate why solving this problem works towards top-line objectives.
-->

As of this writing [pubsub][IPFS pubsub] is considered experimental and is disabled in go-ipfs.

> Can be enabled by starting a daemon with `--enable-pubsub-experiment` flag

In practice however many teams building products on IPFS use and depend on pubsub:

- Textile uses pubsub to publish thread updates among it's participants.
- 3Box uses pubsub for log replication.
- [OrbitDB][] depends on pubsub to do replication.
- Fission team would like to use pubsub (has user requests, but found it unreliable)

It also fragments network by (JS) nodes having it enabled and nodes that do not making IPNS unrelaible.

> IPFS in browsers use IPNS over pubsub (no DHT for browsers) while other nodes do it over DHT.

Enabling PubSub would populate network with more nodes making it more reliable.



#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->

- Teams building products need pubsub.
- Disabled pubsub makes an ecosystem more complex.
- Building (near) real-time application on IPFS requires pubsub.

#### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->

They would just be able to use `pubsub` without `--enable-pubsub-experiment` flag. Feature becomes usable to ipfs-client's that use IPFS HTTP API.

> **From Fission**:
> 
> If we expect apps to be independent and run on the IPFS network -- like they do with HTTP servers -- then whatever else can be made available natively can be powerful building blocks
>
> Having more capabilities available out of the box for developers is a better reason to build and host on IPFS natively. Pubsub out of the box gives a host of real time and messaging opportunities that our customers would love to use.

#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

<!--
Explain how this addresses known challenges or opportunities.
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

- PubSub becomes more reliable with more nodes on the network.
- Bulding (near) real-time products becomes easier, IPFS nodes are suitable out of the box.

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

<!--
Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

- Improves velocity of teams building products requiring pubsub by removing additional burden.
- Improves pubsub reliability by adding more enabled nodes to the network.
- Enables development of new features that require pubsub.

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

<!--Explain why this rating-->

Level 3

- We know teams building products that depend pubsub.
- Features like IPNS over pubsub depends on this.


## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

- Measure what is the overhead on nodes that do not directly use pubsub
- If overhead is neglegable ship a release of go-ipfs with pubsub enabled (see [ipfs/go-ipfs#6621][])
- Enable / upgrade IPFS nodes operated by PL.
- Raise awareness (blog, tweet, support community transition)

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

- Shipped release of go-ipfs with pubsub enabled
- Increased number of pubsub enabled IPFS nodes in the network.

####  What does success look like?
_Success means impact. How will we know we did the right thing?_

- Various projects (like OrbitDB) no longer have to explain with instructions how to enable pubsub.
- Teams like fission deliver pubsub to their users requesting it.
- Pubsub becomes more reliable due to increased number of enabled nodes. 


<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

- Everyone enables pubsub already anyway.
- Pusub prooves (more) unreliable even with increased number of enabled nodes.

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need ?_

- Alternative messaging primitives (e.g. Federated SSB like pubs)
- [SMTP][] support in IPFS nodes (you can email any node by email address)

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

- none

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->

- Improving IPNS (through IPNS over pubsub)
- DNS Service Discovery (DNS-SD) but over the global IPFS network through PubSub.

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

- Small to Medium

> I am not really qualified to answer this question. If we find overhead reasonable, enabling it should be metter of switching defaults.

#### Roles / skills needed
<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->

- go-ipfs contributor
- someone from infra to help estimate impact

[IPFS pubsub]:https://docs.libp2p.io/concepts/publish-subscribe/
[OrbitDB]:https://github.com/orbitdb/orbit-db
[ipfs/go-ipfs#6621]:https://github.com/ipfs/go-ipfs/issues/6621
[SMTP]:https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol
