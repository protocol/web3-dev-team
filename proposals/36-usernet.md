# Usernet -- a permissioned, stable, zero-cost testnet for experimenting users and web3 devs

Authors: @raulk.

Initial PR: https://github.com/protocol/web3-dev-team/pull/36

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

## Purpose & impact

#### Background & intent
_Describe the desired state of the world after this project? Why does that matter?_

<!--
Outline the status quo, including any relevant context on the problem you’re seeing that this project should solve. Wherever possible, include pains or problems that you’ve seen users experience to help motivate why solving this problem works towards top-line objectives. 
-->

##### User experience (UX)

Imagine I'm a potential user or developer that comes across Filecoin on the interwebs.
I think "this sounds cool, let's give it a try".
This sends me down a rabbit hole:

- I need to purchase FIL in an exchange.
- For this I need to have an account at an exchange.
- Assuming I don't, I will need to go through KYC and surrender a lot of personal data and documents. Then I need to wait to get my account approved.
- Then I need to send funds on my exchange wallet. If I don't own any crypto, I'll have to wire fiat, which won't arrive immediately. Depending on my banking situation, this operation may not be free of charge.
- Wait until the funds arrive.
- Ok, good! The funds are there. I might be in a position to actually buy the token now.
- Let's figure out how this exchange works... the order book... what is a market order? What is spot? What is margin? Whaaaat?
- Yes! I bought 10 USD worth of FIL. Now what do I do?
- Ok, I need to download a Filecoin client, create a wallet, and withdraw my FIL to it.
- Nice, now I have FIL. (Oops, did I realise that I now may have new tax reporting obligations, just because I wanted to try out this thing?)
- (Insert deal making process and associated pain, see [Project F3 pitch](https://github.com/protocol/web3-dev-team/pull/12)).

Compare with Dropbox (personal data) / S3 (API-based cloud storage provider):

1. Sign up for free.
2. Try out the thing.

##### Developer experience (DX)

Developers building on Filecoin have three options:

1. Test on testnet: now defunct.
2. Test on mainnet: requires real money, and iteration is slow due to sealing times, paying for unnecessary guarantees (e.g. 180d deal duration; when testing or developing, you don't need that much).
3. Set up their own local devnet: complex, heavy, requires infrastructure.

Ideally, we'd provide a network that reproduces the conditions of mainnet (including faults), that is hosted, for developers to iterate rapidly and exercise the various scenarios that can occur in the Filecoin integration (happy paths, functional errors, faults, expiries, etc.)

##### A dedicated network

This proposal aims to introduce a new Filecoin network: a **permissioned, stable testnet** that is operated by Protocol Labs and other trusted partners, with zero-cost deals, some form of quick sealing, and short deal duration, so that new users can get started immediately without having to buy FIL, spend a dime, or have to suffer whatever the current market dynamics are (miner market, gas market, etc).

We propose calling this network "usernet" -- to distinguish it from "testnet", which is where the clients test protocol forks, upgrades, and more.

For context, in the deployment sequence of releases, usernet would be situated ___after___ mainnet, i.e. it tracks mainnet, it does not serve as a protocol testing ground.

The envisioned sequence is:

```
testnet (== preproduction) =>
  mainnet (== production) =>
    usernet (== a functional mirror of mainnet with a lower technical footprint)
```

Some attributes of this network:

* Permissioned: the consensus of this network is via Proof of Authority (similar to the Kovan, Rinkeby Eth1 testnets), allowing a closed set of pre-authorized participants (e.g. Protocol Labs, Filecoin Foundation, and partners) to mine. This ensures high uptime, stability, and ease of maintenance.
* Zero-cost: deals and other operations should cost users zero. Gas and deals are still quoted in FIL (actually, usernet FIL, uFIL?), and there is a faucet with appropriate abuse prevention mechanisms (e.g. captcha) to draw uFIL.
* Lower deal duration: minimum duration should be in the order of minutes (allowing app developers to test code paths to renew deals, or to deal with expiring deals), and maximum duration should be 1 day (so that storage dedicated to running this network is )
* Equal power / mining: all participants have equal, fixed power, and they mine in round robin (potentially).
* Fake sealing: real sealing should not be necessary as long as we reproduce the behaviour seen in mainnet (or we provide appropriate disclaimers), so as to not mislead users and create false expectations.
* Limited list of miners, instead of the very many that exist in mainnet.

#### Assumptions & hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->

* Users want to experiment with Filecoin without having to pay out of their own pocket.
* Developers building dapps that integrate with Filecoin want to iterate quickly without having to spin up their own infrastructure to host a Filecoin devnet.
* We have the capacity to spin up and monitor a new network.

#### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->

1. User starts lotus pointing it to usernet, in lite mode: `lotus daemon --usernet --lite`
2. Output displays a generated wallet address that will serve as their default address, and a usernet faucet URL embedding their address (e.g. `https://usernet.filecoin.io/faucet?destination=<address>`) so that user doesn't need to copy-paste.
3. User clicks on link and draws uFIL from the faucet into their address.
4. They wait for 1-2 confirmations, and voilà, they can get started making deals, working with payment channels, multisigs, etc.

#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

<!--
Explain how this addresses known challenges or opportunities.
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

We'd engage users that are curious about Filecoin more readily, as usernet would inarguably reduce the initial friction in the manners stated above.
Developers developing dapps would accelerate their go-to-market since the time and resources they'd invest to spinning up and maintaining a devnet can now be dedicated to actual dapp development.

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

<!--
Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

* A low-friction, lightweight, nimble usernet would accelerate all kinds of experiments and the delivery of projects being built on Filecoin.
* More initial success => more traction => new contributors => etc.
* Also, making the relevant components pluggable would enable us to switch implementations quicker in the future -- thus encouraging experimentation.
* We might see more usernets with different QoS!

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

`2`. TBD.

## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

1. Fully design the technical characteristics of usernet. Decide on operational / maintenance aspects.
2. Pitch key ecosystem members on the idea and get them involved.
3. Implement prototypes for the permissioned mining, fake sealing, and modified deal duration parameters. Evaluate feasibility and iterate on the design.
4. Fully implement all aspects of usernet.
5. Design the bootstrapping strategy and plan.
6. Adjust and deploy the faucet.
7. Write documentation on how to connect to usernet.
8. Launch the network.
9. Monitor, operate, etc.

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

TBD.

####  What does success look like?
_Success means impact. How will we know we did the right thing?_

<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

TBD.

#### Counterpoints & pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

One more network to monitor/operate.

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

1. Subsidizing deals on mainnet via PL miners => not an option because gas still needs to be paid by the user.
2. Awarding small amounts of FIL to testers/experimenters on request => does not scale, manual process, users still have to deal with varying mainnet conditions. Does not work for developers, who'd likely need larger amounts of FIL. It starts looking like a grant programme.

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

N/A.

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->

TBD.

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

Large / XLarge.

#### Roles / skills needed
<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->

* 2 x engineers.
* infra expertise.
* product manager to handle everything related to collaborators.
* TPjM.
