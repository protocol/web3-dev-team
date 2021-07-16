# go-daggregator CLI tool

Authors: @dchoi27

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
Currently, clients making storage deals themselves for files smaller than a sector generally have to make a decision to either put each file into a deal, or aggregate multiple files into a compressed file and put that into a deal. The former introduces complexity to the dealmaking process and increases the costs to the miner, but the latter forces them to often retrieve more than just the files they need.

By allowing clients to aggregate files into CARs that can take advantage of CARv2 / partial retrieval, they can get the best of both worlds.

## Impact
This will increase the efficiency of users making deals directly with miners, especially those with large datasets. It also tells a better story around retrievability of their data, which usually isn't a top-level concern for them (since these are often archival use cases), but can be. For instance, in the next few months Internet Archive is looking to build an interactive use case on top of Filecoin, and is interested in partial retrieval.

## The idea
Package [go-daggregator](https://pkg.go.dev/github.com/filecoin-project/go-dagaggregator-unixfs) into a CLI tool that can read from an IPFS blockstore and aggregate DAGs specified by their CIDs into a Filecoin-compatible .car file with a manifest file compatible with CARv2. Riba estimated this would take a few hours of work for a Go dev.
![example](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/4888ffcc-5df1-456c-9edf-6e84ba47bc13/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210716T053701Z&X-Amz-Expires=86400&X-Amz-Signature=66fdeed9e513a54798faa4b77ce549d8b244f4c209cd0ddbefca3dd5d70c7ab7&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

## Success/acceptance criteria (optional)
_How do we know we're done with this project? How do we know we're successful? This field is OPTIONAL for the first draft of an MPP. Sometimes this field needs to be filled out once we have more detail on the shape of the actual solution._

## Detailed plans (optional)
_Link to more detailed project plans, e.g. product requirements documents (PRDs) and technical design docs, once they have been created for this project._

## Program (optional)
_If this project is part of a program, please indicate the relevant program here._
