# itchy.py v0.1- a menu system for using a RasPi with a Adafruit LCD display (PID 181)
# By Merlin04
# Licensed under the MIT license.
#
# Getting started
# 1. Modify the list of items at comment 1.
# 2. Add a function for each menu item. 2 have already been added for you, modify them. Be sure to include a way to use the command 'break'. This will return to the menu. (see comment 2)
# 3. Add the names of the functions to the places labeled 'comment 3'.
#
# That's all there is to it!
# I created this because all the Adafruit LCD menu programs on GitHub were for the Pi Plate, not the plain LCD.
#
# Use the arrow keys to navigate around the menu.
# Press enter to select an item.


from Adafruit_CharLCD import *
import time

lcd = Adafruit_CharLCD()
lcd.clear()

# comment 1
items = ["H1", "H2", "H3", "H4"]

# comment 2
def menu1():
    lcd.message("Hello World!")
    lcd.clear()
    # If ESC key pressed, break

def menu2():
    lcd.clear()
    lcd.message("Hello World! Again!")
    # If ESC key pressed, break

class menu(self, list_of_items):
    def __init__(self):
        self.loi = list_of_items
        self.loi.append("")
        self.current_item = 1
        Menu.drawMenu()

    def drawMenu():
        lcd.clear()
        lcd.message("-" + self.loi[self.current_item] + "\n" + self.loi[self.current_item + 1])

    def nextMenuItem():
        if not(self.current_item = 4)
            self.current_item+=
            Menu.drawMenu()

    def prevMenuItem():
        if not(self.current_item == 1):
            self.current_item-=
            Menu.drawMenu()

    def handle_select():
        if self.current_item == 1:
            menu1() # comment 3
            lcd.clear()
            Menu.drawMenu()
        elif self.current_item == 2:
            menu2() # comment 3
            lcd.clear()
            Menu.drawMenu()
        elif self.current_item == 3:
            menu1() # comment 3
            lcd.clear()
            Menu.drawMenu()
        elif self.current_item == 4:
            menu2() # comment 3
            lcd.clear()
            Menu.drawMenu()
        else:
            lcd.clear()
            lcd.message("  FATAL ERROR")
            time.sleep(3)
            lcd.clear()
            Menu.drawMenu()


def main():
    Menu = menu(items)
    while True:
        if # up arrow pressed:
            Menu.nextMenuItem()
        if # down arrow pressed:
            Menu.prevMenuItem()
        if # enter key pressed:
            Menu.handle_select()

main()
