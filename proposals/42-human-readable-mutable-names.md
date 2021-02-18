# Reliable and extensible resolution of human-readable mutable names

Authors: @lidel

Initial PR: https://github.com/protocol/web3-dev-team/pull/42 <!-- Reference the PR first proposing this document. Oooh, self-reference! -->
## Purpose &amp; impact 

Improve the way mutable names work in our stack.

- Empower developers with reliable mechanisms for publishing updates
  - Make IPNS useful on its own, and inside of DNSLink records
  - Future-proof the way we do human readable names via DNS interop

#### Background &amp; intent
_Describe the desired state of the world after this project? Why does that matter?_
<!--
Outline the status quo, including any relevant context on the problem you’re seeing that this project should solve. Wherever possible, include pains or problems that you’ve seen users experience to help motivate why solving this problem works towards top-line objectives. 
-->

We see CID, IPNS record, and DNSLink being de-facto standard for cryptographically-verifiable content-addressing and human-readable names on the distributed web. 

There are three distinct types of addresses:
  - immutable content:  `/ipfs/{cid}`
  - mutable content
      - cryptographic, IPNS record signed with a specific libp2p key: `/ipns/{libp2p-key-cid}` 
      - human-readable, [DNSLink](https://dnslink.io): `/ipns/{dns-name}`
        (which in turn, resolves to either an immutable or mutable content path from DNS TXT record)


**There are known gaps in the mutable story:**
- IPNS records are only published by the original author, which severely limits the utility of our mutable names
    - It is not possible to pin/republish `/ipns/{libp2p-key-cid}` names by other peers, so when original publisher disappears, IPNS links no longer resolve and we see "IPNS rot". 
    - **Due to IPNS rot people simply don't use it:**
        - Instead publishing updates via `ipfs name publish {cid}`, website operators choose to constantly update DNSLink's DNS TXT record
            - They point at reliable immutable paths (`dnslink=/ipfs/{cid}`) (no IPNS record means it resolves fast and never break).
            - It works around the need for running a service responsible for constant republishing of IPNS record.
            - This is a pragmatic choice, however:
              - adds admin related to DNS updates (need to learn DNS provider's API for automating this, which introduces soft vendor-lock-in)
              - most likely not the best choice for security-sensitive use cases where human-readable names are not required: means DNS is used in contexts where cryptographic addressing should be used instead.
- **OS-level DNS resolver is used for all DNS TXT record lookups.** 
  - IPFS node is unable to control which DNS resolver is used for specific TLD, all queries go to global DNS server configured in the operating system
    - This harms competition and slows down innovation in the decentralized naming space. For example, if user changes their DNS resolver to one that is capable of resolving all TLDs over ENS, they are unable to resolve TLDs from OpenNIC or UnstoppableDomains. 
  - Given how DNS is implemented in OS and ISPs, queries are most likely sent in plain text and can be spoofed in LAN or MITMd at the ISP level. At the time of writing this proposal DNS over HTTPS is not supported, and it is not trivial for regular user to set up a custom DNS server to change this behavior.

**TLDR:** **We need to fix and future-proof the way mutable names work in our stack:**
- Make IPNS useful on its own, and inside of DNSLink records.
    - DNS TXT record should be set only once, updates should be published over IPNS.
- Future-proof the way we do human readable names by
    - leveraging DNS protocol (not the DNS network run by ICANN) for interop with existing and future user agents and naming systems
    - allowing flexible configuration to improve security (DoH) and interop (DNSLink)



#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->

- Browser is the  main distribution channel for dapps.
- Dapps are simply a subset of all static websites loaded from IPFS.
- Most of websites hosted on IPFS have DNSLink set up for human-readable name.
- We have mainstream browsers like Opera and [Brave](https://brave.com/ipfs-support/) ship support for `ipfs://` and `ipns://` URIs. 
    - Human readable names like `ipns://en.wikipedia-on-ipfs.org` work thanks to DNSLink
    - This removes huge UX friction for dapp developers. 
    - Vendors like Brave are committed to [surfacing DNSLink supportin the UI](https://github.com/brave/brave-browser/issues/13609) which will improve onboarding even further.
- Alternatives to [ICANN](https://en.wikipedia.org/wiki/ICANN)  exist, and we want them to work with our stack to decrease dependency on a single organization.
    - [ENS](https://ens.domains) provides custom TLDs (`.eth`) and leverage DNSLink for interop with IPFS and delegated lookups with clients that are unable to run own blockchain resolver.
        - Updating `ipfs-ns` `contenthash` is a chore and costs extra (gas etc). 
        - Using `ipns-ns` means setting `contenthash` only once, introduces cost savings and simplifies publishing. 
    - We see multiple actors in the space providing either own TLDs or attempting to replace ICANN as the top-level authority: https://unstoppabledomains.com , http://opennic.org, https://handshake.org etc.
    - We want to enable innovation in the decentralized naming space. This means removing ourselves as gatekeepers of what a valid domain name is.
    - When embedded in user agent (Brave) we want to follow user choices regarding DNS resolution.
    



#### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->

- Improving human-readable naming removes huge DX/UX friction for dapp users and developers. 
    - Messaging collapses to "Install Brave or Opera and open ipns://example.com"
    - They use IPNS for publishing updates without ever touching DNS/ENS etc beyond initial setup. Most likely save money on gas and/or admin time.
    - One-liner for setting up a custom DNSLink resolver improves onboarding for naming systems not supported by default and enables vendors like Brave to provide UI for changing resolution settings in more user-friendly manner.


#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

<!--
Explain how this addresses known challenges or opportunities.
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

- IPNS provides a reliable solution for  cryptographically-verifiable mutable names that won't break, as long someone is re-publishing the latest record.
    - Just Works (TM)
    - There is no PKI, no centralization, full transparency and ownership.
- DNSLink provides interop for human-readable names and enables independence from PKI and ICANN.
    - Just Works (TM)
    - No vendor-specific client is included. 
    - No proprietary APIs or formats. RFC-compliant DNS only.
    - We promote competition, letting the best solution win.
    - User agency is respected. 


#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

<!--
Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->


- Brave wants to support alternatives to ICANN  out of the box. 
    - By having resolver configurable per TLD namespace, we will be able to integrate with their resolution logic, providing seamless experience on `ipns://` out-of-the-box 
- Every new project can experiment with IPFS via DNSLink integration without our involvement.
    - We no longer need to say "no" just to keep our code base small or worry about optics of "picking winners and losers".
- Fixing IPNS rot would enable use of `dnslink=/ipns/{libp2p-key-cid}`
    - Improved UX because DNS record needs to be set only once
    - Reduced cost for blockchain-based alternatives to ICANN (like ENS), owner uses IPNS for publishing updates, saving on gas.

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

Medium.

<!--Explain why this rating-->

- After five years we see DNSLink being the only viable solution for human-readable names. 
    - ENS works out of the box on every IPFS Gateway and in Brave thanks to DNSLink interop.
    - Cloudflare embraced DNSlink years ago, and they took over [the eth.link ENS resolver/gateway](https://blog.cloudflare.com/cloudflare-distributed-web-resolver/).
    - `ipns://` in address bar of Brave is an extremely powerful visual and a confidence booster about entire stack
- We see alternatives to ENS popping up, but enabling them requires changes to our code bases and is not a trivial task.
- Unfortunately, `dnslink=/ipns/` is a rare sight, due to IPNS rot, and people default to DNSLink even in cases where use of cryptographic identifiers would be a better choice.

## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

- Tackle IPNS and DNS fixes in parallel, in both Go and JS
- Introduce configurable DNS resolver per TLD while adding DNS over HTTPS support to entire stack

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

- DNS over HTTPS is supported in js/go-ipfs/libp2p
    - User agency around DNS is respected: every code path doing a DNS lookup (resolving DNSLink, `/dnsaddr`, `/dns*` multiaddrs) should use either explicit or implicit DNS resolvers defined in IPFS node configuration file.
      - By default OS-level DNS resolver is used as catch-all, but the user can delegate resolution of all or specific TLDs to specific DoH resolvers.
      - Node tries to resolve with the most specific resolver (if present for TLD), and then fall back to the global one.
    - Visual Aid / config mock-up
      ```json
        "DNS": {
          "Resolvers": {
            "*.eth": "https://eth.link-or-cloudflare/path/to/dns-query",
            "*.crypto": "https://unstoppablesomething.example.com/path/to/dns-query",
            "*.libre": "https://www.opennic.org/path/to/their/dns-query", 
            "*": "https://mozilla.cloudflare-dns.com/dns-query"
          }
        }
      ```
- DNSLink provides interop for human-readable names and enables independence from PKI and ICANN.
    - Anyone can set up and run own naming system without our involvement, blessing or endorsement.
    - No vendor-specific client is included. 
- IPNS provides a reliable solution for cryptographically-verifiable mutable names that won't break, as long someone is re-publishing the latest record.
    - IPNS re-publishing works seamlessly, out of the box, just like providing CIDs for blocks in local datastore (pinned or not).
    - It is possible to pin IPNS address to keep it around and ensure it resolves even when original publisher is gone.
        - Node follows IPNS record updates and keeps re-publishing latest one if original author disappears.
        - Node follows content updates behind the IPNS record, and update content pin every time IPNS record changes. 
            - It is possible to opt-out from this behavior to re-publish IPNS record for `en.wikipedia-on-ipfs.org` without pinning all the data.


####  What does success look like?
_Success means impact. How will we know we did the right thing?_

<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

- We see % of `dnslink=/ipns/` going up.
- We see more IPNS records on DHT
- We no longer see requests for supporting new naming systems.

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_
 
- Configurable per TLDs [DNS over HTTPS](https://en.wikipedia.org/wiki/DNS_over_HTTPS) resolver for  may be not enough to mitigate concerns around centralized nature of ICANN's DNS.
- IPNS may have other problems that block it from practical use in DNSLink records (eg. resolution still taking way longer than immutable path, making initial page load slow).

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

- Deprecate IPNS.
- Announce ENS being the official solution for DNS names and replace every DNS lookup to go via ENS.
- Do nothing and pay the opportunity cost when a better alternative to ENS appears but can't be used with DNSLink due to non-ICANN TLDs.

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

- DNS over HTTPS support in go/js-ipfs and go-/js-libp2p
- IPNS record republishing/pinning


#### Future opportunities
<!--What future projects/opportunities could this project enable?-->

- Dev grants / collabs with  various naming projects to provide DNSLink gateway (similar to https://eth.link) and DNS over HTTPS endpoint for resolving them securely, including JS in browsers.
    - Supporting competition, providing venue for rapid adoption and user onboarding, seeing what sticks.
- P2P swarm resolvers and quorum acceptance criteria 
    - We should look into a way to harden DNS resolution without introducing any dependency on any complex public PKI (DNSLink should not require DNSSEC).
    - Instead of delegating DNS lookup to some DoH endpoint, leverage swarm of peers to increase trust in DNS lookup results.
        - Ask a subset of peers (from different networks, jurisdictions etc) to resolve name for you, and pick record passing some quorum criteria.
- Pinning Services support for IPNS pinning
    - Follow IPNS record, ensure latest data is pinned, keep last-seen IPNS record available.

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

- Medium: 1-3 weeks design/prototyping, 1-2 weeks implementation

#### Roles / skills needed
<!--Describe the knowledge/skill-sets and team that are needed for this project (e.g. PM, docs, protocol or library expertise, design expertise, etc.). If this project could be externalized to the community or a team outside PL's direct employment, please note that here.-->

- js-ipfs/libp2p dev
- go-ipfs/libp2p dev
- DNSlink / DNS / DoH expertise
- IPNS / DHT expertise
