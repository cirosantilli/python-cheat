#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
this illustrates how one might go on about managing
collision detection on a curses game
"""

import curses
import math
import random

##global model params

debug = True
#debug = False

#fun only =)

exit_msg = ''

width = 70
height = 20
obstacle_frac = 0.4 #fraction of the screen that will be occupied by obstacles
posx = 1
posy = 1
obstacles = set()

##setup initial scene

obstacles.add( (posx,posy) )

for x in xrange( 0, width ):
    obstacles.add( (x,0) )
    obstacles.add( (x,height) )

for y in xrange( 0, height ):
    obstacles.add( (0,y) )
    obstacles.add( (width,y) )

#add some random obstacles

n_obstacles = math.floor( width * height * obstacle_frac )

while len (obstacles ) < n_obstacles:
    randx = random.randint( 0, width )
    randy = random.randint( 0, height )
    obstacles.add( (randx, randy) )

def init(screen):
    """
    Startup functions that make the terminal work like a gui app.
    """
    screen.border(0)
    screen.clear()     
    curses.noecho()    
    curses.cbreak()    
    screen.keypad(1)   
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

def can_move(posx,posy,newposx,newposy):
    global obstacles
    if not (newposx,newposy) in obstacles:
        return True
    else:
        return False

def main(screen):

    global posx, posy, width, height, obstacles, exit_msg, debug

    newposx = posx
    newposy = posy

    while 1:

        #get window width and height
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
        for obs in obstacles:
            screen.addstr( obs[1], obs[0], '#', curses.color_pair(4) ) 

        screen.addstr(posy, posx, '@', curses.color_pair(3) ) 

        if debug:
            screen.addstr( height + 2, 0, "pos: %d %d newpos: %d %d" % (posx,posy,newposx,newposy), curses.color_pair(2) ) 

        #wait for user to input a character:
        c = screen.getch()

        if c == ord('q'):
            #quit
            exit_msg = 'quit'
            break

        elif c == ord('l'):
            #right
            newposx = posx + 1
            newposy = posy

        elif c == ord('h'):
            #left
            newposx = posx - 1
            newposy = posy

        elif c == ord('k'):
            #up
            newposx = posx
            newposy = posy - 1

        elif c == ord('j'):
            #down
            newposx = posx
            newposy = posy + 1

        elif c == curses.KEY_HOME:
            newposx = 0
            newposy = 0

        if can_move(posx, posy, newposx, newposy):
            posx = newposx
            posy = newposy

if __name__ == "__main__":

    try:
        screen = curses.initscr()

        curses.start_color()

        curses.init_pair( 1, curses.COLOR_BLACK,    curses.COLOR_BLACK )
        curses.init_pair( 2, curses.COLOR_WHITE,    curses.COLOR_BLACK )
        curses.init_pair( 3, curses.COLOR_RED,      curses.COLOR_BLACK )
        curses.init_pair( 4, curses.COLOR_YELLOW,   curses.COLOR_BLACK )

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
