from setuptools import setup
import os
from glob import glob

package_name = 'zerythron_vector_x'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name, 'swarm_core', 'mesh_comm'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'px4_sitl_worlds'), glob('px4_sitl_worlds/*.world')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Mo Ryan Yunus',
    maintainer_email='zerythron.info@gmail.com',
    description='Resilient BVLOS Swarm Challenge Autonomous Package',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'swarm_planner = swarm_core.swarm_planner:main',
            'comms_manager = mesh_comm.comms_manager:main',
        ],
    },
)
