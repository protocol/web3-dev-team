# Support Large IPLD/IPFS DAGs

Authors: Stebalien

Initial PR: TBD <!-- Reference the PR first proposing this document. Oooh, self-reference! -->

## Purpose &amp; impact 
#### Background &amp; intent
_Describe the desired state of the world after this project? Why does that matter?_

First, it should be possible to store arbitrary and arbitrarily large IPLD DAGs on Filecoin using
the built-in protocols. At the moment, Filecoin can only store "whole DAGs". If a DAG, doesn't fit
into a sector when serialized as a CAR, it must be converted to raw-blocks, chunked, and then stored
as those chunks.

Unfortunately:

1. This workaround erases the underlying DAG structure. This makes it difficult to transfer this
   data for both storage and retrieval. This is especially true when interacting with IPFS.
2. This workaround requires storing an "overlay" DAG in Filecoin (paying for that storage).

Second, it should be possible to retrieve subsets of DAGs. While the underlying protocols support
retrieving subsets of DAGs, the CLI does not. This makes it impossible to, e.g., retrieve a single
file from a directory without modifying Lotus.

#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_

There is no easy way (e.g., no out-of-band deals) to store large (> sector size) IPLD DAGs while
preserving the DAG structure.

#### User workflow example
_How would a developer or user use this new capability?_

* `lotus client deal` should accept an IPLD selector.
* `lotus client deal` should automatically split large DAGs between multiple sectors.
* `lotus client retrieve` should support retrieving IPLD selectors (dag subsets).

#### Impact
_How directly important is the outcome to web3 dev stack product-market fit?_

🔥

At the moment, any tool wishing to support storing IPFS files/directories larger than 32GiB will need to store these IPFS files/directories as "raw blocks", throwing away all the DAG structural information. This will make future retrieval deals for subsets of this data infeasible and will make IPFS interop extremely difficult.

This is only one 🔥 because there are plenty of useful sub-32GiB datasets and non-IPFS datasets.

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

🎯🎯🎯

If we don't solve this now, users will likely store large DAGs any way they can (e.g., as raw
blocks). We could end up with a lot of unfortunately structured data in Filecoin that's difficult to
retrieve and work with, especially from IPFS.

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

??

## Project definition
#### Brief plan of attack

1. Implement selector support in `lotus client deal`. 
2. Implement selector support in `lotus client retrieve`.
3. Support automatically splitting large dags into across deals in `lotus client retrieve`. 

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

All three of the above commands have been implemented.

NOTE: stopping anywhere along the way will yield a useful result. As long as the first step is finished (selector support for `lotus client deal`) the 

####  What does success look like?
_Success means impact. How will we know we did the right thing?_

1. Developers can easily store large directory trees on Filecoin.
2. Developers can easily retrieve individual files from large datasets on Filecoin.
3. Snapshots of English Wikipedia can be stored on Filecoin.

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

The primary risk is that there may be a lack of demand to store large IPFS-formatted datasets in Filecoin. That is, users storing large datasets (> 32GiB) may all be using custom formats and may not care about IPFS files/directories, partial retrieval, etc.

Another risk is that the IPLD selector language may be insufficient to describe useful selectors over IPFS data. It should be at least possible to _store_ DAG subsets using IPLD selectors, but we may need new selectors to, e.g., download individual IPFS files.

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

1. Don't support datasets > 32GiB.
2. Store large datasets as raw objects instead of IPFS files and accept the fact that these datasets
   will be difficult to query/retrieve from IPFS.

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

None.

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->

* Large IPFS datasets.
* IPFS interop.

## Required resources

#### Effort estimate

Small to medium.

#### Roles / skills needed

* Markets (ideally Hannah or Dirk).
* IPLD/Selectors (Riba or Eric).
