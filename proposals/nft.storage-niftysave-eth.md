# NFT.storage - niftysave (Ethereum)

Authors: [@gozala](https://github.com/gozala) [@alanshaw](https://github.com/alanshaw)

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

Many Ethereum based NFTs exist today that link to content that is either **not on IPFS**, or **is on IPFS** and will be available for an unknown period of time or **was on IPFS** and is currently unavailable.

Missing data has a negative impact in the NFT community and missing data that is meant to be on IPFS has a negative impact on IPFS and decentralized storage in general.

The niftysave project aims to _save_ all existing and future NFTs by storing them on NFT.storage where they will be safely stored and guaranteed to be retrievable for as long as possible.

## Impact
_What goals/OKRs are being addressed (for w3dt, a specific program, etc.)? Why is this project important? What do we get with this project that we can't get without it?_

* Storing humanity's important history.
* Good PR for IPFS & Filecoin.
* Exposure for Filecoin.
* An index of all NFTs on Ethereum.
* Stress testing of NFT.storage and more real world data for our Filecoin data aggregation pipelines.

## The idea
_Describe the proposed project solution, at a very high level. Stay at the level of the high-level requirements. Diagrams and interface descriptions can be useful, if you have any that help clarify and explain the idea._

This project aims to ensure NFTs on the Ethereum chain are not lost, by:

1. Inspecting the chain to find existing ERC721 (NFT) compatible contracts.
2. Continue following the chain to import data for newly minted NFTs.
3. Adding content to IPFS that is not already in IPFS.
4. Storing NFT data on NFT.storage, which ensures permenant storage on IPFS and Filecoin.

## Success/acceptance criteria (optional)
_How do we know we're done with this project? How do we know we're successful? This field is OPTIONAL for the first draft of an MPP. Sometimes this field needs to be filled out once we have more detail on the shape of the actual solution._

## Detailed plans (optional)
_Link to more detailed project plans, e.g. product requirements documents (PRDs) and technical design docs, once they have been created for this project._

## Program (optional)
_If this project is part of a program, please indicate the relevant program here._
