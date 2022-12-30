#!/bin/bash -i
# SPDX-FileCopyrightText: 2022 NAGAKI Yuki
# SPDX-License-Identifier: BSD-3-Clause
echo $-

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
pwd
ls -A
colcon build
echo $?
source $dir/.bashrc

ng () {
    echo -e "NG at LINE $1"
    res=1
    exit $res
}

res=0

hour=`TZ=JST-9 date +'%H'`
timeout 2 ros2 run assy times &
timeout 2 ros2 service call /times turtlesim/srv/Spawn "name: now" > /tmp/assy.log
cat /tmp/assy.log |
grep 'turtlesim.srv.Spawn_Response(name=' |
grep $hour
[ "$?" = 0 ] || ng ${LINENO}

timeout 2 ros2 launch assy ass.launch.py &
timeout 2 ros2 run assy client > /tmp/assy.log
cat /tmp/assy.log |
grep '現在の時刻は' |
grep $hour
[ "$?" = 0 ] || ng ${LINENO}

timeout 3 ros2 launch assy ass.launch.py &
timeout 3 ros2 run assy client
echo -e "p\n" > /tmp/assy.log
cat /tmp/assy.log
