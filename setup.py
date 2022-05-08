""" Reference: https://gist.github.com/gboeing/dcfaf5e13fad16fc500717a3a324ec17 """

from setuptools import setup, find_packages

from asciiplot import __version__


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='asciiplot',
    packages=find_packages(exclude=(["tests"])),
    version=__version__,
    license='MIT',
    description='Platform-agnostic, highly customizable sequence plotting in console, offering high suitability for '
                'GUIs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='plotting, terminal, console, ascii, gui, data, visualization, statistics, sequences',
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
    url='https://github.com/w2sv/asciiplot',
    python_requires='>=3.6',
    install_requires=[
        'colored==1.4.2',
        'more-itertools',
        'dataclasses'
    ],
    author='w2sv',
    author_email='zangenbergjanek@googlemail.com',
    platforms=['Linux', 'Windows', 'MacOS']
)



