# Dealbot Controller for Slingshot Retrieval

Authors: @mgoelzer

Initial PR: [#96](https://github.com/protocol/web3-dev-team/pull/96)

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

Like [#87](https://github.com/protocol/web3-dev-team/pull/87), this proposal is for a Dealbot controller.  Controllers drive the execution of Dealbots for specific purposes.

In order to judge the Slingshot competition, a large number of retrievals need to be made to check the data stored in the competition.  Without this controller, this checking will be substantially more time-consuming and manual.


#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->

 - The [Dealbots project](https://github.com/protocol/web3-dev-team/pull/84) must resulting in working dealbots that can be run in parallel with tasks dispatched by a single controller.
 - `{miner,CID}` tuples of Slingshot data must be available.
 - A low-latency, high-speed link to a go-ipfs node must be available from the bots in the mainnet dealbot cluster.

#### User workflow example
_How would a developer or user use this new capability?_

Input:

 - A list of `{miner,CID}` tuples to be retrieved

Output:

 - Each successful retrieval must be written to the go-ipfs node mentioned above for later download and review locally.  (Note:  Filecoin retrieval to go-ipfs node storage already exists and does not need to be built for this project.)
 - An output metadata file listing all retrievals attempted their outcome.  An outcome would be a timestamped record of either:
   - a success status for the retrieval and the IPFS hash where the retrieved data can be found
   - a failure status for the retrieval (along with the exact error message of the failure)
  
  Here is an example of what the metadata file might look like:
  
```
[
  // example of a successful retrieval
  {
     "request":{"datetime":"YYYY-MM-DD hh:mm:ss","minerId:"f0XXXX","CID":"bafxxxxxxxxxxxxxxxxxxxxxxxxxxx"}, // <-- the input dealbot team was given
     "retrievalResult":"success",
     "ipfsHash":"Qmxxxxxxxxxxxxxxxxxxxxxxxxxxx", // <-- where the retrieved data lives on Riba's ipfs node
  },
  
  // example of a failed retrieval
  {
     "request":{"datetime":"YYYY-MM-DD hh:mm:ss","minerId:"f0YYYY","CID":"bafyyyyyyyyyyyyyyyyyyyyyyyyyyy"},
     "retrievalResult":"failure",
     "errorMessage":"deal failed: (State=26) error calling node: publishing deal: mpool push: failed to push message: not enough funds (required: 0.19999999998338535 FIL, balance: 0.037461935577982576 FIL): not enough funds to execute transaction",
  },
  
  ...more retrieval attempt objects...
]
```

#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

<!--
Explain how this addresses known challenges or opportunities.
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

This work enables the Slingshot competition, which increases usage of our stack by onboarding more useful content onto the Filecoin network.

#### Internal leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

<!--
Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

 - There is the potential for cross-learning between this project and other controllers (like [#87](https://github.com/protocol/web3-dev-team/pull/87))
 - There is the potential to find mainnet bugs in the Dealbot through this project, since it implements a unique type of controller that retrieves data not stored by the Dealbot itself.

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

<!--Explain why this rating-->

Confidence:  High

This controller utilizes only a subset of the dealbot functionality (only retrieval deals), so if we can get [#87](https://github.com/protocol/web3-dev-team/pull/87) to work, this project should be no more difficult to make work as well.


## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

 - The go-ipfs node (to be set up by @ribasushi outside this project proposal) should contain the retrieved bits of all successful retrieval
 - The metadata file (described with example above) should be generated.

####  What does success look like?
_Success means impact. How will we know we did the right thing?_

<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

 - All deliverables listed above are delivered.
 - The people responsible for judging Slingshot are satisfied that they got what they needed for judging the competition.

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

 - Unknown requirements (e.g., all retrievals need to be attempted in a certain geography) that we discover cannot be accomodated before the judging deadline

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

 - The retrieval work could be done entirely manually (e.g., by hiring a human contractor specifically for this purpose).
 - Bash scripts could be written that don't depend on the Dealbots project.

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

 - The [Dealbots project](https://github.com/protocol/web3-dev-team/pull/84)

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->

 - Judging for future rounds of Slingshot
 - Validation for large-scale Filecoin storage projects currently underway (e.g., Starling/Shoah)

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
