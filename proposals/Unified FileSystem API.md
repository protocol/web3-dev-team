# Unified FileSystem API

Authors:
- @gozala

Initial PR: TBD <!-- Reference the PR first proposing this document. Oooh, self-reference! -->

<!--
This template is intended to be used by those who would like to pitch a new project for one of the Web3 Dev project teams to take on. It should contain sufficient detail that others can understand how this project contributes to our team’s mission of  product-market fit for our unified stack of protocols, what is included in scope of the project, where to get started if a project team were to take this on, and any other information relevant for prioritizing this project against others.
Good project scope aims for ~3-5 engineers for 1-3 months (though feel free to suggest larger-scoped projects anyway). Projects do not include regular day-to-day maintenance and improvement work, e.g. on testing, tooling, validation, code clarity, refactors for future capability, etc.
-->

### Purpose &amp; impact 
##### Background &amp; intent
_Describe the desired state of the world after this project? Why does that matter?_
<!--
Outline the status quo, including any relevant context on the problem you’re seeing that this project should solve. Wherever possible, include pains or problems that you’ve seen users experience to help motivate why solving this problem works towards top-line objectives. 
-->

Today IPFS comes with two sets of FileSystem APIs, one offering global network level view (and is less file systemy) and second local node level (mutable) view. Not only thas is confusing and suboptimal, but neither provide an adequate solution for various use cases:

###### File Tree in DAGs

Sometimes you want to stick tree of files into a DAG. This is reasonable straight forward with `ipfs.add` API if tree structure can be represented as stream of file paths and contents. 

However there are cases where representing a file tree as a steam is impractical (e.g. it happens in response to on various events). Such cases are much better serverd with `ipfs.files` API, however it is also not ideal because tree built ends up in the node local FS path and concurrent tasks could introduce race condititions.

###### Multitenant Nodes

When multiple apllications share an IPFS node they end up with shared local filesystem view, which is impractical because they can introduce race condition and access each others secret files.


###### Content Froking

Neither of the existing file system APIs are adequate for forking file tree and performing edits on it. Global filesystem API does not really has write API, and with local filesystem API file tree needs to be assigns a path, which not only requires adding file tree and removing afterwards but is also prone to race conditions.

---

What we need instead is an API similar to `ipfs.files` that can be instantiated with an arbitrary `CID`. This would address all the above use cases.

**TODO**: Talk to collabs to figure out if we could further abstract this so that it's just as easy to plug encryption.


##### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->

##### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->

##### Impact
_How directly important is the outcome to our top-level mission?_

🔥🔥🔥 = 0-3 emoji rating

<!--
Explain why you have chosen this rating
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

##### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

🎯🎯🎯 = 0-3 emoji rating

<!-- Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

##### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

<!--Explain why this rating-->


### Project definition
##### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

##### What does done look like?
_What specific deliverables should completed to consider this project done?_

#####  What does success look like?
_Success means impact. How will we know we did the right thing?_

<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

##### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

##### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

##### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

##### Future opportunities
<!--What future projects/opportunities could this project enable?-->

### Required resources

##### Effort estimate
<!--T-shirt size rating of the size of the project. If the project might require external collaborators/teams, please note in the roles/skills section below). 
For a team of 3-5 people with the appropriate skills:
- Small, 1-2 weeks
- Medium, 3-5 weeks
- Large, 6-10 weeks
- XLarge, >10 weeks
Describe any choices and uncertainty in this scope estimate. (E.g. Uncertainty in the scope until design work is complete, low uncertainty in execution thereafter.)
-->

##### Roles / skills needed
<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->
