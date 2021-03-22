# Fast lane IPNS 

Authors:
- @gozala

Initial PR: TBD <!-- Reference the PR first proposing this document. Oooh, self-reference! -->
Related to: [Reliable Mutability Primitive][]

[Reliable Mutability Primitive]:https://github.com/protocol/web3-dev-team/pull/19/
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
_Describe the desired state of the world after this project? Why does that matter?_
<!--
Outline the status quo, including any relevant context on the problem you’re seeing that this project should solve. Wherever possible, include pains or problems that you’ve seen users experience to help motivate why solving this problem works towards top-line objectives. 
-->

##### Problem statement

Today [IPNS][] fails to provide reliable mutability primitive. There is no implementation that works across go, node and web, which makes it impractical.

| Routing | web  | go   | nodejs |
| ------- | ---- | ---- | ------ |
| DHT     | ❌    | ✅    | ❌      |
| pubsub  | ⚠️    | ⚠️    | ⚠️      |

> ❌ - Not available
> ✅ - Available
> ⚠️ - Not out of the box
>
> - ❌ DHT in web nodes is impractical as most nodes will be undialable and so will be a web node.
> - ❌ DHT implementation in nodejs is buggy, untersted and unoptimized ([ipfs/js-ipfs#3469][]). 
> - ⚠️ PubSub in web nodes only works in swarms formed around central ICE server that are disjoint from go nodes. In practice creating fragmented networks of ephemeral peers.
> - ⚠️ IPNS over pubsub is disabled in go by default (Can be enabled by running daemon with `--enable-namesys-pubsub`). Pubusb itself is also disabled by default ([protocol/web3-dev-team#53][]).
> - ⚠️ IPNS over pubsub in nodejs still requires DHT to bootstrap overlay network of participating peers. Lack of proper DHT implementation prevents it. Which could be overcome via delegated routing but it does not work out of the box.

Only DHT based implementation in go works out of the box. But it still fails to meet user expectations because:
  1. *Slow* publish and resolution.
  2. Requires continues republishing. (see [ipfs/go-ipfs#4435])

Teams that have tried using IPNS in their products either switched to using [DNSLink][] or opted-into IPNS over pubsub and still find it *(too slow)* for certain updates *(Textile)*.

To meet a market fit for products with changing state requirement _(that is anything interactive)_ IPNS needs to work reliably, fast _(comparable to web2 solutions)_ and across all supported enviroments _(go, web, nodejs)_.

##### Proposition

At the high level this proposal promises an efficienecy of centralized publishing and resolution while retaining resilience of distributed system.

Proposed name resolution system is inspired by Domain Name System (DNS) as it introduces athoritative name resolvers _(from now on referred as)_ **name keeper** nodes. But unlike DNS, **name owners** _(private key holders)_ are in charge of choosing a name keepers and retain ability to change a name keeper in the future.

> It is assumed that pinning services would be a natural fit for name keeping as they they already are responsible for keeping the content around and mantain list of user pins.


This promises to provide efficiency and speed of centralized systems as peers can cache *name keeper* address(es) for name _(on first resolution)_ and use it in all future resolutions, without disturbing rest of the network.

Name publishing becomes also efficient as name owner can notify *name keeper* directly without disturbing rest of the network.

> Please note that this enables peers to effectively resolve and/or publish name without having to remain online.

###### Initial resolution optimization

To make a very first name resolution nearly as efficient as subsequent ones it is proposed to develop a new **name routing** service and deploy it on boostrap nodes. Name routing nodes will maintain `IPNS name → multiaddrs[]` mapping enabling peers to resolve an address of a name keeper on a first name resolution. Under assumbiton that reassigment of *name keepers* is going to be rare, overhead on name routing nodes should be insignificant as:

1. Name routers could cache addresses for a long time.
2. Resolving peers could cache address locally (and require router only first time).
3. Name routers can deny service to peers resolving name too frequently.
4. Name routers are not involved in publishing.

It is assumed that name routers will be infrastructure nodes, implying that they can be dialed from limited nodes like browsers _*(Have SSL certificates setup, or have a WebRTC address)*_ and can leverage DHT and PubSub so thay they:

1. Can resolve new name on demand by raced query of DHT and PubSub.
2. Can become aware of new names through PubSub messages.
3. Can become aware of name keeper changes through PubSub.

> Note that since name keeper changes are expected to be rare TTL can be really high.

Name routing service does not has to be limited to infrastructure nodes, peer could provide that service and resolve name keeper address from a local cache.


###### DNSLink Optimization

Name owners could include addresses to chosen name keepers in the [DNSLink][] record, which would enable name resolution without resolving an address through name routers first.

##### Visual illutrations

###### Name resolution

Diagram illustrates a name resolution flow. Note however that it does not show how name router can discover new names and their keepers from pubsub.

<!--
```flow
pubsub=>start: PubSub
peer=>start: 📱 Peer 
router=>start: 🖥 Router Node.  
keeper=>start: 🖥 Name Keeper
resolve_keeper=>operation: Resolve QmName keeper
resolve_name=>end: Keeper resolved
cid=>end: QmV8
localcached=>condition: Is keeper address cached
routercached=>condition: Check the cache
dht_query=>operation: Query DHT
pubsub_query=>operation: Query PubSub
query=>parallel: Query
cache_router=>inputoutput: Save Keeper Address
cache_local=>inputoutput: Save Keeper Addresss
resolve_cid=>operation: Resolve CID for QmName
resolved_cid=>inputoutput: QmName is QmV17

peer->localcached
  localcached(yes)->resolve_cid
  localcached(no, right)->resolve_keeper(right)->router

router(right)->routercached
  routercached(yes)->resolve_cid
  routercached(no, right)->query

query(path1, bottom)->dht_query->cache_router
query(path2, right)->pubsub_query->cache_router
cache_router(left)->resolve_cid

resolve_cid->keeper->resolved_cid
pubsub->peer
```
-->
![name resolution](./fast-lane-ipns/resolution.svg)



###### Name update

Diagram illustrating how name update flow.

<--
```flow
owner=>start: 📱 Name Owner
ok=>inputoutput: ✅ QmName is QmV2
error=>inputoutput: ❌ QmV1 is not a head
update=>operation: Update QmName from QmV1 to QmV2
incremental=>condition: QmName is QmV1 ?
keeper=>end: 🖥 Name Keeper


owner->update->keeper->incremental
incremental(yes)->ok
incremental(no)->error
```
-->
![publish](./fast-lane-ipns/publish.svg)


###### Humane readable name resolution

Diagram illustrates name resolution through DNSLink.

<--

```flow
peer=>start: Peer
keeper=>start: Name Keeper
router=>start: Name Router
DNS=>end: DNS
dnslink=>operation: a.com -> QmName
lookup=>operation: lookup a.com
has_keeper=>condition: DNSLink has keepr address
resolve_cid=>operation: Reslove QmName
resolve_keeper=>operation: Reslove Keeper
keeper_resolved=>inputoutput: Resolved address
cid=>inputoutput: QmV321
ttl_name=>condition: a.com in cache?

peer->ttl_name
    ttl_name(no, right)->lookup(right)->has_keeper
    ttl_name(yes, bottom)->resolve_cid

has_keeper(yes, bottom)->resolve_cid
has_keeper(no)->resolve_keeper(bottom)->router->keeper_resolved(left)->resolve_cid
resolve_cid(bottom)->keeper
keeper->cid
```
-->
![publish](./fast-lane-ipns/dnslink.svg)

#### Assumptions &amp; hypotheses

_What must be true for this project to matter?_
<!--(bullet list)-->

- Applications need canonical address for a current state.
- Should work across all supported environments out of the box. 
- To be practical solution, resolution should be reliable (publish / resolve works at least 99.9%).
- To be practical solution, resolution should be really fast (as fast or faster than DNS resolution).
- To be practical solution publishing should be really fast (To be competitive with web2 should be comparable to sending a HTTP request to the server)
- Overhead should be neglegable.

#### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->

#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

<!--
Explain how this addresses known challenges or opportunities.
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

🔥🔥🔥 This would provide mutability primitive that is reliable and fast as DNS, but does not require centralized authority or blockchain style concensus.

Furthermore it would make updating far more convenient than DNS. 

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

<!--
Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

🎯🎯 - This would turn IPFS into an essential building block for web3 applications _(that need to do state updates)_ by removing a need for a custom server-side components to address this limitation.

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

<!--Explain why this rating-->

3 - As high confidence as we can have without doing actual user studies. We know teams that have tried IPNS but found it unrelaible, ultimately rolling out an alternative solution. We also know teams that have evaluated IPFS but chose alternative due to lack of reliable mutability story.

## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

- Define fast lane name resolution specification.
- Define name keeper serivce specification.
- Define name routing service specification.
- Implement name routing service in go-ipfs.
- Implement name keeper service in go-ipfs.
- Implement fast lane name resolution across web, go, node ipfs. 
- Deploy name routing service to PL operated boostrap nodes.

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

- IPNS records can be published and resolved across all supported environments (web, go, node).
- Publishing takes couple of miliseconds.
- Resolution in all but pathological case goes through fast lane.
- Resolution in fast lane takes just couple of miliseconds.

####  What does success look like?
_Success means impact. How will we know we did the right thing?_

<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

- Teams start using IPNS in [DNSLink][] records as opposet to CIDs.
- We see people storing IPNS addresses in ENS to save on blockchain transactions costs
- We see new projects leveraging IPNS (when human readable name is not a concern) instead of working around it with [DNSLink][].
- Most lookups go through fast lane.

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->

## Required resources

#### Effort estimate
<!--T-shirt size rating of the size of the project. If the project might require external collaborators/teams, please note in the roles/skills section below). 
For a team of 3-5 people with the appropriate skills:
- Small, 1-2 weeks
- Medium, 3-5 weeks
- Large, 6-10 weeks
- XLarge, >10 weeks
Describe any choices and uncertainty in this scope estimate. (E.g. Uncertainty in the scope until design work is complete, low uncertainty in execution thereafter.)
-->

#### Roles / skills needed
<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->

## Appendix

<!-- ### Fast lane name routing

Today IPNS supports two name resolution/publishing schemes. They make different tradeoffs, but both disturbing a network when publishing and/or resolving a name.

- Over DHT
    - 💔 Slow to resolve / publish.
    - 💔 Has an overhead of needing to republish.
    - 💔 Not an option for web peers.
    - 💔 Not implemented for node peers.
    - 💚 Very resilient 
- Over PubSub.
    - 💔 Disabled in go peers.
    - 💔 Does not work in web (**TODO:** Figure out if we expect it to work).
    - 💔 Has a constant overhead (uses resources whether used or not).
    - 💔 Initial resolution is slow which makes it slow for non long living peers (mobile devices, web) 
    - 💚 Super simple and convinient protocol

 -->

#### F.A.Q

- Add your question here


[Pinata]:https://pinata.cloud/
[DNSLink]:https://docs.ipfs.io/concepts/dnslink/
[IPNS]:https://docs.ipfs.io/concepts/ipns/
[Pinning Services API]:https://ipfs.github.io/pinning-services-api-spec/
[Petname]:https://en.wikipedia.org/wiki/Petname

[ipfs/js-ipfs#3469]:https://github.com/ipfs/js-ipfs/issues/3469#issuecomment-775944675
[protocol/web3-dev-team#53]:https://github.com/protocol/web3-dev-team/pull/53
[ipfs/go-ipfs#4435]:https://github.com/ipfs/go-ipfs/issues/4435
