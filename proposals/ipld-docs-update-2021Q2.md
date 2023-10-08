# IPLD Docs Update 2021Q2 

Authors: @biglep, @warpfork

<!--
This minimal project pitch (MPP) template is for a proposal/brief/pitch for a significant project to be undertaken by a Web3 Dev project team.
The goal of project proposals is to help us decide which work to take on, which things are more valuable than other things.
-->
<!--
A minimal project pitch (MPP) should contain enough detail for others to understand what problem this project solves and why this is important for our
team's goal of achieving product-market fit, a high-level description of what the idea/proposed solution is, and space to add more detailed technical 
design and planning information as we develop this information.

The MPP itself does not need to describe the work, technical design, scope, and project plan in much detail.

Projects can include work for major programs (such as Bedrock and Nitro), but they can focus on other areas, e.g. refactors for future capability, 
improving our testing infrastructure, testing and validation, and other engineering-oriented projects.
-->
<!--
For ease of discussion in PRs, consider breaking lines after every sentence or long phrase.
-->

## What is the problem this project solves?
_Describe the status quo, including any relevant context on the problem you're seeing that this project should solve. Who is the user you're solving for, and why do they care about this problem? Wherever possible, include pain points or problems that you've seen users experience to help motivate why solving this problem works towards top-line objectives._ 

There are currently these problems with IPLD documentation:
1. Some of it is aspirational without articualting what is real today.
2. Some good/recent content of the last year has been put other places (e.g., hackmd)
3. The docs site itself is slow and failure-prone to build
4. Readers miss the relevant bits and/or end up resulting to pings to IPLD experts to get their questions answered, which isn't getting pushed back to a public/central channel to make it more self-service the next time.

## Impact
_What goals/OKRs are being addressed (for w3dt, a specific program, etc.)? Why is this project important? What do we get with this project that we can't get without it?_

This project is important because we have inaccuracy and incomplete documentation around a key portion of our stack.  It hasn't been easy for IPLD experts to fix/add documentation there, which further causes more documentation fragmentation.

## The idea
_Describe the proposed project solution, at a very high level. Stay at the level of the high-level requirements. Diagrams and interface descriptions can be useful, if you have any that help clarify and explain the idea._

Fix/create an IPLD site that is accurate (even if incomplete) and is self-service/easy to update going forward.

## Success/acceptance criteria (optional)
_How do we know we're done with this project? How do we know we're successful? This field is OPTIONAL for the first draft of an MPP. Sometimes this field needs to be filled out once we have more detail on the shape of the actual solution._

When PL IPLD experts are asked questions, they respond with URLs to the IPLD docs site.  This may be because they just wrote the answer up, but we have to get out of answers strewn across HackMD, slack, etc. given that doesn't scale.

## Detailed plans (optional)
1. https://github.com/ipld/ipld/issues/96#issuecomment-855691281

## Program (optional)
n/a