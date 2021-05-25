Unixfsv1 directories as ADLs
============================

Authors: @warpfork, @lidel, and other reviewers

Initial PR: TBD <!-- Reference the PR first proposing this document. Oooh, self-reference! -->

Purpose & Impact
----------------

### Executive Summary

Current unixfsv1 APIs provide bad developer experience in numerous ways,
having direct bug-creation effects that are causing close collaborators to have serious problems,
as well as having longer-term confusion effects which slow down development
or at worst, may mislead development due to situations where the correct thing is not easy to do and a semantically mis-layered thing is easier than the correct thing.

One example of a currently pressing problem is that users have stumbled upon a way of using the current APIs
which results in the creation of data that is not actually transferable by libp2p (e.g. oversize blocks).
While a series of "quick fixes" ("ducktape" solutions) to the most immediate problems are possible,
there are still serious maintainability issues to address,
and most of the "quick fixes" are user-hostile in some way (i.e. failing earlier in the path, and telling users to use a different API),
or further complicated the developer experience in the long run (i.e. telling users to use a higher level API which avoids the most critical problem but provides _different semantics_ than the direct features the user wanted --
which may further mislead any future development!).

This proposal is for a targetted piece of development work which will solve this problems
by supplying Unixfsv1 functionality through a clean implementation as an ADL (short for Advanced Data Layout,
a concept from the IPLD project which is meant to provide a solution area for problems like sharding).

