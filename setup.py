from setuptools import setup, find_packages
from pathlib import Path

version = {}
exec(open(Path(__file__).parent /'asciichartpy_extended/version.py').read(), version)


setup(
    name='asciichartpy_extended',
    packages=find_packages(exclude=(["*.tests", "*.tests.*", "tests.*", "tests"])),
    version=version['__version__'],
    python_requires='>=3.8',
    author='W2SV',
    author_email='zangenbergjanek@googlemail.com',
    platforms=['Linux', 'Windows', 'MacOS']
)
