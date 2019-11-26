
cur_x = 10
cur_y = 12
target_x = sys.argv[1]
target_y = sys.argv[2]


### three point interpolation
### for four point, uncomment x[1,2]/y[1,2] lines
mid_x = int(cur_x + .6 * (target_x - cur_x))
mid_y = int(cur_y + .6 * (target_y - cur_y))
#mid_x1 = int(cur_x + .25 * (target_x - cur_x))
#mid_y1 = int(cur_y + .25 * (target_y - cur_y))
#mid_x2 = int(cur_x + .75 * (target_x - cur_x))
#mid_y2 = int(cur_y + .75 * (target_y - cur_y))

move_x (mid_x)
move_y (mid_y)
#move_x (mid_x1)
#move_y (mid_y1)
#move_x (mid_x2)
#move_y (mid_y2)
move_x (targetx)
move_y (targety)
