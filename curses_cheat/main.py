#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simple collision detection curses game.
"""

import curses
import math
import random

debug = True
#debug = False
exit_msg = ''

# Global model params:
width = 70
height = 20
# Fraction of the screen that will be occupied by obstacles:
obstacle_frac = 0.3

# Initial state:
posx = 1
posy = 1
obstacles = set()
obstacles.add((posx,posy))
for x in xrange(0, width):
    obstacles.add((x,0))
    obstacles.add((x,height))
for y in xrange(0, height):
    obstacles.add((0,y))
    obstacles.add((width,y))
# Add random obstacles:
n_obstacles = math.floor(width * height * obstacle_frac)
while len (obstacles) < n_obstacles:
    randx = random.randint(0, width)
    randy = random.randint(0, height)
    obstacles.add((randx, randy))

def init(screen):
    """
    Startup functions that make the terminal work like a GUI app.
    """
    screen.border(0)
    screen.clear()
    curses.noecho()
    curses.cbreak()
    screen.keypad(1)
    curses.curs_set(0)

def cleanup(screen):
    """
    Cleanup actions in case of an exception (e.g. KeyboardInterrupt),
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
        # Get window width and height:
        maxy, maxx = screen.getmaxyx()
        maxy = maxy - 1
        maxx = maxx - 1
        if width > maxx or height > maxy:
            exit_msg = "your terminal is too small\nrequired size: %d x %d\nactual size: %d %d" % (width, height, maxx, maxy)
            break

        # Clear screen:
        for y in xrange(maxy):
            screen.addstr(y, 0, maxx * ' ', curses.color_pair(1))

        # Draw scene:
        for obs in obstacles:
            screen.addstr(obs[1], obs[0], '#', curses.color_pair(4))
        screen.addstr(posy, posx, '@', curses.color_pair(3))

        # Print messages;
        screen.addstr(height + 2, 0, "You: '@', obstacles: '#'. Move: 'ASDW'. Quit: 'Q'", curses.color_pair(2))
        if debug:
            screen.addstr(height + 4, 0, "pos: {} {} newpos: {} {}".format(posx,posy,newposx,newposy), curses.color_pair(2))

        # Wait for user to input a character:
        c = screen.getch()
        if c == ord('a'):
            # Left
            newposx = posx - 1
            newposy = posy
        elif c == ord('d'):
            # Right
            newposx = posx + 1
            newposy = posy
        elif c == ord('q'):
            # Quit
            exit_msg = 'quit'
            break
        elif c == ord('s'):
            # Down
            newposx = posx
            newposy = posy + 1
        elif c == ord('w'):
            # Up
            newposx = posx
            newposy = posy - 1
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
        curses.init_pair(1, curses.COLOR_BLACK,  curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_WHITE,  curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_RED,    curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
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
