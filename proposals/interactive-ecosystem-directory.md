# Interactive ecosystem directory

Author: @jessicaschilling

Initial PR: https://github.com/protocol/web3-dev-team/pull/72 

Larger-scale proposal for overall ipfs.io work: https://github.com/protocol/web3-dev-team/blob/ipfsio-modular-rework/proposals/ipfsio-modular-rework.md

Project tracking board for overall ipfs.io work: https://github.com/orgs/ipfs/projects/11

## Purpose &amp; impact 
#### Background &amp; intent
_Describe the desired state of the world after this project? Why does that matter?_

The existing [raster IPFS ecosystem diagram](https://ipfs.io/images/ipfs-applications-diagram.png) is replaced by an interactive, information-rich version that more effectively illustrates how IPFS adds critical value and essential tech enablement for our collabs’ orgs, projects, and industries. This information inspires and empowers prospective developers with concrete examples of success within orgs and projects like theirs.

The complete ecosystem directory lives at ecosystem.ipfs.io (or similar), but is also "teased" from a variety of locations via a minimized, visually themeable version that offers a sortable subset of info with a strong CTA to visit the full version.

The directory will initially launch with IPFS data, but is easily forked and customized for other parts of the w3dt stack, or even for showcasing participants at hackathons and similar events.

#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_

✓ Prospective developers want to know about existing success in areas similar to theirs

✓ Showcasing known wins is essential to inspiring others to adopt the w3dt stack

✓ We have enough known-win builders to be able to make a positive impact by showing them off

#### User workflow example

1. Developer or other decisionmaker is curious about decentralization/dweb/web3 in general, and/or the w3dt stack or IPFS in particular
2. They see a "who's building on IPFS" teaser on ipfs.io, docs.ipfs.io, or other high-level locations, and click through to explore the larger directory
3. They quickly understand the following, *relative to their own need at hand*:
    - many others are already building and succeeding with IPFS
    - including existing wins on their own platform/language of choice
    - existing winners successfully used IPFS to meet their core functional or ideological goals
    - existing winners have repos, case studies or other resources to view as reference/inspiration
4. They try IPFS themselves and progress to the next circle in the Magic State Machine

#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

This directory is an explicit demonstrator of w3dt product-market fit: It literally lays out how w3dt stack ingredients fit into the functional success of high-value builders.

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

By explicitly conveying the benefits of IPFS in real-world use cases, this directory enables more contributors as well as gives them a greater idea of what's specifically possible right off the bat. By pointing to concrete real-world successes (including repos, case studies, etc), this directory should also help shortcut the path between experimentation and initial success for new devs.

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

- **Impact = 10** (top of funnel is presently neglected and fundamentally leaky, and this project acts both as a data source and as a lever for many other developer-adoption efforts)
- **Confidence = 8** (abundance of internal/external feedback the current diagram is outdated and lacking in clarity)
- **Ease = 6** (lots of moving parts, but few outright technical challenges in the work itself)


## Project definition
#### Brief plan of attack

1. Research participants in outdated raster diagram to cull known-invalid ones, add new ones from existing institutional knowledge, etc; consolidate into database (to be used as JSON data source)
2. Survey all participants to ensure data is accurate and inclusion in directory is approved
3. Spec out information architecture, use cases for "teaser view" vs full view, etc
4. Spec out modularity needs so work can be forked for other purposes
5. Wireframe and test wireframes
6. Build phase, including periodic stakeholder check-ins
7. Documentation for future fork-ers
8. Integration in ipfs.io, docs.ipfs.io
9. Social promotion

#### What does done look like?
- Initial (IPFS) implementation is live in full view at ecosystem.ipfs.io (or similar), including metrics collection
- Summary/teaser views are installed on ipfs.io and docs.ipfs.io
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
