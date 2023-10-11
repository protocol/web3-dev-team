# NFT school

Authors: @atopal

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
* The NFT space is exploding, people are defining a bunch of practices in the wild, and we want to make sure they encode best practices for addressing and persistence to ensure NFT data is protected
* We intend this to be a one stop shop for any developer interested in the NFT space. That includes learning about concepts, and  hands on tutorials guides. A cross between a docs site and a marketing site


#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
* Most people who’ll be active in the NFT space haven’t joined it yet, so there will be a lot of people who need to be convinced that they should care about how NFTs are addressed and stored
* Most people in this space are not aware of best practices when it comes to addressing, storing, metadata, minting etc.

#### User workflow example
_How would a developer or user use this new capability?_
* Googling "nft metadata" and similar keywords bring devs to this website
* developers use resources to learn about metadata
* developers use resources to build their own applications

#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_
NFT content addressing is a perfect use case for IPFS, establishing it as the default will make it easier to transition to persistence with Filecoin, effectively utilizing the PL stack.

<!--
Explain how this addresses known challenges or opportunities.
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

#### Internal leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_
This has the potential to massively increase the community using and experimenting with our stack.

<!--
Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.
Confidence: 7
<!--Explain why this rating-->
While the content part of this is fairly straightforward, getting people to the site is not. It will take a significant amount of work in generating enough backlinks for this site to rank in search results, at which point it can become self-sustaining.

## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->
* Agree on mvp content
* Get started on content
* In parallel design and set up website
* Launch with mvp
* Keep adding content regularly


#### What does done look like?
_What specific deliverables should completed to consider this project done?_
The initial milestone is to have a set of documents online that cover the basics, backed up by partners. We’d then need to agree on follow up milestones. As a product this would be an ongoing concern.


####  What does success look like?
_Success means impact. How will we know we did the right thing?_


<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->
* Lagging indicator:
  * Ultimately, success is developers choosing to use IPFS for content addressing and Filecoin for storage for all of their NFTs
* Leading indicator:
  * Developers linking to this from stack overflow
* Significant traffic


#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_
For this to work developers need to actually land on the site either through googling or via backlinks.
Developers need to believe that this is an unbiased source of actual best practices
Maintaining an active site like this requires a long term commitment. If we can’t sustain regular new content, it can appear abandoned quickly.



#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_
* We could add the content to protoschool. That way we could focus on the content primarily.
* We could publish the content in a series of blog posts
* We could include the content into the current IPFS and Filecoin docs

The downside of all of those alternatives is their close connection to PL, making it potentially harder to come across as unbiased, but also the dilution of focus.


#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->
* Content
* Design
* Some of the standards might not exist yet (metadata schema)


#### Future opportunities
<!--What future projects/opportunities could this project enable?-->
There is an opportunity to turn this into a community co-owned space in the medium to long term. NFT hackathons in particular create a lot of opportunity for new tutorials that we can showcase on this site.
As we create new tools in this space, this site can be leveraged to generate interest and traffic.


## Required resources

#### Effort estimate
medium
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
* PM
* technical writer
* web dev
* design
