import os   #IMPORTS
import curses
import time
import sqlite3 as sl
import sys
from curses.textpad import Textbox, rectangle

con = sl.connect('pantry.db')

menu = ["View Items", "New Item", "Remove Item", "Exit"]


def print_menu(scrn, selected_row_idx): #PRINT MENU
    h, w = scrn.getmaxyx()

    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            scrn.attron(curses.color_pair(1))
            scrn.addstr(y, x, row)
            scrn.attroff(curses.color_pair(1))
        else:
            scrn.addstr(y, x, row)
    scrn.refresh()

def main(scrn): #MAIN

    current_row_idx = 0

    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    print_menu(scrn, current_row_idx)

    while 1:
        key = scrn.getch()
        scrn.clear()
        scrn.refresh()

        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(menu)-1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10,13]:
            scrn.clear()
            if current_row_idx == 0:
                scrn.addstr(0, 0, "ADD VIEW MENU")
            elif current_row_idx == 1:
                add_item(scrn)
            elif current_row_idx == 2:
                scrn.addstr(0, 0, "ADD REMOVE MENU")
            elif current_row_idx == 3:
                scrn.addstr(0,0,"PRESS")
                sys.exit()

        print_menu(scrn, current_row_idx)
        scrn.refresh()

def add_item(scrn): #ADD MENU
    scrn.clear()
    h, w = scrn.getmaxyx()
    x = w//2 
    y = h//2
    add_message = "Add Item To Pantry"
    scrn.addstr(y-1,x - len(add_message)//2, add_message)
    curses.echo()
    curses.textpad.rectangle(scrn, y, x - 10, y + 2, x + 10)
    item = scrn.getstr(y + 1, x - 9, 20)
    item = item.decode('utf-8')
    scrn.clear()

    item_statement = "Quantity of " + item + " to Add"
    scrn.addstr(y-1,x - len(item_statement)//2, item_statement)
    curses.textpad.rectangle(scrn, y, x - 2, y + 2, x+ 1)
    while 1:
        quantity_input = scrn.getstr(y+1,x-1, 2)
        try:
            quantity = int(quantity_input)
            break
        except ValueError:
            not_int = "Enter an Integer"
            scrn.addstr(y + 3, x - len(not_int)//2, not_int)
            continue

    confirmation = str(quantity) + " " + item + " Added"
    scrn.addstr(y+3,x - len(confirmation)//2 ,confirmation)
    cont = "Press Any Button To Continue"
    scrn.addstr(y+4,x - len(cont)//2, cont)
    scrn.getch()
    scrn.clear()

    curses.noecho()
    sql = 'INSERT INTO PANTRY(name, quantity) VALUES (?,?)'

def view_pantry():
    aaaa = 1


curses.wrapper(main)

