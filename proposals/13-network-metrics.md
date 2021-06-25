# Project Pitch: Protocol Metric Tracking

Authors: @willscott

## Purpose &amp; impact 
#### Background &amp; intent

We have a range of options for getting insight into the health of various protocols stewarded by Protocol Labs. This includes https://ecosystem-dashboard.com a range of DHT crawlers, and logs from gateways among others.

We lack however two important pieces of visibility:
We do not have a way for a developer using our networks to get visibility or insight into users of their software.
We do not have the ability to answer deeper analytical questions about the dynamics of our network: what is the churn rate of nodes? Are there issues with latency and connectivity to China? How many of the new users we’re seeing are from Brave?

#### Assumptions &amp; hypotheses

* These metrics are important
Having this data allows us to make more informed decisions about prioritization
* Developers will expect visibility into their user base
We will regret not having historic data

#### User workflow example

Dapp developer makes a new libp2p based app. Sees thousands of downloads, but struggles to provide 30 day active user metrics. Developer complains they don’t have insight into their user base and adds centralized metrics like google analytics.

#### Impact

🔥🔥

Useful tooling for developers, and useful for us.

#### Leverage

🎯🎯 

Faster surfacing of potential issues and pain points.

#### Confidence

1 - low / anecdotal. Haven’t directly heard the need from many developers.


## Project definition
#### Brief plan of attack

There are a few subcomponents that make up this project:
* Get to a more useful user agent view of users in libp2p identification. Currently it’s difficult to do segmentation of ipfs users by supported protocols, and an additional extension of tags to allow self-identification when e.g. embedded in brave would be useful.
* Extend data collection, currently really only shows DHT server makeup, to also provide some view into clients - either by watching for requests that organically come in and seeing who made them, or via data from gateways or other current crutches.
* Build out an analysis pipeline. In MVP likely surfacing additional data to grafana, depending on developer feedback potentially extending to either allow self-service dashboard creation or custom interface.

#### What does done look like?

* We have metrics for top 3 requested metrics
* We have a place to point too for current metrics of live network and know which apps are doing well.

#### What does success look like?

Developers don’t instrument their dapps with google analytics

#### Counterpoints &amp; pre-mortem

Knowing one app is doing well while another isn’t doesn’t tell us ‘why’, so qualitative input is still needed, and be more important for our prioritization

#### Alternatives

* Developers continue to add external centralized instrumentation to their apps.
* We make one-off dht / other crawlers for specific things we care about
* We continue to not have a particularly great segmentation of which apps make up the libp2p mesh

#### Dependencies/prerequisites

* Come to consensus on how ‘user agent’ will be visible within the network to allow apps building on go-ipfs to be differentiated.

#### Future opportunities

Permissioned developer dashboard providing additional insight into their user base.

## Required resources
#### Effort estimate

Implementation / consensus of user agents visible in network - 1-2 weeks / small
Analysis / from-data-collection-to-dashboard - 4-6 weeks / medium

#### Roles / skills needed

* SWE - write analysis pipeline / ipfs+libp2p changes
* PM - figure out most important metrics
* Fullstack - dashboard view
