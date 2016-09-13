# in

Every Python file in this dir must implement the `plot` method and can generate only a single figure (`svg`, `png`, etc.).

This will automatically be done with a `Makefile` outside this dir.

If you want to generate more than one plot per file, put the file that will do that outside this dir and customize the makefile.

1.  [Axis](axis.py)
1.  [Label title](label_title.py)
1.  Line style
    1.  [Line points](line_points.py)
    1.  [Tick](tick.py)
1.  Subplots
    1.  [Subplots](subplots.py)
    1.  [Subplots add](subplots_add.py)
1.  [Two lines](two_lines.py)
    1.  [Legend outside](legend_outside.py)
1.  Data from files
    [plotfile](plotfile.py)
