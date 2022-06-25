from setuptools import setup

package_name = 'crl_executer'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mor',
    maintainer_email='1912.mor@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'executer = crl_executer.executer:main',
            'gazebo_launcher = crl_executer.gazebo:main',
            'spawn_burger = crl_executer.spawn_burger:main'
        ],
    },
)
