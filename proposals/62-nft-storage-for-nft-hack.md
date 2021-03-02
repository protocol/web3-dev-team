# `nft.storage` for [NFTHack](https://nfthack.ethglobal.co/)

Authors: [@alanshaw](https://github.com/alanshaw)

Initial PR: https://github.com/protocol/web3-dev-team/pull/62

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

This is a proposal for time limited storage of NFT data on IPFS, backed by Filecoin and provided **free** to NFTHack participants during the hackathon.

* Register `nft.storage` (or other cool domain name) and expose a [pinning service API](https://blog.ipfs.io/2021-02-19-go-ipfs-0-8-0/#remote-pinning-services).

    This will either be a proxy to [Pinata](https://pinata.cloud/) (or other pinning service) or use PL's own [pinbot](https://twitter.com/ipfspin).
    
    This gives us space to experiment. Data storage and retrieval is de-risked by the service we pin the data to. It affords us a playground with "_real_" data that we can store on Filecoin.

    Here's some of the AWESOME things we could build and deploy in this space:

    * Create a library that automatically makes deals on Filecoin for the pinned data (use/adapt the dealbot?). This is mentioned in the [AWS Facade proposal](https://github.com/protocol/web3-dev-team/pull/34) and could be re-used here and there.

    * Implement a [deal batching service](https://github.com/protocol/web3-dev-team/pull/60) prototype for increased successful deal probability.

    * Run a "[Free Retrieval via IPFS](https://github.com/protocol/web3-dev-team/pull/52) Lotus node" that `nft.storage` can make deals with and that will expose the NFT data to IPFS.

    * Build and run a "[Retrieval from Filecoin](https://github.com/protocol/web3-dev-team/pull/57) IPFS node" that will allow NFT data we store in deals to be pulled directly from Filecoin and available via IPFS.

* Create a single page website at `nft.storage` explaining how to use the service with registration for API keys.

* Implement the [remote pinning service in js-ipfs](https://github.com/protocol/web3-dev-team/pull/58) so that it can be used in web based NFT hacks.

    If this is not ready on time, folks can always use the Pinata API directly. Obviously, for non-web based hacks users can run a go-ipfs node, configured to use `nft.storage` as their remote pinning service.

Essentially, everything after building a simple pinning service API and website is a bonus and won't effect QoS for NFTHack participants negatively.

It gives us purpose, a (albeit soft) deadline and a safe area for building out and deploying project proposals _in production_ that directly address PMF issues like deal flow and Filecoin ↔️ IPFS interop.

As an added bonus, we'll be dogfooding our own tech and ideas for greater understanding and appreciation of any difficulties. It also will help to validate assumptions made in our project proposals.

## Purpose &amp; impact 
#### Background &amp; intent
_Describe the desired state of the world after this project? Why does that matter?_
<!--
Outline the status quo, including any relevant context on the problem you’re seeing that this project should solve. Wherever possible, include pains or problems that you’ve seen users experience to help motivate why solving this problem works towards top-line objectives. 
-->

A remote pinning service API and a simple website for information and registration will exist for use by NFTHack participants to store NFT data for free for a limited time.

This will cement IPFS as the primary means of off-chain NFT storage and will raise awareness of Filecoin as a storage provider.

Currently a lot of NFT data is stored on IPFS with no clear story for permenance. Leveraging the remote pinning service API and providing guarantees of availability for the duration of the hack will prompt developers building NFT related software to think about permenance and who provides it. It will present Filecoin as an option for consideration and will likely drive some traffic to pinning services like Pinata.

#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->

* NFT users want to store NFT data on IPFS.
* NFT users want guarantees of data availability.

#### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->

* Register an API token on `nft.storage`.
* Run IPFS with remote pinning service configured as `nft.storage`.
* Pin data to IPFS node: it is stored for e.g. 1 year on `nft.storage`.

#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

<!--
Explain how this addresses known challenges or opportunities.
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

* This primarily exposes and builds on the status quo of using IPFS to store NFT data. It roughly equates to advertising for IPFS and Filecoin
* Secondarily, it gives us purpose, a (albeit soft) deadline and a safe area for building out and deploying project proposals _in production_ that directly address PMF issues like deal flow and Filecoin ↔️ IPFS interop.

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

<!--
Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

We may see an uptick in the number of developers working with NFTs that use IPFS for storage.

The component part of actually storing the NFT data on Filecoin has invaluable potential to inform us on real world usage of the API's involved with making a deal. It should enable us to more confidently build solutions knowing they are the right thing to build.

One other potential future for this project is to extend its lifetime so that we continue to receive NFT data for storage, this would allow us to measure our ability to make deals on the Filecoin network over time and make optimizations for the size and structure of NFT data.

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

<!--Explain why this rating-->

Med-Low

We do not know if any NFTHack participants will even use the service.

## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

See overview at top of page.

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

* A remote pinning API is available at `nft.storage` that pins to the chosen pinning service.
    * It exposes a feed of pinned CIDs (to be used for persisting NFT data to Filecoin).
* A service runs that consumes the pinned CIDs and attempts to store them on Filecoin.
* A beautiful and engaging website exists.
    * Has information on how to configure go-ipfs/js-ipfs to use `nft.storage` as the remote pinning service.
    * Has functionality for registration, login and API key generation.
    * Draws attention to data being backed by Filecoin.
    * Explicitly outlines period for free storage and other rules.

####  What does success look like?
_Success means impact. How will we know we did the right thing?_

<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

* \>25% of NFTHack participants use the service for persisting their NFT data.
* \>50% of NFT data submitted during the hackathon is also stored on Filecoin.
* Increased adoption of the remote pinning API in developer applications.

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

There is not a lot of time before the hackathon 😬.

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->

* Extend it as a paid for service and gift it to a pinning service to run/maintain?

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

Medium

#### Roles / skills needed
<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->

* Frontend Engineer
* Go Engineer x2
* Web Designer

Resource from other w3dt teams to implement project proposals described above:

* Sudo
* Datasystems
