from graphics2 import *

win=GraphWin("Editor",1000,670)
win.setBackground('white')

input_box = Entry(Point(500,335), 100)
input_box.draw(win)
txt = Text(Point(500,350), "")
txt.draw(win)


while True:
	txt.setText(input_box.getText())


win.getMouse()
win.close()