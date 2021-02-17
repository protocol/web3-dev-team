# Proposal: Educate internally and externally on the intersection of Filecoin & IPFS

Authors: @terichadbourne

Initial PR: https://github.com/protocol/web3-dev-team/pull/17 <!-- Reference the PR first proposing this document. Oooh, self-reference! -->

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

As we become a W3DT team, we're looking for ways to encourage people--especially exisiting IPFS users--to adopt Filecoin as a piece of our larger stack. However, there's no information published about how to use Filecoin with IPFS, and very few materials describing Filecoin and IPFS in relation to each other to answer questions like: 
- If Filecoin incentivizes IPFS, does that mean I pay people to store my files on the existing IPFS network? 
- If I already have a file on IPFS and I want to pay someone to store it to Filecoin, can I just reference its CID, or do I have to somehow upload or send it to them? 
- How do I add a file from the IPFS network to Filecoin? (Can I reference a CID? Are the chunking requirements the same?)
- Why would I choose Filecoin over just using IPFS? 
- Do both projects use blockchain? 
- Are Filecoin and IPFS interoperable now? Will they be in the future? How? 

Some of these questions are hard to answer even for Labbers, especially those who haven't been working on the Filecoin team. 

There's currently internal resistance to publishing docs, blog posts, ProtoSchool tutorials, etc. about the intersection of Filecoin and IPFS. These efforts are sometimes postponed because someone knows the message isn't quite right but doesn't have time to weigh in to correct, sometimes postponed on the grounds that "no one is asking for that information right now," and sometimes postponed because it's too soon to cover the topic we'd like to (eg. we haven't figured out the path for a certain aspect of interoperability that we'd like to build a tutorial about). We have blog drafts and tutorial proposals stacking up which we don't feel empowered to work on.

By establishing the W3DT team, we've prioritized focusing on the interoperability and adoption of our full stack and -- I hope-- committed to addressing questions about the intersections of its components head on. In a company without a strong marketing or sales culture, education and press are our primary routes to attracting and onboarding users. While we may need to wait on teaching about features or flows that don't yet exist, it's time to commit to clarifying--both internally and externally--everything we can about how IPFS and Filecoin differ, how they're alike, and how they can work together to accomplish users' goals. I'd argue that the nature of the intersection of IPFS and Filecoin is the biggest unanswered question in our stack as a whole right now, and avoiding or postponing the effort to answer it is a tremendous blocker to much other onboarding work for W3DT. 


#### Assumptions &amp; hypotheses
- It's important for the public to use the right product names when referring to IPFS and Filecoin
- There's a high level of brand confusion between IPFS and Filecoin, especially in China, where companies based on Filecoin are named IPFS Something-or-other.
- We want developers to choose the protocol that best meets their needs, and they need to understand the differences between protocols in order to do that. 
- We want a subset of existing IPFS users to start using Filecoin in coordination with IPFS (or perhaps instead of using IPFS directly?). These users won't spontaneously start using Filecoin without education about benefits it provides that their current usage of IPFS doesn't.
- Existing IPFS users for whom Filecoin makes sense will want to access add/retrieve files from Filecoin using IPFS CIDs, without re-"uploading" their files.
- Some of our IPFS users - including high-name collabs - came to IPFS as a result of actually wanting to use Filecoin but it not being ready yet. It might be worth explicitly addressing these folks: to let them know what of their initial assumptions about Filecoin turned out to be true, what changed, what's possible now, what's not possible yet, etc.
- If we surveyed Labbers about the differences/dependencies/nteroperablity between IPFS & Filecoin, both in their current state and future intended state, we'd get a wide range of conflicting answers.
- We're unable to explain concepts to users before understanding them ourselves.
- There are things that are true about Filecoin that don't make sense to include in marketing or education materials.


#### User workflow example

