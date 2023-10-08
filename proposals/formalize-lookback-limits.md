# Formalize lookback limits

Authors: vyzo

## What is the problem this project solves?

There is no lookback limit enforced in code for how far back we can refer in the chain, e.g. for randomness lookback.
This makes it *impossible* to run a node with fixed hardware requirements, as the datastore will grow indefinitely even with a splitstore configured with a noop coldstore.
This impacts our ability to run network boosters.

## Impact

A real, code enforced maximum lookback will be defined, thus allowing us to comfortably run nodes with fixed hardware.

Note: This is consensus breaking, so it must happen in a network upgrade.

## The idea

Define a maximum lookback and enforce it in actos code.

Note that there is an _effective_ limit of 30 days in hyperdrive, but
we can't rely on it in production code as an attacker would simply
send a crafted object that performs arbitrary chain lookback and brign
down a booster.

## Success/acceptance criteria (optional)

## Detailed plans (optional)

## Program (optional)
