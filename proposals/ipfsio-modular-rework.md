# Modular rework of ipfs.io for PMF alignment

Author: @jessicaschilling

Initial PR: https://github.com/protocol/web3-dev-team/pull/10

## Purpose &amp; impact 
#### Background &amp; intent
_Describe the desired state of the world after this project? Why does that matter?_

This project will enable us to finally have a concise, up-to-date, clearly-pathed entry point for prospective w3dt developers that illustrates what IPFS is, offers clear value propositions of IPFS for our most important use cases, and provides a concrete on-ramp for getting started building. *As our overall mental model of the w3dt stack develops and solidifies, the site will (eventually, but not for initial build) also illustrate where IPFS fits into the w3dt stack as a whole, and expand value propositions to present IPFS as part of a w3dt whole.*

This matters because:
- It enables us to have an entry point to our PMF measurement funnel that doesn't itself detract or muddy our metrics
- With the Jan 2021 paradigm shift to a w3dt model, we are gradually incurring "comms debt" about how IPFS fits into the w3dt stack as a whole

Happy side effect: If we build this correctly, even though our messaging is for prospective devs, it also makes it *much* more likely for non-devs (media, engineering managers, CTOs, etc) to understand w3dt and its potential.

#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
- ✓ There must be existing confusion around IPFS use cases and value proposition
- ✓ There must be existing frustration around the effectiveness of the existing ipfs.io site
- ✓ ipfs.io must be a common search result for those curious about the dweb and/or IPFS

#### User workflow example
_How would a developer or user use this new capability?_

1. Developer or other decisionmaker is curious about decentralization/dweb/web3 in general, and/or the w3dt stack or IPFS in particular
2. They easily find the ipfs.io site due to its longstanding SEO weight
3. They quickly understand the following, *relative to their own need at hand*:
    - what IPFS is
    - the potential it offers, including how it can play well with web2 tech as needed (in time, this will also be contextualized within a w3dt-stack mental model)
    - how IPFS can provide tangible value to their project or solve an existing need, including examples from industries/use cases similar to theirs
    - how to get started building
    - where to go for help or other next steps
4. They get started trying it out and progress to the next circle in the Magic State Machine

#### Impact
_How directly important is the outcome to web3 dev stack product-market fit?_

🔥🔥🔥

- We'll finally clearly convey value propositions for important use cases, explictly communicating product-market fit
- We'll have a clearly-defined, explicitly measurable funnel entry that we can use to measure and validate our PMF progress over time

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

🎯🎯🎯

* Enable prospective developers to immediately understand what IPFS is, where it fits into their larger world, and how to get started
* Provide means for measuring developer/prospective-developer engagement from the very beginning of the funnel
* Provide measurable entry points for docs, repos, forums and other resources
* Level-set on how we present IPFS value propositions — enabling us to establish an initial point for further iteration/improvement

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.


