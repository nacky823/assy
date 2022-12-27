import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():

    listener = launch_ros.actions.Node(
        package = 'ros2_smile',
        executable = 'listener',
        output = 'screen'
        )
    talker = launch_ros.actions.Node(
        package = 'ros2_smile',
        executable = 'talker',
        output = 'screen',
        prefix="xterm -e"
        )

    return launch.LaunchDescription([ listener, talker ])

