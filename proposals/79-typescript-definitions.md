# TypeScript Definitions for core libraries

Authors: @rvagg

Initial PR: https://github.com/protocol/web3-dev-team/pull/79

## Purpose &amp; impact 

Consumers of our JavaScript libraries & components should have sufficient TypeScript definitions, available through standard means, to write fully typed TypeScript code, or use that code to drive tooling that consumes these definitions - such as VS Code editing enhancements, documentation production pipelines, type checking tooling for test & CI pipelines.

This work is high-value and high-impact for the JavaScript ecosystem and those of us working on open source JavaScript libraries can all provide anecdotal evidence for the frequency with which developers request better TypeScript annotations for our libraries. The rate of TypeScript adoption, particularly within larger-scale projects, is increasing, but TypeScript definitions are increasingly useful as they are included in general JavaScript linting, checking and documentation tooling.

This work provides high-leverage within our suite of JavaScript tools as we mature, refactor, modularize and create. We are already establishing a suite of practices and tooling that are used in varying ways across PL JavaScript projects that use definitions, even though we have very few TypeScript projects throughout our GitHub orgs (<https://github.com/ipfs/js-dag-service> being a rare example, which was initially contributed by Textile). It is reasonable to expect that the majority of new JavaScript code produced by Protocol Labs into the future will make use of TypeScript annotations in some way.

Work on this effort has been largely completed, thanks primarily to @hugomrdias, @Gozala, and @achingbrain with assistance from the entire JavaScript team in various ways. The bulk of the activity has been tracked as a roll-up in to js-ipfs @ <https://github.com/ipfs/js-ipfs/issues/2945>.

Remaining work to integrate the current set of js-ipfs dependencies into js-ipfs and address the typing for code directly in js-ipfs is happening here: https://github.com/ipfs/js-ipfs/pull/3550

Aside from completing the remaining js-ipfs itegration work, the scope of this project includes some additional libraries that re not currently part of the js-ipfs dependency tree, including:

 * Next-generation IPLD codec libraries (using the js-multiformats pattern)
 * _TODO: what other non-archived, non-dormant project should we include here to achieve the above value & impact ideals?_

Project-specific decisions will be made regarding the depth of TypeScript definitional work. Projects with greater expected future usage should include full type checking in CI and will therefore require basic inline TypeScript annotations. Projects that are dependencies but are not expected to be actively maintained or developed further into the future may just include basic API type definitions so that dependents can make use of those.

<!--
#### Background &amp; intent
_Describe the desired state of the world after this project? Why does that matter?_
#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
#### User workflow example
_How would a developer or user use this new capability?_
#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_
#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_
#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.
## Project definition
#### Brief plan of attack
#### What does done look like?
_What specific deliverables should completed to consider this project done?_
####  What does success look like?
_Success means impact. How will we know we did the right thing?_
#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_
#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_
#### Dependencies/prerequisites
#### Future opportunities
## Required resources
#### Effort estimate
#### Roles / skills needed
-->
