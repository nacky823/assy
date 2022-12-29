from setuptools import setup
import os
from glob import glob

package_name = 'ros2_smile'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='NAGAKI Yuki',
    maintainer_email='youjiyongmu4@gmail.com',
    description='A ros2 package that makes you smile.',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "talker = ros2_smile.talker:main",
            "listener = ros2_smile.listener:main",
            "tas = ros2_smile.tas:main",
            "lis = ros2_smile.lis:main",
            "tac = ros2_smile.tac:main",
            "lic = ros2_smile.lic:main",
        ],
    },
)
