# POC Projects with Tutorials

Authors: zebateira

Initial PR: #6

## Purpose &amp; impact 
#### Background &amp; intent

It's hard for developers to start using web3 tech and contextualizing IPFS, libp2p and Filecoin in their own needs can go a long way to make them feel at home.
Building a hello world cli chat app is a good fun exercise, but it's not the end game.

For more complex use cases, it might not be easy to understand if our stack can really pull it off. We need to put it to the test, show everyone how we did it and how they can do it too.

Developing POC Projects along with tutorials can provide just that: proof that our stack works and how devs can go ahead and use it for their specific use cases.
An example of this is [Share IPFS](https://share.ipfs.io).

Tutorials could build on top of each other by incrementally introducing new parts of our stack. As an example, the part one of a tutorial could start with communication using libp2 and part two of the tutorial could add IPFS integration to store files.

#### Assumptions &amp; hypotheses

- Mature enough tech that can be used to build POC apps
  - This probably means that libp2p and IPFS are more preferable targets to start with for now as opposed to Filecoin
- Tutorials in form of articles are a very good entry point for developers to read on new ways to build apps

#### User workflow example

Developers would most likely start with the tutorial/article that details how we can create X app using libp2p and/or IPFS.
The app should be deployed and publicly accessible for devs to play with: this is the proof that our stack works so it needs to be fairly bug-free and stable.

#### Impact

🔥🔥🔥

Developers would be able to gain clear confidence in our stack because they saw with their own eyes that it works. If we invest on making a fair share of POCs, we can always respond to questions of the form "Can we do this with IPFS?" with an url to the POC app.

More importantly, if the apps really succeed, they might even spin off into their own projects and succeed and solving the issue they tackle in such an amazing way that everyone wants to use it and contribute to improve it.

#### Leverage

🎯🎯🎯

POCs for specific use cases can bump into limitations or even bugs in the stack. This would contribute to our objective of improving the stack by providing this feedback to the stack development in order to prioritize issues to be solved.
We wouldn't publish apps that do not work, but we would be bumping up the importance of specific issues that arise from building such apps.

#### Confidence

**Impact=8**

**Confidence=7**

**Ease=6**

**ICE=7**

The end result would most likely very well received by developers. The major limitations would be driven by what our stack currently can achieve.

## Project definition
#### Brief plan of attack

Brainstorm some ideas for POCs. Build one, deploy and publish the tutorial and analyse impact.
Create guides and other helpers to incentivize POC building and publishing.
Automate anonymous data collection to analyze impact.

#### What does done look like?

1. First POC Project and Tutorial built and published to show the impact
1. Detailed guide for building more POC Projects and Tutorials
    - Would focus on making sure the projects are a good fit for this purpose and guide them on specific nuances of building these apps and tutorials.
1. UI kit guide or even a design system to reduce visual UI implementation to almost zero.
1. Process for people to submit ideas, build and publish.
1. Have a plan for releasing the POCs and tutorials on a frequent schedule.
1. Streamlined process for analyzing impact with specific metrics
    - Since we will own the apps, we can easily track the user journey from the tutorial to the app and request feedback from the user.


####  What does success look like?

POC apps get good traffic and response from the tutorials are mostly positive.


#### Counterpoints &amp; pre-mortem

Our stack could limit the capabilities of the POCs, so we need to be very careful to reduce the limitations the POC projects have. For example, until we have a solid foundation to store and retrieve content in Filecoin, we can't really pursue that as a feature to showcase in a POC.

#### Alternatives
Developers themselves can create the actual apps, but in those situations we do not have the control over them, so they might not pursue continuing to use our stack with the intent of improving it, but rather to simply solve their own problems, which could lead them away from our stack at the first issue they encounter, instead of staying around to help and contribute.

#### Dependencies/prerequisites

We need a stable stack for this to be feasible. Part of it is in a good enough state that we can pursue this, so we would continue expecting the rest of the stack to be mature enough to be a target of POC building.

#### Future opportunities

Projects might spin off on their own if they become an asset to the community.
This would be very beneficial for the stack because of input we would have in the project.

## Required resources

#### Effort estimate

6-8 weeks with one person with the appropriate skills.
4-6 weeks with two people with the appropriate skills.

#### Roles / skills needed

- Fulltime: Web App development (good candidate for external agencies).
- Only needed in some phases:
    - Design expertise to aid on some specific UI issues (good candidate for external agencies).
    - Docs (not strictly necessary since we can have docs folks doing the review only, but would be a plus).
