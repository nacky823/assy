import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():

    talker = launch_ros.actions.Node(
        package = 'ros2_smile',
        executable = 'talker',
        output = 'screen'
        )
    listener = launch_ros.actions.Node(
        package = 'ros2_smile',
        executable = 'listener',
        output = 'screen'
        )

    return launch.LaunchDescription([ talker, listener ])

