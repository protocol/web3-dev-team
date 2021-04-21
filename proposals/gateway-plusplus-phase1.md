# Gateway++ 

Authors: @mikeal (with ideas from many people)

Initial PR: TBD <!-- Reference the PR first proposing this document. Oooh, self-reference! -->

## Background

Developers often have to deploy code into constrained environments. Mobile devices, browsers and cloud functions all have a variety of limitations that make running and maintaining a full IPFS node impractical or even impossible.

For the most part, these developers are falling back to HTTP and stringing together whatever HTTP interfaces we currently provide so that they can offload these tasks to a shared IPFS node.

HTTP is the lowest common denominator so when we see environmental constraints in application stacks we see HTTP as the means by which developers work around these limitation in order to access IPFS. This also allows developers to leverage additional infrastructure they already have deployed for HTTP, like caching, with IPFS.

We should lean into this rather than push against it. In the short term, we can’t expect every user and developer to have a full implementation of the protocol. Strengthening the Gateway protocol to meet user needs is the path of least resistance and can enable numerous thin clients to be built for IPFS that can run in virtually any environment.

This proposal establishes "Gateway++" as a meta-project for meeting these user needs with extensions to our gateway protocols and infra.

## Problem Statement

For reading data, the IPFS Gateway is already serving these users quite well. Not only does it allow them to read data from the IPFS network without running a full node, they are able to integrate with existing HTTP caching infrastructure to improve performance.

However, the user needs for writing data to the network are not being met well by our current solutions. We have two interfaces that support writes over HTTP and neither was designed as a full solution to these user needs.

- Pinning Service API.
    - 😡 Requires you to already be running a full IPFS node as a client.
    - 😡 Is not transactional. You have to poll in order to tell when the data is actually available.
    - 😃 Is intended to be multi-tenant and authenticated using a flexible bearer token.
- HTTP RPC API
    - 😡 Is single-tenant. No authentication system.
        - The RPC API is designed for a single user to manage a remote node, it was not designed and built to be multi-tenant and would look very different if it were.
    - 😡 Is not always transactional. Many write calls return before they are available.

These interfaces were built with particular user profiles in mind. The users we’re seeing in NFTs (including our own service as a user of IPFS) are not well served by these interfaces and we need a new “project” definition (Gateway++) that is centered around these user needs.

Developers are building applications that have to run in a lot of constrained environments that can’t support a full node. Strengthening the Gateway to serve these needs over HTTP leverages endpoints they are already using and provides the features they need in a stateless protocol that has ubiquitous support.

We are never going to hear “Sorry, I can’t use HTTP in this environment” from a developer.

## Phase 1

We should expect this to be a long term project with additional proposals in due time.

For now, we have a list of high priority tasks that need to be fixed.

In [nft.storage](http://nft.storage) we have the following high priority needs:

- Add the Pinning API to ipfs-cluster.
- Add transactional CAR file uploads to the Pinning API.

We also need to do the following to kick off the project.

- Document configuring IPFS Gateway to pass Pinning API requests to a cluster or other IPFS node with the Pinning API enabled.
- Configure and deploy our own gateway with this configuration. (We won’t be handing out auth tokens to anyone who doesn’t already have one, this is just to eat our own dogfood).

#### What does done look like?

Each work item in Phase 1 is something nft.storage needs so we have a builtin "first user" who would have all their requirements satisfied by this proposal.

Once this is deployed you'll be able to write thin client interfaces with only a gateway URL and bearer token as configuration.

####  What does success look like?

Beyond just having satisfied the needs of nft.storage, this should also satisfy the needs that Cloudflare has and we would hopefully see support for IPFS in Cloudflare Workers as a thin
client to their Gateway.

#### Alternatives

There are alternative approaches to building thin clients. The proposals around changing/improving the RPC API could be designed for this purpose,
but the RPC interface is a larger API (not very "thin") and wasn't designed for multi-tenant. There would probably be **more** work involved in getting
the RPC interface to support these users than this proposal.

#### Counterpoints &amp; pre-mortem

While this maps well to where web developers are today, it's not a "pure p2p" approach to solving problems. We're beefing up the ability to rely on large IPFS nodes that end up
being federated rather than fully decentralized.

#### Dependencies/prerequisites

None

#### Impact

*Just* for nft.storage, 7. Overall, a 9 or 10, this should unlock numerous thin clients to be built and will allow developers to leverage a lot more of their existing infrastructure.

#### Confidence

Confidence is a 10 for "nft.storage needs this" but is an 8 or 9 for "this is absolutely the right thin client interface."

## Future opportunities
### New Thin Clients

Rather than thinking of a thin client as the current IPFS API with less code, let’s consider what a smaller overall API profile looks like for this new interface.

The JS library work we’ve been doing for the last year could be leveraged for a much smaller and higher impact JS library built against the Gateway++ interface.

Since all writes that pass through the CAR file interface are transactional we now have availability guarantees for all of the writes.

We can do file encoding in the client (we’re going to have to write this anyway for [nft.storage](http://nft.storage) in order to get over the 100MB Cloudflare Worker limit) using the latest codecs.

Finally, since the protocol is so simple we should expect to see serveral thin clients designed to meet a variety of user needs and integrations.

### Content Routing for Large Providers

Gateways and large providers need to be directly peered since large providers have too much content to provide in the DHT.

As a stopgap we’re maintaining a list of peers all large providers and gateways should peer to and encouraging large providers to add themselves to it. This is not a viable long term solution.

We need “BGP for Content Routing,” which is to say that we need a federated protocol for efficient content routing in a network of directly peered large providers.

### GraphQL

It's @gozala’s idea to get GraphQL in the Gateway but there has been GraphQL IPLD stuff happening for about a year now.

If we want to reach a lot of developers quickly we should consider ways that we could expose GraphQL access to IPLD data through the Gateway using GraphQL’s standard HTTP protocol.

The amount of tooling that already exists for GraphQL is quite large so this would allow for a number of high impact integrations.

## Required resources

The first phase of Gateway++ is primarily work in Cluster and Infra, so I'll defer to that team to estimate the resources required. Hector has already made some progress on adding CAR file input to cluster so it would be great if he could continue with this work as well.

