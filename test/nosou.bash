#!/bin/bash -i
echo $-

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
pwd
ls -A
#colcon build

#timeout 10 ros2 launch ros2_smile talk_listen.launch.py > /tmp/ros2_smile.log
#cat /tmp/ros2_smile.log |
#grep 'age=15'
