# Reliable Mutability Primitive

Authors: [@gozala](https://github.com/gozala)

Initial PR: https://github.com/protocol/web3-dev-team/pull/19/
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


Today ecosystem has to work around the lack of functional mutability primitives. [IPNS][] does not provide reliable solution forcing community to adopt different custom solutions.

- [Pinata][] gets asked about how to change content for CID once every few weeks _(Most of the time they find that is not what the users actually need)_.
- [fission.codes](https://fission.codes/) found IPNS persistance unreliable and had to build custom solution that updates [DNSLink][] records (**TODO**: Get a quote / link from Boris)
- **TODO**: Survey textile, last time we talked they found IPNS to be unreliable for propagating thread updates.
- ...
- Protocol Labs uses dns simple API to [publish site updates](https://github.com/filecoin-project/specs/blob/71f37208a1f4f56b33ea307d7cbdb4b06996b115/.github/workflows/main.yml#L40). 


This gap in the stack makes building software which runs on end user computers and meets modern expectations more difficult than traditional hosted solutions. This creates a hurdle for adoption of the technology.



##### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->

- Applications want to provide a canonical address for a current state.
- Application authors will prefer built-in mutability primitive over custom solutions. 
- Developed solution would provide simpler mechanism for publishing updates (than DNSLink updates)
- Developed solution would provide a reliable mechanism for producing updates on not always connected end user computers (think browsers, phones)
- Solution should not require shipping secret keys or tokens with devices.

##### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->

Team builds an application enabling user to write and share notes with each other. They chose to use IPFS as that enabled them to focus on the applications writing exprience free from having to write and maintain backend infrastructure or ensuring data safety. Application stores encrypted notes in the embedded IPFS node and publishes CID to the latest shared notes DAG root via IPNS API. This enables collaborating users to fetch updated notes via embedde IPFS. Application also leverage [Pinning Services API][], enabling their users to choose from growing number of service providers or to bring their own endpoint for better availability.

Choosing IPFS not only reduced an engineering effort, but also made their product fully off-grid capable (thanks to IPNS update propagation over mDNS) with no additional effort on their end. Team often likes to points out that their product has an edge over the competition, not only all user e2e encrypted, but their users can also choose where that data is persisted.

##### Impact
_How directly important is the outcome to our top-level mission?_


🔥🔥🔥 This would enable building competitive software that does not introduce custom server components (Standard [Pinning Services API][] provides data persistance and standard mutability primitive provides updating mechanism).

It would also give an edge to the whole ecosystem, because [there is no step three](https://www.youtube.com/watch?v=YHzM4avGrKI) (as in no servers to run or maintain).


<!--
Explain why you have chosen this rating
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

##### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_


<!-- Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

🎯🎯 - This would enable projects that need to have a canonical identifier for evolving dataset. It would also provide a greater interop across products built around IPFS by removing need for custom incompatibile solutions that teams need to implemente today.


##### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

<!--Explain why this rating-->

3 - As high confidence as we can have without doing actual user studies. We know teams that have tried IPNS but found it unrelaible, ultimately rolling out an alternative solution. We also know teams that have evaluated IPFS but chose alternative due to lack of reliable mutability story.



### Project definition
##### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

- Implement third party IPNS republishing (see [ipfs/go-ipfs#4435](https://github.com/ipfs/go-ipfs/issues/4435))
- Collaborate with Pinning Services to make this part of the API.
- Fix IPNS publishing in browsers.
- Enable pubsub by default + IPNS over pubsub.
- Implement & deploy strategic republishing system on PL hosted nodes that will republish popular content and drop stalled one. So that IPNS works even thought pinning services.
- (Nice to have) Implement and rollout delegated publishing to enable updating from multiple devices.
- (Nice to have) Implement and rollout versioning system so that nodes can see full update history.

##### What does done look like?
_What specific deliverables should completed to consider this project done?_

- Publishing IPNS record takes just a few miliseconds. 
- Shutting laptop and loading `https://ipfs.io/ipns/{key}` week later on other device loads the content published as fast as loading corresponding `https://ipfs.io/ipfs/{cid}`.
- It is possible to pin IPNS address to keep it around and ensure it resolves even when original publisher is gone (AKA solving IPNS rot).
  - Node follows IPNS record updates and keeps re-publishing latest one if original author disappears.
  - Node follows content updates behind the IPNS record, and update content pin every time IPNS record changes. 
  - It is possible to opt-out from this behavior to re-publish IPNS record for `en.wikipedia-on-ipfs.org` without pinning all the data.


#####  What does success look like?
_Success means impact. How will we know we did the right thing?_

<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->
- People and teams are storing IPNS keys in [DNSLink][] records as opposed to CIDs, because that provides a more effective and simpler way to publish updates.
- We see people storing IPNS addresses in ENS to save on blockchain transactions costs.
- We see new projects leveraging IPNS (when human readable name is not a concern) instead of working around it with [DNSLink][].
- We see more requests for  `/ipns/{libp2p-key}` paths on our public gateway (dweb.link &  ipfs.io).


##### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

- IPNS has bad reputation, changing it may prove to be a challenge.
- Teams may find that general primitive is not adequate for custom needs.
- Required key management (e.g. key recovery, key compromise) still may prove it impractical.
- Higher level alternatives like textile threads may prove to be better layer of abstraction.

##### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

- Integrating textile threads as core component of the ecosystem.
- Standardizing DNS record updates mechanism and intergating into IPFS.
- Work with Pinning Services to implement stardized DNSLink updating mechanism.

##### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

- Functioning IPNS in browsers
- Enabling pubsub in go-ipfs

##### Future opportunities
<!--What future projects/opportunities could this project enable?-->

- [Petname][] system for memorable but non canonical names (kind of how our phones allow us to not remember numbers).
- IPNS-based autoupdate mechanisms for our own stack (eg. go-ipfs, ipfs-desktop etc)
- Subscribtion based deny lists (node can subscribe to any endpoint)
- RSS like systems (In RSS readers memorable namse were not a concern)
- DAGs revisions carrying IPNS key so that last latest revision or any past revision could be discovered.

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

Large. Requires lot of coordinated changes across implementations and collabs. Uncertainty in the scope until concrete actionable plan is in place. Uncertenty in collab buy-in. 

##### Roles / skills needed
<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->

- go-ipfs development
- js-ipfs development
- cross org coordinator (to get pinning services onboard)

[Pinata]:https://pinata.cloud/
[DNSLink]:https://docs.ipfs.io/concepts/dnslink/
[IPNS]:https://docs.ipfs.io/concepts/ipns/
[Pinning Services API]:https://ipfs.github.io/pinning-services-api-spec/
[Petname]:https://en.wikipedia.org/wiki/Petname
