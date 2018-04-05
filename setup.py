from setuptools import setup, find_packages


setup(
    name='horserace',
    version='0.2.0',
    description='Horse Race Simulator',
    author='Santiago Blanco Ventas',
    license='MIT',
    project_urls={
        'Source': 'https://github.com/sblancov/horserace'
    },
    packages=find_packages(exclude=['docs']),
    install_requires=['petname'],
    entry_points={
        'console_scripts': ['horserace = horserace.horserace:main']
    }
)
