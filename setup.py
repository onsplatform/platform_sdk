from distutils.core import setup

setup(
    name='ONS Platform Python SDK',
    version='0.1.0',
    author='STA',
    author_email='gibson@ons.org.br',
    packages=['platform_sdk',],
    description='TODO',
    install_requires=[
        "requests >= 2.21.0",
        "peewee == 3.9.5",
    ],
)
