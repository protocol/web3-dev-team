# "One-Click" for running Lotus on DigitalOcean

Authors: johndmulhausen

Initial PR: #5

## Purpose &amp; impact
#### Background &amp; intent

Currently all information about our "stack" is siloed across multiple websites
that are in various states of maintenance. There is no place to learn how the
various pieces of the stack such as libp2p, IPFS, Filecoin, IPNS, etc work
together. There is also no place where the benefits of the W3DT stack can be
expressed in a definitive and reliable place. The tech that drives our site
(built on Vuepress) has to be kept in sync manually across multiple websites.
This way, one code push elevates the documentation and user experience across
all our offerings and the popularity of one offering can "boost" another as we
begin to show the integration points.

Building a mental model of Web3 development is a primary adoption barrier for us,
one that pairs very poorly with the difficulty inherent in experimenting with the tech
itself. We need a place where we talk with a unified voice about how it's
different, what its benefits are, why you would and wouldn't use it, how it
compares to Web2, what good metaphors are in the current world for where we
envision things going, and how the tech works together to address common
scenarios in a unique way.

Onboarding is an art, and creating a golden path through our offerings that
shows various pieces of tech working together will require all of us pulling on
the same oar, not continuing to maintain our silos.

To continue to sink development time into any one particular website - such as,
say, ipfs.io - is to create further inconsistency between experiences among our
sites, and takes valuable development time away from dealing with our key
problems: that we have too much to maintain and things are going stale, and we
have no place to paint the whole picture and make the value clear. Symptoms of
these core issues cropped up again and again in discovery.

To address an elephant in the room: we don't have to stamp "PL" onto a unified
site. It can be at "w3dt.io," for example, and we can maintain an "About" page
that talks about the team at PL that is tasked with the mission of bringing this
tech to the world, as well as community and partner contributions and
strenuously highlight that the tech consists of a collection of open-source
projects. However, if the time has come to acknowledge these as PL projects, I
think unifying the docs with protocol.ai would be fine, too.

#### Assumptions &amp; hypotheses

- There are too many repos
- Sites are in a various state of maintenance
- We are not clearly stating how tech works together
- There is no easy path to upgrade all of our websites at once
- There is very little "lift" from one technology being popular translating to another technology gaining in adoption
- There is no place where we are onboarding people onto our stack as a whole or building a general W3 mental model
- We are sinking time into maintaining siloed projects and there is an opportunity cost inherent there

#### User workflow example

They would load this website. At first I presume we would have a simple project list, sort of like https://www.cncf.io/sandbox-projects/

In the long term we should build up scenario-based onboarding that is more
geared towards building the mental model of how the stack solves problems, such
as what you see at https://www.digitalocean.com/business/

#### Impact

🔥🔥🔥

How can we even talk about the "web3 dev stack product-market fit" without a
website that is dedicated to it, or without even regarding it as a stack in the
first place?

#### Leverage

🎯🎯🎯

The amount of distraction that would be avoided alone by trying to do this
across multiple websites, projects, and repos justifies the project, but if we
actually wnat to start convincing people that there is such a thing as a "web3
dev stack" we need to take a stab at providing a "stack experience" complete
with messaging, docs, and onboarding and getting feedback from devs who try to
navigate it as we envision it.

#### Confidence

High. We already have real world data here: the list of "assumptions" is
actually just a restatement of problems we already spoke about together.

## Project definition
#### Brief plan of attack

1. Create new GitHub repo with a new VuePress site
2. Declare "freeze" on existing docs repos, merge/close any open PRs, and pull in "final state" content, putting each tech into subfolders in the new repo
3. Create front page using docs engine that introduces the mission and the various tech
4. Create an "About" page
5. Navigation design exercise: how does switching between projects feel on the site? What happens when you're three-levels deep into a navigation node?
6. Ship
7. Shut down old repos, post redirect scripts on old sites, and import relevant outstanding GH issues

#### What does done look like?

There is one website and one repo with all the documentation in it.

####  What does success look like?

If the project is successful, we should be able to say "yes" to these questions:

- Has traffic, forking/stars, and page ratings for docs on poorly-maintained projects gotten better?
- Do we know where to post something that relates to the whole stack that teaches people high-level Web3 concepts?
- Are we spending less time maintaining various sites, repos, and documentation sets and more time creating content?
- Do we have greater awareness and understanding of the stack amongst ourselves and find ourselves more willing and able to pitch in across projects other than the ones we were working on previously?
- Is it easier to upgrade the user experience and site functionality across our documentation offerings?
- Are docs contributions from the outside world getting more frequent now that there's only one place to do them?
- Are we able to replicate successes (such as delivering a good API docs implementation) that happen in one project (e.g. Filecoin) in another project?
- Are GitHub issues staying open for a shorter amount of time now that they aren't being opened in poorly-monitored repos?

#### Counterpoints &amp; pre-mortem

It would only fail if we do not promote the site properly, or if the developer
community decides there isn't value in our stack after engaging with our best
effort at explaining it in one place with a unified voice and a golden path. In
the case of the former, I would expect that such an important site would have
great support from PL. In the case of the latter: if we are failing after
unifying and clarifying our message to this degree, then there are bigger
problems than just onboarding at play.

#### Alternatives

There's not really an alternative to doing a unified site that would acheive the
same thing as a unified site. There is either one repo and a unified docs
experience, or there isn't. To some degree you could "fake" unification by using
submodules across repos for things like navigation, etc, but that gets extremely
messy and would actually end up increasing the amount of things to maintain
rather than reduce them.

#### Dependencies/prerequisites

The main pre-requisite is buy-in on the idea that this unified voice is possible
without running afoul of PL's desire to remain at a certain "distance" from its
projects. To consolidate this way is to present a certain point of view about
how to apply our technology to the world. "Yes, these projects work together and
are part of a common solution" - but whose? Whose point of view are we hearing? We
have to address that concern. The implementation details are largely academic
after that.

#### Future opportunities

The creation of stack-wide solutions docs, stack-wide onboarding, and a huge
increase in efficiencies w/r/t content creation.

## Required resources

#### Effort estimate

- Medium, 3-5 weeks
- Large, 6-10 weeks

#### Roles / skills needed

- Docs writers are "all hands on deck"
- PM to help drive buy-in and make sure consolidation runs smoothly across projects
- Design should weigh in at a minimum but ideally would be engaged from the beginning
- If design recommends radical changes from our current Vuepress docs implementation, some dev time will be required
