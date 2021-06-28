# NFT.storage database migration

Authors: [@hugomrdias](https://github.com/hugomrdias) [@gozala](https://github.com/gozala) [@alanshaw](https://github.com/alanshaw)

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

NFT.storage currently uses Cloudflare Key-Value (KV) stores for persistence. This was great for getting the site up and running ASAP but they provide a very simple data structure that is not addressing our needs anymore. The problems are as follows:

* KV stores are eventually consistent - potential for data and work duplication as well as UX issues on the website (e.g. newly uploaded NFT does not appear in files listing).
* Heavily rate limited, both within worker invocations and externally over the HTTP API.
* No ability to query data. For example, we can't query for all NFTs created by a user after a given date. It's possible to create a new KV with keys structured in a way that would allow this, but it is complicated and duplicates data.
* Pagination page size limited to 1,000 items.
* No ability to count the number of items in a KV. We currently have to paginate over a KV to count the number of items. Due to rate limits this takes a long time and gets worse as the KV grows.
* No data export/backup facility.

## Impact
_What goals/OKRs are being addressed (for w3dt, a specific program, etc.)? Why is this project important? What do we get with this project that we can't get without it?_

* Significant speed improvements for querying our dataset.
* Fast metrics creation.
* Transactional reads and writes.
* GraphQL schema.
* Scalability.

## The idea
_Describe the proposed project solution, at a very high level. Stay at the level of the high-level requirements. Diagrams and interface descriptions can be useful, if you have any that help clarify and explain the idea._

Migrate to a database recommended by Cloudflare that provides solutions to the problems listed above without sacrificing latency, elasticity or availability. Cloudflare has [two database partners it recommends](https://blog.cloudflare.com/partnership-announcement-db/) for complex datasets.

## Success/acceptance criteria (optional)
_How do we know we're done with this project? How do we know we're successful? This field is OPTIONAL for the first draft of an MPP. Sometimes this field needs to be filled out once we have more detail on the shape of the actual solution._

## Detailed plans (optional)
_Link to more detailed project plans, e.g. product requirements documents (PRDs) and technical design docs, once they have been created for this project._

## Program (optional)
_If this project is part of a program, please indicate the relevant program here._
