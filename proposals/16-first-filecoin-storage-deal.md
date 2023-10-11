# REVISED Proposal: Reduce friction and time to first successful storage and retrieval deals for new Filecoin storage clients

Authors: @terichadbourne

Initial PR: https://github.com/protocol/web3-dev-team/pull/16 <!-- Reference the PR first proposing this document. Oooh, self-reference! -->

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
As demonstrated in recent walkthroughs by Andrew Nesbitt and Jonathan Victor, there are a number of critical hurdles blocking an easy path to storing files on Filecoin, including both engineering issues (e.g. helpful improvements to Powergate), UX issues (lack of description in CLI about what stages exist, showing miners who aren't actually accepting deals, etc.), and documentation issues (incorrect or incomplete instructions for steps in the process that otherwise are functional).

Since our goal is to promote use of the full W3DT stack by developers with storage needs (as opposed to miners), and we aim to include Filecoin in that journey, most paths to general adoption are blocked until it's easier and faster to make one's first storage deal and clear how to retrieve files once they're stored.

**IMPORTANT NOTE ON REVISIONS**: After reviewing other submitted proposals with similar goals, the scope of this proposal has been revised to focus only on how we can **improve our documentation** to reduce friction in the onboarding process, while [this complementary proposal](https://github.com/protocol/web3-dev-team/pull/12) focuses on the **engineering improvements** that meet the same goal. We've also added file retrieval documentation to the scope of this proposal, since it's a clear need after a storage deal is made.

#### Assumptions &amp; hypotheses
- It should be possible to store a file on Filecoin and retrieve it.
- Documentation should accurately reflect the current best practices for deal storage and retrieval, as well as explaining associated expenses such as gas costs where relevant.
- Developers who attempt to use Filecoin for storage now and are frustrated by an unclear process are unlikely to trust us in the future, once the experience has improved.
- While some frustrations currently faced by users can only be improved by engineering tweaks, many can be tackled by better documenting current best practices.

#### User workflow example
A developer using Filecoin for the first time would visit docs.filecoin.io and successfully follow instructions there to acquire Filecoin to use for the deal, sync or copy the chain (with an understanding of trade-offs in this decision), view available miners with useful information about pricing and availability for storage deals, negotiate a deal, transfer their file, and receive confirmation that the data has been stored successfully. They would also be able to follow all required steps to retrieve a file using our documentation, with a clear understanding of how to calculate the costs involved (gas fees, etc.).

#### Impact
🔥🔥🔥  
The Filecoin network currently appears to be used primarily by miners, with more supply than demand for storage space, and many docs are focused (explicitly or not) on miner needs with respect to hardware equipment, etc. Developers are unable to quickly and confidently store a file on Filecoin while experimenting with the product, which may lead them to settle for an IPFS pinning service or resort to 3rd party storage solutions. After their first bad experience, they're unlikely to return and try Filecoin again in the future, which makes the situation urgent: we need to either make Filecoin a more reliable and easy-to-use storage solution for devs or intentionally pause advertising it as one until it meets expectations.

#### Leverage
🎯 🎯 
External: Nailing the onboarding path to Filecoin storage and retrieval is core to promotion of the W3DT stack. If we define the stack in a way that requires including Filecoin, we are unable to educate folks on how to combine pieces of the stack until the onboarding processes for Filecoin storage and retrieval are unblocked. 

Internal:  By necessity, this project will require us to set up a workflow for x-functional communication/coordination between PM, engineering, and documentation/education teams, which can be leveraged for future W3DT work.


#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

**NEED HELP HERE**

Formal interal user testing, as well as questions commonly asked internally and on public forums provide evidence that many users have trouble completing a storage deal and retrieving their data by following our documentation as currently written. 

Nailing the onboarding process for Filecoin won't guarantee successful adoption, but not nailing it will guarantee failure. 

## Project definition
#### Brief plan of attack

Step 1: _DONE!_ Have sample users attempt to store a file on Filecoin by walking through existing available documention, with no help from fellow Labbers. (Note that although we could use lots more user testing in the future, we will start prioritizing our backlog for storage deals based on the results of these user interviews rather than waiting for additional user research to get started on known issues.)

Step 2: Using Andrew's video and [JV's slides](https://docs.google.com/presentation/d/1UbO7LKo47KTZcPL8xK41ubFEZwJ7MeFnnAT0_y1yIII/edit?usp=sharing) as a starting point, PM creates a system for tracking, prioritizing, and assigning the critical tasks on this path. Tracking system will cover _both_ documentation and engineering needs, with help from JV's slide 42 where he outlines which problems can be solved by documentation and which require engineering (and presumably subsequent changes to documentation).

Step 3: Docs writers fix the documentation pain points by adding more details, ensuring recommendations are tailored to storage clients (not miners), etc. (This person will need regular contact with protocol engineers to get answers to questions on current best practices.) 

Ongoing: 
- While updating documentation to accurately describe current best practices for deals, flag additional improvements that could be made to UX by the engineering team. 
- As engineers tackle related issues noted in proposal #16 (core protocol implementation for dealmaking and user experience needs in in the CLI (progress indicators, etc.), the two teams will communicate to ensure docs are updated when underlying engineering affects best practices / user actions and thereby creates documentation needs.
- As major documentation improvements and/or engineering improvements are made by the two teams, new testers will try the process from scratch to re-assess pain points. 


#### What does done look like?
_What specific deliverables should completed to consider this project done?_

The subset of frustrations flagged by Andrew & JV _that can be solved by documentation alone_ are solved. Documentation reflects current best practices for making a storage deal and retreiving data in the way that is easiest and most straghtforward give current technical limitations. Workarounds are presented for any engineering issues that haven't yet been addressed.

####  What does success look like?

If we succeed, a developer new to Filecoin will find all the information they need to make a storage deal and retrieve their data within docs.filecoin.io. They will not have to reference external resources unless clearly linked from the docs (e.g. how to set up a Droplet with Digital Ocean), and they won't have to ask questions of Labbers or seek help in Slack or other forums. They won't receive any CLI messages that make them feel they're left hanging; instead they'll see progress indicators (step 3 of 5) or an indication of how long to expect something to take (syncing the chain, etc.) to make them feel confident they're on the right path, even when the path takes longer than they'd like. (Such delays will also be explained in docs, but I believe it's insufficient to only share in docs and not in the CLI.) 

Metrics to track:
- time to do X 
- a user new to Filecoin can confirm a storage deal for a file of X size within Y time
- a user new to Filecoin can retrieve a file of X size within Y time
- monitoring forums/Stack Overflow/etc for: 
    -  people referring to the new tutorials
    -  people expressing fewer frustrations with the process this project aims to improve
- **NEED HELP HERE**

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

Currently, acheiving the most frictionless path to creating a storage deal on Filecoin requires having a protocol engineer on hand to point you in the right direction. If we did not assign protocol engineers to advise the documentation team on current best practices, we could fail to document the best approach. 

Poor communication between the engineering team making storage deal improvements and the documentation team educating on best storage deal practices could lead us to document incorrect or less-than-ideal solutions, or could lead us to fail to flag additional issues beyond those notod in original user tests.

Dropping efforts to engineer better solutions and UX, and relying only on documentation of current state, would cap the benefits of our efforts. (For example, tackling this proposal without also tackling #16.)

Scope creep is a risk here, as documentation is an ongoing process (every time we make a user-facing engineering improvement, new documenation is required). When we review Andrew & JV's notes to create a backlog, we'll need to clearly delineate the minimum requirements that meet our documentation needs for the storage deal process. 

We could use folks with too much pre-existing knowledge as our testers, leading us to miss documentation steps that are important to outline for newer users but feel obvious to more advanced users.

We could make it super easy to store a file on Filecoin without making it clear how to retrieve said file. 

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

The Lotus CLI could be made more intutive and verbose so that it provides enough guidance on its own that users don't need to reference documentation. That would likely be harder than the task proposed here, where the user would need to keep the documentation site open while using the CLI. (I personally believe improving the UX of the CLI is incredibly important and needs to happen alongside our documentation improvements.)

We could build a user-friendly GUI web app to use when creating deals for storage and retrieval, rather than the Lotus CLI. That might be a nice solution for a casual end user, but I presume it would be more time-consuming than documentation updates and would not adequately support developers looking to incorporate file storage with other processes.

Creating an easier onboarding path through a new usernet with funny money, a smaller chain, etc. could remove friction for first-time users deciding whether to pursue Filecoin. However, they could invest lots of time into building an app based on the positive experience they have there and then feel we've bait-and-switched them when unable to perform the same actions on mainnet. 

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->
Documentation of any feature that doesn't yet exist is blocked by implementation of that same feature. However, JV has laid out which challenges need attention from engineering and which from documentation, so there will be plenty for both sides to get started on immediately.  

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->

This project is intended to unblock further education efforts for storage clients and minimize churn. Once a developer is confident they can store and retrieve a file on Filecoin, we can educate on how to interop between Filecoin and existing IPFS nodes, how one might deal differently with other kinds of files or data, etc.

It will also help us establish a workflow for how we do cross-team work under our new org structure: we know we want to do these sorts of x-functional projects, but this is a good, relatively simple straw man for learning HOW to do them.

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

**NEED HELP HERE**

#### Roles / skills needed
<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->
- Documenation writer(s)
- Protocol engineer familiar with Filecoin deal making (part time for advising)
- PM to manage issue identification and ensure identified needs are tackled by both documentation and engineering teams 
- Guinea pig(s) willing to use a beginner mindset to test the process (these could be internal or external, so if anyone is working on a project to create regular user testing opportunities for external users, this could be a test run)
