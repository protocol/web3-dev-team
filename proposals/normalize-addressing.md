# Normalize ipfs://${CIDv1}

Authors:
- @gozala

Initial PR: https://github.com/protocol/web3-dev-team/pull/93 <!-- Reference the PR first proposing this document. Oooh, self-reference! -->

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

Raising popularity of NFTs triggered debates how NFTs stored on IPFS should be addressed. On one hand links like `ipfs://${cid}/` are more future proof and decentralized, but on the other hand chances are high that such links in the wild will not be clickable and can harm adoption.

Things are complicated further by a fact that same content can be addresed in several ways even on the same gateway. E.g. here is all the various ways [QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR](https://explore.ipld.io/#/explore/QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR) could be encountered by the users


1. `ipfs://QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR`

   > Which should be invalid and really should be following instead
   >
   > `ipfs://bafybeigdyrzt5sfp7udm7hu76uh7y26nf3efuylqabf3oclgtqy55fbzdi`

2. https://bafybeigdyrzt5sfp7udm7hu76uh7y26nf3efuylqabf3oclgtqy55fbzdi.ipfs.dweb.link/

3. https://dweb.link/ipfs/QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR

4. https://dweb.link/ipfs/bafybeigdyrzt5sfp7udm7hu76uh7y26nf3efuylqabf3oclgtqy55fbzdi

5. https://dweb.link/ipfs/?uri=ipfs://QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR


All but `ipfs://` URL will get normalized into 2nd from, that is good but it also different enough from native `ipfs://` URL to make it confusing / inconvenient to work with.

This proposal suggests to address those pain points through following:

1. Making `ipfs://${CIDv1}` canonical representation.
   > 
   > We can drive adoption by adopting these representation across our libraries [like propsed here](https://github.com/multiformats/js-multiformats/issues/71)
   > 

2. Ensure that users see `ipfs://${CIDv1}` regardless of gateway they're on.
   > Above examples from 2nd to 5th could redirect to:
   > `ipfs://${originHash(CID)}.dweb.link/ipfs://${CIDv1}/`
   >
3. Adopt `https://gateway.tld/ipfs://{CIDv1}/path/to/thing` URLs.
    - They would redirect to derived subdomain to ensure content isolation.
4. Prompt users to register `ipfs://` protocol handler from `ipfs.io`
    - We have worked with partners to make [registering `ipfs://` protocol handler possible](https://blog.ipfs.io/weekly-104/). Lets drive adoption of `ipfs://` URLs by utilizing this.
    - We can also partner with teams that embed NFTs so they can help drive registration.

5. Surface something like https://ipfs.github.io/public-gateway-checker/ on https://ipfs.io/ and possibly other gateways so users can choose which gateway to use when navigating to `ipfs://` native URLs.



#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->

- We fail to communicate and/or encourage idiomatic way to address content on IPFS.
- Different ways to address, redirects that change URLs etc.. is confusing and it is easy to overlook tradeoffs across different formatting options.
- Surfacing `https://${gateway}/ipfs://${CIDv1}` across all the addressing schemes will trigger natural human pattern recognition and make things less confusing.
- Driving adoption of native `ipfs://` URLs will reinforce it as a norm that apps need to adopt.

#### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->

#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

<!--
Explain how this addresses known challenges or opportunities.
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

- Prominance of native `ipfs://${CIDv1}` style URLs will puts apps not supporting this addressing scheme at disadvantage, creating incentive to adopt it.
- Adoption of `ipfs://${CIDv1}` style URLs can unlock further decentralization.

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

<!--
Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

- If we succeed in making `ipfs://${CIDv1}` usable to avarage web user we will unlock more opportunities to drive adoption our our technology.

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

<!--Explain why this rating-->

Don't know


## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

- IPFS gateway implementation uses `/ipfs://{CIDv1}` in paths.
- ipfs.io lets users register native `ipfs://` handler from various reputable gatways.

####  What does success look like?
_Success means impact. How will we know we did the right thing?_

<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

- Navigating to any IPFS content on the web includes `ipfs://${CIDv1}` somewhere in the URL.
- Increase in native `ipfs://${CIDv1}` style URLs in the wild.
- Increased understanding that `gateway` in `http://${gateway}/ipfs://${CIDv1}` is a user choice.



#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

- IPFS aspired to replace URL addressing with path addressing which this proposal is at odds with.
- Despite our efforts for avarage web user `ipfs://` style links are not clickable so it does not pick up.
- Adding yet another notation does not solve the problem, but magnifies it.
- Changing the default paths complicate setup on reverse proxies.
- Having `://` twice in URL will make IPFS links look even more suspicious (less technical users) or simply wacky (technical) hurting us more than helping.

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

- Different addressing scheme that is very clear across various gateways.
- All major browsers support `ipfs://` out of the box.

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->

- We can work with borwser vendors to provide better default handling `ipfs://` protocol out of the box. E.g. surface various options on first encounter so that users can choose from.
- Attempt to pursue popular product teams e.g. Slack, Notion, Signal etc... to drive adoption of native `ipfs://` URLs.

## Required resources

We can do estimation excercise if we this proposal gain momentum.

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
