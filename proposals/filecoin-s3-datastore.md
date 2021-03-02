# [outcome or objective here] 

Authors: @cory

Initial PR: TBD <!-- Reference the PR first proposing this document. Oooh, self-reference! -->


## Purpose &amp; impact 
#### Background &amp; intent

Network storage is desirable -- Chains stored on local disks make it difficult to migrate applcation between
nodes.

Common storage is desirable -- There are many applications in a mining operation that need chain access, and multiple copies of the chain are required. These copies may or may not all be in sync.

For example, sentinel dashboards are attached to a single daemon at any given time. When the fullnode has problems, sentinal has to be migrated to another fullnode.

"high availability" and "high resiliancy" fullnode servies are difficult to achieve. A naieve approach to
achieve HA for a lotus node might involve adding a load balancer and a number of replicas, but there are a
number of reasons this approach could not work, but perhaps it is possible to have a single state shared by
multiple compute nodes which would enable the lotus api to remain up under heavy load or individual system
failures.

By establishing a common network storage layer, the stateful portion of the lotus daemon can be persisted
to network storage while the computational component can be considered relatively stateless, with all the
operational benefits gained from running stateless vs stateful services.

We currently work around this by using network-attached block storage, which permits for migration without
unreasonable difficulty, but does noting for storage efficiency, HA, or having a true common view of the
database between multiple applications. Each application must be indiviidually monitored to make sure
it is not falling behind, redundantly storing and computing.

There are other projects that would accomplish a similar goal, such as postgresql storage. There are a few
reasons why I think S3 might be an appropriate target for this application.

* S3 isn't just amazon. It's also min.io, openio.io, ceph-gw, openstack swift-s3, swiftstack...
* The Cologix DC has a large ceph installation, for which the s3-compatible gateway could be used at high speeds.
* S3 is an object store API, not a relational database query language.
* Object storage such as S3 can scale to PB-scale datastores, whereas most relational databases cannot.

In the future, if there are light-weight nodes that are read-only or made to trust a well-known source that
is writable only from a well-known PL daemon, it would be beneficial if this source were highly-available.
S3 would be a better option for such a source than postgresql. I'm not confident that any lightweight
lotus implementation would go in this direction, so this isn't a main reason I think this is a good target,
but it is *a* reason this might be a good target. We could keep a PL-recognized chain on Amazon S3 and
permit light-weight chain-analyzers to leverage it. 

A few weeks ago I did a *very* rudementary implementation wherein datastores were swapped out with
https://github.com/ipfs/go-ds-s3, hard-coded for my personal AWS account. I ran a lotus node that
imported a snapshot and it was able to complete the import and keep up with the network even though
it was storing the data on Amazon over the internet. I suspect, then, that any s3-compatible implementation
will be fast enough to keep up.


#### Assumptions &amp; hypotheses
* network storage is desirable 
* common storage is desirable
* S3-compatible object stores are quick enough.
* External locking is either available and useful, or is not required.

#### User workflow example
1. Setup LOTUS_PATH to point to s3://your/s3/compatable/bucket/
   a. Or some component of the repo, the cold-storage portion of split repo, perhaps.
2. Run a lotus as usual.
3. Migrate the lotus node to another machine and see that it's already synced.
4. Add a second node to scale up API performance (with write-locking, perhaps?)

#### Impact

This enables ceph users, or users of several other object storage databases to leverage this layer
for filecoin storage rather than block-level storage with an object storage database (leveldb, boltdb) resting
on top of it.

* Easier lotus node migration
* Common view of filecoin data between multiple systems


#### Leverage
Perhaps....If the blockchain were available on Amazon S3, there would be more chain analysis.
Users interested in analysis would not need to be able to run lotus daemons, just a simpler python
or javascript reading from a trusted, well-known chain.

Miners who have their own S3-compatible API service running in house (for example ceph in the cologix DC),
can leverage this for its operational benefit. However, even miners that run on cloud infrastructure
would see operational benefits, and it is likely they already have an S3-compatible API service available
to them. I suspect this would enable smaller miners to more easily run larger configurations, and we would see
more of their operational pain points pointed out to us.

#### Confidence
Impact: 5
Confidence: 0.7
Ease: 8-9

Overall: 4.5

I think the software implementation for a proof-of-concept is quite easy. However, if this were implented,
the more arduous test would be in proving validitiy of assumptions. If we ran a mining operation, it might be
easier to observe an impact to operational procedures. Even without this, however, we can measure the impact
of various vailure modes using ipfs testground to estimate the difference in reilability and availability compared to block storage. This could be measured by the uptime of a lotus-api consumer, such as sentinel, given 
failure of lotus node.




## Project definition
#### Brief plan of attack
Develop a quick and dirty proof of concept to do basic performance comparisons with alternative network
storage solutions -- such as relational databases, etc.

Consider future plans, potential for lightweight 

#### What does done look like?
Lotus users are given the option to use an s3:// object service.

(optional) -> there is a PL-managed lotus daemon that writes to a world-readable S3-bucket.

####  What does success look like?
If the lotus daemon has become a stateless compute service, operators everywhere will be happy.


#### Counterpoints &amp; pre-mortem
This is a blockchain, there are supposed to be a whole bunch of redundant copies.
More daemons more consensus.

Storing in postgresql allows you to perform indexes and complex queries on the database.


#### Alternatives
Any other network storage database could have a similar goal. Postgresql-datastore would also be pretty good.

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

#### Future opportunities


## Required resources
Lotus dev
Lotus infra

#### Effort estimate
medium

#### Roles / skills needed
Lotus
