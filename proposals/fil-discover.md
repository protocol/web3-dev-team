# Discover Rollout 

Authors: @jnthnvctr, @riba 

Initial PR: TBD <!-- Reference the PR first proposing this document. Oooh, self-reference! -->

## Background

Filecoin Discover is a project we publicly announced last year to help support the onboarding of a massive volume of open source, significant data. 

This project has motivated a number of important developments in Filecoin and served as a test case for many important components of Lotus that will lay the groundwork for scaled onboarding of very large datasets.

We’ve come a long way to preparing this data and making it ready for onboarding, but there are a few remaining work items that are required to both enable onboarding to begin and sure it smoothly ramps. 

## Problem Statement
We’ve broken this work into two phases - the first is required in order to begin onboarding, the second will be required to operate the onboarding process when we’re ready. 

### Phase 1 - Pre-Onboarding
1. Augment the `curl`-able app developed for nft.storage (being designed to support Filecoin Discover and nft.storage) to additionally allow for custom logic to on top of the existing rate limiting logic: 
  - Modifications: 
    - In addition to the input of miner, the end point needs to take an input of manifest + serial number
    - Runs validation logic to verify the manifest, serial number, and miner eligibility.
      - The validation logic will require
        - Taking in input from a retrieval bot to verify miners are fulfilling their obligations for fast retrieval
        - Modifying the basic rate limiting tooling in nft.storage to address Discover-specific concerns regarding onboarding
    - If eligible:
      - Curl-able app will request our Client to fire off ~32-36 deals outright
      - Returns an ordered list of lotus-miner storage-deals import-data {{propcid}} commands (for the miner to run)
    - Otherwise: 
      - Returns a “something isn’t right, come talk to us on slack”
2. A separate service (leveraging Sentinel or SQLotus) integrates the registered deals above with the retrieval-bot to validate the miner eligibility for future deals.
  - This leverages the retrieval-bot being designed for Slingshot that takes a Miner and a CID
  - The response from the retrieval-bot is fed into the validation logic above
### Phase 2 - Onboarding

Once the above tooling has been built and the other Discover [dependencies](https://docs.google.com/spreadsheets/d/1oL7ZygzDn-DxR2PVXr8LfHpR69qzjbTaZXyCTRP9Y8k/edit?usp=sharing) have landed, we will be at a stage where onboarding can begin. 

From previous work, we’ve designed a way for a lotus client to operate statelessly - this enables us to make the onboarding process largely self serve for miners. However, given the complexity of onboarding this volume of data (and the requisite rate limiting to prevent abuse) - we envision needing some amount of manual intervention (particularly in the first few weeks) to ensure the process smoothly executes.

Operationally, this will require someone knowledgeable with the deal making infrastructure to dedicate 10-20% of their time for a period of 4-6 weeks to manage the inbound onboarding volume. For the remaining weeks until 3 months, there may be small ongoing touch points depending on how many stragglers there are for onboarding. At the outset, it is likely this might be higher touch if there are miners who run into issues. The primary actions here will be: 
- Diagnosing deal making errors when the curl-able script refuses to make deals with a miner for a drive
- Ensuring DataCap is being acquired appropriately
- Manually flagging or unflagging Miners who have been designated as needing to be rate limited

####  What does success look like?

In the pre-onboarding Phase, success looks like a completed onboarding flow that will enable miners to request deals from a Client node, that Client node to verify that the miner has valid data / drives and is eligible for deal making, and for deal making to begin. 

#### Alternatives

Given the stage of Discover, there aren’t alternatives. 

#### Counterpoints &amp; pre-mortem

This seems quite high touch for a period - is it something that can be outsourced to another team? 
Unfortunately given the novel-ness of much of this work, it will require someone with a high amount of contextual knowledge and experience with our protocols. 

#### Dependencies/prerequisites

See other dependencies to Phase 2 [here](https://docs.google.com/spreadsheets/d/1oL7ZygzDn-DxR2PVXr8LfHpR69qzjbTaZXyCTRP9Y8k/edit?usp=sharing). 

#### Impact

10 - not only will this help land the largest onboarding of data onto Filecoin to date, but this will help seed the network with petabytes of valuable data. 

#### Confidence

Confidence is a 10 for Discover needs these things to begin onboarding and ramp properly.



## Required resources
Phase 1
- (block) Retrieval-bot completion
- (block - 2 weeks out) NFT.storage tooling being complete
- 1 week for 1 engineer to modify validation logic and integrate the retrieval-bot components and the NFT.storage components.


Phase 2
- (soft block) Sector spawning bug
- (soft block) PublishStorageDeal improvements
- (block) Large Scale DataCap allocations
- 4-6 weeks
  - 20% time from one engineer (propose Riba)
  - 2 part time customer support (flexible - propose JV, Davie)
