from setuptools import setup, find_packages
import os

from asciiplot import __version__


with open(os.path.join(os.getcwd(), 'README.md'), 'r', encoding='utf-8') as f:
    readme_content = f.read()

setup(
    name='asciiplot',
    packages=find_packages(exclude=(["*.tests", "*.tests.*", "tests.*", "tests"])),
    version=__version__,
    # long_description=readme_content,
    # long_description_content_type='text/markdown',
    license='MIT',
    keywords=['plotting', 'terminal', 'console', 'ascii', 'gui', 'data', 'visualization', 'statistics'],
    url='https://github.com/w2sv/asciiplot',
    python_requires='>=3.6',
    install_requires=[
        'colored==1.4.2',
        'more-itertools',
        'dataclasses'
    ],
    author='w2sv',
    author_email='zangenbergjanek@googlemail.com',
    platforms=['Linux', 'Windows', 'MacOS'],
    description='Platform-agnostic, highly customizable sequence plotting in terminal for GUIs'
)



