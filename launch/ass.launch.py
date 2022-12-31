import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():

    times = launch_ros.actions.Node(
        package = 'assy',
        executable = 'times',
        )
    quiz = launch_ros.actions.Node(
        package = 'assy',
        executable = 'quiz',
        )
    sub = launch_ros.actions.Node(
        package = 'assy',
        executable = 'sub',
        output = 'screen',
        )
    pub = launch_ros.actions.Node(
        package = 'assy',
        executable = 'pub',
        )

    return launch.LaunchDescription([ times, quiz, sub, pub ])

