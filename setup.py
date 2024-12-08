from setuptools import setup, find_packages

setup(
    name="mayan_api_plugin",  # Name of your plugin package
    version="0.1",  # Initial version number
    description="A plugin for integrating Mayan EDMS with an API for metadata completion",  # Short description
    #long_description=open("README.md").read(),  # Long description (optional)
    #long_description_content_type="text/markdown",  # Specify Markdown if README.md is used
    author="rion morgenstern",  # Your name
    author_email="rioncm@gmail.com",  # Your email
    url="https://github.com/rioncm/mayan_api_plugin",  # URL of your repository
    packages=find_packages(),  # Automatically find all packages in the directory
    include_package_data=True,  # Include additional files specified in MANIFEST.in
    install_requires=[
        "django>=3.2",  # Example: dependencies for your plugin
        "requests>=2.25.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "mayan.apps": [
            "mayan_api_plugin = mayan_api_plugin.apps.MayanApiPlugin",
        ]
    },
    python_requires=">=3.6",
)