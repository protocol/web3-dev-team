# CAR-native DAG store

Authors: @raulk

## What is the problem this project solves?

_Describe the status quo, including any relevant context on the problem you're seeing that this project should solve. Who is the user you're solving for, and why do they care about this problem? Wherever possible, include pain points or problems that you've seen users experience to help motivate why solving this problem works towards top-line objectives._ 

In Lotus, the monolith Badger blockstore is a point of contention during deal making. Inbound data transfers are placed in the Badger store, and outbound data transfers are staged in the badger store from their unsealed copies. Other processes such as commP calculation also feed off the Badger store. In reality, the only reason that Badger is used is to provide random access to IPLD DAGs. Unfortunately Badger does not scale well for this use case beyond 100s GiB, thus becoming a bottleneck and fragile element in the deal-making process.

The purpose of the CARv2 + DAG store endeavour is to eliminate overhead from the deal-making processes with the mission of unlocking scalability, performance, and resource frugality on both miner and client side within the Filecoin network.

## Impact
_What goals/OKRs are being addressed (for w3dt, a specific program, etc.)? Why is this project important? What do we get with this project that we can't get without it?_

As the volume and frequency of deals increases in the networks, miners need to be able to handle those volumes, otherwise the foundation is shaky. Badger is currently a weak link that introduces enormous overhead. Eliminating this buffering will make deal-making more efficient, stable, and performant.

## The idea
_Describe the proposed project solution, at a very high level. Stay at the level of the high-level requirements. Diagrams and interface descriptions can be useful, if you have any that help clarify and explain the idea._

Refer to https://github.com/filecoin-project/dagstore/pull/2.

## Success/acceptance criteria (optional)
_How do we know we're done with this project? How do we know we're successful? This field is OPTIONAL for the first draft of an MPP. Sometimes this field needs to be filled out once we have more detail on the shape of the actual solution._

DAG store is implemented and integrated in Lotus.

## Detailed plans (optional)
_Link to more detailed project plans, e.g. product requirements documents (PRDs) and technical design docs, once they have been created for this project._

Technical architecture doc: https://docs.google.com/document/d/118fJdf8HGK8tHYOCQfMVURW9gTF738D0weX-hbG-BvY/edit#.
Technical design: https://github.com/filecoin-project/dagstore/pull/2.
Technical plan: https://linear.app/protocol/issue/W3D-6/

## Program (optional)

Bedrock M1.
