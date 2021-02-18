# Simple IPLD encryption

Authors: @rvagg

Initial PR: https://github.com/protocol/web3-dev-team/pull/49

## Purpose &amp; impact 

#### Background &amp; intent

_Describe the desired state of the world after this project? Why does that matter?_

IPLD is not encrypted. IPFS is not encrypted. Filecoin is not encrypted. It's BYO with a bit of YOLO.

DAG-COSE and [DAG-JOSE](https://github.com/ipld/specs/blob/master/block-layer/codecs/dag-jose.md) are two proposals that have arisen out of our ecosystem (3Box and Textile) that attempt to solve this problem. These build on the existing COSE and JOSE specifications and wrap them around our DAG-CBOR and DAG-JSON specifications to form new signed and/or encrypted blocks. Read more at https://www.memoryandthought.me/golang,/ipfs/2020/09/04/dag-jose-project.html

These are fine solutions, but are complicated and more heavy-weight than we probably need. @mikeal created a proposal for a new format that does simple encryption of blocks, excluding much of the complexity, deferring that to users. Users needing additional complexity could create additional wrapping or enveloped data using our existing flexible codecs (most likely DAG-CBOR).

https://github.com/ipld/specs/pull/349 is the base proposal for a new binary format, requiring a new IPLD multicodec and some cipher multicodecs as well. https://github.com/multiformats/js-multiformats/pull/59 is a proposed JavaScript implementation.

This work could be completed and published in both Go and JavaScript and shipped to our ecosystem as a recommended solution for producing encrypted IPLD data—allowing wrapping of all our standard data types, including RAW and DAG-PB (for UnixFS) and any other supported IPLD format.

A small amount of additional clarification and refinement is likely required (see discussion in ipld/specs PR). The JavaScript implementation should probably be a separate library. A Go implementation will need to be produced for go-ipld-prime. And documentation will be needed to help guide users on using these codecs to encrypt their data.

An additional step _could_ be to include this new codec as default in Lotus (and make it standard for other Filecoin nodes?) so it can be used for retrieval.

#### Assumptions &amp; hypotheses

_What must be true for this project to matter?_

 * Users want to encrypt their data for sharing and long-term storage
 * Current solutions are not so great - current solutions mostly involve losing most benefits of using coherent IPLD graphs as they push encryption too far up the stack

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

<!--Briefly describe the milestones/steps/work needed for this project-->

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

Small

#### Roles / skills needed

<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->

 * IPLD developer(s)
 * JS & Go developer(s)
 * Documentation
