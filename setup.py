
from setuptools import setup, find_packages
from bibliotheca.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='bibliotheca',
    version=VERSION,
    description='Bibliotheca manages your personal library of scholarly works.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='William Payne',
    author_email='wtpayne@gmail.com',
    url='https://github.com/wtpayne/bibliotheca/',
    license='Apache',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'bibliotheca': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        bibliotheca = bibliotheca.main:main
    """,
)
