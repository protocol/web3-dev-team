# Store-my-text Filecoin example app

Authors: @zenground0 @rvagg

Initial PR: https://github.com/protocol/web3-dev-team/pull/46

## Purpose &amp; impact 

#### Background &amp; intent

_Describe the desired state of the world after this project? Why does that matter?_

We have an extremely simple example application, _and_ a functioning service that has real-world utility that exercises Filecoin and deal-making.

 * A **very** simple web application, minimal UI fluff and distraction: **Save my text to Filecoin**
   - Text field to enter some UTF-8 text
   - Field to submit your email address
   - A button to "Submit"
 * User enters some non-empty text and their email address and presses "Submit"
 * Application performs a simple confirmation-of-email ("click this link") to confirm a real user and manage trivial DoS
 * Application handles storage of text on Filecoin and sends confirmation email
   - Application mediates the storage deal-making process for small content - finding miners, batching content, etc.
 * CID provides persistent "proof-of-text" to the user

Initially this is just a very simple system that demonstrates (and exercises, and educates us on) the full deal flow for simple content.

There's plenty of extensions that could be made to this, turning it into a genuinely useful application, such as:

 * IPFS integration
 * Other input types (images, etc. getting toward the NFT use-case)
 * Payments ("Deposit X FIL to this address...", "Enter your CC to purchase X FIL")
 * ETH integration to turn content into an NFT (ERC721, ERC1155, whatever is needed, maybe integration with an existing NFT service?)

#### Assumptions &amp; hypotheses

_What must be true for this project to matter?_

 * when attempting to do deal, frequently it is difficult to get it completed
 * Building applications that perform simple & small storage deals to Filecoin is currently difficult
 * Web3 developers want solid but grokkable example applications they can copy (fork-and-go!)

#### User workflow example

_How would a developer or user use this new capability?_

 * Play with application live (we host and manage and pay for storage of small amounts of text, with limits per email address)
 * Fork open source application
 * Make new web3 app with Filecoin storage
 * Profit

#### Impact

_How would this directly contribute to web3 dev stack product-market fit?_

 * Exercise deal-making for small resources
 * Provide a very simple example for web3 app developers to build on

#### Leverage

_How much would nailing this project improve our knowledge and ability to execute future projects?_

#### Confidence

_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.


## Project definition

#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

#### What does done look like?

_What specific deliverables should completed to consider this project done?_

####  What does success look like?

_Success means impact. How will we know we did the right thing?_

<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

#### Counterpoints &amp; pre-mortem

_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

#### Alternatives

_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

#### Dependencies/prerequisites

<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

#### Future opportunities

<!--What future projects/opportunities could this project enable?-->

## Required resources

#### Effort estimate

Medium

#### Roles / skills needed

 * Backend webapp developers (probably Node.js)
 * Filecoin deal-making expertise
 * Documentation
