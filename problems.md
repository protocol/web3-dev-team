# Top Problems from Product Team

## P0 Problems

 - **Problem:  The fact that storing and retrieving data with the stack (IPFS+Filecoin) can ever fail.**

   - Problem
     - For a reliable storage system, the basic operations of store and retrieve should never fail. (Compare with S3 or a laptop hard disk. These routinely undergo tens of millions of writes without any unrecoverable failures.)
     - Data loss on IPFS can occur because the data is not pinned (user misunderstanding / UX problem), or the pinning service fails.
   - Impact
     - If our stack is not trustworthy -- in the sense that storage and/or retrieval can fail sometimes -- we will lose users.
   - Desired Outcome
	  - Storage deals should succeed 99+% of the time.
	    - When they fail unavoidably (e.g., due to user error), the user should see clear error messages that explain
	    - Retrieval deals should succeed 99+% of the time.
	      - (ditto)
	  - IPFS should provide a clear UX so that users understand the difference between pinned and unpinned data, and users who want to persist their data understand they have to pin it (or else this happens automatically in some manner when dealing with a user who wants to persist data).
	  - IPFS should be resilient against the failure of a single pinning service.
## Stack Ranked P1 Problems

 - **Problem: We currently do not always understand why storage deals (in the wild) fail so frequently.**

   - Problem
     - Storage deal success rate has increased dramatically in controlled environments in the last few months.
     - However, in the wild, storage deals still fail often, with miners failing to accept deals. Even among those miners that do accept deals, the deal success rate (DSR) is <100%.
       - Any DSR<100% hurts us because we are perceived as unreliable and users will not entrust important data to us.
   - Desired Outcome
     - A dashboard that shows metrics/stats on overall deal success and failures, and reasons why they’re failing. More detail in the doc above.

- **Problem: Data that has been stored successfully is not guaranteed to be retrievable.**

   - Problem
     - Once a storage deal has successfully concluded, it’s not always possible to retrieve the data later. The miner may refuse retrieval or disappear.
       - Retrieval refusal especially is very common.
       - We also don’t track retrieval success rate (RSR), so severity is unclear.
     - We have seen that many miners, especially those storing larger datasets on behalf of clients, delete unsealed copies of their data regularly and there is no enforcement mechanism for this.
       - Then, when a retrieval is triggered for that file, miners are forced to unseal their sectors, which is an expensive operation that many miners don’t want to do (especially as it competes with sealing, the main operation most miners care about). So most miners subsequently turn off retrievals altogether.
       - Now a client’s data is locked in with the miner, and there’s nothing that can be done about it.
   - Desired Outcome
		 - As a user of Lotus, I should be able to store data on the network and then:
		   - At random time intervals, I should be able to do a trial retrieval of the data. In 99.999% of cases, I should get the original data back.
		 - As a PL PM, I should be able to see a dashboard of retrieval success rate (RSR) across the entire network.

 - **Problem: Filecoin does not support small file storage well, even though small files are the most common use case.**

     - Desired Outcome:
       - As a developer using Filecoin, I should be able to store 100 small files (ranging from 32 bytes to 200 MiB), within the time it takes to transfer the data.
       - As a developer using Filecoin, I should be able to retrieve any of those files at any time within the time it takes for data transfer (i.e., no extra time required beyond network latency time constraints).
         - If a “fast data path” is required, this option should be exposed to me and it should be clear that I need to use it from documentation and UX.
         - If a DataCap is required, [ditto].

 - **Problem: IPFS users can’t pin their data to Filecoin.**

   - Problem
     - Filecoin was promised to be and needs to be the default pinning solution for IPFS data. Users want it. It doesn’t work today.
   - Desired Outcome
			 - IPFS users can pin to Filecoin directly
			 - IPFS users can persist their IPFS pins via Filecoin
			 - IPFS users can retrieve from Filecoin directly
			 - (maybe) Filecoin miners can receive IPFS pinning requests and serve data back to IPFS users.

 - **Problem: New developers have to spend too much time and money to go through a simple storage/retrieval workflow.**

     - Problem
       - Currently, getting started with Filecoin requires a full node (local or cloud) and a lot of knowledge just to make your first storage and retrieval deal... in our experimentation and user walkthroughs, it’s ~10hours + $3000 local machine (or $100s / month for a cloud node) to get started. 
     - Desired Outcome
       - As a first time developer-user kicking the tires of our system, I should be able to store/pin a piece of data and retrieve it within 60 minutes WITH APIs (not direct CLI) without any prior training or expertise.
			 - I should not have to run a node. (A lightweight piece of software that works on an 8 or 16GB consumer laptop is fine.)
			 - I should be able to do this in a variety of programming languages: JS, PHP, Python. See [Arweave’s list here](https://www.arweave.org/build#interfaces). 
 
 - **Problem: Garbage collection in IPFS blocks normal node operations.**
    - Problem
		  - Garbage collection in IPFS locks the node and blocks other mutation operations like `ipfs add`. On a node with millions of pins, GC will block the node for an entire day. For our largest IPFS collaborators, this becomes a prohibitive issue.
		- Desired Outcome
      - GC in background without locking the node.

 - **Problem: Clients find it extraordinarily difficult to discover reliable miners who will meet their storage needs (SLA, geography, miner cost quotes).**

   - Problem
     - Users don’t have any information about the various miners with which they can store data (SLA, geo, nation or regional bloc, percentage uptime, reachability, etc)
     - The SHORT-TERM, unsustainable fix we hacked together for this problem is the MinerX program. This cannot be the long-term solution for miner discovery. The network needs a proper marketplace (can also be built by teams in the ecosystem) where clients can choose reliable miners.
	 - Desired Outcome:
		 - Before the user decides to make a storage deal, she has all the information about the miner including geography, national location, SLA terms (uptime, data transfer rates, other custom terms).

## Stack Ranked "Probably P1 Problems" (but need investigation)

 - Problem: Clients in certain cases can lose data that they have stored to the Filecoin network.

 - Problem: Clients want to store redundant copies of their data, but cannot do so without paying for multiple data transfers.

 - Problem: Clients today don’t know how much Filecoin storage will actually cost them.

 - Problem: Clients cannot renew DataCap, making Filecoin Plus significantly less useful.


## Stack Ranked P2 Problems

 - Problem: Clients with massive datasets do not know what best practices to follow when storing those datasets on the stack.

 - Problem: Users don’t have a "standard" cloud configuration to deploy without manual configuration of Lotus.

 - Problem: Highest-value IPFS users (pinning services) do not advertise their pins publicly

 - Problem: The total cost of integration+storage on the stack is higher than using AWS

 - Problem: Clients that want to extend the amount of time their data is stored on Filecoin cannot do so in a reasonable way.

## Stack Ranked P3 Problems

 - Problem: Developers cannot rely on our stack to provide stable APIs (eg, semver). Instead, they have to contend with unexpected breaking changes.

 - Problem: A user with millions of pins should be able to store them on the stack

 - Problem: Developers cannot build complete browser-based and desktop dapps with our JS libraries.

 - Problem: Developers cannot find reliable information about our stack when doing Google searches.

 - Problem: Filecoin is currently unsuitable as the default storage solution for NFTs.


