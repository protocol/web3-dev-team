# Selectors have sufficiently predictable resource budgets to be used in low-trust environments

Authors: @warpfork

Initial PR: https://github.com/protocol/web3-dev-team/pull/27


Purpose & impact
----------------

#### Background & intent
_Describe the desired state of the world after this project? Why does that matter?_

The status quo is: we have Selectors, and they can be used to describe walks of graphs of data.
(They're sorta like regexps for DAGs, if that's a useful comparison for you.)
We want to expose these

The problem is: if a service wants to accept Selectors which are user-specified,
then the user can ask the service to do arbitrarily expensive work.
This would create a way for users to take the service down (a DoS).

The intent is: we should create a resource budgeting system for Selectors.
The system should be declarative and comprehensible,
and must be something that administrators of services built with Selectors can configure in order to limit their exposure to DoS.

#### Assumptions & hypotheses
_What must be true for this project to matter?_

- Selectors are something that either PL's or our community's projects expose as an API;
- and that API is expected to be able to accept user-specified Selectors;
- and the Selector would be evaluated by a different resource owner than the author;
- and denial-of-service via maliciously crafted Selectors would be problematic.

(That sounds like a lot of conditions, but from what I can tell,
users often want to treat Selectors like they're "free" to evaluate,
and that results in folks building APIs with exactly these expectations.)

Another way to address the underlying issue is to make Selector evaluation connected to a billing system,
but the work would also be required to make that kind of connection possible.
(A billing system does no good if one can submit a task that bankrupts you before the bill is settlable.)

#### User workflow example
_How would a developer or user use this new capability?_

When users ask for data from a service like IPFS,
they submit a Selector, and expect to receive a series of blocks in response
(typically in the form of a "car" or "dar" or other such format).

This workflow from the user's perspective shouldn't change significantly.

From the service host's perspective,
they should probably have some some configuration file which lets them set limits
for how much data is matched by a single selector before the service cuts off that request.

Ideally, the limit system is comprehensible enough that users can estimate the costs of a query before submitting it,
because it's typically not pleasant to get a failure after some effort has already been expended.
(It's not clear how possible this is, but if possible, it's desirable.)

#### Impact
_How directly important is the outcome to web3 dev stack product-market fit?_

However important Selectors are to web3 dev stack PMF, this is that times about 0.95.

Within the relevance of Selectors: this budgeting requirement is not critical right up until it's critical.

Building services which accept user-specified Selectors and evaluate them and are exposed to the public is an unwise thing for someone to do until this is addressed.

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

Leverage of this is probably low.
We can already design systems using Selectors.

Assuming it's reasonable to bet that adding resource budgets to Selectors will not drastically change the way they fit together into systems overall,
this work is overall is fairly deferrable without causing pipeline stalls in other work.

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

(Not really sure how to apply the numeric scale to this, sorry.)

3?  10?  I think we're extremely sure that this will be a problem for certain user stories.
We can consult folks working on Filecoin features which block on this for more information.


Project definition
------------------

#### Brief plan of attack

1. Design work: Figure out what good budgeting means.
	- @warpfork's initial bet is: just having a single global counter which monotonically decreases during evaluation is the right direction.
2. Design work: Figure out how the limits should be expressed in the Selector format.
	- Should a limit value be always required at the root?
	- Should other sub-limits (i.e. can only further drop the limit, not start a new budget) be allowed throughout the query?
	- What unit is the limit?  Blocks or nodes?  Or binary size (e.g. does selecting a large string count harder against the budget than a small one)?
	- Consider: that walks with selectors are currently defined as yielding `(path,node)` pairs -- which means reaching the same data by a different path is considered distinct, and causes time to be expended on a visitation that's arguably a repeat.  Do we want to revisit this?  It has unfortunate performance implications on some densely linked graph structures.
	- Figure out exactly what behavior we expect from APIs when they encounter a limit -- simply halting addresses the DoS concern, but what will a user's action options be when they receive a halt due to budget exceeded?  Will there be any option for resumability?  Etc.
3. Design Work: Work through how service operators will be able to look at a Selector and decide if they want to evaluate it or not.
	- This is a sanity-checking process for the either design phase.
