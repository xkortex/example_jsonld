import os
import sys
from setuptools import find_packages, setup

PY2 = sys.version_info.major == 2
PY3 = sys.version_info.major == 3

pkg_name = "example_jsonld"

def package_files(directories):
    if isinstance(directories, str):
        directories = [directories]
    paths = []
    for directory in directories:
        for (path, directories, filenames) in os.walk(directory):
            for filename in filenames:
                paths.append(os.path.join('..', path, filename))
    return paths

packages = find_packages()
print('Packages:', packages)


# todo: deal with data files properly. this should work for now though
# data_files = package_files(['reflection_authentication/models',
#                             'reflection_authentication/data'])
data_files = ['data/*.bin',
              ]

# Currently using symlinks to make directory structure look more like a package
# since package_dir is not behaving properly with pip -e.

# common dependencies
deps = [

]


setup(
    name=pkg_name,
    version="v0.0.6",
    script_name='setup.py',
    zip_safe=False,
    package_data={"example_jsonld": data_files},
    packages=packages,
    install_requires=deps,
    include_package_data=True,


)
