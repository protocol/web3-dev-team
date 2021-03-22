# TypeScript Definitions for core libraries

Authors: @rvagg

Initial PR: https://github.com/protocol/web3-dev-team/pull/79

## Purpose &amp; impact 

Consumers of our JavaScript libraries & components should have sufficient TypeScript definitions, available through standard means, to write fully typed TypeScript code, or use that code to drive tooling that consumes these definitions - such as VS Code editing enhancements, documentation production pipelines, type checking tooling for test & CI pipelines.

This work is high-value and high-impact for the JavaScript ecosystem and those of us working on open source JavaScript libraries can all provide anecdotal evidence for the frequency with which developers request better TypeScript annotations for our libraries. The rate of TypeScript adoption, particularly within larger-scale projects, is increasing, but TypeScript definitions are increasingly useful as they are included in general JavaScript linting, checking and documentation tooling.

This work provides high-leverage within our suite of JavaScript tools as we mature, refactor, modularize and create. We are already establishing a suite of practices and tooling that are used in varying ways across PL JavaScript projects that use definitions, even though we have very few TypeScript projects throughout our GitHub orgs (<https://github.com/ipfs/js-dag-service> being a rare example, which was initially contributed by Textile). It is reasonable to expect that the majority of new JavaScript code produced by Protocol Labs into the future will make use of TypeScript annotations in some way.

Work on this effort has been largely completed, thanks primarily to @hugomrdias, @Gozala, and @achingbrain with assistance from the entire JavaScript team in various ways. The bulk of the activity has been tracked as a roll-up in to js-ipfs @ <https://github.com/ipfs/js-ipfs/issues/2945>.

Remaining work to integrate the current set of js-ipfs dependencies into js-ipfs and address the typing for code directly in js-ipfs is happening here: https://github.com/ipfs/js-ipfs/pull/3550

Aside from completing the remaining js-ipfs integration work, the scope of this project includes some additional libraries that are not currently part of the js-ipfs dependency tree, including:

 * Next-generation IPLD codec libraries (using the js-multiformats pattern)
 * [js-multiformats legacy interface](https://github.com/multiformats/js-multiformats/issues/67) needs updating to match the newly exported js-ipfs/js-ipld types.
 * [js-multiaddr](https://github.com/multiformats/js-multiaddr/pull/159) is mostly done, but needs to be a non-breaking change to land
 * js-libp2p core types had a first iteration, but there are a few gaps that should be addressed, specially in the configuration, [as follow up](https://github.com/libp2p/js-libp2p/issues/830).
   * _Scope:_ the priority for js-libp2p is in the generally exported API, so direct users of js-libp2p have types for that interface.
   * _Out of scope for this project:_ there is also a general libp2p typescript [tracking](https://github.com/libp2p/js-libp2p/issues/659) with all the libp2p modules, but these do not appaer to be high priority at the moment, as most users typically only interact with the core API.

During execution of this project, where questions of scope arise that are not covered above, library-specific decisions will be made regarding the depth of TypeScript definitional work using the following criteria:
  * Projects with greater expected future usage should include full type checking in CI and will therefore require basic inline TypeScript annotations.
  * Projects that are dependencies but are not expected to be actively maintained or developed further into the future may just include basic API type definitions so that dependents can make use of those.
  * Any work estimated to be consisting of more than 2 days for 1 FTE will be either scoped as a separate project (or bundled into another, existing project, collecting future work), or be brought back to [the PR for this proposal](https://github.com/protocol/web3-dev-team/pull/79) for further discussion of expansion of scope.

#### Background &amp; intent
_Describe the desired state of the world after this project? Why does that matter?_
#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
#### User workflow example
_How would a developer or user use this new capability?_
#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

Roughly half of the projects that depend on our core JavaScript stack are using TypeScript in some way according to metrics we have. This is expected to expand over time given the adoption rate of TypeScript and TypeScript annotations.

Anecdotally, developers find type annotations useful in the development process even if they don't use TypeScript. It also allows for additional checking in the test/CI process for dependents of our libraries.

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

We have some existing TypeScript in the PL suite of JavaScript. This may expand as we have some developers who have a preference for working with strongly typed, or minimally type checked code. Annotations on our core libraries allows us to add tighter type checking to our CI process for any existing and new libraries that consume that code.

We already have [one example](https://github.com/ipfs/js-dag-service) of code being contributed to the PL stack from a third-party that uses TypeScript and could be improved by typing in the rest of our stack.

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

## Project definition

#### Brief plan of attack

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

See Scope description above.

####  What does success look like?
_Success means impact. How will we know we did the right thing?_

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

Historically it has been very difficult to estimate and scope the TypeScript work in the PL stack. This work has been underway for approximately 1 year and there exists a risk of scope-creep and a strong risk of estimation-error. It will be important to track scope and be able to cut losses when sufficient value has been achieved _or_ alternative, higher-value, opportunities for our developer-time investment are identified.

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

#### Dependencies/prerequisites

#### Future opportunities

* Deeper typing in our stack, such as in the dependencies of js-libp2p which are not in scope of this project.
* More sophisticated test/CI integration across our stack to test against the typing data.

## Required resources

#### Effort estimate

S _(with some risk of M depending on discoveries along the way, see notes regarding Scope above)_

#### Roles / skills needed

* JavaScript
* TypeScript
* js-ipfs/ipld/libp2p and related stack expertise
