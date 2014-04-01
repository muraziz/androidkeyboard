#!/usr/bin/python
import locale
import curses
import subprocess
locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()
keymapping = {
curses.KEY_DOWN:(20,'DOWN'),
curses.KEY_UP:(19, 'UP'),
curses.KEY_LEFT:(21, 'LEFT'),
curses.KEY_RIGHT:(22, 'RIGHT'),
curses.KEY_NPAGE:(93, 'PAGE_DOWN'),
curses.KEY_PPAGE:(92, 'PAGE_UP'),
curses.KEY_BACKSPACE:(4, 'BACKSPACE')}

counter = 0 
def listenKey():
    global counter
    stdscr = curses.initscr()
    stdscr.keypad(1)
    curses.noecho()
    curses.cbreak()
    winheight, winwidth = stdscr.getmaxyx()
    blankspaces = ""
    for i in xrange(0,winwidth):
       blankspaces += " "

    while 1:
       c = stdscr.getch()
       if c in keymapping:
           code, desc = keymapping.get(c)
           calladb(code)
           printtoscreen(stdscr, desc)
           counter += 1
           if counter == winheight-1:
               counter = 0
               stdscr.addstr(0, 0, blankspaces)
           else:
               stdscr.addstr(counter, 0, blankspaces)
           stdscr.refresh()
               
           continue
       if c == ord('q'):
           print "Quitting..."
           curses.nocbreak()
           stdscr.keypad(0)
           curses.echo()
           curses.endwin()
           break
       elif c == ord('\t'):
           calladb(61)
           printtoscreen(stdscr, 'TAB')
       elif c == ord('\n'):
           calladb(66)
           printtoscreen(stdscr, 'ENTER')

def printtoscreen(stdscr, desc):
    stdscr.addstr(counter, 0, str(desc)+" is pressed\n")
        
def calladb(keycode):
    subprocess.call("adb shell input keyevent " + str(keycode), shell=True)
listenKey()
