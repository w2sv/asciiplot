from setuptools import setup, find_packages
from pathlib import Path

version = {}
exec(open(Path(__file__).parent /'asciiplot/version.py').read(), version)


setup(
    name='asciiplot',
    packages=find_packages(exclude=(["*.tests", "*.tests.*", "tests.*", "tests"])),
    version=version['__version__'],
    license='MIT',
    description='Package enabling asciiized sequence plotting in terminal across platforms',
    keywords=['plotting', 'terminal', 'console', 'ascii', 'gui', 'data', 'visualization'],
    url='https://github.com/w2sv/asciiplot',
    download_url='https://github.com/w2sv/asciiplot/releases/download/v0.0.3/asciiplot-0.0.3-py3-none-any.whl',
    python_requires='>=3.6',
    install_requires=['colored==1.4.2'],
    author='W2SV',
    author_email='zangenbergjanek@googlemail.com',
    platforms=['Linux', 'Windows', 'MacOS']
)
