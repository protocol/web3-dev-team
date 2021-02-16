# Proposal: A tutorial for building NFTs with Ethereum and IPFS

Authors: @yusefnapora

Initial PR: [#11](https://github.com/protocol/web3-dev-team/pull/11) 

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

A lot of current interest in our stack is driven by decentralized finance applications, especially "non-fungible tokens" (NFTs).
NFTs are tokens with a unique identity, which can have associated metadata. This [OpenSea NFT Bible](https://opensea.io/blog/guides/non-fungible-tokens/)
has a good overview of what NFTs are and the history of their development over the past few years.

We don't currently offer advice or guidance to users interested in creating NFTs and storing their metadata on IPFS. As a result, we have limited "empathy" for their specific needs, and are largely unaware of their unique pain points, and users building NFTs need to rely on third party resources.

This proposal is to build a guided tutorial that creates an NFT token on ethereum that links to assets stored in IPFS using IPFS cids in the token metadata.

#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->

- Users want to store NFT assets on IPFS
  - Seems to be supported by evidence, e.g. Pinata fireside chat
- Users are confused about how IPFS can be leveraged when developing NFTs.
  - Uncertain. Perhaps existing resources, e.g. from Pinata are enough?
- We at Protocol Labs would gain a better understanding of a key user demographic by producing this tutorial
- The existence of this tutorial would be a positive signal to ethereum devs that PL is invested in things that matter to them

#### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->

A developer interested in building NFTs googles "IPFS NFT" and finds our tutorial. At a glance, they can tell that:

- IPFS is a great fit for NFTs
- A proof-of-concept is acheivable in less than a day

They decide to spend an afternoon following along. At the end, they have a working token that runs on a local ethereum devnet, with content persisted to their local IPFS daemon.

To wrap up the tutorial, we talk about the "path to production," which would require pinning IPFS content, etc. This gives devs
a clear sense of what they'll need to do to get from toy example to raking in that sweet crypto kitty cash.

#### Impact
_How directly important is the outcome to web3 dev stack product-market fit?_

🔥 = 0-3 emoji rating

I think this tutorial would be valuable, but it's not a "make or break" proposition, hence the one 🔥 rating.

Other tutorials already exist, for example, [this very fine guide by our friends at Pinata](https://medium.com/pinata/how-to-build-erc-721-nfts-with-ipfs-e76a21d8f914),
and these may already serve the needs of NFT developers well enough.

The main impacts from having our own tutorial are:

- NFT developers know that we are aware of and support them
- We control the messaging around how IPFS fits into the NFT picture
  - I think this is important because we're not the only option. You can build NFTs backed by an S3 bucket, etc.
- We can set the stage for a future IPFS / Filecoin NFT pinning service (e.g. as described in https://github.com/protocol/web3-dev-team/pull/3) in our "path to production".
  
<!--
Explain why you have chosen this rating
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

🎯🎯 = 0-3 emoji rating

The benefits of developing this tutorial would be as much for us at Protocol Labs as for our end users. If NFT developers are a key part of our audience / userbase, we should be working to empathize with and understand them as much as possible. As a prerequisite for writing the tutorial, we'll need to understand exactly how NFT devs are currently using IPFS. This will give us insight into things we need to improve and will let us speak more confidently as an organization about the needs of this highly specialized community.


#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

0.1
<!--Explain why this rating-->

I have no data to support my assertions about impact, just "self conviction" and general hunches.

## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->
- Do a brief review of existing tutorials & resources. Follow along with at least one other guide (ideally 2+) to completion.
- Define the scope and functionality of the example project
  - e.g., should our toy tokens try to "do something" like crypto kitties?
  - do we assume readers already know solidity & are familiar with eth dev?
- Build the example and prove it works
- Write the tutorial to guide users through building it themselves


#### What does done look like?
_What specific deliverables should completed to consider this project done?_

The tutorial exists and has been advertised via our social media channels, etc. A user with no prior experience building NFTs with IPFS can follow the tutorial through to completion.

####  What does success look like?
_Success means impact. How will we know we did the right thing?_

- We get traffic to our tutorial & engagement on social media when announced
- We solicit feedback at the end of the tutorial. Hopefully captures positive sentiment.

<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

- If NFT developer needs are already being served, e.g. by Pinata tutorials, they may not care much about ours.
- Our internal learning / empathy building benefits may be less than expected or hard to scale within PL. In other words, the team builiding the tutorial may learn something, but that may not translate to greater understanding org wide.
- We may not be well-equiped to define "best practices" for NFT + IPFS development, because we're not yet intimately familiar with the domain.
- The NFT "landscape" is rapidly evolving, which risks this tutorial going stale. If major changes occur in e.g. the ethereum tooling we recommend, we need to keep the tutorial updated or risk losing credibility.

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

- Education:
  - Prominently link to and promote external resources (e.g. pinata tutorial)

- Community building:
  - Establish a category on discuss.ipfs.io to discuss NFT development and engage with the community. Have someone at PL monitor and engage with the forum.
  - Invite NFT developers to have a sync "fireside chat" style discussion with PL devs, to solicit feedback

- "leveling up" internally:
  - have an "NFT workshop" event that people at PL can join to build an NFT on IPFS, to get our hands dirty with the tech & build empathy

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

We need a place to put the tutorial (docs.ipfs.io, or elsewhere?).

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->

If we develop tooling / new capabilities that are tailored for NFTs (e.g. https://github.com/protocol/web3-dev-team/pull/3), we can use the tutorial as a starting point to advertise and explain the new stuff.

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

Medium, ~3-5 weeks for a team of 2 or 3 people. Less if the team has prior experience building NFTs with IPFS.

#### Roles / skills needed
<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->

- "solution builder" who can design and implement the example token
  - a dev with prior experience building on ethereum would be a plus and could shave 1-2 weeks off the time estimate.
- technical writer to develop the tutorial.
- ideally, at least one other technical writer to review and revise (part time)
- devs with little / no prior experience to beta test and validate that the tutorial is possible to complete
