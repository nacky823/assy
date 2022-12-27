import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():

    lis = launch_ros.actions.Node(
        package = 'ros2_smile',
        executable = 'lis',
        output = 'screen'
        )
    tas = launch_ros.actions.Node(
        package = 'ros2_smile',
        executable = 'tas',
        output = 'screen'
        )

    return launch.LaunchDescription([ lis, tas ])

