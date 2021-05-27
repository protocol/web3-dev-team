# Filecoin Plus Registry App UX/UI overhaul

Authors: @dkkapur @atopal

Initial PR: TBD <!-- Reference the PR first proposing this document. Oooh, self-reference! -->

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
The Filecoin Plus Registry (plus.fil.org/) site was developed with Keyko to ensure there was a way to manage applications for Notaries and clients in Fil+. This eventually grew to include additional flows like helping clients find miners who would store their deals. As a result, while the site has basic functionality, it is extremely difficult to use and does not serve as a strong entry point (either functionally or in terms of mitigating "scam fear") for clients looking to get DataCap and make deals on the Network. Additionally, it does not present UX flows that encourage and enable notaries and root key holders in the Fil+ ecosystem to conduct their work effeciently. This then increases the friction and time it takes for a client to receive DataCap and be enabled to make cheap/free deals on the network.

A list of recommendations for basic fixes has been compiled in UX Improvements for Fil+ App. The Keyko team is currently making its way through this. Though this addresses some of the basic pain points, it still does not address the following:
- Information presentation on the website is not intuitive for new Clients
- The website does not give the impression (does not inspire confidence) that it is a central hub for a critical piece of the Filecoin Network's productivity
- Several aspects of the website's design and architecture do not lend well to scaling its use up in the future (i.e., additional flows added to Fil+, leveraging the Fil+ model and website in other programs)


#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->
- the workflows/happy paths identified for this app continue to be applicable for stakeholders in the Fil+ ecosystem
- Fil+ is a key lever in enabling and enhancing the usefulness of the Filecoin network

#### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->

4 core types of users have been identified for this app: 
- clients: make DataCap allocation requests to notaries and find miners to make deals with
- notaries: view and approve DataCap allocation requests from clients
- root key holders: view and approve on-chain requests based on Fil+ governance
- miners: ensure that they are fairly represented to clients looking to onboard valuable data

See [Filecoin Plus Pathways](https://hackmd.io/1h0_cPVyQCSpHlWdPHtKtA?view) for specifics on the workflows and happy paths for each of these user types.

#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_
<!--
Explain how this addresses known challenges or opportunities.
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

#### Internal leverage
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
_What specific deliverables should completed to consider this project done?_

####  What does success look like?
_Success means impact. How will we know we did the right thing?_

<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->

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
