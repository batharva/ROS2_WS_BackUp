from setuptools import find_packages, setup

package_name = 'my_first_py'

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
    maintainer='atharva',
    maintainer_email='atharva@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "py_test = my_first_py.my_first_node:main",
            "robot_news_station = my_first_py.my_first_publisher:main",
            "robot_news_subscriber = my_first_py.my_first_subscriber:main",
            "add_two_ints_server = my_first_py.my_first_service:main",
            "add_two_ints_client = my_first_py.my_first_client:main",
            "hardware_status_publisher = my_first_py.HardwareStatusPublisher:main",
            "hardware_status_subscriber = my_first_py.HardwareStatusSubscriber:main",
            "compute_rectangle_area_server = my_first_py.ComputeRectangleAreaServer:main",
            "compute_rectangle_area_client = my_first_py.ComputeRectangleAreaClient:main",
            "led_panel_node = my_first_py.led_panel_node:main",
            "battery_client_node = my_first_py.battery_client:main",
        ],
    },

)
