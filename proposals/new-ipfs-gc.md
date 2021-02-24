# Project Pitch: IPFS Garbage Collection v2
###### Making GC fast, efficient, and targeted

Authors: @gammazero

## Purpose and Impact

### Background and Intent
When storage is reclaimed by removing unpinned blocks, this garbage collection requires stopping other IPFS activities for its duration, and can take significant time.  For users such as [Pinata](https://pinata.cloud/), this can take “literally days” for a single node.  For large pin sets, this is expensive in both memory and time.  Garbage collection needs to operate differently, to significantly reduce the impact on IPFS.  Another request from multiple users is to be able to remove specific content from an IPFS node.  Currently, GC removes all unpinned blocks.  It would be useful for GC to be able to remove all blocks associated with a specific DAG.

After this project, these specific pain-points will be resolved:
- GC takes too long for nodes with large pin sets
- Need to GC content when it becomes unpinned
- Need to be able to remove specific content 

This project is critical for continued growth of users such as Pinata, as the current GC implementation is a significant obstacle for them.  The project is also important to users who need to remove specific content from their nodes, but do not want complete GC.

#### Related discussions
- [Call with Matt Ober (Pinata) about GC](https://www.notion.so/Pinata-5157fa6d2a4741a593bb8ff32bfdb08e)
- [Github tracking of related issues](https://github.com/ipfs/go-ipfs/issues/7752)
- https://protocollabs.slack.com/archives/G01KZD3FETY/p1613779249428300

### Assumptions and Hypotheses

For this project to matter, it must significantly improve operations for highly impacted customers like Pinata. Faster GC will have a directly improve Pinata’s use of IPFS.  Having the ability to remove content when it becomes unpinned will further enhance the improvement for Pinata’s use case, as GC can avoid looking at all blocks and can operate on only those that became unpinned. 

For users who do not see or care about the GC performance issues, this project will still matter to users who need to remove specific content from nodes, but do not want to remove all unpinned content.

It is assumed that the overall time to examine the reference count of each block is less that the time to load all pinned blocks, store their CIDs in memory, and then search those CIDs for every block to see the block can be removed.

### User workflow example

#### Bulk GC
A user would use the new GC in the same way as the previous version, but with potentially significant reductions in duration and therefore less disruption to IPFS operation.  This may eliminate the need to work around the disruption by doing things like taking nodes offline to perform GC.  Ideally, GC lock time should be minimized to allow GC to be done effectively concurrently with normal IPFS operation.

#### Removing Specific Content
Certain users may only need to remove content that becomes unpinned.  This is particularly true of pinning services such as Pinata, and will be their primary, if not only, method of garbage collection. To remove content that becomes unpinned, the command line workflow is:
- Unpin the desired content: `ipfs pin rm <cid>`
- GC the unpinned content: `ipfs repo gc --cid=<cid>`

The above could also be done with a single command, if it adds value: `ipfs pin rm -gc <cid>`
It may be valuable once local named pinning is available.

In the case that a user wants to remove content that was never pinned, they execute step 2 from above. This tells GC to walk the IPLD DAG identified by the CID and remove any associated blocks that are not referenced.

### Impact
While impact varies greatly for different types of users, some of our most important users (e.g. Pinata) are heavily impacted and have a need for this feature.  It will have a significant effect on their business operations.  Therefore, this gets an impact rating of 3.
🔥🔥🔥 

### Leverage
This fixes a few specific issues, but is not highly leverageable.  The ability to remove specific content may allow implementation of a custom data retention policy.  Therefore this gets a 1 for leverage. 
🎯

### Confidence
Medium (level 5) confidence, according to [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

## Project definition

### Brief plan of attack

1. Design how reference counting is implemented, exploring what interfaces will change, and what subsystems will be affected.  Address handling storage limits, preventing removal of newly arrived blocks, need for transactions in datastore, etc.
2. Implement reference counting of blocks in the blockstore.  Counts  are updated by pinner and MFS.
3. Implement new garbage collector that operates on reference counts instead of pinned CIDs
4. Implement targeted GC (GC that follows a DAG and deletes associated unreferenced blocks)
5. Implement metrics for both new and old GC to compare performance.
6. Optional, if it adds value: Implement command to remove pin and then immediately GC the unpinned CID
7. Distribute an experimental version of go-ipfs for evaluation and feedback.

Garbage collection performance issues arise because GC attempts to remove blocks by loading a set of all pinned CIDs into memory and searching for each block’s CID in this set.  The plan attack operates on the following premises:

- Maintaining reference counts for blocks will make it quick to determine if a block can be removed, because it is not necessary to load all pinned CIDs into memory and search this.
- Specific content can be removed by performing GC on the blocks associated with a IPLD DAG identified by CID.

### What does done look like?
#### Functional
- Bulk GC should be faster and use less memory. 
- Targeted GC: Ability for GC to remove content identified by CID
  - New `--cid` option: `ipfs repo gc --cid=<cid>`
- Metrics for new and old GC: time to complete GC, blocks examined, blocks removed

These metrics should also be implemented for the old GC so that when running in "verify" mode the overall performance of the both GC implementations can be compared.
#### Implementation
- Block reference counts stored in datastore
- Block reference counts updated by pinning, unpinning, adding to MFS, removing from MFS. 
- New GC implementation that operates on block reference counts instead of on set of all pinned CIDs

Targeted GC will allow users like Pinata to remove specific content that has been unpinned, instead of doing bulk GC to search the entire blockstore for content to remove. When combined with a reference-counted GC that does not require loading all other pinned content into memory and searchin it, this will result in hugely significant improvement in the GC time.

Removing pins will be slower because it requires walking DAG to decrement reference counts. Adding items to MFS and removing items from MFS will be slower due to needing to update reference counts. These increases should not be significant.  Datastore will use more space, one key-value entry per block in blockstore.  This may be significant, but should not cause problems for most users.

### What does success look like?
Success, for Pinata, means that they can remove unpinned content with significant reduction in time that node is unavailable during GC.  Best case is that this allows Pinata to perform GC without having to take a node offline, and with little or no impact to IPFS running on the node.

Success also means that this functionality does not have a significant negative impact, such as consuming large amounts of storage space, or impairing the performance of operations outside of GC  This must be true for all usersA user should be able to remove only content that becomes un 

### Counterpoints and pre-mortem
If high performance GC results in reduced performance elsewhere, users not affected by GC performance issues will see this as a negative impact. The following areas could be negatively affected by the new GC, but hopefully none will be significant for any user
- Removing pins will be slower because it requires walking DAG to decrement reference counts.
- Adding items to MFS and removing items from MFS will be slower due to needing to update reference counts.
- Keeping reference counts will consume for storage space

The project could fail, or fail to be deliverable in the proposed time if reference counting incurs unforseen complexity in its implementation or changes required to other subsystems.  The risk of the will be mitigated by early review of reference counting design and prototyping.

### Alternatives
There does not currently appear to be alternate ways to solve these issues.  There may be tools that are better suited to implementing portions of GC, such as a specific key-value store that is better suited to managing reference counts

### Dependencies/prerequisites
Desirable, but not required: Possible MFS bug fix for reported loss of MFS root

### Future opportunities
- Incremental GC: Remove some unpinned blocks as needed to maintain storage limits. 
- Choice of, or flexible, data retention configuration.

## Required resources

### Effort estimate
1-2 people 4-6 weeks

### Roles / skills needed
Go + IPFS expertice
