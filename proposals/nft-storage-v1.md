# nft.storage v1 

Authors: @mikeal @alanshaw

Initial PR: TBD <!-- Reference the PR first proposing this document. Oooh, self-reference! -->

## Purpose, Impact, Definition 

We have a round of features and improvements we want to make to nft.storage.
Each feature is the first step towards larger ongoing efforts so we're packaging
this work as "v1" as it sets the scope of the project for the rest of the quarter.

Those efforts are:

* [Metadata Creation API](https://github.com/ipfs-shipyard/nft.storage/pull/56)
  * Most users don't want to create these metadata files by hand. We can significantly reduce
  errors and inconsistencies by doing this ourselves.
  * This interface also sets us up to extend the metadata for other use cases. Eventually this
  will turn into a larger spec project to define schemas for common use cases in NFTs.
* Import all Ethereum NFT data
  * The beauty of a permissionless public ledger is that we don't need anyone's permission
  to just go and grab this data and store it for the benefit of NFT developers.
  * This will go a long way toward reducing the number of "missing" NFTs.
  * Once we have the data indexes we can start to provide other web visualizations, APIs, and
  widgets for developers to leverage the public chain data.
* Wallet Auth
  * We need to migrate to magic.link anyway for our authentication. Once that is complete,
  adding wallet authentication will be easy.
  * This substantially reduces the barrier to entry for using the service. Developers
  won't need to signup with us or run any backend service, they can use our JS client
  or widget to simply mint the NFT and sign an auth token with us that is leveraged for the
  storage interface.
* Batched Filecoin Deals
  * The service should be batching deals on a regular basis even if there hasn't been a full
  sector's worth of data added to the service.
  * The exact methods and data structures for this initial version are simple and rely on 
  a centralized index of the data.
  * Eventually this process will migrate to a better collections data structure and is on a roadmap
  to be fully decentralized.

#### Background &amp; intent

In its current state, nft.storage is a great free pinning service with a few APIs that provide
sugar for NFT developers. After this work the scope, mission and roadmap of nft.storage will be clear
and much broader than "pinning."

* Both active and passive storage (you give us the data via an API **and** we pull data out of public chains.
* We provide indexes and useful tools for developing NFT applications against public data.
* Everything in nft.storage is backed up in Filecoin and *eventually* that process will be integrated
  into the initial storage request/transaction.
* We are storing this data on behalf of NFT **users** as well as *developers*. In a decentralized
  application model data is leverage by multiple applications so it's important that the storage
  solution is not scoped to a single application.

#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_

NFT development is currently popular and rising in popularity. If that changes this project would
matter less.

#### User workflow example
_How would a developer or user use this new capability?_

That varies by interface, detailed above and in individual feature PR's.

#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

This will meet the user needs around NFT's **today**. It's not the fully realized decentralized
dream since we are meeting these user needs with a centralized service, but it puts all of these
user workflows on our core protocols which is the most important part.

#### Internal leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

This will lead to more users which we can continue to leverage to identify additional user needs.

This will also capture a lot of data about NFT's in public chains that we can learn from.

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

8

## Required resources

#### Effort estimate

- Small, 1-2 weeks
- Medium, 3-5 weeks

Most of these will land in under 2 weeks. A few may stretch out beyond that but not by much for these
initial releases.

#### Roles / skills needed

The whole Spark team along with key Product and Marketing folks.
