# Miners can know what content they have 

Authors: @willscott

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

Currently miners complete a deal, and have a car file with a bunch of data. They do not generally know what is in that data though,
and therefore can't maximize the value of it. They will only be able to allow retreaval for clients who already know the content address of the
resulting car, and are able to specify the discovery portion of what item they want, and how to navigate in the car archive to get it (e.g. a selector)

#### Assumptions &amp; hypotheses

* miners want to get money by providing parts of the content they store
* users are willing to pay money to get data
* users would prefer to pay less money to get just the data they care about, than pulling that data out of a 32gig car file.

#### User workflow example

* a user queries a miner for a cid
* the miner indicates if they have that cid or not, and what piece it is in.
* the user makes a retreaval deal with the miner for the piece, and selector to the cid of interest.

#### Impact

high. a piece in the puzzle to allow retreaval / discovery of data stored in filecoin more easily

#### Leverage

high. unless we can easily discover what data is where, data retreaval will be slower and more expensive

#### Confidence

medium. we know improving the retreaval story is important. this seems to be an imporant piece in that puzzle

## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

#### What does done look like?

* queries can be made to miners to request a cid and recieve either 'don't have' or a piece the miner has with that cid.
* miners have a separate, light-weight program they can run that indexes deals upon completion, and provides this API.

####  What does success look like?

* miners run this light-weight program.
* number of deals for parts of full cars increases.


#### Alternatives

* Maybe this should happen as part of the deal process / we should move the 'piece' to be a dar with or to have a pre-computed index rather than make the miner do it

* maybe we should have some external retreaval mining entity that's motivated to make the index do it rather than the miner

#### Dependencies/prerequisites

none

#### Future opportunities

* with this building block, can figure out how to better respond to content discovery requests from miners

## Required resources

#### Effort estimate
Medium

#### Roles / skills needed
* knowledge of the deal process
* knowledge of cars
* golang programming
