from os import path

from setuptools import (
    find_packages,
    setup,
)

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    install_requires = [l.split('\n')[0] for l in f.readlines()]

setup(
    name='pytest-mockservers',
    version='0.1.0',
    description='A set of fixtures to test your requests to HTTP/UDP servers',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Nikita Grishko',
    author_email='gr1n@protonmail.com',
    url='https://github.com/Gr1N/pytest-mockservers',
    packages=find_packages(exclude=(
        'tests.*',
        'tests',
    )),
    install_requires=install_requires,
    entry_points={
        'pytest11': [
            'http_server = pytest_mockservers.http_server',
            'udp_server = pytest_mockservers.udp_server',
        ],
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='asyncio pytest plugin http upd mock',
    project_urls={
        'Bug Reports': 'https://github.com/Gr1N/pytest-mockservers/issues',
        'Source': 'https://github.com/Gr1N/pytest-mockservers',
    }
)
