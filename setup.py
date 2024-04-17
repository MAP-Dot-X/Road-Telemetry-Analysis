from setuptools import setup, find_packages

setup(
    name='road-telemetry-analysis',
    version='0.1',
    description="A python package for analyzing road telemetry data.",
    author="Kevin Lai",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
    ],
)
