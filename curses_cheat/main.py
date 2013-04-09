#!/usr/bin/env python
# -*- coding: utf-8 -*-
#?fun=10

"""
make interactive command line interfaces

similar interface to the original c program

this is so **cool**
"""

import curses
import math
import random
import itertools

##global model params

debug = True
#debug = False

#fun only =)

exit_msg = ''

width = 70
height = 20
posx = 1
posy = 1

def init(screen):
    """
    Startup functions that make the terminal work like a gui app.
    """
    screen.border(0)
    screen.clear()      #clears the screen
    curses.noecho()     #don't echo user input
    curses.cbreak()     #no enter to process key
    screen.keypad(1)    #accept special keys such as directionals

    ##curs_set

    #set cursor visibility

    #-0: invisible
    #-1: normal
    #-2: very visible

    curses.curs_set(0)

def cleanup(screen):
    """
    Cleanup actions in case of an exception (typically KeyboardInterrupt),
    or terminal may be left in a messy state.
    """
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin() 
    curses.curs_set(1)

def main(screen):

    global posx, posy, width, height, exit_msg, debug

    while 1:

        #get window width and height and check if is enough
        maxy, maxx = screen.getmaxyx()
        maxy = maxy - 1
        maxx = maxx - 1
        if width > maxx or height > maxy:
            exit_msg = "your terminal is too small\nrequired size: %d x %d\nactual size: %d %d" % ( width, height, maxx, maxy )
            break

        #clear screen
        for y in xrange(maxy):
            screen.addstr(y, 0, maxx * ' ', curses.color_pair(1) ) 

        #draw scene:
        screen.addstr(posy, posx, '@', curses.color_pair(3) ) 

        if debug:
            screen.addstr( height + 2, 0, "%d %d" % (posx,posy), curses.color_pair(2) ) 

        #wait for user to input a character:
        c = screen.getch()

        ##addstr

        #writes string at pos

        #overwrites existing

        if c == ord('q'):
            #quit
            exit_msg = 'quit'
            break

        elif c == ord('l'):
            #right
            screen.addstr(posy,posx,' ')
            posx = min( posx + 1, width )

        elif c == ord('h'):
            #left
            screen.addstr(posy,posx,' ')
            posx = max( posx - 1, 0 )

        elif c == ord('k'):
            #up
            screen.addstr(posy,posx,' ')
            posy = max( posy - 1, 0 )

        elif c == ord('j'):
            #down
            screen.addstr(posy,posx,' ')
            posy = min( posy + 1, height )

        elif c == curses.KEY_HOME:
            #go to 0,0
            screen.addstr(posy,posx,' ')
            posx = 0
            posy = 0

if __name__ == "__main__":

    #creates the window object
    screen = curses.initscr()

    #put everyting in the try, so that if there is an exception,
    #you can cleanup the screen afterwards
    try:

        ##colors

        #must be called if you want to use colors:
        curses.start_color()

        #must come after start_color
        curses.init_pair( 1, curses.COLOR_BLACK, curses.COLOR_BLACK )
        curses.init_pair( 2, curses.COLOR_WHITE, curses.COLOR_BLACK )
        curses.init_pair( 3, curses.COLOR_RED,   curses.COLOR_BLACK )

        init(screen)
        curses.wrapper(main)

    except KeyboardInterrupt:
        print "interrupt"
    except Exception, e:
        print e
    finally:
        cleanup(screen)
        if exit_msg:
            print exit_msg
