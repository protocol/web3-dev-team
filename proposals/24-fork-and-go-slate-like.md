# Create fork-and-go Slate-like example project that exercises the stack

Authors: @rvagg

Initial PR: https://github.com/protocol/web3-dev-team/pull/24

## Purpose &amp; impact 

 * Internal team education and experience with our full stack and the pain points for web3 app developers
 * Create an example project that can be easily forked and evolved to create a web3 app that leverages our stack

#### Background &amp; intent

_Describe the desired state of the world after this project? Why does that matter?_

[Slate](https://slate.host/) / [filecoin-project/slate](https://github.com/filecoin-project/slate) provides an excellent example of a user-focused web3 application that uses our stack. It's evolving more as a _product_ in its own right and as the complexity increases, the example-utility for new developers using our stack decreases.

The project aims to build a slim Slate-like example project that exercises our stack in similar ways to Slate but excludes some of the complexity that is not required to demonstrate the key interactions with our stack.

The project will have to contend with various choices and compromises that web3 developers currently have to make to:
 * deliver compelling and responsive applications for users while attempting to build toward the ideal of fully decentralised services; and
 * interact with the more prickly parts of our stack as they currently exist (e.g. having to use third-party tools that make it easier, like Textile).

The project **must** be idiomatic to our target audience—developers creating applications for end-users, who are most likely using existing web2 patterns and skills to level up into the web3 world. Therefore, its choice of code dependencies, development and testing style should be as close as possible to typical for this audience and not include quirky tooling, style or architectural choices that distract from the learning experience.

The project should include documentation that:
 * walks developers through setting up and running the application,
 * clearly describes the architecture; and
 * clearly explains the integration with the web3 stack and how such integration can be achieved by developers for their own applications.

The project should ideally evolve over time as our stack improves. Such maintenance and improvements are not included in this proposal but should not be neglected if this project is successful.

Competing with Slate is _not_ a goal, the project should only be useful as a developer example.

#### Assumptions &amp; hypotheses

_What must be true for this project to matter?_

 * Slate is a good starting point for such an example, _or_ its architecture and exercising of our stack is worth copying, otherwise we'll need to generate alternative ideas.
 * Developers are wanting good e2e examples for building web3 apps using web2 app development techniques.

#### User workflow example

_How would a developer or user use this new capability?_

 1. Clone project, install code dependencies, sign up to required services or create tokens/wallets, etc., start any additional local services required (perhaps Dockerised for portability and ease of use), setup environment and start applicaiton.
 2. Run through simple user workflow to interact with the service, upload assets, observe back-end flow that illustrates interaction with our stack and/or third-party ecosystem tooling.
 3. Fork project and hack to make it perform desired functionality based on components, workflows or ideas in the example.
 4. Profit.

#### Impact

_How directly important is the outcome to web3 dev stack product-market fit?_

 * Provides a clear example of simple interactions with our stack, not too obscured by the complexity of real-world application needs
 * Provides a non-theoretical base for documentation on how to use our stack.
 * Exercises our stack to prove, or highlight pain-points we need to address.
 * Education for us, as leverage for the _next_ thing.

#### Leverage

_How much would nailing this project improve our knowledge and ability to execute future projects?_

Very high leverage - exercising our stack and educating the team on the areas of difficulty and where we need to look for further improvements.

#### Confidence

_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

Very low. This is not even based on hearing "I want this!" externally (but is based on that signal internally).

## Project definition

#### Brief plan of attack

 1. Learn as much as possible from the Slate team about their architectural choices as they relate to our stack and the important things they think need highlighting and seek their help on defining what a simplified Slate-like might _do_.
 2. Basic architecture design.
 3. Development - which may include borrowing liberally from Slate.
 4. Documentation and other educational materials - likely in parallel to development.
 5. Promotion.

#### What does done look like?

_What specific deliverables should completed to consider this project done?_

A project that can be easily cloned and started by an average web3 (or web2-graduating) developer, provides a useful example of working against our stack and includes enough documentary materials to provide a clear understanding of _what_ and _how_.

####  What does success look like?

_Success means impact. How will we know we did the right thing?_

Project feedback—pull requests and issues asking questions.

Social promotion by third-parties.

Seeing real-world applications with a clear lineagae to our code would be ultimate success.

#### Counterpoints &amp; pre-mortem

_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

 * We already have a bunch of example projects, particularly in the js-ipfs stack
 * Inability to access key parts of our stack _directly_ and having to use third-party services that suggest there is lower value in the key technologies ("why am I using Textile when I just want to use Filecoin?")
 * Not web3 enough, too close to classic web2 but with a some web3 ribbons (perception, or maybe reality?)

#### Alternatives

_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

 * Documenting Slate as it exists today, working with the Slate team to ensure it remains a good technical example for using our stack.

#### Dependencies/prerequisites

 * Cooperation with folks from Slate

#### Future opportunities

 * Deeper integration as our affordances become easier to use - ditch third party layers and use our stack directly?

## Required resources

#### Effort estimate

Medium

#### Roles / skills needed

 * Active Slate developers who can speak to their architectural choices and learnings in using our stack
 * Backend developer(s) (Node.js + required services)
 * Frontend developer(s) and some design input (so it doesn't _look_ terrible!)
 * Documentation and tutorial development
