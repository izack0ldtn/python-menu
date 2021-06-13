from consoleMenu import Menu_CheckBox
array = ['a','b','c','d','e']
head = """Hello
World"""
stm = "Please Select One :"
obj = Menu_CheckBox(array,stm,head)
obj.main()
print(obj.get_selected_items())