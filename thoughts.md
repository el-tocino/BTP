layout grid:
- Map corners plus "center"
- track AP via nodes, adjust camera to point at it, wait at least ten seconds for data to get averaged
- repeat at three other corners in order
- repeat for center point
- save settings as P1, P2, P3, P4, C0

server:
- get results from nodes
- store current plus two previous results for each node
- calc expected new position in space based on trajectory of last three points
- map expected position to layout grid
- calc servo difference
- send servo movements
- repeat

nodes- blast ap rssi non-stop, basically
