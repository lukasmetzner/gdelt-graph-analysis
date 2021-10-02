# Graph Analysis of GDELT Data
## Explanation
### Actors
Actors are entities that have been identified by GDELT. Each article has an actor1 and actor2.
### EventCodes
EventCodes describe an event or action that actor1 performed on actor2. Each EventCode has its own color in the graph.
### Nodes
All actors found in the dataset occur in the graph as nodes.
### Edges
Each event that is in the dataset is displayed as a directed edge from actor1 to actor2.

## Example
**Example using 500 dataset entries to generate the graph.**
<img src="./assets/example_graph.png">

### TODOs
- Embed color coding in the README.md
- Embed color coding with event names into website
- Try gephi with force atlas
