# End to End Tests for Deal Flow in Lotus

Authors: [@alanshaw](https://github.com/alanshaw)

Initial PR: https://github.com/protocol/web3-dev-team/pull/28

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
<!--
_Describe the desired state of the world after this project? Why does that matter?_

Outline the status quo, including any relevant context on the problem you’re seeing that this project should solve. Wherever possible, include pains or problems that you’ve seen users experience to help motivate why solving this problem works towards top-line objectives. 
-->

People who use the Lotus CLI for making storage deals face significant hurdles that make the experience painful, time consuming and unsuccessful. The experience report by Andrew Nesbitt is the case in point. In this report Andrew recorded himself attempting to store data on Filecoin. It took a very long time and he was ultimately unsuccessful.

After this project is completed, a set of end to end (E2E) tests will exist that can be run in CI to verify users are able to use the Lotus CLI to store data in Filecoin by successfully negotiating deals with storage providers. The tests will verify that users continue to be able to do so in the future.

We'll also gather data on "close to real life" usage that can help determine success of projects wishing to improve the flow.

#### Assumptions &amp; hypotheses
<!-- _What must be true for this project to matter?_ -->

* There's no existing (and working/usable) test suite for running E2E tests for deal flow.
* The CLI will remain as an interface to negotiating storage deals.
* It is possible to launch a test network of lotus nodes.

#### User workflow example
<!--
_How would a developer or user use this new capability?_
(short paragraph)
-->

_To be confirmed_. In general it should be runable from CI, and users should be able to initiate ad-hoc runs with particular branches to test changes.

Some ideas:

* Run on every PR to Lotus to identify regressions.
* Run nightly as a separate project to collect and graph data such as:
    * Average "time to deal".
    * Minimum number of commands to store data.

#### Impact
<!--
_How would this directly contribute to web3 dev stack product-market fit?_

Explain how this addresses known challenges or opportunities.
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

The tests are likely to expose bugs and bottlenecks in the flow. Resolving these issues will improve the user experience.

They will give us a better understanding of the flow and it's shortcomings. This should help to inform future projects looking to streamline the process.

The tests will gather data on the flow that can be used to help future projects determine their success.

#### Leverage
<!--
_How much would nailing this project improve our knowledge and ability to execute future projects?_

Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

Having adequete E2E tests for deal flow will catch any regressions introduced that are not tested by unit/functional tests. This saves time fixing bugs discovered in production, shields users from experiencing issues, and maintains the view of professionalism of the Lotus team.

#### Confidence
<!--
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

Explain why this rating
-->

```
ICE Score = (Impact + Confidence + Ease) / 3
ICE Score = (7 + 7 + 8) / 3
ICE Score = 7.333
```

**Impact 7** because the project touches on the following areas:

* User Aquuisition - Doesn't Abandon.
* Activation - Makes a deal first time.
* Retention - Reducing bad experiences that force the user to try something else.
* Revenue - Generates revenue.

**Confidence 7** because these will generate test results and benchmarking data.

**Ease 8** an estimate that this will take 3 weeks to get up and running. The time is reltively short because there's no changes to Lotus that need to be made, it can be created as a separate greenfield project.

## Project definition
#### Brief plan of attack
<!--Briefly describe the milestones/steps/work needed for this project-->

1. Identify test scenarios.
    * See the "Lotus Release Checklist" for some desired E2E tests to include.
1. Identify tests that will generate benchmarking data.
1. Decide on runner (BYO or testground?).
1. Build a runner/learn a testground.
1. Write the tests.
    a. Observe the pain points.
    b. Experience the bugs and open issues.
    c. Note the bottlenecks and open issues.
    d. Ensure tests with obvious bottlenecks generate benchmarking data.
1. Integrate the suite (CI in Lotus/run nightly etc.).
1. Collect/graph the metrics.
1. Create new project(s) to streamline the flow.

#### What does done look like?
<!--
_What specific deliverables should completed to consider this project done?_
-->

1. E2E test suite exists.
1. E2E tests are run frequently.
1. Metrics are graphed for other projects to use.

####  What does success look like?
<!--
_Success means impact. How will we know we did the right thing?_

Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

1. One or more bugs are found in the deal flow and fixed in Lotus.
1. The E2E tests catch a bug that would not have been otherwise caught until found in production.
1. Another w3dt project uses metrics from these E2E tests to define it's success.
1. Andrew Nesbitt is able to successfully negotiate a storage deal.
1. Over time, performance for the collected metrics improves.

#### Counterpoints &amp; pre-mortem
<!--
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_
-->

If the deal flow changes before the project is complete then there will be additional work to do to update the tests either at the end or mid development.

If the tests are "flakey" then their results will not be trusted and they may become abandoned.

#### Alternatives
<!--
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_
-->

We could hire a team of human testers to perform this job.

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

1. We need to be able to spin up a test network of Lotus nodes.
1. Hopefully testground is good for this job.

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->

1. Creates a yard stick by which any project aiming to improve the deal flow can measure itself by.
1. More test scenarios can be added when needed.
1. This should hopefully create a template that can be used to E2E test other areas of Lotus.

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

Medium.

#### Roles / skills needed
<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->

Someone to introduce testground and help with questions.