**An existing IPFS user** has heard of Filecoin in passing but hasn't looked into it. While she's exploring the IPFS Course on ProtoSchool, she finds a course about how to store and retrieve files on Filecoin using IPFS CIDs. The following week, she receives an edition of the IPFS Newsletter pointing to a new HackerNews article about how Filecoin enhances IPFS. Getting curious about whether she could add a new feature to her dapp thanks to Filecoin, she explores trusted resources to find the answer: IPFS docs, Google ("What's the difference between IPFS and Filecoin" or "How to use Filecoin with IPFS"), the Filecoin website and its doc site. Each of these searches leads her to information in different formats, with different target audiences, that lets her understand how Filecoin is different from IPFS, whether it makes sense for her use case, and what trade-offs there might be in adopting it. When she decides she'd like to try it, she finds a tutorial on how to use IPFS and Filecoin together, and walks through it with no hiccups, quickly able to create a storage deal for one of her existing files using its existing IPFS CID.  

#### Impact
🔥🔥 

- Interop engineering and tutorials on how to use IPFS & Filecoin together will allow us to target new use cases and convince more IPFS users to try Filecoin.
- Improved education and reference materials on the intersection and IPFS and Filecoin will reduce negative vibes in community forums where we don't have enough bandwidth to address these questions and misconceptions one-off.

#### Leverage
🎯🎯 
- Externally: Clarifying the relationship between IPFS and Filecoin will unblock our path to transforming IPFS users into Filecoin users. 
- Internally: With a better educated staff, we'll have less chance of bottlenecking based on the critical knowledge of a few. By investing time into creating reference docs, we can reduce the amount of future time we spend answering one-off questions.

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

**NEED HELP HERE**

The interviews that our PMs are doing with trusted IPFS users show that they (and their users) are unable to find the data they need about IPFS & Filecoin distinctions and interop. We know some have chosen IPFS + pinning over Filecoin in part because of this documentation gap. 

## Project definition
#### Brief plan of attack

**Step 1: Educate internally**

Share questions internally, giving people a place to anonymously ask questions that they or their users have. What are the common misconceptions about Filecoin and IPFS? What interoperability is planned but not yet realized (eg retrieval using IPFS CIDs?)?

Share knowledge internally. Have the folks who actually know the answers plan an All Hands preso. Have the people who specialize in beginner-friendly content proof it and ask for clarification as it's developed. Use language that doesn't require an engineering background. Present at an All Hands.  Follow up with a ProtoSchool quiz? 

The questions asked by our team and answers provided (minus PL-private info) could provide a starting point to incubate a public-facing FAQ without having to do a bunch of initial surveying and testing: we can then use the testing to iterate on the questions raised internally *as well as* add new ones from the public.

**Step 2: Prioritize engineering issues to unblock interop** 

Look at the questions people have about interop. Which can we not answer because we're still deciding how things will work? Prioritize the engineering issues that will unlock turning IPFS users into Filecoin users. Get engineers working on the tasks that are blocking our user onboarding path for using Filecoin alongside our other products.

Ensure engineers know how/where they'll communicate when their projects are complete. What docs will need to be updated? What communications will be unblocked by their success? 

**Step 3: Make a comms/education plan**

Gather folks from a few specialties (PM, engineering, docs, ProtoSchool, PR, etc.) to discuss messaging that's acceptable now and messaging we're excited to use once X features are unblocked by engineering. If there are people whose input is required, be sure to get their input here rather than after we've spent time writing in the wrong direction. 

Think through the variety of user profiles we need to reach and where we'll reach them, identifying content approaches right for each audience (different tone, vocab, and specifics for press for the general public vs a developer, etc.): 
- Websites, ProtoSchool & docs
- Press, newsletters, blogs
- YouTube

Spread out the timeline for publishing, but don't be afraid to hit multiple mediums at once. 

Save the pieces that have engineering as a pre-req for later, but scope them now and identify the triggers that will indicate we're ready to proceed. 


#### What does done look like?
_What specific deliverables should completed to consider this project done?_

We can make this project as big or medium as we need to, but I would recommend going all out to meet people where they are and maximize SEO. Some options: 

