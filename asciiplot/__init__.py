""" Core sequence asciiization algorithm adopted from
kroitor@https://github.com/kroitor/asciichart/blob/master/asciichartpy/__init__.py

Package functionality comprising:
    - wide array of eligible colors thanks to the incorporation of https://pypi.org/project/colored/
    - ability of setting the color of all chart components
    - enablement of cross-platform usage
    - possibility to set a consistent margin between data points through in_between_points_margin
    - determination of chart height
    - possibility of title and axes descriptions display
    - adding of x-axes with determinable labels, possibly being of both numeric and string type
    - centering the resulting plot within the target terminal or indenting it by a passed number of columns respectively """


from asciiplot.version import __version__
from asciiplot._asciiization import asciiize
from asciiplot._coloring import Color
