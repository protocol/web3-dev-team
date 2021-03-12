# IPFS blog enhancements

Author: @jessicaschilling

Initial PR: https://github.com/protocol/web3-dev-team/pull/74

Larger-scale proposal for overall ipfs.io work: https://github.com/protocol/web3-dev-team/blob/ipfsio-modular-rework/proposals/ipfsio-modular-rework.md

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

#### Internal leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_


#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

- **Impact = 8** (opportunity to resolve neglected media page with something easy to maintain; making posting significantly easier speeds blog post delivery; tagging and search significantly improve user experience AND add metrics collection points)
- **Confidence = 10** (effort will directly resolve known pain points, including deployment woes, image size, difficulty of posting, no search functionality, etc)
- **Ease = 5** (lots of moving parts, but few outright technical challenges in the work itself)


## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

#### What does done look like?
- Existing content on blog.ipfs.io is migrated to new platform and deployed via Fleek with no disruption of service, broken links, etc
- Workflow and DRI exist for submitting, adding and maintaining non-blog content types
- Any follow-up work is documented, issue-ized, and assigned
- Metrics collection implemented via Countly

####  What does success look like?
- Uptick in overall visitors vs existing blog
- Public-submitted or labber-submitted links are at a "good" number (TBD - will need to establish baseline since this is new functionality)
- Internal satisfaction with ease of posting/publishing/deploying
- Fewer internal fire drills at publishing/revision time; blogging plays a smooth role in overall marketing workflow

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

- Failing to keep content up to date and/or properly tagged
- Failing to make the most of added content types (e.g. only adding blog posts)

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

- Training all blog writers/editors on Markdown practices
- Remedying flaws in our existing CI/CD pipeline

#### Dependencies/prerequisites
None

#### Future opportunities
- More blog authors or more frequent posts due to ease of publishing
- Establishment as a central "IPFS news clearinghouse" and IPFS event directory if those content types are consistently updated

## Required resources

#### Effort estimate
Shirt size: Large

_Note that there's been some slight scope creep (performance instrumentation, CSS cleanup) that may expand this effort if we don't push it into post-launch followup._

#### Roles / skills needed
- Project lead/PM (Jessica Schilling): Coordinate tasks, manage schedule/dependencies, ensure adherence to spec, etc
- Build/test developer (João Peixoto): Replatform, add metrics, add additional functionality, pre-launch testing
- Metrics/continuity dev help (Zé Bateira): Help with adding metrics and other functionality in a manner consistent with other PL sites
