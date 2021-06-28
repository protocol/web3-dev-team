# NFT.storage - client side content addressing

Authors: @olizilla @vasco

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

Concurrent upload of NFT content and on-chain minting. In order to mint an NFT, creators typically need to link the token to the content by some URI. The URI must include a CID but currently NFT.storage only provides a CID _after_ content has been uploaded. This change will allow creators to generate a CID prior to uploading their content, enabling them to perform the upload and minting of their NFT concurrently.

The CID can also be used with the NFT.storage "check API" to see if it is necessary to upload the data at all.

Generating CIDs on the client side is also beneficial in a decentralized future where the client does not need to trust the service is generating a _correct_ CID for their content.

## Impact
_What goals/OKRs are being addressed (for w3dt, a specific program, etc.)? Why is this project important? What do we get with this project that we can't get without it?_

## The idea
_Describe the proposed project solution, at a very high level. Stay at the level of the high-level requirements. Diagrams and interface descriptions can be useful, if you have any that help clarify and explain the idea._

- 📡 **Update API and clients to allow a user to upload CARs.** CAR creation will be handled a separate tool... either [ipfs-car](https://github.com/vasco-santos/ipfs-car) or similar.
- 📄 **Create an explainer on how to create a car file either in the browser or server-side** that OpenSea can adopt, and switch to posting CARs so they can locally derive the CID for the asset, set it in their metadata and post the CAR to NFT.storage and guarantee that the CID they generated is the same as the one used to store the asset
    - See: [car.ipfs.io](https://car.ipfs.io)
    - See: [github.com/vasco-santos/ipfs-car](https://github.com/vasco-santos/ipfs-car)
- 🚫 **We won't focus on splitting large uploads across multiple car files yet.** It is detailed in [this proposal](https://github.com/protocol/web3-dev-team/blob/main/proposals/nft.storage-chunked-car-uploads.md).
- ⏩ Nice to have, once that's all in place, we'll look at making metadata creation something that can all be done client side as well, as part of the general direction of decentralising nft.storage. We've figured out a good pattern for creating nft metadata, now you can use it without relying on our infra kind of thing

## Success/acceptance criteria (optional)
_How do we know we're done with this project? How do we know we're successful? This field is OPTIONAL for the first draft of an MPP. Sometimes this field needs to be filled out once we have more detail on the shape of the actual solution._

## Detailed plans (optional)
_Link to more detailed project plans, e.g. product requirements documents (PRDs) and technical design docs, once they have been created for this project._

## Program (optional)
_If this project is part of a program, please indicate the relevant program here._
