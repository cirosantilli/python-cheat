#!/usr/bin/env python

"""
At the moment this is a hackish implementation for the question asked at
<http://stackoverflow.com/questions/20842687/rapidly-develop-gui-for-command-line/20998839#20998839>

If this ever gets decente, lets split it into a new repo and make it pip installable.
"""

import Tkinter
import tkFileDialog

class Option(object):
    def __init__(self, optype, name, widget=Tkinter.Entry):
        self.optype = optype
        self.name = name
        if self.optype == 'switch':
            self.widget = Tkinter.Checkbutton
        else:
            self.widget = widget

##INPUT
options = [
    Option("key-value", "--text="),
    Option("switch", "-s"),
    Option("positional", "pos0"),
    Option("positional", "pos1", tkFileDialog.askopenfilename),
]

def askopenfilename(filename):
    filename.set(tkFileDialog.askopenfilename())

# Build command
def ok_func():
    cmd = "cmd_line"
    for option in options:
        if option.optype == "key-value":
            val = tkvars[option.name].get()
            if val:
                cmd += ' '
                cmd += '%s"%s"' % (option.name, val)
        elif option.optype == "switch":
            cmd += ' '
            if tkvars[option.name].get() == 1:
                cmd += option.name
        elif option.optype == "positional":
            val = tkvars[option.name].get()
            if val:
                cmd += ' '
                cmd += val
    print cmd


tkvars = {}
app = Tkinter.Tk()
grid = Tkinter.Frame()
row = 0

# Build GUI
for option in options:
    Tkinter.Label(grid, text=option.name).grid(row=row, column=0, sticky='W')
    if option.widget == Tkinter.Entry:
        tkvars[option.name] = Tkinter.StringVar()
        widget = Tkinter.Entry(
            grid,
            textvariable=tkvars[option.name]
        )
    elif option.widget == Tkinter.Checkbutton:
        tkvars[option.name] = Tkinter.IntVar()
        widget = Tkinter.Checkbutton(
            grid,
            variable = tkvars[option.name],
            onvalue = 1
        )
    elif option.widget == tkFileDialog.askopenfilename:
        tkvars[option.name] = Tkinter.StringVar()
        widget = Tkinter.Button(
            grid,
            text='Browse',
            command=lambda: askopenfilename(tkvars[option.name])
        )
    widget.grid(row=row, column=1, sticky='W')
    row += 1

grid.pack()
Tkinter.Button(app, text="ok", command=ok_func).pack()
Tkinter.Button(app, text="quit", command=app.quit).pack()
app.mainloop()
