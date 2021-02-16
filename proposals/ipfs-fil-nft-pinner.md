# Proposal: IPFS+FIL NFT Pinner

Authors: @momack2

Initial PR: TBD <!-- Reference the PR first proposing this document. Oooh, self-reference! -->

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
There should be a site/API that enables easy pinning for NFT creators to store IPFS-addressed NFTs to Filecoin similar to ipfs2arweave.com 

There is a huge explosion in NFTs happening this year, most of which are content addressed off-chain data that are a perfect fit for IPFS -- but the persistence of those NFTs (so the font or video you bought doesn’t vanish) needs long-term, decentralized resiliency not well supported by IPFS alone. To fill this need, Filecoin needs to offer a very simple pinning endpoint that NFT devs can trust will continuously back up their data resiliently to Filecoin without having to worry about choosing specific miners, running a node, handling the batching of many small files, etc.

#### Assumptions &amp; hypotheses
- NFTs need to be growing
- NFT devs need to have persistence needs not met by IPFS alone

#### User workflow example
A developer would go to a website that walks them through the exact code snippets to add to their NFT as it's minted to persist it to IPFS+Filecoin, giving them the cid to stamp into the blockchain as the NFT's content ID. Marketplaces would test out this code snippet and add to their minting platform, calling an easy API / service that handles the data persistence (making redundant storage deals with a number of miners). The NFT developers can then look up the deal record to see evidence of it's persistence over time with various Filecoin miners ([a la slate](https://slate.host/_?scene=NAV_STORAGE_DEAL)).

#### Impact
🔥🔥🔥  -- we are currently at risk of a large and quickly growing area of static asset storage on web3 (the very closest market of PMF users we are aiming for) developing a standard for an alternative distributed storage network vs Filecoin. The standard here will emerge in the next few months - and other players in this space are quickly moving with a simple/easy solution. This should be our bread and butter and we’re going to miss it!

#### Leverage
🎯 -- Nailing the NFT use case is very core to our value offering, and would likely "pull" additional useful improvements from our work (and maybe inspire other groups to add similar functionality a la Fleek for NFTs) - but it won't directly improve our execution velocity.

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

**~1-3** (competitors have it, interested customers, many already using IPFS but not FIL - ex rarible)
We haven’t done deep research or made a POC here, but there’s a lot of organic IPFS adoption and Filecoin competitors have this feature.

## Project definition
#### Brief plan of attack

Create an easy way for NFT developers to smoothly add their data to IPFS and Filecoin as part of minting a new NFT (see sample flow here). 

**Option 1:** We create a site & API backed by an IPFS+Filecoin (maybe powergate node?) service that constantly takes new NFT storage requests and stores them to the network
- We sponsor all storage deals for now (registering for FIL+ Data Cap to minimize cost)
- Audit deal success and make new deals as needed
- Integrate this site/API into NFT minting flows (PRs to opensea, mintbase, etc)
- Ensure all pinned NFTs can be served via IPFS gateway

**Option 2:** Create a “collection” actor in Filecoin for storing long-lived threads of data
- (TBD - needs scoping)
- Would need to NOT require NFT users running a lotus node (remote deals)

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

todo

####  What does success look like?

If we succeed, the large influx of NFTs being created will all be stored to Filecoin (and Filecoin+IPFS can become the defacto standard here). If we fail, it’s likely that groups will position themselves as the “trusted storage layer” that is easy to use for web3 devs - competing for a growing share of web3 storage.

Metrics to track:
- number of NFT devs / creators building on IPFS&Filecoin (via this service/protocol)
- number & size of storage deals made for NFTs via this service/protocol
- number of of NFT marketplaces that recommend Filecoin for storage
- % of new NFTs created that are stored with an IPFS cid

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

todo

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

todo

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->
todo

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->
todo

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
TBD - but likely ~M for option 1 (something the prototyping team could accomplish in a single sprint)

#### Roles / skills needed
<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->
- IPFS API design
- (TBD) Textile threads?
- Filecoin deal making
- Infra
- FE website design
