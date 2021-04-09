# Message Sending User Experience in Lotus

Authors: @Kubuxu

Initial PR: https://github.com/protocol/web3-dev-team/pull/15


## Purpose & impact 
#### Background & intent
<!--_Describe the desired state of the world after this project? Why does that matter?_-->
<!--
Outline the status quo, including any relevant context on the problem you’re seeing that this project should solve. Wherever possible, include pains or problems that you’ve seen users experience to help motivate why solving this problem works towards top-line objectives. 
-->

Wide range of users interacting with Filecoin network through Lotus stumble, again and again, across current experience of sending messages. There are multiple caveats to actively interacting with the chain.

Some of them are:
- sending messages with unsynced node
- sending messages with too low fees given current network conditions
- having too little funds to send given message
- head of the line blocking on previous messages

Many of the issues that users hit while trying to interact with the chain stem from the fact that Lotus CLI is lacking interactive feedback. The CLI does not warn the user when these situations happen, and if it does the only resolution available right now is failing (and expose flag like `--force` for advanced use-cases). This approach only increases user confusion as its not clear for them how to proceed.

The aim of the project is to make actively interacting with Filecoin network through Lotus a delightful experience by removing the multitude of sharp corners awaiting the user.


#### Assumptions & hypotheses
<!--_What must be true for this project to matter?_-->
<!--(bullet list)-->
- Lotus is used directly to interact with the chain. This will be the case until applications that fulfill roles of wallets, storage clients, retrieval clients are built. Even still application developers will likely use Lotus directly. 
- Sharp edges of Lotus in this area are causing users to abandon/reduce their involvement.
- 
#### User workflow example
<!--How would a developer or user use this new capability?\_-->
<!--(short paragraph)-->

_All of the below are reported issues with message sending UX._

- Sending message from (partially) unsynced node, resulting in wrongly estimated gas fees.
	- **Solution**: warn the user that node is not in sync, ask for confirmation to send the message
- Default `MaxFee` configuration option results in message fees being too low, resulting in message not landing on chain:
	- **Solution**: for interactive usage use the `MaxFee` as guideline. If message wouldn't immediately land on chain due to it (or would be at a risk of being squeezed out in short time), suggest to the user alternative fee. The alternative fee can be accepted, refused or modified. If low fee is specified, estimate the time message will need to land.
- Previous messages are blocking new messages due to changing network conditions or insufficient funds.
	- **Solution part 1**:  Warn users when new messages are submitted and ask for confirmation that user wants to proceed.
	- **Solution part 2**: Build an interactive tool for observing state of messages, allowing the user to reprice them, discard them and showing the user what is the exact issue with them (head of the line blocking, insufficient funds, too low fee)

#### Impact
<!--\_How directly important is the outcome to web3 dev stack product-market fit?\_-->

🔥🔥 
This project has potential to decrease attrition of new users that are starting to experiment with Filecoin, while at the same time improving the experience of existing users. 

<!--
Explain why you have chosen this rating
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

#### Leverage
\_How much would nailing this project improve our knowledge and ability to execute future projects?\_

🎯

This project develops features needed by other functionalities.


<!-- Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

#### Confidence
\_How sure are we that this impact would be realized? Label from \[this scale\](https://medium.com/@nimay/inside-pro1duct-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)\_.
<!--Explain why this rating-->


## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->
- Assemble a prioritized list of message sending issues users have encountered from Lotus issue tracker, user reports, Slack. 
- Fix issues that can be resolved with detect and warn/fail approach.
- Design and implement interactive message sending UI. 
- Design and implement interactive message watching UI - it should fulfill following roles for the user.
	- Clear indication of whether the message will land on chain in short time
	- Clear indication of past messages, number of confirmations, exit status.
	- Provide a way to resolve "struck" messages, interactive functionality of `mpool replace`.

#### What does done look like?
<!--\_What specific deliverables should completed to consider this project done?\_-->
Issues identified in the first step are resolved, users are protected against issues mentioned in this document.

####  What does success look like?
<!--\_Success means impact. How will we know we did the right thing?\_-->
Number of issues and complaints by users and end users regarding message related interactions with Filecoin is reduced. Message sending related problems are no longer mentioned when on-boarding new users.
<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

#### Counterpoints &amp; pre-mortem
<!--\_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?\_-->
- Lotus CLI is part of the interface for user interaction but also for scripting, agreeing both of these world can be problematic but can be done.
- Lotus CLI can stop being the primary way developers/users actively interact with Filecoin. It is almost sure in the long term but in short to medium term it is very much unlikely.

#### Alternatives
<!--\_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?\_-->
- Building a separate Wallet + Storage and Retrieval client interface. This will happen in medium-term but it will not stop Louts CLI from being used buy both new and old users.
- 

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->
None.

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->
- "Bring your own signature" workflow in Louts - it needs similar facilities
- Message Pricing Policies - allow users to specify fee settings per message type or user defined tag instead of one global setting.
- Split of Porcelain and Plumbing APIs in Lotus

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
Medium with some variance depending on semi-unknown complexity of modifying Lotus to allow user interactions for messages sent internally in the API  


#### Roles / skills needed
<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->
- 2 x engineers with knowledge of Lotus
- 0.25x PM
