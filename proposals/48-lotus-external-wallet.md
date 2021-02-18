# Lotus can interact with external wallets

Authors: @rvagg @dineshshenoy 

Initial PR: https://github.com/protocol/web3-dev-team/pull/48

## Purpose &amp; impact 

#### Background &amp; intent

_Describe the desired state of the world after this project? Why does that matter?_

Lotus has a number of operations that require messages to be signed before landing on chain. The current set of JSON-RPC calls as well as the Lotus CLIs do a number of tasks which simplify the process for the user:

 1. Assemble the JSON message
 2. Generate a nonce
 3. Sign the message

These steps require internal state:

 1. A `From` address.
 2. A nonce (a monotonically increasing integer that’s associated with a particular actor)
 3. A key for message signing

Storing these items internally make it difficult for scaling in certain circumstances as a wallet is associated directly with a Lotus node. Decoupling would activate many use-cases:

 * Multiple wallets used by a single node to sign messages - shared node among multiple users
 * Wallets fully detached from nodes, allowing for lightweight interaction with the chain by message signers
 * Removing custodial requirements for nodes enables better security models, particularly for complex configurations (both miners and clients)

It is atypical for blockchain nodes to have custody of keys on behalf of Dapp developers but we are currently forcing this, or forcing alternative architectures (such as node operators transferring FIL to their own wallets to perform transactions).

We currently don't support the typical MetaMask + Infura style Dapp model and our partners and potential partners are asking for this decoupling.

**Example:**

Raw message generated from user input:

```json
{
    "Version": 0,
    "To": "f12qy5dbvss5wjpiucebkkp4hjixcmotnmzpx2bka",
    "Value": "60000000000000000000",
    "GasLimit": 611585,
    "GasFeeCap": "101067",
    "GasPremium": "100013",
    "Method": 0,
    "Params": null
}
```

Currently lotus performs the following steps:

* Add the `From` attribute
* Add a `Nonce` value
* Add a message CID calculated from the resulting assembled message (TODO: is this a CID of the original message? it can't be of the "assembled message" as that's self-referential)
* Sign the message
* Add a payload CID calculated from the resulting payload

Resulting in the final message to be submitted to the chain:

```json
{
  "Message": {
    "Version": 0,
    "To": "f12qy5dbvss5wjpiucebkkp4hjixcmotnmzpx2bka",
    "From": "f1hbls2zmkfk7tzjre3rlv3faxh7n4ntb47dnii5i",
    "Nonce": 6,
    "Value": "60000000000000000000",
    "GasLimit": 611585,
    "GasFeeCap": "101067",
    "GasPremium": "100013",
    "Method": 0,
    "Params": null,
    "CID": {
      "/": "bafy2bzacedu4nx3lzxf2njupasdqg5xl2imbyoa6ksib6cjyykgxyybb6nxbs"
    }
  },
  "Signature": {
    "Type": 1,
    "Data": "X6EBxXARBRfMlOd89lFnC98RFlkV6ZYcaupLiIfopfVe32hpcgvQvNgp3+QA2+DtsBjK14S/ShiEFnvPrGpTTwA="
  },
  "CID": {
    "/": "bafy2bzacebifjagyqbypbxjiekkclerj4apxwyucao2glmvi4ufm6olvw3wc2"
  }
}
```

There are two critical steps in deal-making that require signing:

* Client signs a message to move funds into StorageMarketActor (to chain)
* Client signs a proposal and proposes a deal to the miner (direct libp2p to miner)

These steps would need to be separated as well. (TODO: I think?)

Enabling decoupled signing would likely mean ammending the API to:

1. Add a flag that causes Lotus to generate a base message but return the envelope to the API callee rather than submitting it
2. Augment the API to allow submission of raw, signed messages that are a result of the callee receiving the message from step 1 and performing their own signing operation (TODO: is this possible already?)

The `MpoolGetNonce` API call can be used to get the appropriate nonce for signing.

API methods that would need this ability are:

* `ClientStarttDeal`
* `ClientCancelDataTransfer`
* `Deals`

TODO: more?

It may also require additional software development / libraries to support client-side signing. e.g. in [Filecoin.js](https://github.com/filecoin-shipyard/filecoin.js) and / or simple Go dependencies.

#### Assumptions &amp; hypotheses

_What must be true for this project to matter?_

 * Partners and potential partners want to scale managed nodes and allow signing by multiple wallets
 * Partners and potential partners _do not_ want to deal with key custody concerns
 * Lighweight interaction will be enabled by this decoupling and this lightweight interaction will accelerate Filecoin Dapp development
 * The security models enabled by this decoupling are _better_ than currently afforded

#### User workflow example

_How would a developer or user use this new capability?_

 * Request generation of raw, unsent message from Lotus API
 * Sign message using client logic
 * Submit back to Lotus for further handling

#### Impact

_How would this directly contribute to web3 dev stack product-market fit?_

Apparently quite high, web3 app developers are used to the model enabled by MetaMask++ which are currently difficult or impossible with our stack. Requring a full Lotus node, or even a light one, is not a good answer. Partners running nodes on behalf of users are at high risk when they have to act as custodians and this also involves trust problems with app developers that could be avoided.

#### Leverage

_How much would nailing this project improve our knowledge and ability to execute future projects?_

#### Confidence

_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

## Project definition

#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

#### What does done look like?

_What specific deliverables should completed to consider this project done?_

####  What does success look like?

_Success means impact. How will we know we did the right thing?_

#### Counterpoints &amp; pre-mortem

_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

#### Alternatives

_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

#### Dependencies/prerequisites

#### Future opportunities

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

Small - Medium depending on skills and knowledge involved

#### Roles / skills needed

<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->

Lotus development experience
