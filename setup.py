from setuptools import setup, find_packages

setup(
    name='colrfx',
    version='0.1.0',
    description='Python utilities for color handling (RGB, HEX) and visualization.',
    author='Muhammad Abrar',
    author_email='legendabrar44@gmail.com',
    url='https://github.com/abrarishere/colrfx',
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'colrfx = colrfx.__main__:main'
        ]
    },
)
