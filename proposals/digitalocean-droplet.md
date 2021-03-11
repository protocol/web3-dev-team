# "One-Click" for running Lotus on DigitalOcean

Authors: johndmulhausen

Initial PR: #63

## Purpose &amp; impact
#### Background &amp; intent

Ship one-click machine image for Lotus nodes so that it is easy to get started, and bake-in some state downloading so we can jumpstart the sync process. 

#### Assumptions &amp; hypotheses

We believe being able to deploy Lotus nodes with a single click will significantly reduce startup friction. The proposed image will download a `.car` file from an S3 bucket with a usable chain state, which should complete about 20 minutes after the one-click is fired up, rather than taking days. 

#### User workflow example

User is linked to marketplace.digitalocean.com URL from the docs, then they click "Create" to fire up a Lotus node on their DigitalOcean account. After making a couple selections about the machine they'd like to run the software on, it is created with Lotus installed, and a script fires to download the .car file. Shortly afterwards (ETA 20 minutes) the node is live.

#### Impact

🔥🔥🔥

This is a huge pain point now, we're reducing the number of steps significantly and the startup time is reduced to a fraction of the original.

#### Confidence

High

## Project definition
#### Brief plan of attack

- Create Image
- Create Vendor account w/DigitalOcean
- Work w/Marketplace team to make sure image scans are clean
- Ship!

#### What does done look like?

Marketplace URL is live.

####  What does success look like?

We can point to a startup process that takes less than a half hour rather than days.

#### Counterpoints &amp; pre-mortem

TBD

#### Alternatives

TBD

#### Dependencies/prerequisites

TBD

#### Future opportunities

TBD

## Required resources

#### Effort estimate

- Medium: Days

#### Roles / skills needed

- Ops/dev (image creation)
- Tech Writer (documentation, image submission)
