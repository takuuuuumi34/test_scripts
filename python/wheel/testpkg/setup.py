import os
import sys
import re
import pathlib
from setuptools import setup

if sys.version_info < (3, 4):
    raise RuntimeError('requires Python3')

DIR = str(pathlib.Path(__file__).resolve().parent)

requires = [
    "numpy"
]


entry_points = {
    'console_scripts': [
        'greet = testpkg.hello:greet',
    ]
}

versionpy = os.path.join(DIR, 'testpkg/__version__.py')
version = re.search(r'"([\d.]+)"', open(versionpy).read()).group(1)


setup(
    name="testpkg",
    version=version,
    entry_points=entry_points,
    packages=['testpkg'],
    install_requires=requires,
    include_package_data=True,
    zip_safe=True,
    # cmdclass={
    #     'build': BuildNPM,
    # },
)
