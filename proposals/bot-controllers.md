# Dealbot Controller for Deal Testing and Metrics

Authors: @mgoelzer

Initial PR: [#87](https://github.com/protocol/web3-dev-team/pull/87) <!-- Reference the PR first proposing this document. Oooh, self-reference! -->

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

Let's start with the state of the world *before* this project is completed.

Currently, we are about to start a project to build [storage and retrieval dealbots](https://github.com/protocol/web3-dev-team/pull/84). These bots will attempt storage and retrieval deals on the Filecoin mainnet based on input provided to them on stdin (or a command line supplied input file).  They will output their results to stdout, with that output then piped to a log aggregator for visualization (eg, Kibana, Observable, etc).

For most use cases of these bots, we don't just want to invoke them manually on the command line. Instead, we need a higher-level orchestration system that will carry out a series of storage and retrieval attempts to generate the data we want for that use case.

One such controller will be the one for deal success testing. This PR covers only that controller.  Future controllers (in future PRs) will include those for reputation systems, scraping data from other sources and storing it in Filecoin, etc.

The desired state of the world after building this deal success controller is:

 - We will have a long-running daemon program that repeatedly attempts storage and retrieval deals on mainnet
 - This collection of results from many storage and retrieval deals will get aggregated into the log aggregator that the bots output to.
 - These aggregate results will be visualized via the [deal success dashboards project](https://github.com/protocol/web3-dev-team/pull/85).


#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->

 - The storage and retrieval bots are built and able to output test results to a dashboard.
 - The bots are capable of accepting instructions on stdin or a unix socket or some other kind of command issuance interface.

#### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->

```
$ ./dsr-bot-controller --input my-tests.json start
```

The input file `my-tests.json` might look something like this:

```
[
	{
		"dealType":"storeThenRetrieve",
		"storeThenRetrieveParameters":
			{
				"retrievalDelayHours":"72",  // store the file, wait 72 hrs, then try to retrieve it
			},
		"miner":"f0xxxx",
		"dataToStore":"random",  // this could alternatively be a file path
		"randomDataParameters":
			{
				"sizeBytes":"1073741824",  // 1 GiB
			},
		"schedule":
			{
				"startDateTime":"yyyy-mm-dd_hh:mm:ss",
				"endDateTime":"yyyy-mm-dd_hh:mm:ss",
				"repeatIntervalDays":"7",  // means the test is re-run every 7 days
			},
	}
]
```

#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

<!--
Explain how this addresses known challenges or opportunities.
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

 - To achieve PMF, we need storage and retrieval deals to be highly reliable (success >= 99% on first attempt)
 - Regardless of the type of user, reliability is critical

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

<!--
Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

 - We need an controller like this to make the dealbots useful for deal success testing
 - The combination of dealbots and this controller will give us data on deal success rates
 - Knowledge of deal success rates will help us know where to focus our debugging efforts as we improve the Filecoin network

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

<!--Explain why this rating-->

Confidence = 8

The reasons why this impact might not be achieved are covered in the Pre-mortem section below.


## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

 - An orchetration program to drive the dealbots exists
 - The orchestration program follows the general usage design described in User Workflow Example above

####  What does success look like?
_Success means impact. How will we know we did the right thing?_

<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

 - We are getting a continuous feed of storage+retrieval tests in our dashboard visualization system
 - Stakeholders and decision makers are using these dashboards:
   - To make decisions about where to focus debugging efforts
   - To understand how reliable storage and retrieval deals are on the network

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

 - The controller, which is a long-running daemon program, crashes and no one is available to restart it and debug the cause of the crash
 - The controller tests artificial conditions that do not represent real world usage on the network
 - The controller is not robust enough to handle complex tests like multiple retrievals, storage of a wide range of file sizes -- AND testing these turns out to be important/relevant

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

 - We could build a more informal controller, like a simple bash script that we run on a cron schedule

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

 - [Storage and retrieval bots project](https://github.com/protocol/web3-dev-team/pull/84) is completed

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->

This project will serve as a prototype for how to write other controllers that utilize the dealbots in different ways, such as:

 - Reputation systems
 - New kinds of KPIs we want to track
 - Scraping data and persisting it on Filecoin

This project will also provide open source example code that community members can use as a starting point to build their own controllers.

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
