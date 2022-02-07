# [outcome or objective here] 

Authors: @aschmahmann @stebalien

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

Currently IPFS users with very large amounts of content (e.g. pinning services, internet archive, etc.) have no way to make that content discoverable to other IPFS peers without those peers having some out of band knowledge that they should connect directly to the users with the large amounts of data. This means that some of the users who can contribute a lot to the network are left in difficult spots of either working with application code or trying to find other ways to connect to make themselves discoverable by users.

Some users with a medium amount of data (e.g. 10M objects) are having issues making their content available due to the way go-ipfs does providing which could be alleviated by some of the solutions proposed [here](https://github.com/protocol/web3-dev-team/pull/31). However, other users with particularly large amounts of data (e.g. the internet archive has over 500B websites) would have to spend a large amount of money if they needed to frequently send all of these records out to the network (even sending 500B records once is around 50TB which is pretty costly). After completing this project it should be possible for users with a large amount of data to make their data available to users without excessive costs.

<!--
Outline the status quo, including any relevant context on the problem you’re seeing that this project should solve. Wherever possible, include pains or problems that you’ve seen users experience to help motivate why solving this problem works towards top-line objectives. 
-->

#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->
- There are users who currently have too much data to provide in the IPFS DHT
- Users who cannot provide all their data in the IPFS DHT have difficulty making their data available to the people who want to download that data
- Having a non-optimal short term solution to this problem is better than waiting for a longer term solution

#### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->

User with many objects (hub - name TBD): They add a config option in go-ipfs indicating that they want to be a hub.

All users: By default they automatically send queries to the hub pubsub channel in addition to the DHT, but it can be disabled.

#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

It supports groups with large amount of data that want to make their data available via the stack. This is particularly useful since users who don't want to run their own infrastructure will get some larger bodies (e.g. centralized pinning services, Filecoin miners, etc.) to store a copy of their data for them.

<!--
Explain how this addresses known challenges or opportunities.
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

<!--
Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

Solving this problem should increase the number of projects and collaborations in our ecosystem as well as provide information on how people are using content routing that could be useful in future designs.

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

<!--Explain why this rating-->
3 . Among users with a large amount of data figuring out how to make that data findable is a top request.

## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

The idea is that hubs will each subscribe to a pubsub channel (e.g. `/ipfs/content-routing/1.0.0`) and when users are looking for who has content they'll publish to that pubsub channel a request for the CID they are looking for. When a hub receives an inbound request for a CID they will check if they have it and if so they'll connect back to the user who will then end up fetching the data via Bitswap.

- Enable pubsub by default in go-ipfs
  - Note that since this use case is compelling enough for most users to have a pubsub channel that any overhead from running pubsub is likely worthwhile
  - i.e. not much need to wait on some of the analysis from https://github.com/protocol/web3-dev-team/pull/53, even though it'd be nice
- Create a pubsub topic that has some of the Gossipsub 1.1 resiliency parameters enabled
- Create a simple message type for broadcasting CID requests
- Create an additional implementation of the router interface in go-ipfs that sends these messages on the pubsub channel
- Create a handler for hubs to run on receipt of pubsub messages and do a dialback to the peer if they have the CID in their blockstore
- Add config options to go-ipfs to enable/disable these features
- Add option to disable automatic providing that occurs within Bitswap

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

- Content that is available on a hub node with providing turned off, and nowhere else, is findable via go-ipfs
- Testground tests demonstrating the system should behave as expected
- At least 10 large nodes that are currently unable to provide all their content are running hubs

####  What does success look like?
_Success means impact. How will we know we did the right thing?_

- There are many members on the hub network
- Users with lots of content have a much easier time making their data discoverable
   - User surveys
   - Lower incidence, or qualitative less critical, submitted GitHub issues around content discovery

<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

- The ecosystem impact of the users with lots of content (e.g. 100M+ objects to advertise) might not be significant
- Users with lots of content might not want to become hub nodes
  - e.g. the proposed protocol could eat up resources in ways the hub nodes are not prepared for (e.g. inbound/outbound bandwidth in the pubsub channel from every IPFS client)


#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?

- Asking users to just configuring permanent peering with the largest nodes
- Create a secondary more centralized content routing service (that people can modify/add to in their configs) and have users (both large and small) send their records to these content routing services.
  - This would help users with large amounts of data since they could just their records to the largest content routing services once (and even just ship HDDs of records if the bandwidth was way too high)
- Fleshing out + designing an alternative approach to content routing for peers with lots of data

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->

- New/improved content routing systems
  - Metrics collectable from this system will inform future decisions around improving content routing
- Pluggable content routing
  - We've had pluggable content routing for a while, but with only one implementation it's hard for people to see the alternatives, with a second implementation this becomes clearer and easier for us to build new systems

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

Small. Most of the risk and complexity here is in creating, running and analyzing the testground tests to verify correct behavior and scale properties.

#### Roles / skills needed
<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->

- Go engineer (testground experience ideal)
- Go engineer (go-ipfs experience ideal)