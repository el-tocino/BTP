2d mapping

layout grid:
- Map corners plus "center" and nodes.
- track AP via nodes, adjust camera to point at it, wait at least ten seconds for data to get averaged
- repeat at three other corners in order
- repeat for center point
- save settings as P1, P2, P3, P4, C0, N0, N1, N2, etc..

server:
- get results from nodes
- write results to file for later consideration?
- calc position based on latest result from nodes
- map position to layout grid
- calc target servo position
- calc servo easing
- send servo movements
- repeat

- time sync 

nodes (reporter.py):
- blast ap rssi non-stop (time.sleep(.016) worked 68-72 times in one second on a pi3)

- sync time

##### node positioning

If sufficient space is used between nodes, then it's not really necessary to place them precisely. Layout should, theoretically, get the data averaged correctly. 

##### how many nodes?

Three would be the real minimum.  Allow server to track up to say, six nodes.  Too many could slow down calculations, maybe?  Test and see.

##### Layout

The grid should be broken into a exponential mapping. IE, the closer (y) and middle (x) areas get increasingly dense the closer to 50,0 you get.

##### what if a udp packet drops?

we'll get another.  List of last three should allow for targeting fairly accurately even if one node has recent but not current entries.

##### UDP?

simple, effective. If no update, assume last values still valid.

##### smooth out servo movements

Will require tracking last positional argument for each axis. 
N-point easing? 3 to start with.  See interp.py.  After figuring out how much overhead that adds, adjust as needed. 

See also:

(https://github.com/cansik/smooth-servo)
(https://makingfernand0.wordpress.com/2014/06/30/smooth-movement-with-servos/)
(https://www.raspberrypi.org/forums/viewtopic.php?t=105554)
(https://en.wikipedia.org/wiki/Spline_interpolation#Algorithm_to_find_the_interpolating_cubic_spline)

##### wuuuuuttt

Test to see which works best? Speed considerations on a pi?
https://appelsiini.net/2017/trilateration-with-n-points/
https://github.com/lemmingapex/trilateration
https://gist.github.com/tuupola/0df4934758fa04a3f07c96d55cd31bb1
https://github.com/akshayb6/trilateration-in-3d
https://github.com/robinroyer/trilateration
https://www.101computing.net/cell-phone-trilateration-algorithm/ 
