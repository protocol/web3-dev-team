# Single-source documentation 

Authors: @johnnymatthews 

Initial PR: TBD 

## Purpose and impact 

### Background and intent

Readers can find all IPFS documentation on a single website or in a single GitHub repository.

### Assumptions and hypotheses

This project assumes that folks who want to learn about IPFS don't like hopping around blog posts, websites, and GitHub repos to find the information they need.

### User workflow example

1. The reader goes to docs.ipfs.io.
1. They find the information need.
1. They use that information to perform a task.
    a. If the task failed, they return to docs.ipfs.io for more information.

### Impact

🔥🔥🔥

Developers get upset when a project's documentation does not answer their questions. Having docs all over the place is an excellent way to make sure we don't answer user questions correctly. Therefore, having docs in one place is a straight-forward way to increase developers' chances of finding the information they need.

### Leverage

🎯 

Moving all docs into a single repo doesn't help _our_ developers build IPFS too much. But it really, _really_ helps developers who want to use IPFS but don't personally know an IPFS developer.

### Confidence

I don't understand this section. I'm very confident that what I've written so far is true and that completing this project will make developers' lives easier.

## Project definition

### Brief plan of attack

[There's a project available in the ipfs-docs GitHub repo](https://github.com/ipfs/ipfs-docs/projects/3). This project includes a one week discovery phase where the team bounces around the internet, finding IPFS documentation, and determining whether it's still relevant or needs updating.

### What does done look like?

All documentation listed in the GitHub project has been migrated to ipfs-docs or deemed out-of-date.

###  What does success look like?

We reduce the bounce-rate of folks coming to docs.ipfs.io.

### Counterpoints and pre-mortem

This project requires the developers and owners of other GitHub repos (js-ipfs, go-ipfs, etc.) to be committed to updating docs in the ipfs-docs repo.

### Alternatives

We leave users to filter through blog posts, third-party sites, and multiple GitHub repos to get the answers they need.

### Dependencies/prerequisites

I can't think of any right now.

#### Future opportunities

I can't think of any right now.

## Required resources

### Effort estimate

Medium: 3-6 weeks. This rating assumes we have 100% of my (@johnnymatthews) time, and there are no other distractions.

#### Roles / skills needed

- Docs
- PM