4. Implement: in the [go-ipld-prime/traversal/selectors](https://github.com/ipld/go-ipld-prime/tree/master/traversal/selector) package.
5. Test: make sure we have examples of datasets and selectors to run on them which we expect to be halted by budget limits.
	- Ideally this should be in language-agnostic test fixture files, so we can reuse them in other selectors implementations.
6. Documentation: update it.
7. Synchronize: other implementations!
	- The [ChainSafe forest](https://github.com/ChainSafe/forest/) project contains a Selectors implementation -- communicate with them about these changes!
8. Propagation to downstream, possible small migrations?
	- If we make the budget system non-optional, then existing Selector documents may not work.
	- Or, there might be no special work needed here, if the budget system is entirely optional.

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

- Selectors in the go-ipld-prime implementation should have resource budgeting.
- Test fixtures should demonstrate what a selection which halts due to a resource budget exhaustion behaves like.
- The resource budget specification declaration system should be reasonably comprehensible and look like something we can tell administrators of hypothetical services using this system how to configure.
	- Probably: it should be as simple as _one number_.

####  What does success look like?
_Success means impact. How will we know we did the right thing?_

When developers such as the Filecoin team feel comfortable exposing features using Selectors to users, then this project is a success.

#### Counterpoints & pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

- Overcomplicating the budget system could result in usability failure.
  (Arguably, the current limit systems are this, because they're too granular, which is no substitute for a holistic system.)

- Technical consideration: Beware the "[Billion Laughs](https://en.wikipedia.org/wiki/Billion_laughs)" problem.
  (This is why this document keeps emphasizing a budget that is holistic and monotonically decreasing.)

- A system that halts but returns insufficient information about why could be frustrating to users,
  even if it successfully addresses the DoS problem.

- Keep in mind: this proposal only describes implementing this in golang.
  We do not currently have a javascript Selectors implementation (and creating one is a larger task).
  This is not a problem per se; it's just something to remember when considering what can be immediately built upon this work.

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

One: See remarks about budgeting in the Assumptions & Hypothesis section.
Some system of resource currency could be associated with this problem as part of the solution.
(This doesn't necessarily remove the need for engineering work on the Selector system to support it, though,
which means this should probably be considered a stretch goal or future work rather than an alternative.)

Two: It's possible to work around this in some cases by building APIs around selectors,
but then only accept a known, pre-specified set of selectors.
(If I understand correctly, this is how several pieces of Filecoin currently around around this issue.)
This is not a general workaround, though, and ruins most of the point of Selectors -- they're *supposed* to be user-specifiable.

Three: a totally distinct graph query mechanism could be proposed.
However, whatever that system is: it would have the same need for a budget mechanism.

#### Dependencies/prerequisites

- No strict dependencies known.
- Bonus/Accelerant: if the Selector implementation in go-ipld-prime was refactored to be built off a Schema and use codegen, it would probably be easier to update.
- Bonus/Stabilizer: if the documentation site which covers Selectors was connected with an automated test suite which checks that examples in the documentation actually match behavior of the libraries,
it would be much easier to be confident in the correctness and completeness of our documentation.

#### Future opportunities

Selectors with resource budgets make them safe to use in services which accept user-defined Selectors.


Required resources
------------------

#### Effort estimate
<!--T-shirt size rating of the size of the project. If the project might require external collaborators/teams, please note in the roles/skills section below).
For a team of 3-5 people with the appropriate skills:
- Small, 1-2 weeks
- Medium, 3-5 weeks
- Large, 6-10 weeks
- XLarge, >10 weeks
Describe any choices and uncertainty in this scope estimate. (E.g. Uncertainty in the scope until design work is complete, low uncertainty in execution thereafter.)
-->

Probably "Medium, 3-5 weeks".

It's not Small, because the design phases shouldn't be skimped on.
(It will be easy to implement something that compiles, but doesn't solve the problem correctly;
therefore it seems unwise to try to cram this into a small 1-2 weeks timeline.)
(_Maybe_ it will turn out to be small, but I'd rather greet that as a pleasant surprise.)

It's not likely to be Large (6-10 weeks) because there's just not that much work to do here if tackled by a team.
(It's renovation work and a new feature within an existing system, not a whole new system.)

The "resumability" consideration should probably be considered out of scope,
or the effort estimate increases significantly and the confidence decreases significantly.

Other Selectors implementations will not necessarily be updated during this work period;
however, these are maintained by teams outside of PL, so this is natural:
we should just aim to leave them set up and aware of what they would need to do.

#### Roles / skills needed

- Golang developers (work is required in go-ipld-prime)
	- Bonus if they're already familiar with Selectors

I probably wouldn't recommend trying to spin this out to a community or external team.
The task size isn't big enough to be worth the overhead,
the amount of separability of the task is low and would result in friction,
and the amount of trust we need to have in the result is high,
so we'd spend as much time reviewing the result as we would just doing the design work ourselves.
