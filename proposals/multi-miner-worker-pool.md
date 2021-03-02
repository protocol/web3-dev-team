# Shared Worker Pool

Authors: @cory

Initial PR: TBD <!-- Reference the PR first proposing this document. Oooh, self-reference! -->

Problems Addressed:

  * Improve hardware efficency, particularly for multi-miner operations, to save operational cost.
  * Enable worker nodes to scale up and down economically.

## Purpose &amp; impact 
#### Background &amp; intent

Mining operations consisting of multiple lotus miners with separate worker nodes must be consistently
over-provisioned. Individual miners may have too-few or two many workers at any time without any
simple way to re-allocate worker nodes into a more optimal configuration.

For example, in the Cologix datacenter, there are 3 miners, 12 nodes optimized for PC1 work and 12 for PC2.
These machines have equal access to the Datacenter's 4PB of storage via ceph and to local storage.
A naieve worker allocation would assign 4 of each worker nodes to each of the miners, however, there is
little reason to believe each miner will be equally busy as the others. Clients may pick a favorite miner
and use it heavily, or sort in a way that one of them is usually selected. If such a load imbalance were to
happen, the favorite miner could become overwhelmed while there is still idle worker nodes. Because of this
inefficiency, each miner must be over-provisioned for the number of workers assigned to it, which could be
a substancial expense for the operation.

One way to overcome this problem is to place a message broker between miners and workers.

By adopting a shared worker-queue pattern, lotus workers would operate as a single work pool. Instead of the
internal queueing mechanism currently employed, miners would publish commands to a broker. (i.e. rabbitmq,
activemq, Google pub/sub, Amazon SQS, etc) The message would be consumed by the worker pool as soon as possible
by any node in the worker pool. The worker would not be connected to the miner, except in the context for
that specific seal job.

Failure handling is simplified with a worker-queue model. When a node fails, or must be taken down for maintenance,
its work can be accomplished by any other node. Typically, the broker handles this by issuing a lease to subscribers
that must be acknowledged within a period of time. If a node goes offline, the job would be re-scheduled by the broker

In addition to greater efficiency for medium to large miners, small miners who rarely accept deals may also
benefit from this pattern. Small miners could run with a node just large enough to compute window posts, and
have zero worker nodes until needed. Miners like this could scale up when necessary and scale back down. However,
I suspect the additional complexity for running a separate broker may negate any benefit for smaller miners.


#### Assumptions &amp; hypotheses

* Running a mining operation is expensive
* Multi-node mining topology is relatively rigid
* Mining operators want to efficiently allocate resources

#### User workflow example

1. Install message broker of choice. Leave the choice up to the user.
2. Configure lotus-miner to pass work to amqp://<broker> or maybe mqtt://<broker> NOT to the worker
3. Configure lotus-worker to subscribe to the broker NOT to the miner
4. Setup lotus-worker to scale with their cloud provider (optional)


#### Impact
A work-queue would simplify running lotus on large-scale operations. Miners who experience high operational
cost and toil would appreciate the ease with which brokered work queues scales compared to the monolithic model.

#### Leverage
I suspect this project is low-leverage because it would target larger miners, but I have no reasonable estimation.

#### Confidence

Impact: 5 -- I'm not sure. The purpose for this proposal, in addition to easing our own future mining aspirations, is to increase
retention by making it easier to run lotus at at large scale
Confidence: 0.3 -- There are plenty of worker-queue applications that work well. None of them I know of are Filecoin implementations.
Ease: 7 -- This chainge would require changes to the miner, worker, and perhaps the protocol they use to communicate. It's not clear to me whether it's better transmit sectors in-band or assume the existance of a shared volume.

Overall: 4.1

## Project definition
#### Brief plan of attack

Write a testground plan to simulate idle workers under different load conditions. This simulation will be used to measure success.
* Implement proof of concept.
* Using the proof of concept, test for scalability and try to extrapolate cost savings estimations for miners of different size and configuration.
* learn and improve toward a production implementation.

#### What does done look like?
Brokered pubsub queue between miner and worker

####  What does success look like?
Worker nodes are 100% utilized even with uneven miner allocation.

#### Counterpoints &amp; pre-mortem
I'm not confident that this is the biggest problem big miners have.
It will be more complex to maintain two different kinds of job scheduling.

#### Alternatives
* Workers could be made to connect to multiple miners simultaneously. Operators with multiple miners would try to schedule on workers with the least-load, or round-robin, hash-ring or some other mechanism and re-try when there is too much load on the worker.

#### Dependencies/prerequisites

#### Future opportunities
* Worker pools that are shared between different miner operations.

## Required resources

#### Effort estimate
Medium

#### Roles / skills needed
* Lotus dev
* Basic pub-sub knowledge
