import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():

    times = launch_ros.actions.Node(
        package = 'assy',
        executable = 'times',
        )
    order = launch_ros.actions.Node(
        package = 'assy',
        executable = 'order',
        )

    return launch.LaunchDescription([ times, order ])

