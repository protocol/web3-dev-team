# Configurable DNS resolvers for human-readable mutable names

Authors: @lidel

Initial PR: https://github.com/protocol/web3-dev-team/pull/42 <!-- Reference the PR first proposing this document. Oooh, self-reference! -->
## Purpose &amp; impact 

Improve the way mutable names work in our stack.

- Empower developers with reliable primitive for publishing updates on human-readable names
- Future-proof the way we do human readable names via DNS interop
- Reduce privacy risks related to DNS leaks  in plaintext 

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
    - This is out of the scope of this proposal, for IPNS improvements see [Proposal #19: Proposal: Reliable Mutability Primitive](https://github.com/protocol/web3-dev-team/pull/19)
- Future-proof the way we do human readable names by
    - leveraging DNS protocol (not the DNS network run by ICANN) for interop with existing and future user agents and naming systems
    - allowing flexible configuration to improve security (DoH) and interop (DNSLink)




#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_
<!--(bullet list)-->

- **NFTs require dedicated, user-friendly dapps .**
- Browser is the  main distribution channel for dapps and NFTs.
- **Dapps are simply a subset of all static websites loaded from IPFS.**
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
    - Brave is looking into using DNS over HTTPS to resolve DNSLin for  non-ICANN TLDs like ENS (resolve `*.eth` via `https://eth.link/dns-query` etc)
    - We want to enable innovation in the decentralized naming space. This means removing ourselves as gatekeepers of what a valid domain name is.
    - When embedded in user agent (Brave) we want to follow user choices regarding DNS resolution.
    



#### User workflow example
_How would a developer or user use this new capability?_
<!--(short paragraph)-->

- Opening `ipns://mydapp.tld` "just works" in Brave
- go-ipfs ships with implicit resolvers for non-ICANN naming systems (where feasible)
    - OS-level resolver as the default
    - https://eth.link/dns-query for `*.eth`
    - TBD for UnstoppableDomains 
- User or user agent is able to override implicit resolver for all or specific TLDs
    - use encrypted DoH resolver for all DNS lookups
      (eg. for privacy reasons,  or lack of trust for OS-level resolver from ISP)
    - run local Ethereum client and set up IPNS node to resolve ENS natively via localhost resolver (removing the need for trusting eth.link)




#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

<!--
Explain how this addresses known challenges or opportunities.
What awesome potential impact/outcomes/results will we see if we nail this project?
-->

- Human-readable naming removes huge DX/UX friction for multiple  stakeholders:
  - Dapp developers can focus on dev instead of onboarding story
    - Dapp marketing/onboarding collapses to:
      > Install Brave or Opera and open ipns://mydapp.eth
  - Alternative naming systems have way lower barier of entry
    - Interop story with the old web and the entire IPFS ecosystem collapses to "repeat https://eth.link story":
      > Expose DNS endpoint that returns A (gateway) and TXT (DNSLink) records
    - One-liner for setting up a custom DNSLink resolver for specific TLD removes adoption barriers and improves onboarding for new naming systems, as those are no longer blocked by the lack of IPFS stewards blessing.
  - Browser vendors have more confidence in running IPFS node
    - Vendors like Brave are able to provide unified UI for changing name resolution settings in a single place, without fear that IPFS node will ignore user's choice and be responsible for any privacy leaks
    - IPFS involvement is no longer needed when browser vendor wants to support new naming system




#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

<!--
Explain the opportunity or leverage point for our subsequent velocity/impact (e.g. by speeding up development, enabling more contributors, etc)
-->

- NFT dapp developers need marketable names and a clear user onboarding story.
- Brave wants to support alternatives to ICANN  out of the box. 
    - By having resolver configurable per TLD namespace, we will be able to integrate with their resolution logic, providing seamless experience on `ipns://` out-of-the-box, acting as a template for others vendors who want to follow.
- Every new project can experiment with IPFS via DNSLink integration without our involvement.
    - We no longer need to say "no" just to keep our code base small or worry about optics of "picking winners and losers".
- DNSLink provides interop for human-readable names and enables independence from PKI and ICANN.
    - Just Works (TM)
    - No vendor-specific client is included. 
    - No proprietary APIs or formats. RFC-compliant DNS only.
    - We promote competition, letting the best solution win.
    - User agency is respected. 



#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

Medium.

<!--Explain why this rating-->

- After five years we see DNSLink being the only viable solution for human-readable names. 
    - ENS works out of the box on every IPFS Gateway and in Brave thanks to DNSLink interop.
    - Cloudflare embraced DNSlink years ago, and they took over [the eth.link ENS resolver/gateway](https://blog.cloudflare.com/cloudflare-distributed-web-resolver/).
    - `ipns://` in address bar of Brave is an extremely powerful visual and a confidence booster about entire stack
- We see alternatives to ENS popping up, but enabling them requires changes to our code bases and is not a trivial task.
- Brave confirmed they will use DNS over HTTPS and expects go-ipfs to provide configuration option per TLD.

## Project definition
#### Brief plan of attack

<!--Briefly describe the milestones/steps/work needed for this project-->

- Adding DNS over HTTPS support to entire stack
- Make if possible to configura different DNS resolver per TLD
- Decide on short list of mature systems that don't collide with ICANN TLDs and can be included as implicit defaults

#### What does done look like?
_What specific deliverables should completed to consider this project done?_

- DNS over HTTPS is supported in js/go-ipfs/libp2p
    - User agency around DNS is respected: every code path doing a DNS lookup (resolving DNSLink, `/dnsaddr`, `/dns*` multiaddrs) should use either explicit or implicit DNS resolvers defined in  configuration file / constructor params.
      - By default OS-level DNS resolver is used as catch-all, but the user can delegate resolution of all or specific TLDs to specific DoH resolvers.
      - Node tries to resolve with the most specific resolver (if present for TLD), and then fall back to the global one.
    - Visual Aid: a config mock-up for go-ipfs
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
- DNSLink provides interop for human-readable names and enables independence from ICANN.
    - Anyone can set up and run own naming system without our involvement, blessing or endorsement.
    - No vendor-specific client is included. 


####  What does success look like?
_Success means impact. How will we know we did the right thing?_

<!--
Provide success criteria. These might include particular metrics, desired changes in the types of bug reports being filed, desired changes in qualitative user feedback (measured via surveys, etc), etc.
-->

- Brave ships support for more than one alternative TLD backed by local IPFS node
- We see % of requests to non-ICANN TLDs going up (Brave / dweb.link)
- We no longer see requests for supporting new naming systems 
- We no longer see issues filled about our stack leaking DNS names in plaintext

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_
 
- Mainstream browser vendors may decide supporting alternative TLDs is not worth future headache when ICANN decides to sell same name.
- Per TLDs [DNS over HTTPS](https://en.wikipedia.org/wiki/DNS_over_HTTPS) resolver may be not enough to mitigate concerns around centralized nature of ICANN's DNS, namely most of users or user agents  pointing their nodes at DoH endpoint from Google or Cloudflare.
- This is necessary gruntwork, but we may not see DNSLink adoption going up until we provide truly decentralized solution (see Future opportunities).


#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

- Deprecate IPNS.
- Announce ENS being the official solution for DNS names and replace every DNS lookup to go via ENS.
- Do nothing and pay the opportunity cost when a better alternative to ENS appears but can't be used with DNSLink due to non-ICANN TLDs.

#### Dependencies/prerequisites
<!--List any other projects that are dependencies/prerequisites for this project that is being pitched.-->

- Remove hardcoding of `.eth` → `.eth.link`  from go-ipfs
- DNS over HTTPS support in go/js-ipfs and go-/js-libp2p


#### Future opportunities
<!--What future projects/opportunities could this project enable?-->

- User agents like Brave looking into deeper integration of IPFS into their UI and network stack
    - Every Dapp with DNSLink could get [Open from IPFS](https://github.com/brave/brave-browser/issues/13609) badge etc
- Collaborations with various naming projects to provide DNSLink gateway (similar to https://eth.link) and DNS over HTTPS endpoint for resolving them securely in user agents and JS in browsers.
    - Supporting competition, providing venue for rapid adoption and user onboarding, seeing what sticks.
- Implement [content routing hint via DNS records](https://github.com/ipfs/go-ipfs/issues/6516) and act on it with more confidence
- Look into replacing semi-centralized DoH endpoints with P2P swarm resolvers and quorum acceptance criteria 
    - We should look into a way to harden DNS resolution without introducing any dependency on any complex public PKI (DNSLink should not require DNSSEC).
    - Instead of delegating DNS lookup to some DoH endpoint, leverage swarm of peers to increase trust in DNS lookup results.
      - Ask a subset of peers (from different networks, jurisdictions etc) to resolve name for you, and pick record passing some quorum criteria.
- End-to-end website publishing and persistence with our stack
    - Pinning Services support for DNSLink update as part of pinning
    - Updating CID for a pin named `mysite.example.eth`  triggers DNSlink update (or IPNS update)
- Leveraging DNSLink for petnames in private swarms


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
