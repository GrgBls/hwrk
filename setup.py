from setuptools import setup

setup(
    name = 'hwrk',
    packages=["hwrk"],
    version = '0.3',
    description = 'simple script to not forget about your homework',
    long_description = 'because writing your homework on a piece of paper is too mainstream',
    author = 'GrgBls',
    url = 'https://gitlab.com/GrgBls/hwrk',
    py_modules=['hwrk'],
    install_requires=[''],
    entry_points='''
        [console_scripts]
        hwrk=hwrk.main:main
    ''',
)
