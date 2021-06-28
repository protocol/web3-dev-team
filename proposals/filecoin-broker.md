# Filecoin Broker

Authors: [@ribasushi](https://github.com/ribasushi) [@mikeal](https://github.com/mikeal)

<!--
This minimal project pitch (MPP) template is for a proposal/brief/pitch for a significant project to be undertaken by a Web3 Dev project team.
The goal of project proposals is to help us decide which work to take on, which things are more valuable than other things.
-->
<!--
A minimal project pitch (MPP) should contain enough detail for others to understand what problem this project solves and why this is important for our
team's goal of achieving product-market fit, a high-level description of what the idea/proposed solution is, and space to add more detailed technical
design and planning information as we develop this information.

The MPP itself does not need to describe the work, technical design, scope, and project plan in much detail.

Projects can include work for major programs (such as Bedrock and Nitro), but they can focus on other areas, e.g. refactors for future capability,
improving our testing infrastructure, testing and validation, and other engineering-oriented projects.
-->
<!--
For ease of discussion in PRs, consider breaking lines after every sentence or long phrase.
-->

## What is the problem this project solves?
_Describe the status quo, including any relevant context on the problem you're seeing that this project should solve. Who is the user you're solving for, and why do they care about this problem? Wherever possible, include pain points or problems that you've seen users experience to help motivate why solving this problem works towards top-line objectives._

* Developers don't yet necessarily have the knowledge or ability to make deals with Filecoin miners.
* Filecoin miners currently favour large data which is not readily available to all clients who which to make deals.
* Clients do not always know which miners are accepting deals or are reputable.

## Impact
_What goals/OKRs are being addressed (for w3dt, a specific program, etc.)? Why is this project important? What do we get with this project that we can't get without it?_

This is a key component that will be used to allow developers to get data stored on Filecoin (and later retrieved) within minimal knowledge of it's workings.

## The idea
_Describe the proposed project solution, at a very high level. Stay at the level of the high-level requirements. Diagrams and interface descriptions can be useful, if you have any that help clarify and explain the idea._

* Continuously aggregate multiple sources of data and ensure it becomes stored with miners on the Filecoin network.
* Provide a way for miners who are interested in making deals to "self-serve" by downloading pre-packaged car files and then request an offline-deal-flow contract being issued against them at a time of their choosing.
* Maintain an queryable index of which miner is currently storing which data.
* Provide a means of retrieving data for a given CID from a miner who is known to store the data.

## Success/acceptance criteria (optional)
_How do we know we're done with this project? How do we know we're successful? This field is OPTIONAL for the first draft of an MPP. Sometimes this field needs to be filled out once we have more detail on the shape of the actual solution._

## Detailed plans (optional)
Refer to https://hackmd.io/8DOUz0ybT3-ipxfdhN6JIQ?view for design of the pipeline and to https://hackmd.io/O-zleFXsTdKNIyUZ-3bDDw?view for the proto-spec of the deal-packing itself (full spec coming in the next few days to the docsection of https://pkg.go.dev/github.com/filecoin-project/go-dagaggregator-unixfs )

## Program (optional)
_If this project is part of a program, please indicate the relevant program here._
