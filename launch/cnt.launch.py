#!/usr/bin/python3
# SPDX-FileCopyrightText: 2022 NAGAKI Yuki
# SPDX-License-Identifier: BSD-3-Clause
import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():

    sub = launch_ros.actions.Node(
        package = 'assy',
        executable = 'sub',
        output = 'screen',
        )
    pub = launch_ros.actions.Node(
        package = 'assy',
        executable = 'pub',
        )

    return launch.LaunchDescription([ sub, pub ])

