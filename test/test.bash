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

if [ "$hour" -le "9" -a "4" -ge "$hour" ]; then
    cat /tmp/assy.log | grep '素敵な一日になりますように ( ^ ^ )'
    [ "$?" = 0 ] || ng ${LINENO}
fi
if [ "$hour" -le "17" -a "10" -ge "$hour" ]; then
    cat /tmp/assy.log | grep 'また遊びに来てくださいね ( ^-^ )/'
    [ "$?" = 0 ] || ng ${LINENO}
fi
if [ "$hour" -le "23" -a "18" -ge "$hour" ]; then
    cat /tmp/assy.log | grep 'ゆっくり休んでくださいね (*^ ^*)'
    [ "$?" = 0 ] || ng ${LINENO}
fi
if [ "$hour" -le "3" -a "0" -ge "$hour" ]; then
    cat /tmp/assy.log | grep '早く寝ましょう！（笑）'
    [ "$?" = 0 ] || ng ${LINENO}
fi

timeout 6 ros2 launch assy cnt.launch.py > /tmp/assy.log
cat /tmp/assy.log |
grep 'Count second : 4'
[ "$?" = 0 ] || ng ${LINENO}

timeout 3 ros2 run assy quiz &
ros2 service call /select turtlesim/srv/Spawn "name: z" > /tmp/assy.log
cat /tmp/assy.log |
grep '電車に乗っているとき、自分は座っていて'
[ "$?" = 0 ] || ng ${LINENO}

timeout 3 ros2 run assy quiz &
ros2 service call /select turtlesim/srv/Spawn "name: y" > /tmp/assy.log
cat /tmp/assy.log |
grep 'リュックサックのチャックが全開の人を見たとき'
[ "$?" = 0 ] || ng ${LINENO}

timeout 3 ros2 run assy quiz &
ros2 service call /select turtlesim/srv/Spawn "name: x" > /tmp/assy.log
cat /tmp/assy.log |
grep '締め切りが明日だという事を'
[ "$?" = 0 ] || ng ${LINENO}

timeout 3 ros2 run assy quiz &
ros2 service call /select turtlesim/srv/Spawn "name: za" > /tmp/assy.log
cat /tmp/assy.log |
grep '正解だと思います。優しいですね( ^ ^ )'
[ "$?" = 0 ] || ng ${LINENO}

timeout 3 ros2 run assy quiz &
ros2 service call /select turtlesim/srv/Spawn "name: zb" > /tmp/assy.log
cat /tmp/assy.log |
grep '正解だと思います。私もこの選択をしそうです。'
[ "$?" = 0 ] || ng ${LINENO}

timeout 3 ros2 run assy quiz &
ros2 service call /select turtlesim/srv/Spawn "name: zc" > /tmp/assy.log
cat /tmp/assy.log |
grep '大正解だと思います。毎日お疲れ様です。'
[ "$?" = 0 ] || ng ${LINENO}

timeout 3 ros2 run assy quiz &
ros2 service call /select turtlesim/srv/Spawn "name: ya" > /tmp/assy.log
cat /tmp/assy.log |
grep 'かなりやばい行動なのでやめましょう。'
[ "$?" = 0 ] || ng ${LINENO}

timeout 3 ros2 run assy quiz &
ros2 service call /select turtlesim/srv/Spawn "name: yb" > /tmp/assy.log
cat /tmp/assy.log |
grep '全力に負けず劣らずのやばさですね'
[ "$?" = 0 ] || ng ${LINENO}

timeout 3 ros2 run assy quiz &
ros2 service call /select turtlesim/srv/Spawn "name: yc" > /tmp/assy.log
cat /tmp/assy.log |
grep '私も同じ意見なので気が合いますね'
[ "$?" = 0 ] || ng ${LINENO}

timeout 3 ros2 run assy quiz &
ros2 service call /select turtlesim/srv/Spawn "name: xa" > /tmp/assy.log
cat /tmp/assy.log |
grep '素直で素敵な性格だと思います'
[ "$?" = 0 ] || ng ${LINENO}

timeout 3 ros2 run assy quiz &
ros2 service call /select turtlesim/srv/Spawn "name: xb" > /tmp/assy.log
cat /tmp/assy.log |
grep 'そう、何もなかった。何もなかったのだ。'
[ "$?" = 0 ] || ng ${LINENO}

timeout 3 ros2 run assy quiz &
ros2 service call /select turtlesim/srv/Spawn "name: xc" > /tmp/assy.log
cat /tmp/assy.log |
grep '朝が怖いですね、想像するのもいやなので'
[ "$?" = 0 ] || ng ${LINENO}

timeout 3 ros2 run assy quiz &
ros2 service call /select turtlesim/srv/Spawn "name: ending" > /tmp/assy.log
cat /tmp/assy.log |
grep '全てのプログラムを終了しました'
[ "$?" = 0 ] || ng ${LINENO}









