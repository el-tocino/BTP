2d mapping

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
- time sync 

nodes:
- blast ap rssi non-stop, basically
- sync time

#### node positioning

If sufficient space is used between nodes, then it's not really necessary to place them precisely. Layout should, theoretically, get the data averaged correctly. 

##### how many nodes?

Three would be the real minimum.  Allow server to track up to say, ten nodes.  Too many could slow down calculations, maybe?  Test and see.

##### what if a udp packet drops?

we'll get another.  List of last three should allow for targeting fairly accurately even if one node has recent but not current entries.

##### UDP?

simple, effective.  

##### wuuuuuttt

Test to see which works best? Speed considerations on a pi?
https://appelsiini.net/2017/trilateration-with-n-points/
https://github.com/lemmingapex/trilateration
https://gist.github.com/tuupola/0df4934758fa04a3f07c96d55cd31bb1
https://github.com/akshayb6/trilateration-in-3d
https://github.com/robinroyer/trilateration
https://www.101computing.net/cell-phone-trilateration-algorithm/ 
