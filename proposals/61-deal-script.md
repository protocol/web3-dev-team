# DealScript

Authors: @rvagg

Initial PR: https://github.com/protocol/web3-dev-team/pull/60

## Purpose &amp; impact 

#### Background &amp; intent

_Describe the desired state of the world after this project? Why does that matter?_

The current deal-making process is blunt. Miners get to set their public ask parameters, which include:

1. Regular FIL/GiB/epoch
2. FIL+ FIL/GiB/epoch
3. Maximum piece size
4. Minimum piece size

However, there are also mechanisms in addition to these basic parameters which can impact a miners' acceptance of deals. A `Filter` configuration option lets the miner set an external executable that is run for each incoming deal. It's passed complete deal proposal details and can returns an exit code indicating acceptance or not. This information is completely opaque to the potential client who only sees ask parameters. See https://docs.filecoin.io/mine/lotus/miner-configuration/#dealmaking-section for details.

Miners are very sensitive to message cost for publishing deals and this is not factored in to ask amounts. There is only minimum and maximum size with fixed FIL prices for each potential deal size.

Clients making smaller deals are likely to be _less_ price sensitive than for large amounts of data. There is no easy way for a client to make a deal with a miner to store their small thing but pay a premium for it. And there is no way to signal such a willingness on behalf of the miner nor for clients to discover such miners. Typical miner behaviour is to set a high minimum in order to ensure that deals are worthwhile. This means there are very few miners accepting small deals, and those that are may be doing it at a loss.

Many miners don't even respond to `query-ask`, with no information about why. Many deals are rejected, typically with no information about why.

This proposal is to introduce a simple DSL that the miner can use to configure their deal parameters and also communicate to clients what they are willing to accept. Lotus can run the script for deals, and clients can run the script for deals for each miner they are considering.

Such a script could be used to:

 * Set sliding scales of prices for regular vs FIL+ and online vs offline
 * Set price cliffs
 * Set different minimums and maximums for regular vs FIL+ and online vs offline
 * Insert basic logic to encode custom miner requirements
 * Insert comments (and/or textual output from the script) that communicate miner intent and assist in establishing relationships or explain rejection reasons

The complexity of the scripting language is TBD. A simple option would be to use JavaScript which is easy to execute in almost any environment, however the use of a fully-featured language introduces other problems such as the ability for a miner to DoS clients (execution time maximums could be used but this is not easy in some environments). Alternatively, a simple substitionary language with basic variables and operators could be used but unless an existing, widely adopted DSL can be used the imposition of writing a VM in each client environment may be undesireable.

A simplified form of this is to expand on the current configuration options to allow for multiple deal settings to be combined, with different asks for different types of deals are specified and they are evaluated in order until one is found that is satisfied.

#### Assumptions &amp; hypotheses

_What must be true for this project to matter?_


#### User workflow example

_How would a developer or user use this new capability?_

#### Impact

_How would this directly contribute to web3 dev stack product-market fit?_

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

#### Roles / skills needed

<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->
