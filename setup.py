from setuptools import setup, find_packages
from pathlib import Path

version = {}
exec(open(Path(__file__).parent /'asciiplot/version.py').read(), version)


setup(
    name='asciiplot',
    packages=find_packages(exclude=(["*.tests", "*.tests.*", "tests.*", "tests"])),
    version=version['__version__'],
    python_requires='>=3.6',
    author='W2SV',
    author_email='zangenbergjanek@googlemail.com',
    platforms=['Linux', 'Windows', 'MacOS']
)
