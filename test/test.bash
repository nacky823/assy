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

timeout 6 ros2 launch assy ass.launch.py &
yes tests | head -n3 | timeout 6 ros2 run assy client > /tmp/assy.log

if [ "$hour" -le "9" -a "$hour" -ge "4" ]; then
    cat /tmp/assy.log | grep '素敵な一日になりますように ( ^ ^ )'
    [ "$?" = 0 ] || ng ${LINENO}
fi
if [ "$hour" -le "17" -a "$hour" -ge "10" ]; then
    cat /tmp/assy.log | grep 'また遊びに来てくださいね ( ^-^ )/'
    [ "$?" = 0 ] || ng ${LINENO}
fi
if [ "$hour" -le "23" -a "$hour" -ge "18" ]; then
    cat /tmp/assy.log | grep 'ゆっくり休んでくださいね (*^ ^*)'
    [ "$?" = 0 ] || ng ${LINENO}
fi
if [ "$hour" -le "3" -a "$hour" -ge "0" ]; then
    cat /tmp/assy.log | grep '早く寝ましょう！（笑）'
    [ "$?" = 0 ] || ng ${LINENO}
fi

