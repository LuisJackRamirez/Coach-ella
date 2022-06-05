# Describe project and files that belong to it
from setuptools import find_packages, setup

setup (
    name = 'coachella',
    version = '1.0.0',

    # Tells Python what package
    # directories (and Python
    # files they contain) to include.
    packages = find_packages (),

    # Include files such as the 
    # static and template files.
    include_package_data = True,

    zip_safe = False,
    install_requires = [
        'flask',
    ]
)