# Hi-speed Chain Store

Authors: @hannahhoward @acruikshank @willscott @gammazero @mvdan

Initial PR: https://github.com/protocol/web3-dev-team/pull/7


## Purpose &amp; impact 
#### Background &amp; intent

Chain syncing in Filecoin is painfully slow. This affects the whole product -- system requirements to run even a client node are very high, and gas prices and message limits are limited by the speed we can sync the chain. One huge source of this time suck is simply reading data in and out of our datastore.

We have approached data persistence through using off the shelf key-value stores in our stack. Long term, many aspects of our stack are limited by the lack of a datastore/database designed specifically for our data format, IPLD (see this [overview](https://docs.google.com/document/d/1GxUNUaBfaY4HneWCOfyPcyWG_14t-vnsy3NbQRF4Fdc/edit) and [analysis](https://docs.google.com/document/d/16_8TEslIY__54x2lvMNu5dLL0BSAJ2GxkZ9w3p8sUys/edit)). But in the near term, we have several extremely promising alternative key/value store solutions that can deliver immediate concrete improvements to chain performance.

The aim here is to finalize existing explorations to deliver at least a 50% improvement to chain performance.

#### Assumptions &amp; hypotheses

* Datastore performance affects chain sync speed (we have experimental evidence this is true, but not indications of how much)
* Prototyped solutions that demonstrate improvement as prototypes will not get slowed down a lot in getting to production readiness
* Chain performance raises the barrier to entry and creates negative characteristics that cause people to leave Filecoin (see:  high gas fees, long time to get up and running without snapshot)
* A 50% improvement that isn’t an order of magnitude improvement is still worth pursuing, especially if we have a clear path to success
* Existing work that hasn’t been finished and benchmarked will deliver at least modest improvements


#### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->

#### Impact

🔥🔥

Chain speed breaks everything. Even 50% improvement has a big impact on everyone using filecoin.

#### Leverage

🎯🎯

We are specifically picking this as an easy win on the datastore improvement track. However, it might be something we bring to IPFS eventually, and it will set us up to build more specialized IPLD solutions.

#### Confidence

3 - All user reports that the hardware requirements for running a full lotus node are a major pain point -- if we could drop those requirements, even a little, it would make a big difference

## Project definition
#### Brief plan of attack

We have three significant potential solutions that are well prototyped and close to delivery --
 * [Using a custom append only key value store](https://github.com/filecoin-project/lotus/pull/5575)
 * [Split store](https://github.com/filecoin-project/lotus/pull/4992)
 * [Archival store](https://github.com/ribasushi/ltsh/tree/psql_fullcapture)

The plan of attack is to aggressively test these solutions to determine the best combination of data store, including potentially a segregated choice between hot and cold storage, and deliver a solution that can become the default for Lotus.

* Lotus CLI extended to allow a command line flag selection of datastore
* Support code for split store, custom key-value, and archival chain store as in-repo options so they are maintained
* Tests of functionality for all backends to mitigate future breakage / code rot.

#### What does done look like?

A released version of lotus with faster chainsync

####  What does success look like?

Success means drop in gas fees as more messages fit in a block

Success means being able to slightly lower system requirements to run a lotus full node


#### Counterpoints &amp; pre-mortem

* Debugging and resolving all issues with proposed solutions could take a while
* Chain sync speed will likely still be hampered by other factors (CPU load, etc)
* We don’t have good benchmarks already, which means we have only anecdotal evidence that these solutions will work
* If we add a custom key value store that could become a significant point of maintenance work


#### Alternatives

It may be that running a full lotus node on a regular laptop remains far out of reach, and lotus lite is a much faster way to reduce that aspect of barrier to entry

#### Dependencies/prerequisites

@raulk and @vyzo are finishing split store work still which will take 1-2 weeks

#### Future opportunities

Integrating faster data stores into IPFS, adding additional query capabilities customized to IPLD

## Required resources

#### Effort estimate

Medium - 4-6 Weeks

#### Roles / skills needed

* 2 developers dedicated time

* Either the developers should be the people who’ve built prototyped solutions or should have input and guidance from them
