# Filecoin PubSub Observatory

Authors: vyzo

Initial PR: TBD <!-- Reference the PR first proposing this document. Oooh, self-reference! -->

## Purpose &amp; impact
#### Background &amp; intent

We are currently flying blind in terms of block propagation and
network health in the filecoin network.  We are also lacking a
reputation system for filecoin peers.

Investigating and debugging apparent block propagation problems is
difficult without observability into the network’s pubsub activity,
such as message flows, peer scores, and low-level RPCs (that can be
processed to extract higher-level insights).


#### Assumptions &amp; hypotheses
- We care about block propagation and pubsub peer scores in the filecoin network.

#### User workflow example

- A lotus dev (or external party if we make the relevant dashboards open)
  could trace block propagation through the network
- A node operator could check on his nodes score and eventually reputation.


#### Impact

The project would allow us to gain insights in the filecoin network,
which could be invaluable in understanding, debugging, and improving
the system.

#### Leverage
Quite decent.

#### Confidence
Pretty good.


## Project definition
#### Brief plan of attack

1. To evolve the current pubsub traces collector (which receives
   traces from 1.5k concurrent Lotus nodes) to ship the data stream to
   our logz.io Elasticsearch, where it can be queried with Kibana to
   explore and build dashboards.
2. Introduce support for permissioned local peer scoring and message
   flow reporting from trusted sources (e.g. Infura, glif, ourselves,
   etc.), possibly by evolving the traces emitter / collector to
   authenticate with a token.
3. To implement dashboards and (potentially) streaming processing
   scripts to extract insights and create the observability we need.
4. Using insights from our observatory, lay the stage for developing a pubsub reputation system.

#### What does done look like?
We have awesome dashboards and a site where we can inspect block
propagation, network connectivity, and peer scores.

####  What does success look like?
We extract insights to tune the filecoin network and build a reputation system.

#### Counterpoints &amp; pre-mortem
Maybe there is nothing interesting in the data and everything is groovy as it is; but we won't know until we build this.

#### Alternatives
None; we need this.

#### Dependencies/prerequisites

#### Future opportunities
A reputation system for filecoin's pubsub.

## Required resources

#### Effort estimate
- Small, 1-2 weeks

#### Roles / skills needed
A couple of people with understanding of how pubsub works.
