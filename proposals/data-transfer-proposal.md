# Project Pitch: Data Transfer At Lightning Speed
*Insuring our data transfer protocols can transfer data from known peers as quickly as possible, at speeds as fast or faster than HTTP*

Authors: @hannahhoward

## Purpose &amp; impact 
#### Background &amp; intent

Every application that touches the DWeb stack has to transfer data. Traditionally, we’ve had trouble reaching performance in data transfer that compares to traditional web transfer speed. Previous efforts to improve Bitswap have improved but not resolved data transfer performance issues. Filecoin is using Graphsync with promising but mixed results.

Over the past few months, we’ve been refactoring and improving go-graphsync, and building out a strong testbed and metrics to measure performance ([github.com/protocol/beyond-bitswap](https://github.com/protocol/beyond-bitswap))

Between [a strong benchmarking suite](https://github.com/protocol/beyond-bitswap/tree/master/testbed/testbed), [good ideas for using Bitswap and Graphsync in complementary ways](https://github.com/protocol/beyond-bitswap/issues/25), and promising initial measurements ([Graphsync vs Bitswap](https://observablehq.com/@acruikshank/graphsync-vs-bitswap-file-transfer-rates), [Graphsync vs HTTP](https://observablehq.com/@acruikshank/graphsync-vs-http-file-transfer-rates))

#### Assumptions &amp; hypotheses

*   Data transfer speeds matter to all users
*   Data transfer speeds are a pain point, even absent problems with content routing
*   Improving data transfer speed in IPFS will eventually be useful to speed up data transfer in Filecoin
*   We understand the core technologies of Bitswap and Graphsync well enough to make big improvements in data transfer
*   Our benchmarking suite is mature enough to provide real feedback

#### User workflow example

A dapp developer builds a centralized file transfer application. When one of their users adds a 1GiB file another user is able to download that 1GiB file reliably, with speeds close to an HTTP file download and with minimal overhead. Additionally, if 10 users all have the same 1 GiB file an 11th user should be able to download the data much faster than a single download over HTTP and with relatively low overhead.

#### Impact

🔥🔥

*   If users are able to reliably and quickly download files over IPFS then they will increase their development velocity by not worrying about IPFS data transfer issues, and will not be pushed away from IPFS.
*   Additionally, for users who end up relying on gateways to find and transfer data having reliable and fast data transfer that experience will work seamlessly and keep them building on our ecosystem
*   Success could result in freeing up time for infrastructure engineers running major IPFS gateways, as well as decreasing developer attrition and the number of bug reports on data transfer in go-ipfs.

#### Leverage

🎯🎯 

What we learn here will be critical to delivering an awesome storage and retrieval experience in filecoin

#### Confidence

Ability to deliver the feature - 7 or 8 -- we have strong benchmarking tools and early evidence we can make big improvements to data transfer

Confidence in impact - 2 - We have lots of anecdotal reports that transfer speeds continue to impact use of IPFS

## Project definition
#### Brief plan of attack

Much of the groundwork for this project is already laid down. As stated, we have a strong benchmarking suite, and many good approaches to delivering speed improvements.

Our first step is to build prototypes using a raw libp2p-bitswap-graphsync stack -- this will involve some modifications for both bitswap and graphsync. We will run out prototypes against our benchmarking suite and iterate till we have a strong solution.

Once we have a strong solution, we will move to implementing in releasable form in IPFS - which will have to happen in tandem with IPFS in IPLD project, as we really can’t mix Bitswap and Graphsync in the current stack of services without integrating ipld-prime into the current dag service.

#### What does done look like?

*   We release a version of go-ipfs with significant data transfer speed improvements… unless....
*   We find our prototyping does not lead to any clear path to improved performance and quit early

#### What does success look like?

Success means no one leaves the IPFS ecosystem because data transfer is too slow.

Success means new people come into the IPFS ecosystem seeking a way to move data around quickly

Success means people upgrade to our new version of go-ipfs immediately cause of compelling speed improvements

#### Counterpoints &amp; pre-mortem

*   Content routing may still be the big blocker on data transfer speed, because even if you move data, if you spend a long time looking for it, overall transfer speed is low. The subjective sense of a “fast” may be remain out of reach because of this
*   The impact may be reduced because it’s hard to design a solution that wouldn’t require both parties to be on the latest version to see big improvements, and adoption may be slow
*   The IPLD in IPFS project could hit a snag that blocks this work
*   We might have trouble delivering speed improvements through go-graphsync and go-bitswap, or discover unknown sources slowness outside the scope of the technologies we’re working on

#### Alternatives

*   The biggest improvements to perceived data transfer may come from content routing improvements. It’s not clear this is an accessible alternative path to pursue cause of open research problems in the content routing space

#### Dependencies/prerequisites

*   This work is depending on the IPLD in IPFS project either happening in parallel or before we begin

#### Future opportunities

*   This project will answer several questions we may apply to working on Filecoin retrieval market transfer speeds

## Required resources
#### Effort estimate

In a context where the IPLD in IPFS project is complete, I expect this work to take 6 weeks (3-4 weeks to prototype and iterate, 1-2 weeks to deliver solution into IPFS)

In a context where the IPLD in IPFS project is pursued in parallel, I expect both projects to complete in 9 weeks, assuming additional staffing

#### Roles / skills needed

* 1-2 people with intimate knowledge of go-graphsync/go-bitswap codebase (likely  +)
* Support from IPFS steward ()
* 1-2 people with IPLD expertise to provide feedback
