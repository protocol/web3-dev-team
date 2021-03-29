# Minty in the browser - Mint NFTs end to end inside a decentralized web app using js-ipfs

Authors: @yusefnapora

Initial PR: [#92](https://github.com/protocol/web3-dev-team/pull/92) 


## Purpose &amp; impact 
#### Background &amp; intent

In mid-March 2021, based on [this earlier proposal](https://github.com/protocol/web3-dev-team/pull/11) we published a guide on the IPFS docs side called [Mint an NFT with IPFS](https://docs.ipfs.io/how-to/mint-nfts-with-ipfs/), which walks through an example app called [minty](https://github.com/yusefnapora/minty) and dissects the code to show how everything works.

In the interests of simplicity and shipping quickly, minty is a command line Node.js app and can't run in its current form inside a web browser. This proposal outlines the work required to make minty work end-to-end in an ethereum-enabled browser (e.g. with the MetaMask extension).

#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_

- D-app developers want to mint NFTs using IPFS without relying on a centralized backend server
  - This may not actually be the case. I'm not aware of any NFT platform today that's "fully decentralized" in the sense of doing everything on chain without a backend API.

- We want to encourage d-app devs to use js-ipfs directly in their d-apps, as opposed to using an HTTP api from Pinata, nft.storage, etc
  - This seems like a good thing to encourage, but it also raises the bar for adoption a bit, since js-ipfs is a heavier dependency than an HTTP client and may require learning new concepts, etc.
  
- D-app devs are willing to use a remote pinning service for persistence
  - A js-ipfs instance embedded in a browser isn't a great long-term data storage solution for an NFT. The most practical flow I can see is to add content to local js-ipfs and then request a remote service to pin it using the remote pinning API.
  - Minty already uses the remote pinning API, but a browser IPFS instance is more "ephemeral" than a local IPFS daemon, so pinning isn't really optional if we want a good user experience.
 
- D-app devs can manage pinning service credentials in a secure way in the browser
  - A platform can't easily send their own pinning service access token to the client's browser without exposing it, so they would either need to accept user-provided pinning service credentials, or proxy requests to the pinning service to add their own token.
 
- Remote pinning services support js-ipfs browser clients
  - Because the remote pinning API transfers data via bitswap, we need to establish libp2p connections from the service's delegate nodes to the local IPFS node. This likely requires the pinning service to include `ws` or `wss` websocket addresses that are reachable by browser clients.

- IPFS in the browser can reliable retrieve content for published NFTs
  - This may require delegated routing, since content lookups will likely need to hit the IPFS DHT.
  - We may be able to accelerate some lookups by connecting to gateways provided by a pinning service.

#### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->

- A developer deploys an instance of the minty smart contract and compiles the minty frontend web application. 
- The web app requires no backend, so could be completely hosted on IPFS or any other static site host.
- Once the frontend is published, an end user can log into it with an Ethereum wallet (e.g. MetaMask) configured for the network that Minty has been deployed to.
- To mint an NFT, a user drags a file into the browser, which causes it to be added to a local js-ipfs instance, along with the NFT metadata.
- The browser makes a request to a remote pinning service to fetch the data and persist it.
- The browser calls the smart contract's `mintToken` function to create a new token that references the IPFS uri of the NFT.
- When viewing tokens, the browser queries the metadata URI from the smart contract and uses js-ipfs to resolve the metadata and NFT asset.

#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

Minty currently shows how IPFS and Etherum can play nice together, but it doesn't "feel like" the d-apps people are familiar with, which tend to run in the browser. As such, there's a gap between what minty can do and what people are likely to want to do in the real world. That risks people getting excited about making things work in the browser but then encountering too much friction to succeed, which would give a bad impression and may cause people to reject IPFS as a concept because of implementation issues.

Demonstrating how to mint NFTs using IPFS completely in the browser would help position IPFS as an off-chain storage solution for d-apps that don't want to depend on a backend service.

Caveat: the requirement to use a remote pinning service is a "centralizing" factor, but there's no "lock in" with pinning services as there would be with data published to an HTTP domain; the data can be re-pinned later with any provider without changing the address. It's also easy to imagine a path from pinning services to Filecoin-backed persistence in the future, which would allow full decentralization and could potentially be integrated with Ethereum smart contracts to renew deals, etc.

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

There are two broad scenarios that could play out if we develop this proposal:

- The technical prerequisites outlined in the assumptions section are currently satisfied, and we can make minty work in the browser today. 
  - This would be great, but it would indicate that we have a documentation gap, since it's not obvious today how to make everything work, especially to IPFS newcomers.
  - A version of minty that works in the browser could be a compelling demonstration of IPFS as off-chain storage.
  
or:
  
- There are technical blockers to making minty work in the browser today.
  - In this case, the benefit of this proposal is that we have a concrete goal to work towards to resolve those blockers: get minty working in the browser.
  - Once any blockers are resolved, we'll have a more complete and usable solution for off-chain storage, as well as an example that people can fork and modify, etc.


#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

<!--Explain why this rating-->
0.1 - I haven't had anybody reach out about this specifically. 
Personally, I think it may be worth waiting to pick this up until we do get some inbound signal that this is something people definitely want, but I wanted to write the proposal now while Minty is fresh in my head :)

## Project definition
#### Brief plan of attack

1. Resolve any blockers to adding + remote pinning using js-ipfs within a browser environment
2. Write a simple web UI for minty that assumes users have MetaMask or a similar wallet installed
3. Update minty's build process to bundle the contract address and other info into the frontend
4. Test and verify that everything works end-to-end without a backend server
5. Deploy an instance of the contract to an Eth testnet and put the Web UI up somewhere for people to play with

#### What does done look like?
A version of minty exists that can mint and view NFTs completely in the browser, using js-ipfs and MetaMask (or a similar ethereum bridge).


####  What does success look like?
_Success means impact. How will we know we did the right thing?_

Apart from pageviews, repo forks, etc, we could potentially deploy an instance of the minty contract to an ethereum testnet and host the completed web application somewhere. That could give us a rough idea of how many people were interested enough to play with the deployed version. 

We could also do a separate deployment that's not wired to a frontend, but give users instructions on how to build the frontend and connect to the deployed contract. If anyone mints a token from that contract, we can infer that they were able to follow the instructions.

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

People might not actually want their NFT platforms to run without a backend API. Platforms offer services beyond just NFT minting (social reputation, user profiles, etc), and a real-world platform is likely to need a backend anyway. So, it may be simpler for them to just run IPFS on the backend, and just do the contract interactions in the browser.

Similarly, d-app developers may decide they'd rather use an HTTP API for a pinning service instead of using js-ipfs and the pinning service API. This would tie them to a specific pinning provider, but that might be an acceptable tradeoff for reduced js bundle sizes and code complexity.

It's also possible that pinning services won't see value in providing websocket addresses and otherwise ensuring their infrastructure works well with js-ipfs in the browser. I haven't explored the current situation enough to know if this would require significant effort / maintenance cost on the pinning service's part.

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

Instead of developing minty, which is specific to the NFT use case, our efforts might be better spent on making a more generic "off chain storage" js library or boilerplate repo that doesn't deal with NFTs. This could provide interfaces for adding data to IPFS and persisting it (using pinning services today, Fil tomorrow). 

Ideally, such a library could be used to make an app like minty much more quickly and with less code, which could give us more leverage than continuing to develop this one example app further.

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

- Support for the remote pinning service api in js-ipfs
  - in progress: https://github.com/ipfs/js-ipfs/pull/3588
- Working bitswap connections between js-ipfs and pinning service delegate nodes
  - status is unclear... pinata seems to return DNSLink addrs that resolve to TCP multiaddrs for their host nodes.

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->

Once we get things working, we could generalize the technique and make an "off-chain storage support library" to make things simpler for users. 

We can also update the guide on the docs site to use the GUI version of minty instead of / in addition to the CLI.


## Required resources

- 1 or 2 developers
- one PM / support person (part time)

#### Effort estimate
<!--T-shirt size rating of the size of the project. If the project might require external collaborators/teams, please note in the roles/skills section below). 
For a team of 3-5 people with the appropriate skills:
- Small, 1-2 weeks
- Medium, 3-5 weeks
- Large, 6-10 weeks
- XLarge, >10 weeks
Describe any choices and uncertainty in this scope estimate. (E.g. Uncertainty in the scope until design work is complete, low uncertainty in execution thereafter.)
-->

Small to Medium, not counting work needed to satisfy the dependencies / pre-requisites. I think the web UI could be built out and tested in ~2 - 3 weeks, assuming all the IPFS bits work.

#### Roles / skills needed
<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->

- Web developer to build out frontend app
- Someone (probaby yusef) to refactor minty to work well in the browser environment
  - build process
  - remove assumptions about access to the filesystem, etc
- Maybe: someone to coordinate with pinning service partners to ensure websocket support
  - we could also potentially add support to nft.storage ourselves
