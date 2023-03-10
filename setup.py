from setuptools import setup
import os
from glob import glob

package_name = 'assy'

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
    description='A ros2 package.',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "client = assy.client:main",
            "times = assy.times:main",
            "quiz = assy.quiz:main",
            "sub = assy.sub:main",
            "pub = assy.pub:main",
        ],
    },
)
