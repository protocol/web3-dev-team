# IPFS nodes speak Graphsync

Authors: @willscott

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

Currently, ipfs nodes speak [bitswap](https://docs.ipfs.io/concepts/bitswap/) for exchanging blocks of data. bitswap works at a block layer where you ask for a CID, and get back the block that hashes to that cid.

[graphsync](https://github.com/ipfs/go-graphsync) is a protocol for synchronizing graphs of data across peers. It allows a host to make a single request to a remote peer for all of the results of traversing an IPLD selector on the remote peer's local IPLD graph. It is what filecoin uses.

#### Assumptions &amp; hypotheses

* There are cases where users will want to retrieve a piece of structured data they can efficiently describe with a selector, but which would be expensive to retrieve with bitswap.
* There are cases where it would be valuable for an IPFS node and a filecoin node to exchange data.

#### User workflow example

* A user would ask for data using a selector in e.g. the [go-fetcher](https://github.com/ipfs/go-fetcher) interface within IPFS (from a plugin)
* An API is built such that dag exploration of ipld nodes from a client built on IPFS is translated into selectors
* a client builds a car of data to store, creates a filecoin deal for it, and the miner fetches the data from an IPFS client with graphsync

#### Impact

High. we invision cases where we want IPFS and filecoin nodes to be able to communicate

#### Leverage

High. we have other projects that are enabled by IPFS and filecoin nodes being able to communicate

#### Confidence

Two. We haven't heard direct requests for this flow, but it's our best guess at what's practical.


## Project definition
#### Brief plan of attack

[go-merkledag](https://github.com/ipfs/go-merkledag) currently takes a [blockservice](https://github.com/ipfs/go-merkledag/blob/bf51443272bb98cff071eb44ed9ce6c940e82f1f/merkledag.go#L32).  It should also be able to be created from a graphsync provider, or both. We can initially enable graphsync as an opt-in option, and need to design a transition (e.g. do we have merkledag make requests to both graphsync and to blockservice when present? do we make this code somewhat peer-aware, so we know based on provider which one to use?)

#### What does done look like?

* IPFS nodes advertise support for the graphsync multiprotocol
* When an IPFS node at the go-merkledag level receives a request including a selector, it attempts a graphsync session if the other node also advertises support for graphsync.

####  What does success look like?

* observation of increased use of graphsync 

#### Counterpoints &amp; pre-mortem

* graphsync wasn't as ready as we expected
* merkledag / blockservice needed a re-factor to become peer-aware before we added graphsync

#### Alternatives

* we live with bitswap

#### Dependencies/prerequisites

* [ipld in ipfs](https://github.com/protocol/web3-dev-team/pull/25)

#### Future opportunities

moves us a step closer to ipfs and filecoin nodes being able to exchange data

## Required resources

#### Effort estimate
Medium

#### Roles / skills needed

* Understanding of bitswap
* Understanding of IPFS
* Understanding of merkledag
* Understanding of graphsync