# Interactive ecosystem directory

Author: @jessicaschilling

Initial PR: https://github.com/protocol/web3-dev-team/pull/72 

Larger-scale proposal for overall ipfs.io work (deprecated, as broken into smaller pieces): https://github.com/protocol/web3-dev-team/blob/ipfsio-modular-rework/proposals/ipfsio-modular-rework.md

Project tracking board for overall ipfs.io work: https://github.com/orgs/ipfs/projects/11

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

<!--
Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

<!--Explain why this rating-->


## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

#### What does done look like?
- Initial (IPFS) implementation is live in full view at ecosystem.ipfs.io (or similar), including metrics collection
- Summary/teaser views are installed on ipfs.io and, if appropriate, docs.ipfs.io
- Documentation is ready for those who wish to fork

####  What does success look like?
- Steady and increasing traffic to directory as a whole
- Measurable engagement with "next steps" throughout directory: repo/case study/outbound links, dwell time in ecosystem as a whole, etc
- Enthusiasm from other builders who want to be included in directory (TBD if we wish to allow builders to self-submit to be in directory, or if it's by invitation)
- Ease of forking for other projects

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

- Failure to make modular enough to easily fork for other future projects
- Failure to maintain: ecosystem collabs get stale or go out of business, new ones don't get added
- Risk of dilution of messaging due to "design by committee"
- Trying to do too much for too many audiences (too long, too complex, not complex enough, etc)

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

- Refocus Awesome IPFS to _only_ include high-impact/high-value collabs (but this leaves us without a showcase for nifty one-off hacker projects and the like)
- Expand existing raster diagram to include more info (but a code-based solution like this proposal would actually be easier to maintain, particularly because it can be forked for other projects)

#### Dependencies/prerequisites
- Getting enough participants for existing launch (on track for approx 50 participants as of early March)

#### Future opportunities
- Already plans to fork this content for Filecoin ecosystem
- Already plans to fork this content for one-off events, like a showcase of hackathon participants, since data source is JSON rather than an integrated database

## Required resources

#### Effort estimate
Shirt size: Large

_Note that sizing is for the initial (IPFS) implementation only; forks (Filecoin, hackathons, etc) will need extra time for customization._

#### Roles / skills needed
- Project lead/PM/agency liaison (Jessica Schilling): Coordinate tasks, manage schedule/dependencies, ensure adherence to spec, etc
- Agency build team (Agency Undone): Execute to spec, including both design and code
