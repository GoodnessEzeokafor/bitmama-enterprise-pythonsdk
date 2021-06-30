from setuptools import setup, find_packages
from os import path

main_dir = path.abspath(path.dirname(__file__))
with open(path.join(main_dir, 'README.md'), encoding='utf-8') as f:
    description = f.read()

setup(
    name='bitmama_enterprise_pythonsdk',
    version='1.0.0',
    description='Python API wrapper for Bitmam Enterprise API',
    long_description=description,
    long_description_content_type='text/markdown',
    url='https://github.com/GoodnessEzeokafor/bitmama-enterprise-pythonsdk',
    # Author details
    author='Goodness Ezeokafor',
    author_email='chinemeremwork@gmail.com',
    # license='MIT',
    keywords='bitmama-enterprise enterprise sdk crypto python library',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['httpx', 'trio'],
    extras_require={
        'test': ['coverage'],
    },
)
