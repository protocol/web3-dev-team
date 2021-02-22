# Top Problems from Product Team

## P0

 - The fact that storing and retrieving data with the stack (IPFS+Filecoin) can ever fail is a problem.

## Stack Ranked P1

 - We currently do not always understand why storage deals (in the wild) fail so frequently.

 - Data that has been stored successfully is not guaranteed to be retrievable.

 - Filecoin does not support small file storage well, even though small files are the most common use case.

 - IPFS users can’t pin their data to Filecoin.

 - New developers have to spend too much time and money to go through a simple storage/retrieval workflow.

 - Clients find it extraordinarily difficult to discover reliable miners who will meet their storage needs (SLA, geography, miner cost quotes).

## Stack Ranked "Probably P1" (but need investigation)

 - Clients in certain cases can lose data that they have stored to the Filecoin network.

 - Clients want to store redundant copies of their data, but cannot do so without paying for multiple data transfers.

 - Clients today don’t know how much Filecoin storage will actually cost them.

 - Clients cannot renew DataCap, making Filecoin Plus significantly less useful.

 - Garbage collection in IPFS blocks normal node operations.

## Stack Ranked P2s

 - Clients with massive datasets do not know what best practices to follow when storing those datasets on the stack.

 - Users don’t have a "standard" cloud configuration to deploy without manual configuration of Lotus.

 - Highest-value IPFS users (pinning services) do not advertise their pins publicly

 - The total cost of integration+storage on the stack is higher than using AWS

 - Clients that want to extend the amount of time their data is stored on Filecoin cannot do so in a reasonable way.

## Stack Ranked P3s

 - Developers cannot rely on our stack to provide stable APIs (eg, semver). Instead, they have to contend with unexpected breaking changes.

 - A user with millions of pins should be able to store them on the stack

 - Developers cannot build complete browser-based and desktop dapps with our JS libraries.

 - Developers cannot find reliable information about our stack when doing Google searches.

 - Filecoin is currently unsuitable as the default storage solution for NFTs.


