# Project F3 -- Filecoin storage deals reliability and UX

Authors: @raulk, @dirkmc, @nonsense.

Initial PR: https://github.com/protocol/web3-dev-team/pull/12.

## Purpose & impact 

#### Background & intent

_Describe the desired state of the world after this project? Why does that matter?_

Filecoin aims to become the storage layer for the decentralised future.
The web3/dweb communities are excited, engaged, and traction is on the uptick everyday.

Mining, consensus, onboarding storage capacity, and proving sectors, are all fully functional processes in the Filecoin Network, and namely in the reference implementation: [Lotus](https://github.com/filecoin-project/lotus). However, the object of this proposal, **the end-to-end storage deal process in Lotus,** falls short in terms of reliability and usability.

Through various interactions with users and developers, we have confirmed these observations:

1. users of Lotus struggle to understand the various deal stages and concepts.
2. querying the network for status of an inflight deal is non-trivial, and requires too much protocol-specific knowledge.
3. deal-making is a relatively long process, composed of various moving parts. When it fails midway, it's not easy to dig up the root cause.
4. generally speaking, it is hard to strike successful deals on Filecoin mainnet due to a number of technical reasons that compound.

Consequently, first-time users and devs who venture to experiment with Filecoin suffer an frictionful experience. Enough to turn away.

We posit that **deal-making is the bread and butter of Filecoin**; *it is the reason the platform exists in the first place.* Thus it should work like a Swiss clock, and only fail exceptionally and/or for good reasons.

> We decided to name this Project F3 in a wink to shooting to the same level of usability of Amazon S3 (albeit with notable differences).

#### Assumptions & hypotheses

_What must be true for this project to matter?_

1. Users struggle to grasp the concepts and components that comprise the deal-making process end to end.
2. Users don't have intuition of on what happens under the hood (not the details, but the major phases).
3. New users desist, or end up frustrated.
4. Attempting to strike a storage deal takes more than 1 attempt, even if it appears that we're doing everything right.
5. Developers leave with the impression that Filecoin's basic user-facing functionality doesn't work.

#### User workflow example

_How would a developer or user use this new capability?_

**This focuses on the UX elements (functional requirements), not so much on the technical reliability aspects (technical requirements).**

Arguably, the most common use is storing a file in the Filecoin network, and later retrieving it. Implementing a one-stop interactive CLI command that orchestrates the end-to-end flow that goes from having a file to having a deal, with all the intermediate steps, would be a desirable workflow.

`lotus store <path>`

1. add file to the repo.
2. display miners (miner directory in the future).
3. select several miners.
4. get a quotes from those miners.
5. select a miner.
6. initiate a deal.
7. etc.

However, if we consider the end-to-end flow to span all the way through to on-chain deal confirmation and sealing, interactivity might be suboptimal, as the end-to-end flow is in the order of hours.

Alternatively, the CLI could produce a ticket number, and through a different command, the user could enquire about progress on that ticket number.

Taking a step back, user-friendly CLI commands are nice, but if we want to push the UX even further, it would be desirable to have a companion graphical web-based deals dashboard that one can point to a node to display the status and details of all deals. An interface like this could be enriched with instructional cues to educate the user progressively.

The Spark team could help prototype this web UI ;-)

#### Impact

_How directly important is the outcome to web3 dev stack product-market fit?_

🔥🔥🔥

This problem statement addresses massive painpoints in the primary use case that Filecoin was built for (file storage and retrieval). Not executing on this translates into first-time user failure and, consequently, bounce.

#### Leverage

_How much would nailing this project improve our knowledge and ability to execute future projects?_

🎯🎯🎯

High. For seeveral reasons: this project will likely land a bunch of refactors that will make the affected areas of the codebase (markets, data transfer, graphsync) more accessible to new developers. Additionally, having a consistent high deal success rate, with a seamless and great UX that gets good user feedback, will get the team much satisfaction, which will translate into higher drive to continue driving improvements. Finally, we hope that new users/devs arriving to Filecoin and having success when making their first deal will translate into interest and hunger for more, and ultimately into some form of contribution.

#### Confidence

_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

3. We have very solid evidence that the deals flow is... suboptimal. We've used this input to design our action plan. Note that this doc is just a draft and indexes mostly on the problem and not so much in the solution. We'll discover more action items as we execute on the project, but we're confident in the trajectory and themes we're setting.

## Project definition

#### Brief plan of attack

**UX track**

1. Study the user flow in detail. Inventorise the specific elements that are confusing users.
2. Initiate discussions about user-friendlier terminology.
3. Design a new CLI UX, prototype it, iterate.
4. Implement CLI UX changes (and underlying code changes)
5. One-stop set of JSON-RPC operations that encapsulate the new behaviour with no frills (without leaking implementation details as much as possible).

**Technical reliability track**

0. Do a full inventory of outstanding issues; get to the bottom of the long-standing mystical issues; analyse; fix. Some known tasks:
1. Testing: Design and implement test suites to reproduce the concrete issues and serve as regression tests. Nightly tests for deals.
2. Fix memory footprint issues.
3. Fix resumability of data transfers.
4. Consider p2p file-oriented transfer protocol to cut out complexity for now.
5. Identify areas of the deals flow code that need more informative logging (eg data transfer restarts / connection retries).
6. Add logs and journal events.
7. Fix miner datastore bloat.

#### What does done look like?

_What specific deliverables should completed to consider this project done?_

1. A new version of Lotus (and associated modules) that achieves the success criteria.
2. A new interactive CLI command (`lotus store`) that guides the user through the process of performing a storage deal, and provides visibility and a polished flow.
3. A simplified, porcelain S3-like JSON-RPC API that covers the deals flow and provides the logical sequence of steps outlined in previous sections, under a refined, well-documented, and opaque API that doesn't leak Filecoin implementation details.
4. (Optionally) A prototype for a deals dashboard web UI (in collaboration with The Spark).

#### What does success look like?

_Success means impact. How will we know we did the right thing?_

- 80% of deals initiated via the CLI result in success, as long as prerequisites are met (enough balance, synced node, etc.) under a variety of conditions (e.g. connection losses, slow bandwidth, concurrent deals).
- Most open issues related to deals on the Filecoin issue tracker are closed, and not reopened, and new ones related to deals are not created shortly thereafter (i.e. we don't introduce new problems).
- Users give consistent positive feedback about the usability and visibility characteristics of deal-making.

#### Counterpoints & pre-mortem

_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

N/A. There's pretty good consensus that this is a high impact project.

#### Alternatives

_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

N/A.

#### Dependencies/prerequisites

Possibly https://github.com/protocol/web3-dev-team/pull/9.

#### Future opportunities

We won't be focusing on the deals dashboard web UI right off the bat, but we could work with The Spark to deliver a prototype, and then open up a bounty/grant for full development.

## Required resources

#### Effort estimate

Large/XLarge, depending on final scope and solution design.

#### Roles / skills needed

* 2 x engineers well-versed in Lotus and Filecoin.
* 0.25 x PM.
* 1 x frontend engineer (The Spark), if we decide to prototype the web UI.