In addition to solving the problem examples above,
this work will also immediately result in several new features becoming reachable
(such as IPLD Selectors becoming operable over Unixfsv1 pathing!,
and build a strong foundation for future work.

We believe that that the work outlined below will
make the stack more robust,
more consistent,
and easier to understand for future developers both inside and nearby the core stack.

### Background & intent
_Describe the desired state of the world after this project? Why does that matter?_
<!--
Outline the status quo, including any relevant context on the problem you’re seeing that this project should solve. Wherever possible, include pains or problems that you’ve seen users experience to help motivate why solving this problem works towards top-line objectives.
-->

Unixfsv1 is a large and key subsystem of IPFS.
It is the internal format used by IPFS whenever users are experiencing "files" and "directories".
(When users are using "dag" APIs or other direct-to-IPLD APIs, they are not (necessarily) experiencing Unixfsv1;
most other APIs, such as `ipfs add`, `ipfs cat`, including also MFS, etc, _are_ experiencing Unixfsv1.)

Unixfsv1 implementation components are currently scattered among many source code repositories,
and the API boundaries are not especially clear.  Maintenance is generally difficult.
It would be desirable for our own development and productivity if more of this implementation was unified in one place.

At the same time, Unixfsv1's current implementation in golang predate much of the latest generation of work in IPLD.
We believe significant gains of features, as well as clarity of design,
are possible by rebuilding Unixfsv1 features in the form of an IPLD concept known as ADLs.

Closer to users: The APIs made available to Unixfsv1 from IPFS can be confusing.
Some very low-level features are made available by IPFS APIs, but are not always safe to use,
because they may do incorrect things in "corner cases" which are not obvious to end users, resulting in a general air of fragility.
Some high level features are made available by other IPFS APIs, but jump to such a high level
that users with specific needs can be observed to jump back down to the low level APIs
(and then procede to use them incorrectly, because those APIs do not guide the user to good usage).

Example user stories such as "patch this directory" currently don't work out well, because while we offer "patch" APIs in some places,
they only work on low-level data, or, they work on high level data, but in ways that are not entirely desirable:

- In the low-level way: we encounter problematic scenarios because low-level abstractions do not include enough knowledge
  to engage mechanisms like directory sharding... even when failure to do so means producing blocks of low-level data
  which are so large that they exceed the limits set by data transfer mechanisms elsewhere in our stack.
  This incoherence results in serious usability problems
  (specifically, that users can create data which is then only available from that node, and cannot be transferred).
- In the high-level way: While the "patch" user story can be satisfied (arguably) through the use of the MFS system,
  we don't wish to encourage that route for several reasons:
	- It's a complex system, and we're not happy with its maintenance profile or confident in its current implementation.
	  (We won't go into this further in this document.  The purpose of this document is not to describe work to replace MFS.
	  We mention MFS here only because it's been raised as a potential stopgap or workaround for other issues relating to Unixfsv1,
	  and accordingly, it seems relevant to remark on on reasons that it may not be ideal to lean on.)
	- The semantics of MFS focus in on a filesystem-oriented worldview.
	  While sometimes that is what users are looking for, sometimes it's also considerably more narrow than what users are looking for.
	  When we don't offer features in Unixfsv1 except through MFS, and users weren't already attracted to MFS's semantics,
	  it results in confusion and friction, and potentially mis-guides developments.
	- The MFS system requires multiple steps in order to produce something comparable to "patch":
	  one step to "import", another step to "modify", a final step to "read CID" (roughly speaking).
	  In addition to the semantic gap, this has observable performance taxes in the form of API RTT overhead.
	  (The "import" step may still refer to CIDs rather than freshly ingesting a file, e.g. `ipfs files cp` is an option in addition to `ipfs files write`,
	  but nonetheless this is a step which must be taken in its own API RTT.)
	- MFS has an implicit "root" directory on which commands operate... which means the API can be significantly stateful
	  (which is often not what users are looking for -- observe that the lower level `object patch` APIs which users have often preferred are a single call, and not stateful),
	  and also has observable performance taxes in the form of garbage object creation for tracking that (unnecessary) "root" directory.
	- Work on top of MFS cannot be be used on unixfs without MFS; work on unixfs directly helps MFS.
	  Therefore it's almost always preferable to solve problems in the unixfs layer where possible,
	  because it makes the solutions available more widely.
	- MFS solves pinning and concurrent GC unsafety issues by implicitly pinning everything under its megalithic "root"...
	  but while this certainly works, it's using very high level semantics to solve a very primitive problem,
	  and we should consider whether this results in misleading developers in their designs and use of the system.
	- There has been significant discussion around the likely need to add more locks to the MFS code in order to make it safer,
	  which may require significant development work and may further degrade the performance of MFS.
	  (Again, we'll attempt not to focus further on this subject in this document,
	  but remark on it briefly because it came up in discussion of MFS and its potential as a stopgap.)

We want to move towards is a middle ground:
where Unixfsv1 can have simple "low-level" APIs that act like familiar primitives
(such as "directories" acting as "maps"),
while also having enough internal richness to solve problems
(such as sharding, which should engage transparently and as necessary, based on the scale of the data).

We hope that by working in this direction and implementing Unixfsv1 as IPLD ADLs,
we will gain APIs which provide coherent and predictable experiences,
are easy to explain,
provide solid foundations for more advanced protocol work above them without leaking fragility and edge-cases into higher level abstractions and end-user experiences,
and are easier to maintain.

#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->

- Unixfsv1 continues to matter as a format that users both read and write data in.
- It is becoming increasingly reasonable to prioritize doing something about this, rather than put it off further,
  in particular due to some of the recent indicator events discussed in the background section.
- This approach (ADLs) is a coherent and viable way to frame this work.
- Alternative approaches are not competitive... which could be due to: Any of:
	- All the other alternative ways one could refactor the unixfsv1 systems are not easier... which could be due to: Combinations of:
		- hypothetical alternatives are less well-defined.
		- hypothetical alternatives are not known to be less work.
		- hypothetical alternatives have a higher chance of failure to produce a result that is simple enough to be an improvement.
		- we've already done a substantial amount of the work on this angle of approach anyway.
	- Alternative ways to refactor the unixfsv1 systems provide less value... which could be due to: Any of:
		- hypothetical alternatives do not provide a comparably direct foundation for features like "patch".
		- hypothetical alternatives do not provide a roadmap to Selectors (and thus other advanced goals like Graphsync) working over unixfsv1 data when sharded.
	- Alternative ways to avoid this work have other negative externalities... which could be due to: Any of:
		- unsatisfactory end user confusion from navigating workarounds.
		- unsatisfactory performance of workarounds.
		- unsatisfactory mis-guiding of future developments due to highlighting concepts other than the desired concepts.
		- unsatisfactory maintenance burden or existing bug discovery rates in existing systems which workarounds lean on.

Note: this is not a proposal to deprecate the MFS system.
We've mentioned it in documents near this as a workaround for some of the same issues.
We're concerned about making sure it's not *over-depended* on as a workaround for some of these,
but still also consider the filesystem metaphor that MFS provides valuable in its own right for user stories that prefer this approach.

#### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->

IPFS APIs should make semantics like "patch new entries into a directory" work using this library code.
This will work correctly even for large directories (which need to use sharding mechanisms internally),
which will result in those APIs becoming safe to use even with large volumes of data
(whereas currently these APIs are unsafe and may cause the production of data which exceeds block size limits without sharding,
causing IPFS node to locally persist data which it cannot subsequently transfer).

Implementing these IPFS APIs using the new code should be greatly simplified,
because instead of hitting unixfsv1-novel APIs, the key operations become "append to this map",
which is an API that other code can easily use too.

Any users wishing to programmatically engage with unixfsv1 data on their own in golang should find
the process drastically simplified, because all the necessary code is in one place, in one repository;
and they should be able to interact with Unixfsv1 directories as if they were "just maps",
which is a pleasantly easy story to communicate.

#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

We would like to see better APIs, both programmatically and as exposed by IPFS daemons,
for operations like "patch" on a Unixfsv1 directory... which fully account for all the special logic in Unixfsv1 directories,
such as the need to shard when the data grows beyond some threshhold volumes.

We would like to see fewer end-user problems (!) arising from misuse of APIs.
The changes to APIs such as the "patch" story above should accomplish this.

Making Unixfsv1 available, writably, as ADL means that APIs like "patch this directory" become extremely trivial to implement;
we just implement them as "patch this _map_".
This provides direct value because these "patch" semantics are something that end users are directly looking for.


#### Internal leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

Unixfsv1-as-ADLs is a drastic piece of internal leverage.
It means that all the special logic for unixfsv1 becomes:
- centralized in one place,
- has clear API boundaries,
- can be interacted with like "regular" maps;
- makes pathing APIs simpler;
- makes patching APIs go from wild to trivial;
- is more maintainable;
- sets us up on a clear path for further extracting the logic to WASM or other interpretable portable code in the future, which aligns with a long-term goal of Protocol Labs.

It immediately makes numerous maintenance burdens go drastically down,
and makes several new APIs drastically easier to provide.

We would like the Unixfsv1-related APIs from IPFS to have less special/"magical" code in IPFS itself,
and become mostly thin shims around well-designed Unixfsv1 libraries,
which will both make IPFS more maintainable,
and make it easier for other developers to engage with the raw pieces programmatically should they desire to do so.

"Can be interacted with like 'regular' maps" is a particularly high-leverage outcome:
this means that unixfsv1 directories will work with [`ipfs dag patch`](https://github.com/ipfs/go-ipfs/issues/4782) systems
and [`ipfs dag diff`](https://github.com/ipfs/go-ipfs/issues/4801), which have been highly desired for a long time.
These features will even work, transparently, whether or not they're sharded, which is not merely cool in theory,
but will also directly address major user issues with the current system (e.g. the "patch can create untransferrable oversized blocks" problem).

On top of all these immediate and direct benefits,
finishing Unixfsv1-as-ADLs also gives us a clear, riffable example of how other similar structures could be implemented as ADLs in the future,
and means we generate learning experiences for how ADLs should grow (which helps satisfy other long term objectives).
Gaining these experiences will other make projects (such as, but certainly not limited to, "unixfsv2") become much more approachable and understandable to a larger pool of engineers.
Increasing the amount of work we do as ADLs in the future could drastically increase code reusability, especially for sharding algorithms, etc,
whereas we can already see from our other projects that such code will be reinvented frequently and in low-reusability ways if not guided.

There are few things in our entire stack that are _higher_ leverage, in this author's opinion.

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

Ballpark 4, if not higher.
(And it's not really clear how internal engineering work could rank any higher on that scale until it's already done.)

We have some testimonial quotes from our own developers which include:
"We need to do this or we will end up running around unixfsv1 in circles for the next two years."

And: "We have recent issues with _unixfs not being fully supported by ipfs_."

Furthermore, we're already largely committed to this path of action,
(or finding an alternative to it, quickly), for several reasons.

We already have the 'read' half of the Unixfsv1-as-ADL data pipeline finished.
This started during the ipld-prime-in-ipfs work, of which one cycle has been landed;
future cycles would also almost certainly pick this up.
We just need to finish.

We've already started to mark some APIs which touch these feature areas, but in wrong or fragile ways, as deprecated
(such as [Deprecating the Object API](https://github.com/ipfs/go-ipfs/issues/7936)).
We need to provide good solutions to all the user stories which previously flowed through there,
and this work will give us the foundations to do so solidly.

We already have a long and deep laundry list of issues and wishlist items around `ipfs dag` commands, and making them work gracefully and consistently.
If they work gracefully *with unixfsv1 data* right out of the box, that's a huge advantage in getting our own development to advance,
as well as convincing our users to migrate to the new APIs, which will keep both us and our community and users happier in the long run.

We already have users encountering significant problems using the current APIs.
At least one major user has already started producing data which is impossible to transfer through libp2p
because our object patching APIs readily generate over-sized blocks.
This is a fairly huge problem.
While there are "quick fixes" to that immediate problem,
a solution is needed which better addresses the user story that lead this user into this problem area in the first place.
This is that solution.

Taken together, it seems we have a good number of reasons to be confident in impact from this work.


Project definition
------------------

#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

Long story short: make unixfsv1 structures readable and writable as ADLs.
This means: make code that makes unixfsv1 structures act like "maps" (in IPLD terms: report `Kind()` as `Map`; support `LookupByString`, `MapIterator`, etc).

See roadmap in https://github.com/ipfs/go-unixfsnode/pull/3 .

We want to check most of those boxes.

A lot of this work has already begun in that repo.
Much of the reading direction of the implementations are already present;
most of the work needed is in the writing direction.

The items in that roadmap for dealing with large binary objects are desirable in general,
but unrelated to this specific proposal and need (or, perhaps are stretch goals).
The current most pressing need is focused on directories and their sharding.

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

- [ ] The https://github.com/ipfs/go-unixfsnode/ repo should have tests indicating that we can both **read** and **write** unixfsv1 directories
- [ ] ... at a variety of sizes, including both over and under the sharding threshhold.
- [ ] We should be able to mark several old repos relating to unixfsv1 as legacy, and ideally, archive them.
	- TODO:REVIEW: `go-path`, several others -- generate this list, please.
- We can close several old issues about IPFS APIs consistently engage sharding transparently.
	- [ ] [ipfs get: link resolution not working for HAMT-sharded directories](https://github.com/ipfs/go-ipfs/issues/8072)
	- (This is not an exhaustive list!  There are probably more reports of these issues.)

Additionally, these other goals may be in sufficiently easy reach that we could use them to demonstrate success and ensure true doneness:

- [ ] TODO: I'd like to say we should be able to use `ipfs dag get` to path through unixfs dirs -- but that isn't currently a feature?  Did we not previously have feature that can do steps through dags without sending it to the client?
- [ ] We should be able to offer an `ipfs dag patch` API based on the new code, which should allow updating a directory shard transparently.
	- [`ipfs dag patch` has been desired for some time](https://github.com/ipfs/go-ipfs/issues/4782).
		- this should be replacement to the comparable `ipfs object patch` feature, but also now work with sharding, as well as work consistently across codecs.
	- This would likely need an `--adl="foobar"` flag, in order to make sense -- this is acceptable.
		- We may also be able to craft some other trigger logic based on the CID we started from, but it's a stretch goal and may be of dubious advisability anyway (it could result in a sense of consistency in our APIs if it's "too" magical).
	- Beware of potential rabbitholes here.  A "perfect" patch feature for all usecases may become quite difficult.  A limited form of the feature which does simple adds and updates ("put", "upsert"; choose your term) to a map would be sufficient to demonstrate utility.

- [ ] IPFS API for comparing two DAGs  (requested by pinning services to make their orchestration more efficient)
	- old `ipfs object diff`
	- new (eg. [`ipfs dag diff`](https://github.com/ipfs/go-ipfs/issues/4801) - details tbd)
	- pinata is using diff tools that only work for unixfs data... which means they don't support other data like dag-json.
	- this is probably a stretch goal for the first timeblock of work

#### What does success look like?
_Success means impact. How will we know we did the right thing?_

<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

We're looking for several successes at once from this work.

We're looking for features of Unixfsv1 like sharding to become consistently available through multiple IPFS APIs.
We hope this will be visible by a better experience and fewer bug reports from developers using APIs like the "patch" APIs --
not to mention by seeing usage in the wild which does not encounter the "oversized block" pitfall.
In general, we would hope to see fewer bug reports about inconsistent API experiences from IPFS.

We're looking for an increase in maintainability, which we'll hope to see in the form of less reticence from developers to engage with Unixfsv1 code.
(This should also be easily concretely detectable in the form of old repos archived and code we can fully remove after this work is complete.)

We're hoping to see more developers engage with IPLD concepts underneath their data,
and see how IPLD and Unixfsv1 can relate.
We hope this will result in more engagement with both IPFS and IPLD overall,
as developers become more able to see the range of choices they have for working with data,
and the kind of practical power that can come from this stack and its data models.

#### Counterpoints & pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

Some specific user needs can be solved by redirecting them to use the MFS system.
However, this is undesirable for many reasons, both practical and mechanical and semantic, as detailed earlier, in the Background sections.

There are no competing solution concepts available that nail goals such as "selectors work over unixfs paths" that this author is aware of.

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

- None.  We've done a lot of the backing infra for this already.

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->

Many future DAG APIs will "automagically" become capable of working with Unixfsv1 data as a result of this work --
even those we haven't produced yet (as long as they operate on the semantics of "maps").

Features like IPLD Selectors will work transparently over Unixfsv1 pathing as a result of this work.

We should be able to deprecate and archive several legacy repos as a result of this work,
which should reduce our maintenance burdens.

Using this work as an example for how to produce more ADLs in the future may
pave the road for tackling other work in the same way.

### Required resources

#### Effort estimate
<!--T-shirt size rating of the size of the project. If the project might require external collaborators/teams, please note in the roles/skills section below).
For a team of 3-5 people with the appropriate skills:
- Small, 1-2 weeks
- Medium, 3-5 weeks
- Large, 6-10 weeks
- XLarge, >10 weeks
Describe any choices and uncertainty in this scope estimate. (E.g. Uncertainty in the scope until design work is complete, low uncertainty in execution thereafter.)
-->

This is probably a "Medium" goal, 3-5 weeks, for a dedicated team.

This may depend on how many end-user integration goals we pursue at the same time.
(In particular, the more that such work involves development areas like the IPFS APIs,
the more potential there is for interesting frictions and elongated review cycles
compared to work which is in less encumbered areas.)

#### Roles / skills needed
<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->

Prior experience with go-ipld-prime and ADLs will be helpful,
but can be gained on the fly, and is useful to circulate.

Prior work in the https://github.com/ipfs/go-unixfsnode repo will be helpful,
because we'll want to continue to build on the work that's already been started there.

Prior work in the other unixfs-related repos (which we will aim to deprecate by this work) will be helpful.
Attempting to complete the work as someone not familiar with this code may increase the effort estimate,
or finding someone with that familiarity to consult with might become a blocker to pursuing the work effectively.
