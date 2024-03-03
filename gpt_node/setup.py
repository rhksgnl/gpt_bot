from setuptools import find_packages, setup

package_name = 'gpt_node'

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
    maintainer='hwi',
    maintainer_email='gnl96@naver.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gpt_node=gpt_node.gpt_node:main',
            'gpt_code=gpt_node.gpt_code:main',
            'gpt_api=gpt_node.gpt_api',
        ],
    },
)
