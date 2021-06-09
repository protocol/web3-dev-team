# IPFS blog enhancements

Author: @jessicaschilling

Initial PR: https://github.com/protocol/web3-dev-team/pull/74

Larger-scale proposal for overall ipfs.io work, including this effort: https://github.com/protocol/web3-dev-team/blob/ipfsio-modular-rework/proposals/ipfsio-modular-rework.md

Project tracking board for overall ipfs.io work: https://github.com/orgs/ipfs/projects/11
Repo for the new blog: http://github.com/ipfs/ipfs-blog

## Purpose &amp; impact
#### Background &amp; intent
_Describe the desired state of the world after this project? Why does that matter?_

Prospective and current IPFS and w3dt developers have a “one-stop shop” for up-to-date IPFS info that can be easily filtered and searched to meet the specific needs of a wide variety of audiences (technical users, newcomers, etc) as well as to optimize cross-item discovery, metrics collection, and inbound SEO. Primary content focus is on our (already frequently updated) blog posts, but includes a mix of other relevant content in a manner that surfaces relevant info without creating an ongoing maintenance burden on our core team. This front-end presentation is matched on the back end by a Markdown-driven content rendering engine that significantly reduces friction for post authors/editors, as well as a content submission form accessible by the public and easily managed by administrators.

#### Assumptions &amp; hypotheses
_What must be true for this project to matter?_

✓ Our blog is a valuable source of content for prospective and current devs

✓ Those audiences would also benefit from single-source access to other IPFS-related content: news stories, release notes, tutorials, videos, academic papers, event listings, etc

✓ Not having search or tagging on blog posts is a missed opportunity, both for our readers and for our metrics collection

✓ We can use readership metrics to better understand our audience and PMF in general

✓ Labbers would significantly benefit from an easier post-authorship process and smoother deployments

#### User workflow example
_How would a developer or user use this new capability?_

Reader:
- Visits the blog, either directly or via shared link, search, etc
- Explores additional content beyond the page they originally visited thanks to text search, content type filter, tag cross-discovery, author cross-discovery, etc
- Engages with content (comments on a blog post, shares an item organically or through social-share links, etc)
- Submits content (news link, event, etc) through submission form
- Subscribes to newsletter through direct submission fields in site footer

Post author/editor:
- Drafts content in easy-to-use, WYSIWYG-enabled Forestry CMS
- Uploads images in correctly sized dimensions through Forestry and our custom image scale/crop tool
- Sees instant previews of their work within Forestry
- PRs the Forestry staging environment to prod for approval and easy Fleek-based deployment

#### Impact
_How would this directly contribute to web3 dev stack product-market fit?_

Improving our front-of-the-funnel comms and educational resources, such as the IPFS blog, directly enables early-stage education, exploration and onboarding. Additionally, providing a "one-stop shop" for news, tutorials, videos, events and similar resources ensure that our websites are positioned as a complete, reputable source of information — furthering our trust profile, increasing SEO and site traffic, and generally increasing the size of the funnel as a whole.

Reducing friction for blog authors and maintainers also enables us to increase our overall comms velocity and efficiency, enabling us to create faster, better content — and avoid wasting resources that could better be repurposed to other PMF efforts.

#### Leverage
_How much would nailing this project improve our knowledge and ability to execute future projects?_

This work lays the foundation for future improvements to ipfs.io as a whole, particularly in terms of overall IA of header, footer, nav and other "furniture" — a lot of work will already have been done! Replatforming the blog also brings us the opportunity to collect more complete metrics on front-of-the-funnel visitor priorities and patterns, giving us a baseline for further iterative improvements to our overall website portfolio.

#### Confidence
_How sure are we that this impact would be realized? Label from [this scale](https://medium.com/@nimay/inside-product-introduction-to-feature-priority-using-ice-impact-confidence-ease-and-gist-5180434e5b15)_.

- **Impact = 8** (opportunity to replace neglected ipfs.io/media with something easy to maintain; making posting significantly easier speeds blog post delivery; tagging and search significantly improve user experience AND add metrics collection points)
- **Confidence = 10** (effort will directly resolve known pain points, including deployment woes, image size, difficulty of posting, no search functionality, etc)
- **Ease = 5** (lots of moving parts, but few outright technical challenges in the work itself)


## Project definition
#### Brief plan of attack

1. Migrate existing Hugo blog content to new VuePress platform; test for successful migration, image display, broken links, etc
2. Augment functionality: search, filter, tags, new header, new footer
3. Augment content to match augmented functionality (ensure all posts have appropriate tags, correctly sized images, etc)
4. Overlay Forestry CMS, including documentation for post authors/editors
5. Set up Fleek deployment process, including workflow between staging and prod
6. Set up Countly-based metrics collection
7. Ensure that all net-new posts on old blog are being duplicated on new blog during this time
8. Train authors/editors/maintainers
9. Promote via all appropriate comms channels

#### What does done look like?
- Existing content on blog.ipfs.io is migrated to new platform and deployed via Fleek with no disruption of service, broken links, etc
- Workflow and DRI exist for submitting, adding and maintaining non-blog content types
- Any follow-up work is documented, issue-ized, and assigned
- Metrics collection implemented via Countly

####  What does success look like?
- Uptick in overall visitors vs existing blog
- Public-submitted or labber-submitted links are at a "good" number (TBD - will need to establish baseline since this is new functionality)
- Internal satisfaction with ease of posting/publishing/deploying
- Fewer internal fire drills at publishing/revision time; blogging plays a smooth role in overall marketing workflow

#### Counterpoints &amp; pre-mortem
_Why might this project be lower impact than expected? How could this project fail to complete, or fail to be successful?_

- Failing to keep content up to date and/or properly tagged
- Failing to make the most of added content types (e.g. only adding blog posts)

#### Alternatives
_How might this project’s intent be realized in other ways (other than this project proposal)? What other potential solutions can address the same need?_

- Training all blog writers/editors on Markdown practices
- Remedying flaws in our existing CI/CD pipeline

#### Dependencies/prerequisites
None

#### Future opportunities
- More blog authors or more frequent posts due to ease of publishing
- Establishment as a central "IPFS news clearinghouse" and IPFS event directory if those content types are consistently updated

## Required resources

#### Effort estimate
Shirt size: Large

_Note that there's been some slight scope creep (performance instrumentation, CSS cleanup) that may expand this effort if we don't push it into post-launch followup._

#### Roles / skills needed
- Project lead/PM (Jessica Schilling): Coordinate tasks, manage schedule/dependencies, ensure adherence to spec, etc
- Build/test developer (João Peixoto): Replatform, add metrics, add additional functionality, pre-launch testing
- Metrics/continuity dev help (Zé Bateira): Help with adding metrics and other functionality in a manner consistent with other PL sites