- **Impact = 10** (top of funnel is presently neglected and fundamentally leaky, and this project acts both as a data source and as a lever for many other developer-adoption efforts)
- **Confidence = 8** (abundance of internal/external feedback the current site isn't doing its job)
- **Ease = 5** (lots of moving parts, but few outright technical challenges in the work itself)


## Project definition
#### Brief plan of attack

**This project is architected with piece-by-piece, modular implementation in mind in order to provide impact as efficiently as possible. As such, it's intended to be divided into smaller pieces to fit our new teams' cadences and overall workload.** Suggested working order is as follows, with items for Q1/Q2 2021 implementation noted with 🚧 ...

1. 🚧 **(In progress with MOXY, ETA end Q1)** 🚧  [Rebuild IPFS blog](https://github.com/ipfs/ipfs-blog/issues) with additional news/events/links functionality, improved search, Forestry CMS publishing, and consistency with org usage of VuePress platform.
2. **(MOXY to begin after blog work complete)** "Lift-and-shift" migration of existing ipfs.io content alongside the new blog/news site. This enables us to maintain a baseline-functional public-facing site while working and implementing the remaining project "modules" in parallel.
3. Parallel creation and as-done implementation of the remaining "modules" in the [ipfs.io IA outline](https://docs.google.com/document/d/1ni0kQNTLJ8VcpCu-zvpyWceZ3qbZWTJSJVRLCsOxvbY/edit#). **IMPORTANT: Items that risk substantial reworking when reframed in a w3dt mental model will not be tackled until that model is solidified.**
    - 🚧 **(In progress with PL video team, ETA early Q2)** 🚧  First in “Builders Series” testimonial videos, featuring Pinata ([PRD](https://docs.google.com/document/d/1zOahZK2268i96o3JooiCf8rXBvFgXhUBtQhrSG1pnWg/edit#))
    - 🚧 **(In progress [with Agency Undone](https://github.com/ipfs/website/issues/410), ETA early/mid Q2)** 🚧 Interactive ecosystem directory *(note: this codebase will also be used for Filecoin ecosystem showcase)*
    - “About IPFS” video & interactive explainer ([PRD](https://docs.google.com/document/d/1Av70fWel_BkpPEZ-aQFg3AenW0xfCfaZ6zvC409IoLQ/edit#))
    - “How IPFS Works” interactive explainer ([PRD](https://docs.google.com/document/d/1xujTTf0Y6viPp7P-JTzLGaAdJ6wwCxClXUjji9hq4xU/edit#))
    - Scaffolding text and UI elements to connect the above ([outline](https://docs.google.com/document/d/1ni0kQNTLJ8VcpCu-zvpyWceZ3qbZWTJSJVRLCsOxvbY/edit#), [wireframe](https://ipfs-ia-scratchpad.netlify.app/)), potentially including visual rebrand as proposed by Eric Ronne ([PRD](https://docs.google.com/document/d/1xaLXYKWLG5ZacOSKA_DjX77SLCl56vUN4ewNlza3FIE/edit))
    - For each item above, metrics determined and set up in order to be defined as done
4. **(Timeline TBD once w3dt mental model solidified)** Revisit and re-assess Q4 2020 [ipfs.io IA outline](https://docs.google.com/document/d/1ni0kQNTLJ8VcpCu-zvpyWceZ3qbZWTJSJVRLCsOxvbY/edit#) to augment/replace existing user-tested content and resources with w3dt-focused material. Test and refine as necessary.
 
<!--Briefly describe the milestones/steps/work needed for this project-->

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

**"Done"** is a continuum of implementation of one or more of the modules above. **"Final completion"** is execution of all of the above modules, with active metrics being gathered. Completing a single module still furthers our mission, but the more, the better.

####  What does success look like?
* Qualitative: Measurable engagement with site CTAs
* Quantitative: Upward trends in CTA actions (downloads, forks, tutorials started, etc)
* Qualitative/quantitative: Baseline user pathways established that we can measure, tweak and re-measure
* Qualitative: Increased general situational awareness of IPFS's value proposition and positioning within w3dt, based on sentiment/quantity of forum posts/Reddit/Twitter, surveys, user groups, etc

<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

- Risk of dilution of messaging due to "design by committee"
- Lack of metrics-driven messaging design: e.g. failing to create messaging that encourages quantitatively measurable action
- Failure to indicate well enough where IPFS fits into the w3dt stack
- Trying to do too much for too many audiences (too long, too complex, not complex enough, etc)

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

- Rework messaging on existing website (note though that this doesn't save much effort; migrating the existing website is the least worry, and will lead to duplication of work in the future if we decide to replatform at a later date)

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

- Not strictly a dependency, but development work will go smoother if we wrap up IPFS blog replatform first

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->

- This highly modular site will lend itself well to rapid or even A/B message testing
- Modules can be easily forked/modified for use in other w3dt-stack sites, docs, etc (example: Filecoin ecosystem showcase)

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

Large/x-large, though most execution to be outsourced to MOXY, Agency Undone, or other third-party partners in order to minimize core-team impact

#### Roles / skills needed
- Project lead/PM/agency liaison (Jessica Schilling): Coordinate tasks, manage schedule/dependencies, ensure adherence to spec, etc
    - If rebrand included in this project, probably a separate project lead for this work (Eric Ronne)
- Agency partners: Could potentially include ...
    - Build teams for site overall, individual widgets, or some combination thereof (e.g. we don't have to use the same dev shop for everything)
    - Visual design partner for rebrand
- User tester/validator/researcher and/or content writer
    - Particularly in light of reframing content to include entire w3dt stack
    - Not needed 100% of the time, but needs to be able to be called in periodically to test/validate ideas and assumptions and assure project remains on track

<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->
