# Indexer Node

Authors: @willscott

## What is the problem this project solves?
_Describe the status quo, including any relevant context on the problem you're seeing that this project should solve. Who is the user you're solving for, and why do they care about this problem? Wherever possible, include pain points or problems that you've seen users experience to help motivate why solving this problem works towards top-line objectives._ 

Currently, there isn't a way when a client asks for a cid - as is the current expectation in IPFS
to locate a miner and a piece that contains that cid within filecoin storage.

While the longer term answer for this problem is the full 'retrieval market', it would be good to have a shorter term answer.

## Impact
_What goals/OKRs are being addressed (for w3dt, a specific program, etc.)? Why is this project important? What do we get with this project that we can't get without it?_

This project aims to impact the goals of:
- low latency retrieval from filecoin

These are core goals that the Bedrock program aims to address. 

## The idea
_Describe the proposed project solution, at a very high level. Stay at the level of the high-level requirements. Diagrams and interface descriptions can be useful, if you have any that help clarify and explain the idea._

As described in the [indexer node](https://www.notion.so/protocollabs/Indexer-Node-Design-4fb94471b6be4352b6849dc9b9527825?d=aa69bf93-0984-4070-8ced-b18207dc7734) design document we propose a logically centralized index of cids.
Internally it will be implemented by a pool of nodes partitioning the cid space by prefix.
Each node would keep a cache in memory of requested CIDs, and a sorted index on disk of the full list of CIDs.

## Success/acceptance criteria (optional)
_How do we know we're done with this project? How do we know we're successful? This field is OPTIONAL for the first draft of an MPP. Sometimes this field needs to be filled out once we have more detail on the shape of the actual solution._

Initial success/acceptance criteria:
- We can confidently provide a scale of cids we believe this design scales to for sub 10ms query lookups.
- we can we build an index and can answer queries against the current scale of stored filecoin data.
- we have a library implementation of the index that can also be used within a sharded store within miners.


## Detailed plans (optional)
_Link to more detailed project plans, e.g. product requirements documents (PRDs) and technical design docs, once they have been created for this project._

Described in the (currently private) [design doc](https://www.notion.so/protocollabs/Indexer-Node-Design-4fb94471b6be4352b6849dc9b9527825?d=aa69bf93-0984-4070-8ced-b18207dc7734)

## Program (optional)
_If this project is part of a program, please indicate the relevant program here._

This project is part of the golden path. It most directly affects **Bedrock** program OKRs.
