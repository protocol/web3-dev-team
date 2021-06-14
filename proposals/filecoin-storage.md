# filecoin.storage

Authors: @pooja

## What is the problem this project solves?
_Describe the status quo, including any relevant context on the problem you're seeing that this project should solve. Who is the user you're solving for, and why do they care about this problem? Wherever possible, include pain points or problems that you've seen users experience to help motivate why solving this problem works towards top-line objectives._ 

This project is being proposed in order to address a common storage developer pain point when interacting with Filecoin for the first time: -- it is **really really hard** to get started with storing/retrieving data to/from Filecoin and be successful on your first attempt. Today, even the simplest path to getting started storing/retrieving with Filecoin (lotus lite) requires installing a new tool, setting it up via a host of setup steps, and then familiarizing yourself with the Filecoin-specific concepts of "deals", "padding data up to larger file sizes", and "Filecoin-plus", etc in order to just get one simple file stored on the network. It is a lot of work, takes a long time, and requires users to learn about a bunch of new concepts that are only a means to the end of storing/retrieving data. This process can be frustrating, leading to the overwhelming feeling that using Filecoin is too hard. Anecdotally (from ecosystem team), the getting started process is hard enough that it leads to significant bounce with first-time users. It's especially unfortunate that this is the case since the current "easiest path" for users isn't even the intended golden path -- which is supposed to be storage via "aggregators" on the network for the medium-term.

While this is a bigger pain on the Filecoin side, it is also a pain for first-time IPFS users as well.

Some select quotes from hackathon devs indicating the pain:
- "I had a hard time getting my infura [IPFS] entry point set up and was a bit afraid of the own node solution for the hackathon because there was so much else to do. i would love to learn how to set up a node and how to keep files pinned"
- "Because this was really a one night coding affair, Saturday from 6pm to Sunday 10am since I didn't have a pre-planned project or team getting stuck on library dependency conflicts stymied my progress. That was the pain point. I will have a better answer in a few days. I did resolve the problem after about 3.5 hours."
- "As a software engineer with lots of networking software experience the curve is mainly voluminous in quantity but not too steep as it is mainly about learning the new models, frameworks, platforms and getting up to speed. That is the issue as opposed to some technical barrier."

The target user for this project is web3 developers that are new to our stack (our typical audience for hackathons). They may have heard about IPFS+Filecoin, but haven't ever built using our technologies before.

## Impact
_What goals/OKRs are being addressed (for w3dt, a specific program, etc.)? Why is this project important? What do we get with this project that we can't get without it?_

This project aims to impact the goals of:
- Time from zero to simple dapp on the w3stack
- Increasing the number of off-chain dapps using Filecoin for storage/retrieval

These are core goals that the Bedrock program aims to address. 

## The idea
_Describe the proposed project solution, at a very high level. Stay at the level of the high-level requirements. Diagrams and interface descriptions can be useful, if you have any that help clarify and explain the idea._

The high-level idea is to build a getting started aggregator for the Filecoin network... tentatively called filecoin.storage. This is a simple HTTP service/interface that has a JS client library developers can install in their dapp projects. The JS lib has very simple storage/retrieval functions that don't require you to know anything about Filecoin-specific concepts. filecoin.storage doesn't require you to install nodes or speak non-HTTP protocols in order to get your data IPFS content-addressed and persisted on Filecoin. filecoin.storage will leverage many of the core components of the IPFS+Filecoin golden path -- batching smaller data into larger sector-sized chunks for storage on Filecoin, making deals with DataCap, many redundant copies, and (in later milestones) retrieving from Filecoin miners with content routing via indexers.

This project will need to be accompanied with EXCELLENT, easy to understand documentation on the Filecoin docs site.

## Success/acceptance criteria (optional)
_How do we know we're done with this project? How do we know we're successful? This field is OPTIONAL for the first draft of an MPP. Sometimes this field needs to be filled out once we have more detail on the shape of the actual solution._

Initial success/acceptance criteria:
- filecoin.storage has a website landing page
- filecoin.storage has a JS client lib and is backed by the nft.storage dealmaker/broker
- 2500 signups by end of Q3
- 250 weekly active users by end of Q3
- 1TB data stored by end of Q3


## Detailed plans (optional)
_Link to more detailed project plans, e.g. product requirements documents (PRDs) and technical design docs, once they have been created for this project._

More detailed project planning in progress [in this Notion](https://www.notion.so/protocollabs/filecoin-storage-d9dae8f82b51430db39859688b87d015). Note this Notion doc is only accessible to Protocol Labs employees.

## Program (optional)
_If this project is part of a program, please indicate the relevant program here._

This project is part of the golden path, but is being executed by the Nitro program team. It most directly affects **Bedrock** program OKRs.