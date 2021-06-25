# Extended Blockstore Interface

Authors: vyzo

## What is the problem this project solves?

We currently have a limited "dumb" blockstore interface, which does not allow us to pass context options so as to inform the blockstore about certain properties of objects being stored.

This is particularly important in the context of the splitstore, where we have the following problems:
- We lack the ability to inform the splitstore of the actual epoch an object belongs, which requires us to "guess" by estimating based on the current tipset and wall clock (see [#6474](https://github.com/filecoin-project/lotus/pull/6474)). This is problematic for many reasons, as an object might be misassigned its epoch (and thus become completely broken during catch-up sync in current master).
- We lack the ability to inform the splitstore when an access is initiated from the network. In conjunction with the transactional gc logic in [#6474](https://github.com/filecoin-project/lotus/pull/6474) this would result in network requests keeping objects that would otherwise be pruged from the hotstore live.
This is both a performance/gc issue (the hotstore is larger than it needs to be) but it is also a potential attack vector for nodes that need to run with fixed hardware (e.g. network boosters).
- We lack the ability to inform the splitstore that certain objects should be reified from cold storage to hot storage. For instance, a miner doing tipset state computation in an older tipset may want to keep this in the hot storage. It also means that misses result in permanent banishment in the coldstore and makes it hard to gc by simply removing the coldstore.

## Impact

This will make the splitstore a much more reliable component, working towards making it the default blockstore in lotus.

## The idea

Extend the blockstore interface so as to accept an `Options` struct, which specifies the necessary context constraints.

Methods would look like this:
```
type Blockstore interface {
  ...
  Get(c cid.Cid, opts Options) (blocks.Block, error)
  ...
}
```

We may want to name the new option accepting methods with an `WithOptions` suffix if we want to keep backwards compatibility in the interface.

Note: The reason for using a flat `Options` struct, as opposed to a `context.Context` object or functional options is purely performance. The latter options can have quite a bit of overhead, which we want to eliminate.


## Success/acceptance criteria (optional)

lotus has been updated to define and use the new interface, with proper options assigned in call sites.

## Detailed plans (optional)

## Program (optional)
`lotus` for the win!
