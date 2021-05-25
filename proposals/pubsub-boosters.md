# Filecoin Network Boosters

Authors: vyzo

Initial PR: TBD <!-- Reference the PR first proposing this document. Oooh, self-reference! -->

## Purpose &amp; impact
#### Background &amp; intent

Messages and Blocks propagate in the filecoin network using pubsub (gossipsub).
In general, this works well enough; however it has been observed that small miners outside mainland
China often get blocks late, which results in mining orphan blocks.

This project proposes to build a small network backbone consisting of pubsub boosters that are
directly peered with large miners in mainland China and exchanges in order to ensure fast block
propagation to and from miners in mainland China.

That is, instead of relying in random connectivity and being hampered by GFW issues, we propose
to operate a small number of specialized nodes with the intent of enhancing network connectivity
to our mining base.
The specialized nodes, called boosters, will operate with extended meshes (at the gossipsub
level) and utilize explicit peering agreements with large miners and exchanges.
This will ensure that blocks (and messages) have fast network paths in and out of mainland China
and improve the health of the filecoin network.

#### Assumptions &amp; hypotheses

- Network connectivity to miners in mainland China is a limiting factor.

#### Impact

- Enhance connectivity at the filecoin network.
- Improve block and message propagation times in and out of China.
- Eliminate late blocks and orphan mining.

#### Internal leverage

Reasonably High.

#### Confidence

Resonably Good.

## Project definition
#### Brief plan of attack

In terms of code, there is a little work to be done:
- make sure that the splitstore doesn't have any cache misses, so that boosters can operate
  without a coldstore
- create the pubsub profile for the booster role

In terms of deployment, a small number (eg 4) of boosters should be sufficient.

However, for the project to be successful we will have to reach out to miners and exchanges so as
to establish direct peering agreements with our boosters.

#### What does done look like?

We operate a small number of boosters, explicitly peered with miners
and exchanges, and have spiffy fast block/message propagation.

####  What does success look like?

- Block and message propagation times drop.
- Late blocks and orphan mining is eliminated.

#### Counterpoints &amp; pre-mortem

Maybe the network connectivity to/from china is not the problem and this won't help much; but we don't
think this is the case.

#### Alternatives

It's the best approach to enhancing network connectivity.
The alternative would be for small miners and exchanges to talk to each others and establish their
own explicit peering agreements and hope that a stable network emerges.
However, we are much better positioned to create the necessary agreements and operate the boosters.

#### Dependencies/prerequisites
- splitstore; we need to run without a coldstore so that we don't have ticking bombs with network
  storage in our boosters.

#### Future opportunities

Coupled with the pubsub obervatory we can gain better insight in the network.

## Required resources

#### Effort estimate
- Development time should be small, 1 engineer for 1-2 weeks should complete the necessary code changes.
- Infra would have to provision the booster nodes
- Comms would have to reach out to exchanges and miners to establish the peering agreements.

#### Roles / skills needed
- Devlopment requires knowledge of splitstore and pubsub internals.
