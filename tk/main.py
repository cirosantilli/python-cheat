#!/usr/bin/env python

import Tkinter

def ok_func():
    print 'entry = ' + entry.get()
    print 'entry_variable = ' + entry_variable_var.get()
    print 'checkbutton = ' + str(checkbutton_var.get())

app = Tkinter.Tk()

#if "##frame":

#if "##grid":

if "##entry":

    # Value can bre retreived both via variables and via `get()` directly.

    grid = Tkinter.Frame(app)
    row = 0

    Tkinter.Label(grid, text="entry").grid(row=row, column=0, sticky='W')
    entry = Tkinter.Entry(grid)
    entry.grid(row=row, column=1)
    row += 1

    entry_variable_var = Tkinter.StringVar()
    Tkinter.Label(grid, text="entry_variable").grid(row=row, column=0, sticky='W')
    entry_variable = Tkinter.Entry(grid, textvariable=entry_variable_var)
    entry_variable.grid(row=row, column=1)
    row += 1

if "##checkbutton":

    # It does not seem possible to get the value wihtout an extra var:
    # <http://stackoverflow.com/questions/4236910/getting-tkinter-check-box-state>

    Tkinter.Label(grid, text="checkbutton").grid(row=row, column=0, sticky='W')
    checkbutton_var = Tkinter.IntVar()
    checkbutton = Tkinter.Checkbutton(
        grid,
        text = "",
        variable = checkbutton_var,
        onvalue = 1
    )
    checkbutton.grid(row=row, column=1, sticky='W')
    row += 1

#if "##open file"

    #import tkFileDialog
    #from tkinter.filedialog import askopenfilename
    #filename = askopenfilename()

##pass argument to callback:

    #lambda: action(someNumber)

grid.pack()
Tkinter.Button(app, text="ok", command=ok_func).pack()
Tkinter.Button(app, text="quit", command=app.quit).pack()
app.mainloop()
