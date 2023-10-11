# Symbiosis protocol

Authors:
  - [@gozala](https://github.com/gozala)
  - [@hugomrdias](https://github.com/hugomrdias)

Initial PR: https://github.com/protocol/web3-dev-team/pull/18

<!--
This template is intended to be used by those who would like to pitch a new project for one of the Web3 Dev project teams to take on. It should contain sufficient detail that others can understand how this project contributes to our team’s mission of  product-market fit for our unified stack of protocols, what is included in scope of the project, where to get started if a project team were to take this on, and any other information relevant for prioritizing this project against others.
Good project scope aims for ~3-5 engineers for 1-3 months (though feel free to suggest larger-scoped projects anyway). Projects do not include regular day-to-day maintenance and improvement work, e.g. on testing, tooling, validation, code clarity, refactors for future capability, etc.
-->

### Purpose &amp; impact 
##### Background &amp; intent
_Describe the desired state of the world after this project? Why does that matter?_
<!--
Outline the status quo, including any relevant context on the problem you’re seeing that this project should solve. Wherever possible, include pains or problems that you’ve seen users experience to help motivate why solving this problem works towards top-line objectives. 
-->

There is an inherent asymmetry in node capabilities imposed by the [constraints of the operating environment](#constraints-of-the-operating-environment). Attempts to overcome these limitations often lead to [ad-hoc stop-gap solutions that introduce centralization](#ad-hoc-stop-gap-solutions) into the system. Teams building products on IPFS are required to fill capability gaps with [(unintentionally) incompatible infrastructure](#Unintentionally-Incompatible-infrastructure) of their own.

[IPFS HTTP API provides inadequate solution](#HTTP-API-provides-inadequate-solution) for constrained environments as it is designed to give a single client an **absolute control** of the host node as opposed to coordinating access of multiple tenants.

Here we propose design which embraces asymmetry among node capabilities. Instead of traditional client-server model, symbiotic network is formed through a protocol that enables IPFS nodes with limited capabilities and/or lifespan _(from now on referred as **symbionts**)_ to partner with IPFS nodes that posses greater capabilities and/or lifespan _(from now on referred as **hosts**)_.

<!-- In this design symbionts are a hybrid between IPFS Client and an IPFS node with limited capabilities _(Such as IPFS node embedded in a web site)_. In solitude symbionts operate in limited capacity. They can seamlessely upgrade thier capabilities through a partner host. -->

Through the [symbiosis protocol](#Symbiosys-protocol) a **host** can announce [services](#Services) that **symbionts** can _request_ to overcome own limitations. 

Protocol defines `m:n` relationship implying that a symbiont can have multiple partner hosts and a host could partner with multiple symbionts.


##### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->

- Neither embedded IPFS node nor IPFS client provide an adequate solution for building products in constrained environments.
- OS level node sharing with existing building blocks is impractial.
- Lack of generalized delegation protocol between nodes leads ad-hock stop-gap solutions.
- Teams are unable to plug domain specific extensions without having to fork our stack.
- Proposed solution avoids accidental centralization (0 cost in host symbiont switching)
- Provides a seamless capabilities upgrade and downgrade experience.

##### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->

#### Example: Symbiont leveraging multiple hosts

A symbiont on a phone may be paired with a host on a laptop to leverage improved capabilities when the two are on a same wifi network. At the same time a symbiont on the phone can be paired with a remote host over the internet to allow all user devices to sync on the go.


#### Example: Web content leveraging IPFS Desktop 

Multiple symbionts that are embedded in web apps _(on different origins)_ can request services from the host embedded in an IPFS Desktop. IPFS Desktop would surface a permission prompt, if user grants it, the host will enable the requested services to the requesting symbiont. _(e.g allowing it to have local area network access to discover and connect to other IPFS nodes in the same wifi)_


#### Example: Cloud computing

[Cloud computing][] provider exposes IPFS in their serverless platform. To do so they spin up IPFS symbionts, pre-paired with a multi-tenant always-on host at the edge.

#### Example: IPFS as an OS service

Desktop application embeds a node which can operate as a symbiont and/or a host. At startup it attempts to run as a symbiont that leverages an existing host (E.g exposed through a [Unix Domain Socket][]). If host is not running, it starts one, which can be leveraged by itself and others.

#### Example: Filecoin based cold storage service

Host A provides [AWS Glacier](https://aws.amazon.com/glacier/) as "cold storage" service. Host B abstracts filecoin markets & deals as "cold storage" service. Symbiont can leverage either or both via single interface.

<!--

Jordan discovers awesome Inter Planetary note taking web application. It is great it works offline it's end to end encrypted even allows to backup data in "pinning service" of choice, you could even provide a URL there. After using this product for a week Jordan is offered to download companion desktop app to unlock cool features like exposing those notes in the filesystem, sharing notes with other devices on the same network while offline. Jordan was heading to an off-grid camp with peers next week and decides to give it a try. Once app is installed os level prompts asks permisson to read write files in `~/Documents` and local network discovery. After granting permission all the notes appear in `~/Documents` so they could be edited with all the other application on the system. Local sharing appeared to be a hit at the camp, allowed peers to collaborate without interenet connection from а web browser 🤯

After returning from camp Jordan finds out that there are whole lot of Inter Planetray apps they all seem to work off the grid if given a permission. Better yet those permisions are as easy to revoke as it was to grant them!

Better yet unlike all these other web apps inter planetary ones can access each others documents all it takes, you've guessed it granting a permission!

-->

##### Impact
_How directly important is the outcome to our top-level mission?_

<!--
Explain why you have chosen this rating
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

🔥🔥🔥 

<!-- - Addresses some of the long standing problems (outlined in appendix) that teams building on IPFS are experiencing and are forced to work around. -->

- Enables teams to plug domain specific extensions without having to fork our stack.
- Enables IPFS nodes to leverage local infrastructure.
- Enables short-lived IPFS node use cases (e.g. mobile devices, serverless computing).


##### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_


<!-- Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

🎯🎯🎯

- Enables IPFS to expand into areas like [serverless computing][cloud computing] where both full IPFS node and IPFS Client are impractical.
- Lays foundation for **multi tenanant** nodes that are needed to realize full potential of embeded IPFS  in web browsers (e.g brave) and/or OS.
- By enabling domain specific protocol extensions we grow the network instead of fragmenting it.

##### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

<!--Explain why this rating-->

Level 3

There is enough evidence supported by our own [ad-hock stop-gap solutions](#Ad-hoc-stop-gap-solutions) combined with [solutions our  collaborators need to resort for](#Unintentionally-Incompatible-infrastructure) to justify this level of confidence.

### Project definition
##### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

1. Specificy [symbiosis wire protocol](#Symbiosys-protocol).
2. Implement domain service that host announces (will figure out the right one by talking to collabs).
3. Implement permission handling flow on the host.
4. Make symbiont leverage announced service through the protocol.
5. Collaborate with teams to validate design with differnt use cases.
6. Take learnings and implement zeroconfig service discovery.

##### What does done look like?
_What specific deliverables should completed to consider this project done?_

- Have at least one collab adopt symbiosis protocol.
- IPFS Desktop providing services that enhances in-browser node capabilities.

#####  What does success look like?
_Success means impact. How will we know we did the right thing?_

- Collabs are adopting a protocol to extend a stack instead of forking it.

<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

##### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

- It does not adequately solve problems of our users.
- Solution is to generic to be practical.
- Service discovery is not reliable and still requires node configuration.

##### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

- Implement permission and authentification layer to existing IPFS HTTP API.
- Allow users to extend HTTP API with domain specific routes.

##### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

- none

##### Future opportunities
<!--What future projects/opportunities could this project enable?-->

- IPFS in serverless compute.
- IPFS node sharing across applications.
- Domain specific protocol extensions as services (e.g. replication optimization based on DAG structure knowledge like Textile does)

### Required resources

##### Effort estimate
<!--T-shirt size rating of the size of the project. If the project might require external collaborators/teams, please note in the roles/skills section below). 
For a team of 3-5 people with the appropriate skills:
- Small, 1-2 weeks
- Medium, 3-5 weeks
- Large, 6-10 weeks
- XLarge, >10 weeks
Describe any choices and uncertainty in this scope estimate. (E.g. Uncertainty in the scope until design work is complete, low uncertainty in execution thereafter.)
-->

- Large
- Uncertainty on discovery implementation until several services are implemented.

#### Roles / skills needed

- Ecosystem team member for coolab coordination.
- At least on go engineer for host implementation.
- At least on JS engineer for symbiont implementation.


<!-- ## Vision statement
> _Please describe what the state of the IPFS project would look like if execution of this theme is massively successful._

Building web3 app is no brainer, you no longer need to worry about data availability, persistence or identity. In browser JS-IPFS node can be paired with a delegate node(s) of user's choosing. Each IPFS node already has an identity and pairing multiple of them is all that needed to sync and get consistent view of user data across various devices.

IPFS Desktop becomes an effective way to upgrade in-browser IPFS node capabilities by delegating to it. In other words in-browser IPFS nodes provide great local-first experience with 0 upfront cost, optional IPFS Desktop install upgrades that experience to the next level by providing local area networking capabilities, more permanent storage etc...

Various (payed) delegate services come online that users can choose from to that empower even most limited devices on the network.

Node peering and delegation work lays foundation for multi-tenant IPFS nodes, which enables it to enforce access control across various apps that use node. Brave and other browsers can build upon this to provide a web compatible content security policies. 
 -->

# Appendix

## Constraints of the operating environment

There is an inherent asymmetry in node capabilities imposed by the constraints of the operating environment

#### Networking
- Browsers can not be dialed
  > Other than throughs WebRTC, which has bunch of problems:
  > 1. Implementations in browsers (as of this writing) use significantly more resources (than http connections ).
  > 2. Require centralized signalling
  > 3. Require [TURN server][]s to rely traffic when direct connections can't be establish.
  > 4. Are not available in worker threads.
  > 
  > In practice resulting in significant overhead, additional limitations while still relaying traffic through TURN server. 
- Browsers allow only a handful network connections.
- Browsers can only dial addresses with SSL certificates.
#### Lifetime / Availability
- Mobile operating systems make long lived connections impractical (backgrounding, battery usage)
- Mobile phones oftes switch networks and there for network addresses
- Web platform does not support long lived background tasks
    - service workers are deactivated as soon as fetch is complete
    - workers are terminated as soon as tab is closed
    - shared workers are not implemented in Apple webkit.
- [Cloud computing][] provides short lived execution model
- [Circuit Relay][] allows nodes to overcome some networking contraint by tunneling communication.
- [Pinning Service API](https://ipfs.github.io/pinning-services-api-spec/) standardizes a way to leverage some nodes in the system for data persistence & availabality.
- [Preload nodes](https://github.com/protocol/bifrost-infra/blob/master/docs/preload.md) allows data to remain available after browser node is gone.

## Ad-hoc stop-gap solutions

Attempts to overcome inherent platform limitations often leads to stop-gap solutions that introduce centralization into the system:

#### [Preload Service]

Preload nodes augment JS-IPFS, exposing API endpoints for IPFS that aren't otherwise available in web platform. In practice, that means JS-IPFS clients can add some content locally, then use a preload node to request that CID, effectively caching the data and allowing the browser tab to be closed without the data instantly becoming unavailable.

The addresses are [hardcoded in js-ipfs][preload addresses] and need to be tied to their specific peerid.


#### [Delegated content routing]

(Ab)uses [IPFS HTTP API][] (specifically [`/api/v0/dht/findprovs`](https://docs.ipfs.io/reference/http/api/#api-v0-dht-findprovs) and [`/api/v0/refs`](https://docs.ipfs.io/reference/http/api/#api-v0-refs) endpoints in order to leverage more capable node in the network to perform content routing calls.

Unfortunately it is not part of the protocol. So routing node discovery happens out of band (In practice that is hard coded address in the configuration). It also implies setting up damain name and SSL/TLS certificates on the routing node. 


#### [Pinning Services API]

Custom HTTP API enabling local IPFS node to manage pins on remote node(s).

This is great solution enabling different services to be plugged in. Still, if nodes were able to develop symbiotic relationships delegated pinning would just be part of it. 

#### Centralized Signaling Services

Most discovery schemes supported in web environment requires centralized signalling service

- [websocket-star](https://github.com/libp2p/js-libp2p-websocket-star)
- [stardust](https://github.com/libp2p/js-libp2p-stardust)
- [webrtc-star](https://github.com/libp2p/js-libp2p-webrtc-star)

## (Unintentionally) Incompatible infrastructure


Teams building products on IPFS resort to filling capability gaps with custom (unintentionally) incompatible infrastrcuture.

- http://fission.codes has a server component that enables **(TODO: Verify details**)
    1. User to associate multiple IPFS nodes (across user devices) with an account/identity.
    1. Update [DNSLink][] records to reflect current state of user data.
    2. Data persistence to facilitate cross device sync.
- [Textie threads](https://docs.textile.io/threads/) requires a deamon **(TODO: verify)**
    1. JS library is a client of the deamon.
- 3Box maintains own infrastructure **(TODO: Verify)**
    1. To replicate user data.
    2. Facilitate pubsub.

## HTTP API provides inadequate solution

[IPFS HTTP API][] provides inadequate solution to the constrained environments


-  It gives client an absolute control of the host node
   - This is inpractical even with a localhost as clients (apps) need to be **isolated** and their access needs to be **revocable**.

     - Browser with embeded IPFS node would need to provide each app restricted & isolated access to the node
     - An OS level IPFS service would need to implement similar sandboxing to prevent data races.
     - If malicious web app tricking user into giving access, assume full control of node and all the user data in it.
     - Well intentioned clients can run into race conditions
         - Unintentionally overwrite path in MFS.
         - Unpin content other clients needs.

- It provides inpracitcal path to incremental enhancements.
  - By default requests from web browsers are blocked (Due to [CORS][] vialoation) which requires:
      1. Stopping a host node.
      2. Writing site origin into IPFS config file.
      3. Starting a host node back up.

    _In the process host will drop all other clients. They will need to keep trying to reconnect and on success recreate local state_
    
- Fallback mechanism (like [ipfs-provider][]) will needs to switch between JS-IPFS node and IPFS Client. This results in an observable difference:
    - IPFS Node with different peerid / address(es).
    - Different states of (M)File System and Pinset.
  
   Making it impractical when building competitive product experience.
    
- Not a practical option on mobile
    - It is not viable to run a local IPFS host node on mobile device, due to backgrounding.
    - Remote IPFS host node would require
        - SSL/TLS certificates
        - Some form of authentification
        - A host per modile device.

Similar problems are manifested in desktop operating systems
- Applications may want to use different node configurations
  > This was pressing issue when we had IPFS Desktop, Textile Desktop Photos and Radicle.
  > They all end up embedding differnt IPFS nodes to avoid this problem.
  > // **TODO:** Check how does [IPFS Desktop], and [Space Daemon][] get along with one another
- Using [IPFS HTTP API][] for sharing would still inherit all the issues.

## Symbiosys protocol

> Protocol draws it's inspired from [DNS Service Discovery (DNS-SD)][DNS-SD] a [zero-configuration networking][] technique.

Wire protocol that is agnostic of transport and representation (message encoding) _(This makes it a good fit for cross thread communication and a cross network interface)_.

At the high level protocol allows IPFS nodes to announce services they can provide to other nodes on the network, which can be requested by connected nodes to overcome their limitations.

Protocol defines:

1. Interface enabling host node to announce services it can provide / lease.
   > How announcement gets delivered is not specified, it can be over local mDNS over pubsub off band etc...
3. Interface enables  connected symbiont to request an access to set of capabilities. Request encodes:

   1. Set of requested services / capabilities.
   2. A public key to associate permission / sandbox with.

 Protocol assumes:
   
   1. Host provides service(s) to **multiple** unrelated symbionts.
   2. Host persists granted permissions across multiple sessions.
   3. Host Isolates and enforces access by a public key.
      > [Public key cryptography][] is used to enforce access level _(Typically public key would correspond to peer id, but protocol does not mandate this to enable various use cases)_.
   5. Host is free to revoke permission
      > Revokation reason can be arbitrary. E.g. 
      > - Payment for service was not received.
      > - In IPFS Desktop user revokes permission to specific web page). 

## Services

Protocol does not prescribe specific set of services with an assumbtion that they could be developed as needed. That said below are couple of examples:

- Enhanced dialability (tunneled through the host)
- Local area network access
- Remote pinning
- Content routing
- Content caching
- Content naming (IPNS, DNSLink)
    - fission.codes updates DNSLink when user MFS changes
- Domain specific replication
    - Textile threads sync without having to go back and forth
    - CRDT specific replication scheme
- Querying
    - IPLD selectors
- Inbox / Message queue
    - Textile allows queueing messages so you can get them when you're back online



[Preload Service]:https://github.com/protocol/bifrost-infra/blob/master/docs/preload.md
[Delegated content routing]:https://github.com/libp2p/js-libp2p-delegated-content-routing
[preload addresses]:https://github.com/ipfs/js-ipfs/blob/a153d919516ba6e4ef2b7e2d85340ea26d226db1/packages/ipfs-core/src/components/index.js#L272-L277
[IPFS HTTP API]:https://docs.ipfs.io/reference/http/api/
[TURN server]:https://webrtc.org/getting-started/turn-server
[service workers]:https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers
[DNSLink]:https://docs.ipfs.io/concepts/dnslink/
[cloud computing]:https://en.wikipedia.org/wiki/Cloud_computing
[CORS]:https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
[ipfs-provider]:https://github.com/ipfs-shipyard/ipfs-provider
[IPFS Desktop]:https://github.com/ipfs-shipyard/ipfs-desktop
[Space daemon]:https://github.com/FleekHQ/space-daemon
[Unix Domain Socket]:https://en.wikipedia.org/wiki/Unix_domain_socket
[Pinning Services API]:https://ipfs.github.io/pinning-services-api-spec/
[mDNS]:https://en.wikipedia.org/wiki/Multicast_DNS
[PKI]:https://en.wikipedia.org/wiki/Public_key_infrastructure
[Public key cryptography]:https://en.wikipedia.org/wiki/Public-key_cryptography
[zero-configuration networking]:https://en.wikipedia.org/wiki/Zero-configuration_networking
[DNS-SD]:https://tools.ietf.org/html/rfc6763
[Circuit Relay]:https://github.com/libp2p/specs/blob/master/relay/README.md
