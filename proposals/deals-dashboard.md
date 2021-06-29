# Deals Dashboard

Authors: @mgoelzer

Initial PR: #85 <!-- Reference the PR first proposing this document. Oooh, self-reference! -->

<!--
For ease of discussion in PRs, consider breaking lines after every sentence or long phrase.
-->

## Purpose &amp; impact 
#### Background &amp; intent
_Describe the desired state of the world after this project? Why does that matter?_

To better understand real world deal making performance on the Filecoin mainnet, we need a set of [Observable](https://observablehq.com/) (or similar) dashboards that stakeholders can review to see real time updated data on various facets of deals. Broadly, these dashboards need to cover three areas:

 - **Key KPIs.**  These include key decisionmaker metrics like overall storage and retrieval deal success rates (DSRs), speed of retrievals, rate of deal acceptance by miners.
 - **Deal Testing.**  [Elsewhere](https://github.com/protocol/web3-dev-team/pull/84) we have proposed to develop a dealbot that randomly selects miners on the network and makes storage and retrieval deals with them. Therefore, a dashboard is needed to visualize the data produced by these bots. 

 This would take the form of a filterable list of all deals attempted and their outcome.  Filters would include characteristics like storage or retrieval deal, verified or unverified deal, fast retrieval flag set or not set, date range, and so on.
 - **Other Dashboards.**  A few miscellaneous dashboards that would help us understand the network, such as view of storage and retrieval DSRs over time, histogram of deal failures by stage, and average time spent in each stage of the deal process.

#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_

* The [Dealbots project](https://github.com/protocol/web3-dev-team/pull/84) needs to be completed and producing a feed of data in order to power these dashboards.
* Stakeholder alignment on what dashboard views are useful.

#### User workflow example
_How would a developer or user use this new capability?_

* A stakeholder would browser to an Observable URL and view a real-time updated set of dashboard visualizations.

#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

Key to PMF is proper functioning of the Filecoin network under all "normal" usage conditions. These dashboards would answer the question of about whether the network is performing as expected.

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

The impact of these dashboards would be significant.

Right now, the Filecoin Project is "flying blind" in terms of:

- knowing where bugs may exist in the network
- whether miners (and clienta) are well incentivized to use the network to its full potential
- unexpected deviations from normal operation on mainnet (e.g., today we have no quick way of detecting a sudden spike in deal failures that might indicate a regression in recent network upgrade)
- what kinds of problems users may be encountering that we are not hearing about through other channels

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

Confidence = 10

Management decision making based on automated dashboards is a very common practice in software companies.  I have seen this technique surface information to decision makers effectively in multiple contexts.

Dashboards also enable decision makers to self-serve, discovering important information on their own without having to convene a meeting or wait for a report from others in their organization.


## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

A set of Observable dashboards covering the items listed below.

 - **Key KPIs.**
 
   - **P1** Storage deal success rate (DSR) across all golden path deals
   - **P1** Retrieval DSR across all golden path deals
   - **P2** Time to acquire DataCap (target: <1m)
   - **P2** Time to return QueryAsk (target: <1s)
   - **P2** % of dialable miners
   - **P2** % of proposed storage deals that are accepted
   - **P2** % of proposed retrieval deals that are accepted
   - **P1** % of initiated storage data transfers that are successful
   - **P1** % of initiated retrieval data transfers that are successful
   - **P1** % of accepted storage deals that are ultimately active on-chain
   - **P1** Time to first byte on retrievals
   - **P1** Time to last byte on retrievals for each different deal size
   
 - **Deal Testing.**

   - A list of all bot deals with filters for:
     - **P1** Storage or retrieval deal
     - **P1** Using DataCap or not
     - **P1** Using fast retrieval flag or not
     - **P2** Deal size (various sizes from 4 GiB to 32 GiB)
     - **P2** Version numbers for lotus, graphsync, go-fil-markets, go-data-transfer
     - **P1** Deal stage where failure occurred
     - **P1** specific error codes
     - **P2** Datetime range
   - A top-level metrics dashboard showing all bot deal stages with
     - **P2** Avg time in stage
     - **P2** Success rate in advancing out of that stage
   - Two top level dashboards showing:
     - **P1** Overall bot storage deal DSR
     - **P1** Overall bot retrieval deal DSR
   - **P1** Top level dashboard with a table that contains each attempted bot deal and all info that we have about that deal
 
 - **Other Dashboards.**
   - **P1** View of storage DSR over time
   - **P1** View of retrieval DSR over time
   - **P1** Histogram of failures by deal stage
   - **P2** Time in each stage (i.e. how long each stage takes), and lines that show how the time in each stage has changed over time

####  What does success look like?
_Success means impact. How will we know we did the right thing?_

Success means:

 - Having a set of Observable dashboards that cover all of the performance indicators described in the previous section
 - Stakeholders are actually using these metrics to understand the network and make decisions

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

 - We could be focused on the wrong dashboard metrics
 - There could be dashboard metrics that are important but have not yet occurred to us
 - Stakeholders could decline to make use of the dashboards, either because they are not answering urgent questions or are too complicated to understand or other mismatch with stakeholder needs
 - The data stops being updated due to lack of maintenance bandwidth

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

 - Its very hard to get the benefits of dashboards without building some type of dashboard
 - However, other tools (besides Observable) could be used for visualization
 - Non-automated methods of achieving the goals of these dashboards are possible:  regularly interviewing users, drawing inferences from other known metrics like number of active users, increase/decrease in high value users, etc.

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

 - The dashboards will be powered by data from the [Dealbots project](https://github.com/protocol/web3-dev-team/pull/84)

#### Future opportunities

 - Add additional metrics that we realize would be of use
 - Remove metrics that prove not to be useful and/or complicate the UX of the dashboards

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

(Engineering should make this estimate based on requirements described above.)

#### Roles / skills needed
<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->

 - PM for requirements and requirements changes
 - Experience with Observable (i.e., rudimentary Javascript coding)
