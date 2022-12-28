#!/bin/bash -i
echo $-

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
pwd
ls -A
colcon build
source $dir/.bashrc

timeout 4 ros2 launch ros2_smile srv.launch.py > /tmp/ros2_smile.log
cat /tmp/ros2_smile.log |
grep 'addtest: 56'
