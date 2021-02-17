# Modular rework of ipfs.io for w3dt positioning and PMF alignment

Author: @jessicaschilling

Initial PR: https://github.com/protocol/web3-dev-team/pull/10

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

This project will enable us to finally have a concise, up-to-date, clearly-pathed entry point for prospective w3dt developers that illustrates where IPFS fits into the w3dt stack as a whole, offers clear value propositions of IPFS (as part of w3dt) for our most important use cases, and provides a concrete on-ramp for getting started building.

This matters because:
- It enables us to have an entry point to our PMF measurement funnel that doesn't itself detract or muddy our metrics
- With the Jan 2021 paradigm shift, we now have *massive* "comms debt" about how IPFS fits into the w3dt stack as a whole

Happy side effect: If we build this correctly, even though our messaging is for prospective devs, it also makes it *much* more likely for non-devs (media, engineering managers, CTOs, etc) to understand w3dt and its potential.
<!--
Outline the status quo, including any relevant context on the problem you’re seeing that this project should solve. Wherever possible, include pains or problems that you’ve seen users experience to help motivate why solving this problem works towards top-line objectives. 
-->

#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
- ✓ There must be existing confusion around IPFS use cases and value proposition, particularly vis-a-vis the rest of the w3dt stack
- ✓ There must be existing frustration around the effectiveness of the existing ipfs.io
- ✓ ipfs.io must be a common search result for those curious about the dweb, w3dt, and/or IPFS

#### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->
1. Developer or other decisionmaker is curious about decentralization/dweb/web3 in general, and/or the w3dt stack or IPFS in particular
2. They easily find the ipfs.io site due to its longstanding SEO weight
3. They quickly understand the following, *relative to their own need at hand*:
    - what IPFS is
    - the potential it offers within a w3dt-stack mental model, including how it can play well with web2 tech as needed
    - how IPFS (as part of the w3dt stack) can provide tangible value to their project or solve an existing need, including examples from industries/use cases similar to theirs
    - how to get started building
    - where to go for help or other next steps
4. They get started trying it out and progress to the next circle in the Magic State Machine

#### Impact
_How directly important is the outcome to web3 dev stack product-market fit?_

🔥🔥🔥

- We'll finally clearly convey value propositions for important use cases, explictly communicating product-market fit
- We'll clarify how IPFS fits into the w3dt stack overall, establishing this new mental model to prospective builders as well as the existing community
- We'll have a clearly-defined, explicitly measurable funnel entry that we can use to measure and validate our progress in w3dt PMF over time
<!--
Explain why you have chosen this rating
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

🎯🎯🎯

* Enable prospective developers to immediately understand what IPFS is, where it fits into the w3dt stack, and how to get started
* Provide means for measuring developer/prospective-developer engagement from the very beginning of the funnel
* Provide measurable entry points for docs, repos, forums and other resources
* Level-set on how we present IPFS value propositions and its place in the overall w3dt stack — enabling us to establish an initial point for further iteration/improvement

<!-- Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.


**Impact = 10** (top of funnel is presently neglected and fundamentally leaky, and this project acts both as a data source and as a lever for many other developer-adoption efforts)
**Confidence = 8** (abundance of internal/external feedback the current site isn't doing its job)
**Ease = 5** (lots of moving parts, but few outright technical challenges in the work itself)

<!--Explain why this rating-->


## Project definition
#### Brief plan of attack

**This project is architected with piece-by-piece, modular implementation in mind in order to provide impact as efficiently as possible. As such, it's intended to be divided into smaller pieces to fit our new teams' cadences and overall workload.** Suggested implementation order is as follows:

1. **(In progress with MOXY, ETA end Q1)** [Rebuild IPFS blog](https://github.com/ipfs/ipfs-blog/issues) with additional news/events/links functionality, improved search, Forestry CMS publishing, and consistency with org usage of VuePress platform.
2. **(Proposed Q1 work)** Revisit and re-assess Q4 2020 [ipfs.io IA outline](https://docs.google.com/document/d/1ni0kQNTLJ8VcpCu-zvpyWceZ3qbZWTJSJVRLCsOxvbY/edit#) to augment/replace existing user-tested content and resources with w3dt-focused material. Test and refine as necessary.
3. **(Proposed Q1/Q2, to begin after blog work complete)** "Lift-and-shift" migration of existing ipfs.io content alongside the new blog/news site. This enables us to maintain a baseline-functional public-facing site while working and implementing the remaining project "modules" in parallel.
4. **(Timeline TBD but some work already in progress)** Parallel creation and as-done implementation of the remaining "modules" in the [ipfs.io IA outline](https://docs.google.com/document/d/1ni0kQNTLJ8VcpCu-zvpyWceZ3qbZWTJSJVRLCsOxvbY/edit#) (acknowledging outline is subject to change under item 2 above, and this will impact PRDs below):
    - “About IPFS” video & interactive explainer ([PRD](https://docs.google.com/document/d/1Av70fWel_BkpPEZ-aQFg3AenW0xfCfaZ6zvC409IoLQ/edit#))
    - “How IPFS Works” interactive explainer ([PRD](https://docs.google.com/document/d/1xujTTf0Y6viPp7P-JTzLGaAdJ6wwCxClXUjji9hq4xU/edit#))
    - **(In progress with PL video team)** “What People are Building” testimonial videos ([PRD](https://docs.google.com/document/d/1zOahZK2268i96o3JooiCf8rXBvFgXhUBtQhrSG1pnWg/edit#))
    - **(In progress [with Agency Undone](https://github.com/ipfs/website/issues/410))** Interactive ecosystem directory *(note: this codebase will also be used for Filecoin ecosystem showcase)*
    - Scaffolding text and UI elements to connect the above ([outline](https://docs.google.com/document/d/1ni0kQNTLJ8VcpCu-zvpyWceZ3qbZWTJSJVRLCsOxvbY/edit#), [wireframe](https://ipfs-ia-scratchpad.netlify.app/)), potentially including visual rebrand as proposed by Eric Ronne ([PRD](https://docs.google.com/document/d/1xaLXYKWLG5ZacOSKA_DjX77SLCl56vUN4ewNlza3FIE/edit))
    - For each item above, metrics determined and set up in order to be defined as done
 
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
