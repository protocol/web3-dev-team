# [outcome or objective here] 

Authors: @aschmahmann

Initial PR: https://github.com/protocol/web3-dev-team/pull/31

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

Currently go-ipfs users are able to utilize the public IPFS DHT to find who has advertised they have some CID in under 1.5s in 95+% of cases. However, the process of putting those advertisements into the DHT is slow (e.g. 1 minute) and is a bottleneck for users trying to make their content discoverable. Users who have moderate amounts of content on their nodes complain about their content being hard to find in the DHT as a result of their nodes' inability to advertise. Additionally, some of the measures users can take to reduce the number of provider records they emit by taking actions like only reproviding the roots of graphs (see [reprovider strategies](https://github.com/ipfs/go-ipfs/blob/09178aa717689a0ef9fd2042ad355320a16ffb35/docs/config.md#reproviderstrategy)) are not generally recommended due to some outstanding issues such as the inability to resume downloads of a DAG.

While R&D work on larger scale improvements to content routing is ongoing we can still take the opportunity now to make our existing system more usable and alleviate much of our users' existing pain with content routing.

After completion of this project the state should be that go-ipfs users with lots of data are able to setup nodes that can put at least 100M records in the DHT per day. Additionally, users should be empowered to not have to advertise data that is not likely to be accessed independently (e.g. blocks that are part of a compressed file).


#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->
- The IPFS public DHT content provider subsystem is insufficient for important users
- The work is useful even though a more comprehensive solution will eventually be put forward, meaning either:
    - Users are not willing to wait, or ecosystem growth is throttled, until we build a more comprehensive content routing solution
    - The changes made here are either useful independent of major content routing changes, or the changes are able to inform or build towards a more comprehensive routing solution

#### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->

Users who use go-ipfs would be able to tell what percentage of their provider records have made it out to the network in a given interval and would notice more of their content being discoverable via the IPFS public DHT. Additionally, users would have a number of configurable options available to them to both modify the throughput of their provider record advertisements and to advertise fewer provider records (e.g. only advertising pin roots)

#### Impact
_How directly important is the outcome to web3 dev stack product-market fit?_

🔥🔥🔥 = 0-3 emoji rating

<!--
Explain why you have chosen this rating
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

Probably the most visible primitive in the web3 dev stack is content addressing which allows someone to retrieve data via its CID no matter who has it. However, while content addressing allows a user to retrieve data from **anyone** it is still critical that there are systems in place that allow a user to find **someone** who has the data (i.e. content routing).

Executing well here would make it easier for users to utilize the IPFS public DHT, the mostly widely visible content routing solution in the IPFS space. This would dramatically improve usability and the onboarding experience for both new users and the experience of existing users, likely leading to ecosystem growth.

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

🎯🎯🎯 = 0-3 emoji rating

<!-- Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

Many of the components of this proposal increase development velocity by either exposing more precise tooling for debugging or working with users, or by directly enabling future work.

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

<!--Explain why this rating-->
2 . We don't have direct market research demonstrating improving the resiliency of content routing will definitely lead to more people choosing IPFS or to work with the stack. However, this is a pain point for many of our users (as noted on the IPFS Matrix, Discuss and GitHub) and something we have encountered as an issue experienced by various major ecosystem members (Protocol Labs infra, Pinata, Infura, etc.).

## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

- Enable downloading sub-DAGs when a user already has the root node, but is only advertising the root node
    - e.g. have Bitswap sessions know about the graph structure and walk up the graph to find providers when low on peers
- Add a new command to `go-ipfs` (e.g. `ipfs provide`) that at minimum allows users to see how many of their total provider records have been published (or failed) in the last 24 hours)
- Add an option to go-libp2p-kad-dht for very large routing tables that are stored on disk and are periodically updated by scanning the network
- Make IPFS public DHT `put`s take <3 seconds (i.e. come close to `get` performance)
  - Some techniques available include:
     - Decreasing DHT message timeouts to more reasonable levels
     - [Not requiring](https://github.com/libp2p/go-libp2p-kad-dht/issues/532) the "followup" phase for puts
     - Not requiring responses from all 20 peers before returning to the user
     - Not requiring responses from the 3 closest peers before aborting the query (e.g. perhaps 5 of the closest 10)

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

The project is done when users can see how much of their provide queue is complete, are able to allocate resources to increase their provide throughput until satisfied, and allocating resources is either not prohibitively expensive, or it is deemed too much work to decrease the resource allocation.

####  What does success look like?
_Success means impact. How will we know we did the right thing?_

<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

Success means that much fewer users report issues finding content, instead things either work for them or they file issues or ask questions on how to decrease their resource usage for providing. Things should just work for users who have 10-100k provider records and leave their nodes on continuously.

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

- People have other issues that the DHT put performance is just masking, which means we will not immediately be able to see the impact from this project alone
- Users will not want to spend the raw bandwidth of emitting their records even if lookups are instant
- Decreasing the query `put` time is much harder than anticipated
- Technical work required is harder than anticipated

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other  potential solutions can address the same need?_

These alternatives are not exclusive with the proposal

1. Focus on decreasing the number of provider records
    - e.g. Add more options for data reproviding such as for UnixFS files only advertising Files and Directories
    - might be tricky UX and plumbing, but is something we likely will need to tackle eventually
2. Focus on decreasing the frequency of reproviding records
    - e.g. Build a second routing layer where nodes are encouraged or required to have high availability (e.g. a federated routing layer or opt-in second DHT that tracks peer availability more rigorously)
    - has possibility for high payoff, although has more risk associated with it

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

- None

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->

- Making it easier to implement alternative #1 above (enabled by `ipfs provide` and being able to download sub-DAGs when only the root node is provided)
- Vastly improved lookup performance of the delegated routers that can be used in js-ipfs (enabled by allowing users to have large routing tables)

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

L. There is some uncertainty in how much work will be required to increase `put` performance. However, all of the changes are client side which make them relatively easy to test. This estimate could be an overestimate as some of the changes have some uncertainty which is currently being estimated at the higher end (i.e. the work in go-ipfs and go-bitswap)

#### Roles / skills needed
<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->

- 3-4x go-engineers
  - 1-2x go-ipfs experience
  - 1-2x go-libp2p (ideally go-libp2p-kad-dht) experience
- Some input and support may be required from research
