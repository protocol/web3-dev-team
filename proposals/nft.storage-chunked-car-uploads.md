# nft.storage chunked CAR uploads

Authors: [@alanshaw](https://github.com/alanshaw) [@vasco-santos](https://github.com/vasco-santos) [@olizilla](https://github.com/olizilla)

## What is the problem this project solves?
_Describe the status quo, including any relevant context on the problem you're seeing that this project should solve. Who is the user you're solving for, and why do they care about this problem? Wherever possible, include pain points or problems that you've seen users experience to help motivate why solving this problem works towards top-line objectives._ 

NFT.storage has a hard limit of 100MB for uploads - a limit imposed by Cloudflare Workers (the server side technology that runs the site).

This project proposes a way to work around this limit by sending _multiple_ requests of <100MB.

## Impact
_What goals/OKRs are being addressed (for w3dt, a specific program, etc.)? Why is this project important? What do we get with this project that we can't get without it?_

Allows NFT assets over 100MB to be reliably uploaded to nft.strorage.

This has been requested by multiple marketplaces and is necessary for NFTs that contain video content.

## The idea
_Describe the proposed project solution, at a very high level. Stay at the level of the high-level requirements. Diagrams and interface descriptions can be useful, if you have any that help clarify and explain the idea._

1. Generate a CAR file for the content.

    This has the added benefit of allowing the creator to know the CID up front, allowing them to mint an NFT on a blockchain and upload the content to the nft.storage in parallel.
    
2. Split the CAR file into chunks of <100MB.

    The splitting process does not attempt to understand the DAG, it simply reads the blocks until it has reached 100MB and then starts creating a new CAR with the remaining blocks.
    
    Each CAR has a "chunk root" node which references all the blocks and roots (only the first chunk) in the CAR.
    
    There is a JS module that will perform the chunking: https://github.com/alanshaw/carbites
    
3. Upload the chunks.

    As nft.storage receives the CAR chunks it adds them to IPFS Cluster, pinning the "chunk root" with an **expiry time**.

    Pinning the chunk root node ensures all the blocks in each CAR do not get garbage collected since the chunk root references all the blocks the CAR contains.

    There's no guarantee of order for blocks in a CAR and also no guarantee of order nft.storage will receive the chunks in, so pinning the chunk root mitigates against garbage collection of partial DAGs.

    The expiry time ensures that the chunk root nodes can eventually be garbage collected and also ensures that uploads that never complete can eventually be garbage collected.

4. Pin the root.

    Once all the chunks have been uploaded the actual root CID can be pinned.

    The `https://api.nft.storage/pins` API can perform this action (which is an existing part of the pinning service API).

    We may choose to create a separate HTTP endpoint for this.
    
    This could be done first, but it would cause IPFS to do work to attempt to find the blocks before they are uploaded.
    
    Pinning the root last also ensures nft.storage has all the data for the NFT before it is registered to the user. It's an insentive to continue uploading all the chunks, avoiding any blame for losing data in the case where a user ceases uploading before completion.
    
### Alternative

For completeness, an alternative was suggested that could also work:

1. Generate a CAR file for the content.
2. Split the CAR file into chunks of <100MB. Chunks following the first have an ["empty" CID `bafkqaaa`](https://cid.ipfs.io/#bafkqaaa) as their root node. [See recommendation](https://github.com/ipld/specs/blob/master/block-layer/content-addressable-archives.md#number-of-roots).
3. Upload and pin the root. We'd need to ensure the first CAR contains the root node.
4. Upload the remaining chunks.

Advantages:

* Simplified chunked CAR file creation.
* No separate pin request.

Disadvantages:

* An NFT is registered to the user before all data is received.
* An out of order CAR chunk _may_ be garbage collected since it could be unreachable from the pinned root node.
* Failure to upload all chunks will likely result in an NFT registered to a user with missing data forever.
* A CAR file created with blocks in random order could get garbage collected.

## Success/acceptance criteria (optional)
_How do we know we're done with this project? How do we know we're successful? This field is OPTIONAL for the first draft of an MPP. Sometimes this field needs to be filled out once we have more detail on the shape of the actual solution._

Assets larger than 100MB can be uploaded to nft.storage.

## Detailed plans (optional)
_Link to more detailed project plans, e.g. product requirements documents (PRDs) and technical design docs, once they have been created for this project._

Flow diagram:

![Flow diagram](https://ipfs.io/ipfs/Qmf2pwX8PrLqt5pfJRgZV1VW2xxa1KNfp6wZfj1NRtnmTn)

CAR chunking with chunk root:

![CAR chunking with chunk root](https://ipfs.io/ipfs/QmVQty2S8jCBrUckrqhVVntw88dLEAcPq1bK9rWFobg6Ye)

Where each chunk root node links to the following blocks:

```
bafkcbrt0 -> bafyroot0, bafkblock0, bafkblock1, bafkblock2
bafkcbrt1 -> bafkblock3, bafkblock4, bafkblock5, bafkblock6
bafkcbrt2 -> bafkblock7, bafkblock8, bafkblock9
```

## Program (optional)
_If this project is part of a program, please indicate the relevant program here._

/Nitro/NFT
