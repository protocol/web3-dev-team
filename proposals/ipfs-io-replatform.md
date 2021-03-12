# "Lift-and-shift" replatforming of ipfs.io

Author: @jessicaschilling

Initial PR: https://github.com/protocol/web3-dev-team/pull/75 

Larger-scale proposal for overall ipfs.io work: https://github.com/protocol/web3-dev-team/blob/ipfsio-modular-rework/proposals/ipfsio-modular-rework.md

Project tracking board for overall ipfs.io work: https://github.com/orgs/ipfs/projects/11

## Purpose &amp; impact 
#### Background &amp; intent
_Describe the desired state of the world after this project? Why does that matter?_
<!--
Outline the status quo, including any relevant context on the problem you’re seeing that this project should solve. Wherever possible, include pains or problems that you’ve seen users experience to help motivate why solving this problem works towards top-line objectives. 
-->

#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->

#### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->

#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

<!--
Explain how this addresses known challenges or opportunities.
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_



#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

- **Impact = 10** (top of funnel is presently neglected and fundamentally leaky, and this project gives us a metrics source for prioritizing future front-of-funnel work while providing a stable, up-to-date platform for implementing it)
- **Confidence = 8** (abundance of internal/external feedback the current site isn't doing its job)
- **Ease = 5** (lots of moving parts, but few outright technical challenges in the work itself)

## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

#### What does done look like?
- Existing content on ipfs.io is migrated to new platform and deployed via Fleek with no disruption of service, broken links, etc
- Metrics collection implemented via Countly

####  What does success look like?
- More granular metrics as a whole
- Ability to use those metrics to help us impact-prioritize future site enhancements
- Easier, less "risky" deploys (requires less infra intervention, etc)
- Door open to future rapid iteration on site improvements without first needing to resolve tech debt

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

- Stopping just at replatforming and not using it as a launchpad for further PMF iterations and improvements

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

- Rework messaging on existing website (note though that this doesn't save much effort; migrating the existing website is the least worry, and will lead to duplication of work in the future if we decide to replatform at a later date)

#### Dependencies/prerequisites
- Not strictly a dependency, but development work will go smoother if we wrap up IPFS blog replatform first

#### Future opportunities
- Easier and quicker to iterate on future site improvements
- Speedier, easier deployments
- Enhanced metrics open possibilities for more rapid ore even A/B message testing

## Required resources

#### Effort estimate
Shirt size: Medium if no work apart from lift-and-shift, large+ if additional site enhancements included in initial work (recommend breaking these out into batches for future proposals)

#### Roles / skills needed
- Project lead/PM (Jessica Schilling): Coordinate tasks, manage schedule/dependencies, ensure adherence to spec, etc
- Build/test team (Zé Bateira, João Peixoto): Replatform, add metrics, pre- and post-launch testing
- If work expands to include any site enhancements, skills needed may include user research/testing, content writing, visual design
