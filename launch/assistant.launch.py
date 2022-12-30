import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():

    client = launch_ros.actions.Node(
        package = 'ros2_smile',
        executable = 'client',
        output = 'screen'
        )
    times = launch_ros.actions.Node(
        package = 'ros2_smile',
        executable = 'times',
        )
    selection = launch_ros.actions.Node(
        package = 'ros2_smile',
        executable = 'selection',
        )

    return launch.LaunchDescription([ client, times, selection ])

