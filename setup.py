import setuptools

name = 'requester'
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=name,
    version="0.0.1",
    author="Markus Schader (@mschade_)",
    author_email="mail at markusschader dot de",
    description="A small helper script to get your Python Requests POC started quick",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=['requester'],
    package_data={
        name: ['templates/requester.j2']
    },
    install_requires=[
        'requests',
        'click',
        'jinja2',
    ],
    entry_points={
        'console_scripts': [
            'requester = requester.requester:create_file'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Unix",
    ],
)