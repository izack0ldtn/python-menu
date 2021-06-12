import os
from rich import print
from msvcrt import getch


class Menu:
    selected = 0
    enter_indices = []
    def __init__(self,array):
        self.arr = array

    def consoleDisplay(self):
        os.system('cls')
        for x in range(len(self.arr)):
            print(self.entermanager(self.arr[x]),self.textManager(self.arr[x]))

    def textManager(self,text):
        if self.selected == self.arr.index(text):
            return f"[black on white]{text} "
        else:
            return f"[white]{text}"

    def upselect(self):
        if self.selected <= 0:
            self.selected = len(self.arr)-1
            self.consoleDisplay()
        else:
            self.selected -= 1
            self.consoleDisplay()

    def downselect(self):
        if self.selected >= len(self.arr)-1:
            self.selected = 0
            self.consoleDisplay()
        else:
            self.selected += 1
            self.consoleDisplay()

    def entercase(self):
        if self.selected not in self.enter_indices:
            self.enter_indices.append(self.selected)
        else:
            self.enter_indices.remove(self.selected)
        self.consoleDisplay()

    def entermanager(self,text):
        for eachIndex in self.enter_indices:
            if eachIndex == self.arr.index(text):
                return '[X]'
        return '[ ]'

    def main(self):
        self.consoleDisplay()
        while True:
            key = ord(getch())
            if key == 27: #ESC
                break
            elif key == 13: #Enter
                self.entercase()
            elif key == 224: #Special keys (arrows, f keys, ins, del, etc.)
                key = ord(getch())
                if key == 80: #Down arrow
                    self.downselect()
                elif key == 72: #Up arrow
                    self.upselect()