# JS-driven storing from IPFS-API to Filecoin

Authors: @willscott

Initial PR: https://github.com/protocol/web3-dev-team/pull/69


## Purpose &amp; impact 
#### Background &amp; intent
<!--
Outline the status quo, including any relevant context on the problem you’re seeing that this project should solve. Wherever possible, include pains or problems that you’ve seen users experience to help motivate why solving this problem works towards top-line objectives. 
-->

Currently, to make sure data is persistently stored in a decentralized mechanism as an IPFS user is a complicated process.
In this position, you need to get access to a filecoin node, either by running a full lotus node, or paying someone else, like
infura to run one for you. Then, on the lotus command line, you can make a 'deal' with a miner to store data.
The lotus deal process allows the source of the data to be a local IPFS node, and will then retrieve and stream the data
to the miner for storage, but there's no way to 'push' this data to the filecoin system from IPFS even though doing
so is conceptually similar to the existing 'remote pinning' API that does already exist for centralized pinning providers.

#### Assumptions &amp; hypotheses

* IPFS users wish to store data persistently in filecoin

#### User workflow example

Alice has been using [Pathephone](https://pathephone.github.io/) as a desktop music player with an IPFS database (or a similar dapp) and
wants to store the data longer term. Alice searches for how to 'backup IPFS music' and finds a web page that walks her through the process.

This page asks her to link her filecoin wallet, or allows her to transfer filecoin to a local wallet address generated within the browser session.
It then makes a deal with a miner and backs data she selects up to filecoin.

#### Impact
High. There's a gap with no 'golden path' between ipfs and filecoin at the moment

<!--
Explain why you have chosen this rating
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

#### Leverage
Medium. The core logic can serve as a re-usable block for other adaptions and scenarios - e.g. ones wehre a developer pays on behalf of a user, or a more full-featured dapp that makes use of backup within itself.

<!-- Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

<!--Explain why this rating-->
1-3 - we know there should be something. we haven't heard this approach directly asked for.


## Project definition
#### Brief plan of attack

A core JS library that uses the local IPFS library to
(1) determines the total size of the dag to pin from a root CID using the IPFS API
(2) talks to a lotus / light lotus api endpoint to submit a signed deal proposal and uses the market to find a miner and make a deal with the miner for suffient space to store the dag.
(3) Either 
    (a) the miner attempts a content retreival of the CID over the IPFS network and establishes a connection back to the originating IPFS node, or
    (b) the ipfs client is instructed to dial the miner and
    (c) a bitswap session is set up for transferring the dag.



#### What does done look like?

It is possible for a js DAPP and local IPFS daemon to store deals to filecoin miners

* A dapp proof of concept
* Changes to lotus to handle data retreaval from a non-lotus client
* Changes to ipfs to bitswap with another libp2p node from local API direction.


####  What does success look like?

* IPFS users pin data to filecoin

#### Counterpoints &amp; pre-mortem
* A golang 'lotus-light' might be easier to wrangle than a js library
* perhaps the local filecoin-portion should be able to publish messages to the filecoin network directly rather than needing an api to a lotus node somewhere
* perhaps signing / paying can live on a lotus node somewhere that a developer controls


#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->

## Required resources

#### Effort estimate
Possibly 2 projects to tear apart
(the "transfer from an ipfs node to a filecoin node" data work, and the js library work.)

#### Roles / skills needed

* knowledge of js-ipfs
* knowledge of ipfs's API
* Knowledge of lotus API
* knowledge of crypto / js wallet
* data transfer fu
