# W3DT issue labeling standards

The W3DT org standardizes on the following default core labels for GitHub issues and pull requests. This ensures continuity
between repos, helping to improve the overall experience for contributors as a whole while also making it easier to use project
planning tools (such as ZenHub) to create landscape-level views across multiple repos.

## Mandatory labels

### Global
These are exceptions to the remainder of this labeling taxonomy, but exist for continuity with global GitHub practices for new contributors.

| Label              | Description                                                  | Color     |
| -----              | -----------                                                  | -----     |
| `bounty`           | Has bounty! See https://github.com/ipfs/devgrants/projects/1 | `#1cfc60` |
| `good first issue` | Good issue for new contributors                              | `#7057ff` |
| `help wanted`      | Seeking public contribution on this issue                    | `#0e8a16` |

### Priority
Indicates priority as a function of standard PL-wide OKR priority rankings. **Important: P0 items need an assignee to act as a DRI.**

| Label | Description                                               | Color     |
| ----- | -----------                                               | -----     |
| `P0`  | Critical: Tackled by core team ASAP                       | `#b60205` |
| `P1`  | High: Likely tackled by core team if no one steps up      | `#d93f0b` |
| `P2`  | Medium: Good to have, but can wait until someone steps up | `#e99695` |
| `P3`  | Low: Not priority right now                               | `#f9d0c4` |

### Kind
Overarching type of issue or PR. For an additional layer of specificity, use the `area` label.

| Label               | Description                                                             | Color     |
| -----               | -----------                                                             | -----     |
| `kind/architecture` | Core architecture of project                                            | `#c7def8` |
| `kind/bug`          | A bug in existing code (including security flaws)                       | `#fc2929` |
| `kind/discussion`   | Topical discussion; usually not changes to codebase                     | `#c7def8` |
| `kind/enhancement`  | A net-new feature or improvement to an existing feature                 | `#c7def8` |
| `kind/maintenance`  | Work required to avoid breaking changes or harm to project's status quo | `#c7def8` |
| `kind/support`      | A question or request for support                                       | `#c7def8` |
| `kind/test`         | Testing work                                                            | `#c7def8` |

### Need
These labels indicate needs that must be met in order for the issue or PR to be completed and closed. These will often appear in conjunction with `status/blocked` to add a layer of specificity to the latter. **Important: ALL new issues in a repo should default to `need/triage`, and this label should be removed once all other relevant labels are assigned.**

| Label                   | Description                                | Color     |
| -----                   | -----------                                | -----     |
| `need/analysis`         | Needs further analysis before proceeding   | `#ededed` |
| `need/author-input`     | Needs input from the original author       | `#ededed` |
| `need/community-input`  | Needs input from the wider community       | `#ededed` |
| `need/maintainer-input` | Needs input from the current maintainer(s) | `#ededed` |
| `need/triage`           | Needs initial labeling and prioritization  | `#ededed` |

## Optional (but helpful) labels

### Expertise
Estimate of required experience to solve the issue; note that this is different than `effort`, below.

| Label              | Description                                                | Color     |
| -----              | -----------                                                | -----     |
| `exp/beginner`     | Can be confidently tackled by newcomers                    | `#bfe5bf` |
| `exp/novice`       | Someone with a little familiarity can pick up              | `#bfe5bf` |
| `exp/intermediate` | Prior experience is likely helpful                         | `#bfe5bf` |
| `exp/expert`       | Having worked on the specific codebase is important        | `#bfe5bf` |
| `exp/wizard`       | Extensive knowledge (implications, ramifications) required | `#bfe5bf` |

### Effort
Similar to T-shirt sizing, this estimates the *amount* of work. This can be different than `expertise`, e.g. something can be easy but require a lot of time to complete, or vice versa.

| Label          | Description                                           | Color     |
| -----          | -----------                                           | -----     |
| `effort/hours` | Estimated to take one or several hours                | `#fef2c0` |
| `effort/days`  | Estimated to take multiple days, but less than a week | `#fef2c0` |
| `effort/weeks` | Estimated to take multiple weeks                      | `#fef2c0` |

### Status
Current status of the issue or PR. Note that it may be advantageous to add second-tier variants on `status/blocked` to your repo if there are common blocking scenarios, i.e. `status/blocked/upstream-bug`.

| Label                | Description                                     | Color     |
| -----                | -----------                                     | -----     |
| `status/blocked`     | Unable to be worked further until needs are met | `#b52ed1` |
| `status/inactive`    | No significant work in the previous month       | `#dcc8e0` |
| `status/in-progress` | In progress                                     | `#dcc8e0` |
| `status/ready`       | Ready to be worked                              | `#dcc8e0` |

### Topics
Topics will vary according to the particular project, but will often have commonalities that overlay across multiple projects. Design is one prominent example of this, particularly since the following design labels are used to generate a common design tracking board:

| Label                    | Description                                        | Color     |
| -----                    | -----------                                        | -----     |
| `topic/design-content`   | Content design, writing, information architecture  | `#3f4b56` |
| `topic/design-front-end` | Front-end implementation of UX/UI work             | `#3f4b56` |
| `topic/design-ux`        | UX strategy, research, not solely visual design    | `#3f4b56` |
| `topic/design-video`     | Video and/or motion design                         | `#3f4b56` |
| `topic/design-visual`    | Visual design ONLY, not part of a larger UX effort | `#3f4b56` |

We also use topics to track platform specific issues:

| Label           | Description             | Color     |
| -----           | -----------             | -----     |
| `topic/windows` | Windows specific issues | `#3f4b56` |
| `topic/macos`   | MacOS specific issues   | `#3f4b56` |
| `topic/linux`   | Linux specific issues   | `#3f4b56` |

Other commonly encountered topics across multiple repos include:

| Label                | Description            | Color     |
| -----                | -----------            | -----     |
| `topic/devexp`       | Developer Experience   | `#3f4b56` |
| `topic/docs`         | Documentation          | `#3f4b56` |
| `topic/infra`        | Infrastructure         | `#3f4b56` |
| `topic/interop`      | Interoperability       | `#3f4b56` |
| `topic/perf`         | Performance            | `#3f4b56` |
| `topic/dependencies` | Dependencies           | `#3f4b56` |
| `topic/ci`           | Continuous integration | `#3f4b56` |

### Area
Areas will vary depending on the needs of the particular repo, but refer to a commonly-encountered functional or abstraction layer for a project. They take the following form, where *foo* is a project-specific functional or abstraction layer, e.g. *firefox* or *libp2p*.

| Label      | Description                            | Color     |
| -----      | -----------                            | -----     |
| `area/foo` | *Area-specific description to go here* | `#ccf0ed` |
