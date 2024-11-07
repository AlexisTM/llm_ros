from setuptools import find_packages, setup

package_name = "llm_ros"

setup(
    name=package_name,
    version="0.0.1",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Alexis Paques",
    maintainer_email="alexis.paques@gmail.com",
    description="LLM interface package to ROS 2",
    license="BSD-3-Clause",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": ["ollama_node = llm_ros.ollama_node:main"],
    },
)
