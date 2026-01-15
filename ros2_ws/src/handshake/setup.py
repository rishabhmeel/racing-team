from setuptools import find_packages, setup

package_name = 'handshake'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='meel',
    maintainer_email='meelrishabh4761@gmail.com',
    description='Handshake assignment',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'ai = handshake.ai:main',
            'vcu = handshake.vcu:main',
        ],
    },
)
