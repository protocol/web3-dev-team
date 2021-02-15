# IPFS Gateway HTTP API
Authors: @anorth
Initial PR: TBD

## Purpose &amp; impact 
#### Background &amp; intent
_Describe the desired state of the world after this project? Why does that matter?_

Today, web and other clients must embed a full IPFS node implementation in order to interact with IPFS 
on any level deeper than fetching flattened UnixFS file data from a gateway. 
This embedding is heavyweight, and complex. 
Maintaining a fully-featured js-ipfs implementation, as the only integration option, is a lot of work. 
Delegating to a backend IPFS node directly using the RPC-style API is high friction.

After this project, an HTTP Gateway API supports direct interaction with IPLD data using standard web/REST semantics, 
but abstracts away the complexity of native protocol interactions (DHT, bitswap, graphsync) from clients. 
A gateway client can fetch and verify arbitrary IPLD DAGs. 
The API is application-level (DAG-at-a-time rather than node-at-a-time), maximising ease and minimising round-trips. 
Scripts can fetch DAGs with curl to feed into other tools.

Authenticated extensions to the API can push/pin IPLD data to the gateway for hosting. 
The PL-operated gateway is read-only, but a Dapp provider can host their own for Dapp clients to interact with, or embed/extend it with application logic.

"No API is the best API".
Related ideas are in [Verifiable HTTP Gateway Responses](https://github.com/ipfs/in-web-browsers/issues/128), 
[CAR export from HTTP Gateways](https://github.com/ipfs/in-web-browsers/issues/170).

#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_

- Dapp developers want to use IPFS, and there are lots of them
- Dapps and other applications need a more complex data model than UnixFS files
- Dapps and other integrations would find HTTP easier to interact with than low-level protocols
- Embedding a full go/js-ipfs node is a significant barrier to client use
- go/js-ipfs is slower and more difficult to interact with than an HTTP API
- Dapp developers are satisfied with the imperfect decentralization of using a gateway as an intermediate step.
- Having the same, more powerful HTTP API on localhost removes obstacles towards a deeper interaction with vendors like Brave

#### User workflow example
_How would a developer or user use this new capability?_

A dapp developer builds a decentralized, semi-permissionless photo-sharing app. 
They have a server that authenticates users but the rest of application logic is in the JS web client. 
They embed an IPFS gateway in their server, which pins content posted by authenticated users 
(the authentication protects the cost of pinning and third-party precache request abuse). 
Their web app fetches DAGs describing the social graph, image metadata etc from HTTP API, as well as flattened files for the images themselves. 
It’s fast, like a consumer app should be.

#### Impact
_How directly important is the outcome to web3 dev stack product-market fit?_

🔥🔥🔥. If Dapp development is a strong market segment, but adoption is difficult, then reducing barriers to use is of highest importance.

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

🎯🎯 . The rating of 2 is motivated by the benefits of more rapid prototyping and iteration with low-friction APIs. 
If we remove the need for learning intricate, non-intuitive HTTP API and leverage HTTP semantics so that JS “fetch” or curl is all you need, 
we may see many more people experimenting with IPFS. 
The [existing API](https://docs.ipfs.io/reference/http/api/) was not designed to be exposed on the web and introduces
significant overhead for people who want to use IPFS in something more than read-only mode.

Success could result in freeing up significant resources from maintaining and developing js-ipfs as the only client integration point in the short term.

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

Very Low to Low. I don’t have the market data or direct user feedback that may support a higher confidence here.

@lidel suggests they could provide a list of issues related to existing API being overly complex, 
and then js-ipfs-http-client acting as a programmatic interface to cover those shortcomings hurting us even more 
(breaking API changes, maintenance cost, people confused why they can't just use regular XHR/fetch and need a dedicated client lib).


## Project definition
#### Brief plan of attack

- Design RESTful HTTP semantics on top of content-paths
- Settle on appropriate serial representation of DAGs (e.g. CAR, DAR, something else).
- Implement read-only API in HTTP gateway, and deploy it
- Implement JS client library: request wrappers and IPLD decoding/manipulation
- Implement publishing API (ie. HTTP POST), but deny from our public gateways
- Modularise HTTP gateway to permit dapp devs to embed it their back-ends

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

Our gateway serves arbitrary DAGs over simple HTTP requests. 
Web-apps can fetch, manipulate, and render IPLD data with the standard JS XHR or [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) without the need for any client library. 
Backends that embed/extend the gateway also support publishing and pinning arbitrary IPLD data.

####  What does success look like?
_Success means impact. How will we know we did the right thing?_

Dapp and other developers are creating clients that interact with IPLD data natively, with most application logic implemented client-side. 
Our gateway metrics show growth in use of IPLD data. 
Some dapps are running their own backends embedding a gateway, to support pinning data critical to their application. 
Infura and others provide hosting services for gateways, as well as nodes.

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

- Hypotheses about Dapps being an important market, or HTTP being a more accessible API might prove false
- API design could get stuck in a morass of discussion about standards
- Hard-core decentralization people object to the imperfect decentralization of using a gateway

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

- Just add more RPCs for DAG traversal to go-ipfs, that Infura nodes can then serve. Expose these through JS and other client libraries.
- Our gateways provide the read-only go-ipfs RPC API to the public, and establish that as standard
- Amazing technical work so that embedding js-ipfs is both easier and more performant than using an HTTP API

#### Dependencies/prerequisites

- JS-IPLD libraries capable of core encodings and IPLD representation
- IPLD selectors (for non-trivial DAG traversal)
- (For write path) Gateway<->go-ipfs write & pin integration

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->

- Filecoin Gateway API: the same thing but for Filecoin blockchain state and deals

## Required resources

#### Effort estimate
Medium effort (3-5 weeks for a small team). 
Some uncertainty until the API design is complete, but low uncertainty in execution thereafter.

#### Roles / skills needed
- REST API design
- Backend (Go) development

