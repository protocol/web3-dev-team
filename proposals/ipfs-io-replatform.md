# "Lift-and-shift" replatforming of ipfs.io

Author: @jessicaschilling

Initial PR: https://github.com/protocol/web3-dev-team/pull/75 

Larger-scale proposal for overall ipfs.io work, including this effort: https://github.com/protocol/web3-dev-team/blob/ipfsio-modular-rework/proposals/ipfsio-modular-rework.md

Project tracking board for overall ipfs.io work: https://github.com/orgs/ipfs/projects/11

## Purpose &amp; impact 
#### Background &amp; intent
_Describe the desired state of the world after this project? Why does that matter?_

The existing ipfs.io website is replatformed in order to enhance metrics collection (and move off Google Analytics); bring its neglected codebase up to date; align on a platform for all IPFS website properties to make maintenance easier; and allow for easy Fleek deployment. While the site itself does not undergo major improvements at this stage — apart from incorporating the improved header/footer from the replatformed IFPS blog — this sets the stage for continuous improvement and iteration on the site to improve PMF, all fueled and justified by metrics collection.

#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_

✓ There must be existing frustration around the effectiveness of the existing ipfs.io site

✓ ipfs.io must be a common search result for those curious about the dweb and/or IPFS

✓ Metrics are important, but we don't want to go through the work of implementing them on a neglected codebase

#### User workflow example
_How would a developer or user use this new capability?_

1. Developer or other decisionmaker is curious about decentralization/dweb/web3 in general, and/or the w3dt stack or IPFS in particular
2. They easily find the ipfs.io site due to its longstanding SEO weight
3. They see a site that's primed to better and better meet their needs for understanding what IPFS is and how it's valuable to them — _and while those site improvements are not within this project's scope, this project **enables** those improvements_

#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

This project lays the groundwork for enabling us to finally build a concise, up-to-date, clearly-pathed entry point for prospective w3dt developers that illustrates what IPFS is, offers clear value propositions of IPFS for our most important use cases, and provides a concrete on-ramp for getting started building. As our overall mental model of the w3dt stack develops and solidifies, the site will also illustrate where IPFS fits into the w3dt stack as a whole, and expand value propositions to present IPFS as part of a w3dt whole.

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

Even replatforming alone has tangible benefits through enabling better metrics:
- Provide means for measuring developer/prospective-developer engagement from the very beginning of the funnel
- Provide measurable entry points for docs, repos, forums and other resources

However, this project also lays the groundwork for future enhancements that enable prospective developers to immediately understand what IPFS is, where it fits into their larger world, and how to get started.

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

- **Impact = 8** (top of funnel is presently neglected and fundamentally leaky, and this project gives us a metrics source for prioritizing future front-of-funnel work while providing a stable, up-to-date platform for implementing it)
- **Confidence = 10** (abundance of internal/external feedback the current site isn't doing its job)
- **Ease = 5** (lots of moving parts, but few outright technical challenges in the work itself)

## Project definition
#### Brief plan of attack

1. Research and align upon platform decision based upon existing use of platforms, ease of deployment, possibilities for future scope, etc
2. Lift-and-shift migration of existing site content
3. Incorporate header/footer from new IPFS blog for consistency and functional enhancement (e.g. newsletter signup in footer, etc)
4. Set up Fleek deployment process, including workflow between staging and prod
5. Set up Countly-based metrics collection
6. Set up Forestry CMS overlay for consistent authorship experience (given nature of site content, this may not be strictly necessary)
7. Quiet launch (since initial user experience changes little) but close monitoring of metrics to prioritize future site enhancements in next round of work

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
Shirt size: Medium 

#### Roles / skills needed
- Project lead/PM (Jessica Schilling): Coordinate tasks, manage schedule/dependencies, ensure adherence to spec, etc
- Build/test team (Zé Bateira, João Peixoto): Replatform, add metrics, pre- and post-launch testing
- If work expands to include any site enhancements, skills needed may include user research/testing, content writing, visual design
