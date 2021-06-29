# libp2p Protocol Select

Authors: @marten-seemann and @mxinden <!-- List authors' GitHub or other handles -->

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

### Context and status quo

Today on a new connection or stream, two [libp2p] nodes use the
[multistream-select 1.0] protocol to negotiate the protocol to be used on said
connection or stream. For example on a given TCP connection two libp2p nodes
might negotiate the [Noise] security protocol, followed by negotiating the
[Yamux] multiplexing protocol. On a given stream two nodes might negotiate the
[Identify] protocol.

### Problems

- **Downgrade attacks** and **censorship resistance**: Given that
  [multistream-select 1.0] negotiates a connection's security protocol
  unencrypted and unauthenticated it is prone to [downgrade attack]s. In
  addition, a man-in-the-middle can detect that a given connection is used
  to carry libp2p traffic, allowing attackers to censor such connections.

- **Connection Establishment**: In addition to making us vulnerable to downgrade
  attacks, negotiating the security protocol takes one round-trip in the common
  case. On top of that negotiating a stream multiplexer (on TCP) takes another
  round-trip.

- **Plaintext**: The [multistream-select 1.0] protocol is defined as a plaintext
  protocol with no strict schema definition, making both implementation and
  protocol evolution time consuming and error-prone. See [rust-libp2p/1795]
  showcasing complexity for implementors and [specs/196] to showcase difficulty
  evolving protocol.

- **Bandwidth**: [multistream-select 1.0] is not as bandwidth efficient as it
  could be. For example negotiating a protocol requires sending the protocol
  name back and forth. For human readability protocol names are usually long
  strings (e.g. `/ipfs/kad/1.0.0`).


### Affected users

Given that [multistream-select 1.0] is a core libp2p protocol, all libp2p users
are affected by at least some of the problems mentioned above. Those users
include all IPFS users and all Filecoin users.

## Impact
_What goals/OKRs are being addressed (for w3dt, a specific program, etc.)? Why is this project important? What do we get with this project that we can't get without it?_

Protocol negotiation is at the heart of libp2p. Thus any changes to libp2p's way
of negotiating protocols affects all projects building on top of libp2p (e.g.
IPFS and Filecoin). With that in mind, fixing the problems listed above by
designing and implementing a successor to [multistream-select 1.0], namely
_Protocol Select_, will improve efficiency (see *roundtrips* and *bandwidth*),
long-term stability (see *plaintext*) and security (see *downgrade attacks* and
*censorship resistance*) across the interplanetary stack and beyond.

## The idea
_Describe the proposed project solution, at a very high level. Stay at the level of the high-level requirements. Diagrams and interface descriptions can be useful, if you have any that help clarify and explain the idea._

The idea of this project is to design and implement a successor to
[multistream-select 1.0], namely _Protocol Select_ which addresses the problems
listed above. While the concrete details of the protocol are yet to be designed,
we set the following high-level goals:

- A simple protocol, easy to extend and evolve in the future.

- Support for TCP simultaneous-open (see [specs/196]).

- [Downgrade attack] defense as well as prevention of machines-in-the-middle
  detecting connection as libp2p conection for minimal censorship resistance.

- Security protocols should be advertised, thereby eliminating the need for
  negotiating them.

- For optimized implementations, stream muxer negotiation will take zero round-trips
  for the client (depending on the details of the cyrptographic handshake protocol).
  In that case, the client will be able to immediately open a stream after completing
  the handshake.

- Zero-round-trip stream protocol negotiating for optimistic
  single protocol negotiation.

- Binary data format defined in a machine parseable schema language allowing
  protocol evolution at the schema level.

- The option to improve bandwidth efficiency e.g. around protocol names in the
  future. While _Protocol Select_ might not solve this in the first iteration,
  the protocol should be designed with this optimization in mind, and allow for
  a smooth upgrade in a future iteration.

## Success/acceptance criteria (optional)
_How do we know we're done with this project? How do we know we're successful? This field is OPTIONAL for the first draft of an MPP. Sometimes this field needs to be filled out once we have more detail on the shape of the actual solution._

- A detailed protocol specification is merged into [libp2p/specs]. The
  specification allows anyone to build a compatible implementation without
  having to read other implementation's source code.

- The above specification is implemented and released for two libp2p
  implementations (e.g. go-libp2p and rust-libp2p). The two _Protocol Select_
  implementations have been tested for interoperability.
  
- _Protocol Select_ has been rolled out on a live network (e.g. IPFS or
  Filecoin).

## Detailed plans (optional)
_Link to more detailed project plans, e.g. product requirements documents (PRDs) and technical design docs, once they have been created for this project._

### Previous attempts

This is not the first attempt at replacing [multistream-select 1.0]. References
to previous attempts:

- https://github.com/libp2p/specs/pull/95/
- https://github.com/libp2p/specs/pull/205/
- https://github.com/libp2p/specs/pull/227/

### Project plan draft

1. Write minimal specification based on high-level requirements.
2. Open up for review.
3. Incorporate feedback in specification. If none, go to (6)
4. Once feasable, write / adjust reference implementation.
5. Go back to (2).
6. Merge specification as `Working Draft`.
7. Write second implementation, test compatibiliity and roll out on test
   network.
8. Release implementations, promote specification to `Candidate Recommendation`
   and roll out on live network.

## Program (optional)
_If this project is part of a program, please indicate the relevant program here._

This project is not part of a program.

[libp2p]: https://github.com/libp2p/specs/
[multistream-select 1.0]: https://github.com/libp2p/specs/blob/f36e36371ab16579b7dedf26f6dc3966567fd194/connections/README.md#multistream-select
[Noise]: https://github.com/libp2p/specs/blob/313b9a1ca67cba1443ccd32ee3c037684661a357/noise/README.md
[Yamux]: https://github.com/hashicorp/yamux/blob/3d6f54d66fc83411743d3421f7a84a7d348f071c/spec.md
[Identify]: https://github.com/libp2p/specs/blob/f922a3e4ff6f0166b78c21c3b869279474577d81/identify/README.md
[go-multistream/20]: https://github.com/multiformats/go-multistream/issues/20
[rust-libp2p/1855]: https://github.com/libp2p/rust-libp2p/pull/1855
[downgrade attack]: https://en.wikipedia.org/wiki/Downgrade_attack
[rust-libp2p/1795]: https://github.com/libp2p/rust-libp2p/issues/1795
[specs/196]: https://github.com/libp2p/specs/pull/196
[libp2p/specs]: https://github.com/libp2p/specs/
