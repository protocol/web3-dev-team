# Download migrations over IPFS

Authors: Stebalien

Initial PR: TBD <!-- Reference the PR first proposing this document. Oooh, self-reference! -->

## Purpose &amp; impact 
#### Background &amp; intent
_Describe the desired state of the world after this project? Why does that matter?_

Currently, when the on-disk layout of the datastore changes, go-ipfs will download a "migration"
tool over HTTPS as-needed to "upgrade" the datastore. Unfortunately, this happens over HTTPS so:

1. We're not dogfooding our own tech.
2. It doesn't work in places where https://dist.ipfs.io is blocked (e.g., China).

At the moment, we're unable to ask Brave to update go-ipfs to the latest version because the latest
version will need to download one of these migrations and many of Brave's users are in China.

#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_

- IPFS in Brave needs to matter.
- A significant number of Brave users need to be in China.
- Fetching migrations over IPFS needs to be reliable.

#### User workflow example
_How would a developer or user use this new capability?_

- When starting the go-ipfs daemon with the `--migrate` flag, the migrations would be fetched over IPFS instead of HTTPs.
- When starting the go-ipfs daemon in a bundled application like IPFS Desktop or Brave, the user shouldn't notice anything except that we make no connections to https://ipfs.io when starting go-ipfs the first time after upgrading.

#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

- This would unblock updating go-ipfs in Brave, allowing us to ship bug fixes and new features to Brave users.
- This would prove out IPFS as a way to ship code/updates to users.

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

This is ones step towards our goal of updating go-ipfs itself over IPFS. In terms of knowledge, not much.

#### Confidence
_How sure are we that this is the right problem to tackle? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

3?

- It's a frequent source of upgrade problems: https://github.com/ipfs/ipfs-desktop/issues?q=is%3Aissue+fs-repo-migrations
- It's preventing us from shipping new go-ipfs releases (with important fixes) to brave users.
- It hurts adoption in China.

## Project definition

#### Brief plan of attack

**Design sketch:**

Given a config section like:

```js
{
    "Migration": {
        // Sources in order of preference where "HTTPS" means our gateways and "IPFS" means over IPFS.
        // (an empty list means "do the default thing")
        "DownloadPolicy": ["HTTPS", "custom-gateway.io", "IPFS"],
        // Whether or not to keep the migration after downloading it.
        "Keep": "pin"|"cache"|"discard"
    }
}
```

For the initial version, the default download policy should be `["HTTPS", "IPFS"]` unless the local
node uses private networks (has a swarm key) in which case it should just be `["HTTPS"]` for safety.
As we gain confidence in our ability to reliably download migrations over IPFS, we should make it
the default.

When migrating a repo, until we succeed.

1. If the next source is HTTPS, download from `ipfs.io`.
2. If the source is IPFS:
    1. Create a new _temporary_ repo (go-ipfs can't read the current repo because it's an older version).
    2. Start a new _temporary_ go-ipfs node in the temporary repo.
        a. This node should not listen for inbound connections as it has no way to know which ports/transports should be configured (can't read the config).
        b. This node should not expose an API/gateway.
    3. Download the required migration binaries using the temporary go-ipfs node.
4. Migrate the main go-ipfs node's repo.
5. Start the main go-ipfs node.
6. Maybe store a copy of the migration:
    1. If `Keep` is not "discard", import the migration binary into the main go-ipfs node's repo.
    2. If `Keep` is "pin", pin the migration binary.
7. If running, shutdown any temporary nodes and delete the temporary repo.

**Implementation steps:**

1. Implement everything but step 6.
2. Implement step 6. Unless nodes keep around a copy of the migration, this feature isn't going to be all that useful.
3. Eventually, switch over to using IPFS by default instead of the gateway as the first option.

NOTE: the only reason we're proposing using the gateway first is that the migration blocks startup so it needs to be fast and reliable.

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

1. go-ipfs can download migrations over IPFS (bitswap) without having to contact a centralized server over HTTP.
2. This feature has been tested by multiple labbers (possibly even tested by a subset of ipfs-desktop users).

####  What does success look like?
_Success means impact. How will we know we did the right thing?_

Users can start a new version of go-ipfs that switches to a new repo version without downloading anything from a centralized (easy to block) server.

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

1. We may not be able to download/find the migration on IPFS. Trying the gateway first (or racing) should help mitigate this.
2. The "temporary" node may be missing important parts of the configuration. For example, it may need alternative bootstrap nodes as our nodes may not be reachable. We'll need to think about this carefully and may need to "reach" into the old repo's config file a bit.

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

##### Domain Fronting

A very simple alternative is to simply use domain fronting. If we registered, e.g., ipfs-dist.com and made it an alias for dist.ipfs.io, it _might_ work in China.

However, we'd still be using HTTPS instead of IPFS to download migrations, which seems kind of silly.

##### Bundle the migrations

We could bundle all migrations with go-ipfs. But that would add 100s of megabytes to the go-ipfs distribution so we really don't want to do this.

#### Dependencies/prerequisites

We need to land https://github.com/ipfs/fs-repo-migrations/issues/98 first (in progress).

#### Future opportunities
<!--What future projects/opportunities could this project enable?-->

This is a step towards self-bootstrapped, decentralized IPFS. The remaining parts are:

1. Updating go-ipfs itself over IPFS.
2. Decentralized bootstrapping (reducing reliance on our central bootstrap nodes).

## Required resources

#### Effort estimate
<!--T-shirt size rating of the size of the project. If the project might require external collaborators/teams, please note in the roles/skills section below). 
For a team of 3-5 people with the appropriate skills:
- Small, 1-2 weeks
- Medium, 3-5 weeks
- Large, 6-10 weeks
- XLarge, >10 weeks
Describe any choices and uncertainty in this scope estimate. (E.g. Uncertainty in the scope until design work is complete, low uncertainty in execution thereafter.)
-->

In terms of implementation, Small. But the testing/validation could take a variable amount of time.

#### Roles / skills needed

* Familiarity with go-ipfs, and the go-ipfs repo.
* Ideally, familiarity with go-ipfs repo migrations.

The datasystems team would be the best fit.
