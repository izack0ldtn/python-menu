from rich import print
# print('[black on white]Hello')
import os
from msvcrt import getch

list_of_items = ["Apple","Ball","Cat"]
selected = 0
enter_indices = []

def consolePrint():
    os.system('cls')
    for x in range(len(list_of_items)):
        print(entermanager(list_of_items[x]),textManager(list_of_items[x]))

def upselect():
    global selected
    if selected <= 0:
        selected = len(list_of_items)-1
        consolePrint()
    else:
        selected -= 1
        consolePrint()

def downselect():
    global selected
    if selected >= len(list_of_items)-1:
        selected = 0
        consolePrint()
    else:
        selected += 1
        consolePrint()

def entercase():
    if selected not in enter_indices:
        enter_indices.append(selected)
    else:
        enter_indices.remove(selected)
    consolePrint()

def entermanager(text):
    for eachIndex in enter_indices:
        if eachIndex == list_of_items.index(text):
            return '[X]'
    return '[ ]'

def textManager(text):
    if selected == list_of_items.index(text):
        return f"[black on white]{text} "
    else:
        return f"[white]{text}"

consolePrint()

while True:
    key = ord(getch())
    if key == 27: #ESC
        break
    elif key == 13: #Enter
        entercase()
    elif key == 224: #Special keys (arrows, f keys, ins, del, etc.)
        key = ord(getch())
        if key == 80: #Down arrow
            downselect()
        elif key == 72: #Up arrow
            upselect()
