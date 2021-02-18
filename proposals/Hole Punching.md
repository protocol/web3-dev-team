# NAT traversal in libp2p via Hole Punching with Limited Relays

### Authors:

- @vyzo
- @aarshkshah1992
- @raulk

# Purpose & Impact


### <ins>Background</ins>

Given the pervasiveness of IPV4 peers that are behind NATs on the internet, NAT traversal is an essential requirement for a peer to peer application. The inability to traverse around NATs means that such NATT’d peers are NOT reachable on the network and are thus unable to provide any meaningful service to the network, nor interact with network participants under protocol patterns that require inbound connections (e.g. dialbacks). \
\
Libp2p currently executes NAT traversal using[ Circuit Relays](https://docs.libp2p.io/concepts/circuit-relay/) wherein publicly dialable Relay servers relay the entirety of user traffic to peers that are NATT’d. This approach does NOT scale because:




1. It costs bandwidth on the Relay server.
2. There is NO real incentive to be a Relay server.
3. Introduces communication latency between the two peers that are interfacing via the Relay server.

\
A more scalable approach to NAT traversal is to enable direct communication between the peers via a technique called _[Hole Punching](https://en.wikipedia.org/wiki/Hole_punching_(networking))_. Hole punching removes the need to relay _all_ traffic between two peers via a Relay server. Instead, relay servers are used merely at the connection bootstrapping phase, to convey signalling between two peers intending to connect to each other, sufficient to facilitate NAT hole punching. In most cases, such traffic represents a minimal fraction of the full user payload traffic.

Hole punching  **has been shown to have ~60% success for TCP & ~80% success for QUIC**  ([MIT paper on Hole Punching](https://pdos.csail.mit.edu/papers/p2pnat.pdf)). It has been widely studied in academia and has also been widely adopted in real world large scale p2p applications  ([Tailscale blog on NAT traversal](https://tailscale.com/blog/how-nat-traversal-works/)). Pervasive web protocols like WebRTC rely on ICE, which uses signalling (STUN) to facilitate hole punching. \
\
Based on [metrics that we collected](https://protocollabs.grafana.net/d/lNGQTv9Zz/hydra-boosters?orgId=1&refresh=5m&from=1613523541216&to=1613534341216&var-head=All&viewPanel=50), we have discovered that:



*   **~80% peers in the current DHT network are NOT dialable/reachable**.
*   Relay servers funded and operated by PL aren’t enough given the size of our network, and are also expensive to run.

We posit that implementing hole punching will enable direct connectivity for a significant portion of the network, and will improve overall QoS of the network by increasing the connectivity. In combination with future efforts to strengthen WebRTC support, it will also enable browser-centric use cases to be reliably built on libp2p.


### <ins>Intent</ins>

By implementing a _[Limited Relay](https://docs.google.com/document/d/1bhoVGitiB2rr6i8cVKvwkQONHvsfBxqcK76ePVW_JVs/edit#heading=h.s248pnlqjmsm)_ protocol that ONLY provides the resources and bandwidth needed to coordinate a hole punch instead of acting as full fledged data transfer Relays, we can get public DHT servers to run the Limited Relay protocol without costing them too much bandwidth/resources and thus ALSO get a pervasive & large scale Hole Punching co-ordination infrastructure that can help scale hole punching to the size of the network. \
\
Note that Hole Punching fails if either peer is behind what is known as a _[Symmetric NAT](https://dh2i.com/kbs/kbs-2961448-understanding-different-nat-types-and-hole-punching/)_ as opposed to a _[Cone NAT](https://dh2i.com/kbs/kbs-2961448-understanding-different-nat-types-and-hole-punching/)_,  which is why Hole Punching does not deliver 100% success rates, but it’s much better than the alternative which is NO _direct_ connectivity for ALL NATT’d peers.

Also, based on anecdotal evidence in the wild and engineering war stories (see [Tailscales’s blog](https://tailscale.com/blog/how-nat-traversal-works/)), **Cone NATs are much more pervasive in Home ISPs over Symmetric NATs, which justifies the~60-80% success for Hole Punching**. \
\
Given that libp2p is a library to build peer to peer applications,**implementing Hole Punching in libp2p will allow any application/network that builds on top of libp2p to also benefit from Hole Punching**. This will be a significant step forward in the ease of building well connected p2p networks and will be a major added motivation for developers to build on top of our stack. Based on our research, **no such library that comes with out of the box NAT traversal via Hole Punching exists out in the wild today and we have the opportunity to provide the first such library & infra to herald the age of better connectivity in Web3 apps**.


### <ins>Assumptions & hypotheses</ins>



*   Applications that build on top of our stack want peers to be _directly_ reachable from the network even though they are behind a NAT (~80% peers in the current DHT network).
*   PL is not willing to keep funding expensive  bandwidth-unrestricted Relay servers as the network keeps growing to enable data transfer to/from NATT’d peers.
*   Users would love to use our p2p stack if doing so means the applications they build get NAT traversal via Hole Punching out of the box.
*   Enabling better connectivity in IPFS, Filecoin and other applications that build on top of Libp2p in a world suffering from the tyranny of NATs is a success metric/priority for us.


### <ins>User workflow example</ins>

The User builds an application such as IPFS, Filecoin, Ethereum etc. on top of Libp2p and gets _direct_ connectivity between NATT’d peers (albeit ~60% for TCP & ~80% for QUIC) out of the box without bringing up additional infrastructure and with minimal configuration.


### <ins>Impact</ins> 
🔥🔥🔥



*   Libp2p will be one of the first libraries in the web3 ecosystem that provides Hole Punching and hence better connectivity out of the box. This will increase the functionality of our stack, and will encourage more developers to build on top of it.
*   PL’s applications such as Filecoin & IPFS will get turbocharged with better connectivity as they build on top of libp2p.
*   Important projects such as Eth2, 0x etc that build on top of libp2p will ALSO get this huge benefit should they choose to use it. Eth2 is likely to need this feature in Phase 2, which introduces browser-based light clients.
*   New browser-centric use cases will be possible when this functionality is implemented in js-libp2p.


**Summary: The idea of a peer to peer library that makes NAT traversal via Hole Punching easy and pervasive is a very important & exciting development in the world of peer to peer applications.**


### <ins>Leverage</ins>

How much would nailing this project improve our knowledge and ability to execute future projects?



*   🎯🎯
*   Lack of dialability between peers has been a repeated blocker, in libp2p DHT, pubsub, bitswap, Filecoin deals, and more.


### <ins>Confidence</ins>

**Medium.**



*   The [MIT paper ](https://pdos.csail.mit.edu/papers/p2pnat.pdf)that studied Hole Punching concludes a ~60% success for TCP and ~80% success for QUIC. [Tailscale](https://tailscale.com/), a large-scale VPN that  i[mplemented NAT traversal ](https://tailscale.com/blog/how-nat-traversal-works/)via Hole Punching also achieved similar results. This is because of the pervasiveness of Cone NATs (the good NATs) among Home ISPs.
*   Both IPFS and Filecoin currently suffer in terms of connectivity as they do NOT have Hole Punching and based on the metrics we collected, ~80% peers on the DHT network are NOT reachable/dialable.
*   We already have a working PoC for hole punching and based on the limited testing we’ve done so far, we are able to successfully hole punch and connect Cone NATT’d peers that would otherwise be unreachable.


**Confidence can be reassessed after the dog-fooding and alpha testing phase are complete within a community of Labbers that use Home ISPs and have NATT’d machines. Refer to the Project Definition section for details.**


# Project Definition


### <ins>Brief plan of attack</ins>

*   Implement the _[Limited Relay](https://docs.google.com/document/d/1bhoVGitiB2rr6i8cVKvwkQONHvsfBxqcK76ePVW_JVs/edit#heading=h.s248pnlqjmsm)_ protocol in Libp2p.
*   Implement the _[Hole Punching protocol ](https://github.com/libp2p/specs/pull/173)_to achieve direct connectivity with a NATT’d peer after coordinating a hole punch.
*   Dogfood an alpha version of Hole Punching to Labbers and collect metrics regarding success rates and resource consumption.
*   Based on the results of the dog-fooding endeavour, fix/optimize the hole punching process and release it to the world in a phased manner.
*   In the initial phase,  ONLY use statically configured Limited Relay servers hosted by PL.
*   Once we conclude that PL hosted Limited Relays are stable,  ship a release that turns on the Limited Relay protocol in public DHT servers but continues to use the statically configured Limited Relays.
*   Once ~30% of public DHT servers upgrade to support the Limited Relay protocol(measure using Hydra Boosters), ship automated discovery & use of Limited Relays to coordinate a hole-punch rather than using statically configured Limited Relays servers.
*   Achieve ~90% hole punching success if both peers are behind a Cone NAT  in the second dog-fooding phase that uses AutoRelay to discover and connect to  Limited Relays in the wild.
*   Massive focus on usability, user education and evangelizing the feature by writing blog posts discussing a “how we got here”/ internals / engineering journey of Hole Punching in libp2p with metrics and blog posts and demo videos on how to configure, use and debug Hole Punching.


### <ins>Technical deliverables</ins>


*   **Phase1**
    - ~90% hole punching success if both peers are behind a Cone NAT in the first dog-fooding phase using PL hosted Limited Relays.
*   **Phase 2**
    - Optimise based on Dogfooding results and metrics and ship the feature using statically configured PL hosted Limited Relays.
*   **Phase 3**
    - Once we conclude that PL hosted Limited Relays are stable,  ship a release that turns on the Limited Relay protocol in public DHT servers.
*   **Phase 4**   
    - Once ~30% of public DHT servers upgrade to support the Limited Relay protocol (measure using Hydra Boosters), ship automated discovery & use of Limited Relays to coordinate a hole-punch rather than using statically configured Limited Relays servers.
*   **Phase 5**
    - ~90% hole punching success if both peers are behind a Cone NAT  in the second dog-fooding phase that uses AutoRelay to discover and connect to Limited Relays in the wild rather than using statically configured Limited Relays.


### <ins>Success criteria</ins>

*   Dog-fooding phases deliver ~90% success for labbers using Home ISPs with Cone NATs (TCP & QUIC).
*   No bugs related to Hole Punching failures if both peers involved in a Hole Punch are behind a Cone NAT (we have good PRs for and will ship code/tools for users to detect their NAT type).
*   Users do not file bug reports about their public DHT peers getting DDosed/consuming too much bandwidth/resources because of acting as Limited Relays.
*   We receive great traction and feedback on the ease of use and robustness of Hole Punching on channels such as Twitter, user surveys and from our community of users/partners.


### <ins>Long Term Success criteria</ins> (~ 6 months in as network will take time to upgrade)



*   We are able to remove static configuration of  PL hosted Limited Relays in lieu of discovering Limited Relays. And better still, completely shut them down without causing disruptions to the Hole Punching abilities of the network (disruptions can be measured using Github issues, bug reports and PL hosted Cone NATT’d nodes that scrap the network for unreachable peers with Cone NATs, attempt Hole Punching with them and report corresponding metrics).


### <ins>Counterpoints & pre-mortem</ins>

Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?


### <ins>Alternatives</ins>

Maybe implementing a WebRTC transport in go-libp2p that performs signalling/co-ordination via Limited Relay servers can help solve the connectivity problems that hole punching seeks to address but that means that we get tied to using WebRTC as a transport. Compared to that, implementing hole punching as a first class feature in Libp2p makes the whole feature transport agnostic.


### <ins>Dependencies/prerequisites</ins>

None.


### <ins>Future opportunities</ins>

Better connectivity via Hole Punching in the IPFS & Filecoin networks.


# Required Resources


### <ins>Estimated Scope</ins>

*   4-5 weeks i.e. **Medium for a team of 2 people** AND with some help from the Dev Onboarding Team for landing some kickass documentation/user education.
*   Uncertainty is reviews NOT getting completed on time as we would ideally like the important aspects of our work (Limited Relays, Hole Punching Protocol, AutoRelay changes and Hydra Booster changes) to be reviewed by the Project Captain and/or someone from the Stewards team.


### <ins>Roles / skills needed</ins>



*   libp2p engineers.
*   Infrastructure engineers to deploy Limited Relays, metrics collection using Hydra Boosters, and deploy Cone NATT’d crawler nodes with real-time error reporting.
*   Docs and User onboarding team to help ship blog posts, user education documentation and demo videos explaining the feature in depth and explaining how to configure, use and debug Hole Punching.