Essential deliverables:
- Revised Filcoin docs page on IPFS & Filecoin intersection
- New IPFS docs page on IPFS & Filecoin intersection
- Ability to store/retrieve a file on Filecoin using its existing IPFS CID (incl API docs)
- A tutorial describing how to store/retrieve on Filecoin using IPFS CIDs (docs and ProtoSchool)

Publications in as many of these as we have bandwidth to tackle:
- IPFS blog post
- Filecoin blog post
- IPFS newsletter 
- Filecoin newsletter
- IPFS website copy
- Filecoin website copy
- Press coverage for a business audience

####  What does success look like?

Existing IPFS users will be able to store and retrieve on the Filecoin network by referencing existing IPFS CIDs, and easy-to-locate and easy-to-follow tutorials will walk them through the preocess.

Existing IPFS users will see Filecoin surfaced prominently as an option for them to consider. No matter which established resource they turn to first -- our websites, blogs, docs sites, etc. -- users and prospective users will easily find their way to information that helps them determine whether IPFS, Filecoin, or the combo is right for them. 

Every Labber will be able to confidently explain the difference between Filecoin (the storage network, not the token) and IPFS in terms that match their own technical level. Some will be able to tell stories about two different use cases, some will use words like hot and cold storage, some will use fancy crypto words that the rest of us don't understand. 

Labbers responsible for W3DT education will feel empowered to talk about Filecoin and IPFS without facing internal blockers to progress. 

Labbers on the Ecosystem team can reach out to high-value collabs who have chosen IPFS over Filecoin or used IPFS + pinning as a workaround and update them on our new capabilities, letting them know which of their initial assumptions about Filecoin turned out to be true, what's changed, what's possible now, what's not possible yet, etc.

High-value currently-IPFS-only collabs will confidently add Filecoin to their projects, creating a source for case studies for stack-wide projects.

Metrics to track:
- views on pages/tutorials/posts discussing Filecoin / IPFS connections or interop
- monitoring forums/Stack Overflow/etc for: 
    -  people referencing newly created guides / posts / tutorials
    -  people asking fewer questions or expressing fewer frustrations regarding whether/how IPFS & Filecoin can interop 
    -  reduction in confusion of IPFS and Filecoin project names or descriptions (eg which project uses blockchain)
- NEED HELP HERE, esp with engineering side

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

Experiences to date have shown a "perfect is the enemy of a good" problem, where we can't agree on messaging, so we put the project off. If that continues, we'll be unable to tell the story of how Filecoin fits into the stack (apart from the fact that the stack is included inside it).  

If we were to start this project with the wrong team in place, and miss critical conversations with key decision-makers or knowledgeable engineers early in the process, we could go a long way down the documentation road before flagging that we're on the wrong path, creating tension and extending the length of the project. 


#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_



#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->
Documentation of any feature/interop method that doesn't yet exist is blocked by implementation of that same feature/method. However, there's plenty of content to unlock and present immediately, so we can take the work in chunks, tackling more conceptual and well-cemented pieces now and creating tutorials on IPFS & Filecoin interop when we're able.  

This project will require input from the parties most interested in messaging to unblock the written work before we get started, rather than raising flags on individual projects only as we go along.

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->

Education on the intersection of IPFS and Filecoin is likely to increase our user base, or help them grow into using multiple products. The engineering work here creates the biggest future opportunities, because it will unlock the potential of users to build dapps using our full stack, which we can then showcase in tutorials, case studies, etc.

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
L b/c of engineering work but modular? **NEED HELP HERE**

I don't have a clear understanding of the engineering needs to acheive useful interop (to unblock tutorials on that subject), but there's lots of conceptual content we could get started on right away. 


#### Roles / skills needed
<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->
- PM 
- Interop engineers
- Documenation writers - incl ProtoSchool
- Decision-makers who need to weigh in on messaging 
- Authors for press, blogs, newsletters
- Social media managers to promote (minimal time commitment)
