#!/usr/bin/env python
"""
Plot data from file.

- http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plotfile
- http://stackoverflow.com/questions/11248812/matplotlib-basic-plotting-from-text-file
- http://stackoverflow.com/questions/13545388/plot-data-from-csv-file-with-matplotlib
- http://stackoverflow.com/questions/12311767/how-to-plot-files-with-numpy
"""
import os
def plot(plt, params):
    plt.plotfile(
        os.path.join(os.path.dirname(__file__), 'space.dat'),

        # Which columns to use. First one is x, others y.
        # If only one given, that is y, and x is nrange.
        cols=(0, 1, 2),

        delimiter=' ',

        # Separate plots vs a single one.
        subplots=False,

        # TODO?
        newfig=False,

        # Cannot have header in data.
        # names=('a', 'b', 'c'),
    )

    # Two lines show, but only the second legend.
    # plt.plotfile(
        # os.path.join(os.path.dirname(__file__), 'space.dat'),
        # cols=(0, 2),
        # delimiter=' ',
        # subplots=False,
        # newfig=False,
    # )
