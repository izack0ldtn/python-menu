import os
from rich import print
from rich.console import Console
from msvcrt import getch
console = Console()

class Menu_CheckBox:
    selected = 0
    enter_indices = []
    def __init__(self,array,statement,headertext=None):
        self.arr = array
        self.header = headertext
        self.content = statement
    def consoleDisplay(self):
        os.system('cls')
        if self.header != None:
            console.print(self.header,justify="center")
        print()
        console.print(self.content, style ="red")
        print()
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

    def exitcase(self):
        return self.get_selected_items()

    def get_selected_items(self):
        holder = []
        for x in self.enter_indices:
            holder.append(self.arr[x])
        return holder

    def main(self):
        self.consoleDisplay()
        while True:
            key = ord(getch())
            if key == 27: #ESC
                return "CLI"
            elif key == 13: #Enter
                self.entercase()
            elif key == 32 : #Space 
                return self.exitcase()
            elif key == 224: #Special keys (arrows, f keys, ins, del, etc.)
                key = ord(getch())
                if key == 80: #Down arrow
                    self.downselect()
                elif key == 72: #Up arrow
                    self.upselect()
              


class Menu_RadioButton:

    selected = 0

    def __init__(self,array,statement,headertext=None):
        self.arr = array
        self.header = headertext
        self.content = statement
    def consoleDisplay(self):
        os.system('cls')
        if self.header != None:
            print(self.header)
        print()
        console.print(self.content)
        print()
        for eachItems in self.arr:
            print("►",self.textManager(eachItems))

    def upselect(self):
        if self.selected <= 0:
            self.selected = len(self.arr)-1
        else:
            self.selected -= 1
        self.consoleDisplay()

    def downselect(self):
        if self.selected >= len(self.arr)-1:
            self.selected = 0
        else:
            self.selected += 1
        self.consoleDisplay()

    def entercase(self):
        return self.arr[self.selected]

    def textManager(self,text):
        if self.selected == self.arr.index(text):
            return f"[black on white]{text} "
        else:
            return f"[white]{text}"    

    def main(self):
        self.consoleDisplay()
        while True:
            key = ord(getch())
            if key == 27: #ESC
                return "CLI"
            elif key == 13: #Enter
                return self.entercase()
            elif key == 224: #Special keys (arrows, f keys, ins, del, etc.)
                key = ord(getch())
                if key == 80: #Down arrow
                    self.downselect()
                elif key == 72: #Up arrow
                    self.upselect()
