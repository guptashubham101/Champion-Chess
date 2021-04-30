from graphics import *
import numpy as np
import os

# x0 = [4,2,0,0,0,0,1,3]
# x1 = [6,2,0,0,0,0,1,5]
# x2 = [8,2,0,0,0,0,1,7]
# x3 = [10,2,0,0,0,0,1,9]
# x4 = [12,2,0,0,0,0,1,11]
# x5 = [8,2,0,0,0,0,1,7]
# x6 = [6,2,0,0,0,0,1,5]
# x7 = [4,2,0,0,0,0,1,3]

x0 = [4,2,0,0,0,0,1,3]
x1 = [6,2,0,0,1,0,1,5]
x2 = [8,2,0,0,0,0,1,7]
x3 = [10,2,0,0,0,0,1,9]
x4 = [12,2,10,1,0,0,0,11]
x5 = [8,2,0,0,0,0,1,7]
x6 = [6,2,0,0,0,0,1,5]
x7 = [4,2,0,0,0,0,1,3]

x = [x0,x1,x2,x3,x4,x5,x6,x7]

y0 = [0,0,0,0,0,0,0,0]
y1 = [0,0,0,0,0,0,0,0]
y2 = [0,0,0,0,0,0,0,0]
y3 = [0,0,0,0,0,0,0,0]
y4 = [0,0,0,0,0,0,0,0]
y5 = [0,0,0,0,0,0,0,0]
y6 = [0,0,0,0,0,0,0,0]
y7 = [0,0,0,0,0,0,0,0]

y = [y0,y1,y2,y3,y4,y5,y6,y7]

maxWeight = -99999
minWeight = 99999
checkmateW = 0
checkmateB = 0
isWhiteCheck = False
isblackCheck = False

fileName = 'BoardWeightDictAB.npy'

if os.path.isfile(fileName):
    #print('File exists')
    BoardWeightDictAB = np.load(fileName, allow_pickle=True).item()
else:
    #print('File does not exist')
    BoardWeightDictAB = {}

def set():
	for i in range(8):
		for j in range(8):
			y[i][j] = 0

win = GraphWin("chess", 1000, 670)
win.setBackground('white')

def main():
	global x
	global isWhiteCheck
	global isblackCheck
	
	txt = Text(Point(500,100),"CHESS PYTHON")
	txt.setSize(50)
	txt.draw(win)
	img = Image(Point(500,300), "start.gif")
	img.draw(win)
	txt2 = Text(Point(500,600), "click to start game")
	txt2.setSize(30)
	txt2.draw(win)
	win.getMouse()
	txt.undraw()
	img.undraw()
	txt2.undraw()
	
	board()
	count = 1
	piece = 0
	txt7 = Text(Point(830,50),"CHESS")
	txt7.setSize(30)
	txt7.draw(win)
	knight = Polygon(Point((9*80)+60,(1*80)+90),
					 Point((9*80)+10,(1*80)+90),
					 Point((9*80)+30,(1*80)+50),
					 Point((9*80)+10,(1*80)+60),
					 Point((9*80)+10,(1*80)+45),
					 Point((9*80)+50,(1*80)+25))
	knight.setWidth(5)
	knight.setFill('white')
	knight.draw(win)
	knight1 = Polygon(Point((10*80)+140,(1*80)+90),
					 Point((10*80)+90,(1*80)+90),
					 Point((10*80)+110,(1*80)+50),
					 Point((10*80)+90,(1*80)+60),
					 Point((10*80)+90,(1*80)+45),
					 Point((10*80)+130,(1*80)+25))
	knight1.setWidth(5)
	knight1.setFill('black')
	knight1.draw(win)
	txt5 = Text(Point(770,200),"PLAYER 1")
	txt5.setSize(15)
	txt5.draw(win)
	txt6 = Text(Point(920,200),"PLAYER 2")
	txt6.setSize(15)
	txt6.draw(win)
	txt8 = Text(Point(820,350),"Yellow is cursor\nBlue is selected\nGreen are available\nRed is check\nArrow keys to move the cursor\nEscape to select a piece\nEnter to move the piece")
	txt8.setSize(15)
	txt8.draw(win)

	esc = 0
	x1=0
	y1=0
	x2=80
	y2=80
	i=0
	j=0
	selected = 0
	p = Point(x1,y1)
	q = Point(x2,y2)
	sq = Rectangle(p,q)
	sq.setWidth(10)
	sq.setOutline('yellow')
	sq.draw(win)
	txt4 = Text(Point(825,600), "White's move")
	txt4.setSize(20)
	txt4.draw(win)

	#print('before while checkmateW = ')
	#print(checkmateW is None)
	#print('before while checkmateB = ')
	#print(checkmateB is None)

	while checkmateW == 0 and checkmateB == 0:
		key = win.getKey()
		if key == 'Up' and y1 != 0:
			sq.move(0,-80)
			y1=y1-80
			y2=y2-80
			j=j-1
		elif key == 'Left' and x1 != 0:
			sq.move(-80,0)
			x1=x1-80
			x2=x2-80
			i=i-1
		elif key == 'Right' and x2 != 640:
			sq.move(80,0)
			x1=x1+80
			x2=x2+80
			i=i+1
		elif key == 'Down' and y2 != 640:
			sq.move(0,80)
			y1=y1+80
			y2=y2+80
			j=j+1
		elif key == 'Escape' and esc == 0:
			if count%2 == 1 and x[i][j]%2 == 1:
				if selected == 1:
					x[l][m] = piece
					hideAvailable()
					set()
				sq1 = Rectangle(Point(x1,y1),Point(x2,y2))
				sq1.setWidth(10)
				sq1.setOutline(color_rgb(70,173,212))
				sq1.draw(win)
				l = i
				m = j
				piece = x[i][j]
				getAvailable(x, i,j,x1,y1,x2,y2)
				showAvailable()
				x[i][j]=0
				selected = 1
			elif count%2 == 0:  #and x[i][j]%2 == 0 and x[i][j] > 0:
				# if selected == 1:
				# 	x[l][m] = piece
				# 	hideAvailable()
				# 	set()
				# sq1 = Rectangle(Point(x1,y1),Point(x2,y2))
				# sq1.setWidth(10)
				# sq1.setOutline(color_rgb(70,173,212))
				# sq1.draw(win)
				# l = i
				# m = j
				# piece = x[i][j]
				# getAvailable(x, i,j,x1,y1,x2,y2)
				# showAvailable()
				# x[i][j]=0
				# selected = 1

				# weight, boardMiniMax = minimax(x, 4, 'Black')
				# x = boardMiniMax
				# board()
				# count = count + 1
				selected = 1
		elif key == 'Return':
			if y[i][j] != 0:
				txt4.undraw()
				if count%2 == 0:
					txt4 = Text(Point(825,600), "White's move")
					txt4.setSize(20)
					txt4.draw(win)
				else:
					txt4 = Text(Point(825,600), "Black's move")
					txt4.setSize(20)
					txt4.draw(win)
				if y[i][j] == 1:
					x[i][j] = piece
				if y[i][j] == 2:
					x[i][j] = piece
					x[i+1][j] = 4
					x[i-1][j] = 0
				if y[i][j] == 3:
					x[i][j] = piece
					x[i+1][j] = 3
					x[i-1][j] = 0
				if y[i][j] == 4:
					x[i][j] = piece
					x[i-1][j] = 4
					x[i+1][j] = 0
				if y[i][j] == 5:
					x[i][j] = piece
					x[i-1][j] = 3
					x[i+1][j] = 0
				if y[i][j] == 6:
					x[i][j] = 10
				if y[i][j] == 7:
					x[i][j] = 9
				board()
				p = Point(x1,y1)
				q = Point(x2,y2)
				sq = Rectangle(p,q)
				sq.setWidth(10)
				sq.setOutline('yellow')
				sq.draw(win)
				if count%2 == 0:
					isWhiteCheck = whiteCheck()
					isblackCheck = False
				else:
					isblackCheck = blackCheck()
					isWhiteCheck = False
				count = count+1

				resetMinMax()
				#print('input given to minimax is')
				#print(x)
				set()
				boardMiniMax = minimaxRootAB(4, x, False)
				np.save(fileName, BoardWeightDictAB)
				#weight, boardMiniMax = minimax(x, 4, 'Black')
				x = boardMiniMax
				
				#print('output from minimax is ')
				#print(boardMiniMax)

				board()
				isWhiteCheck = whiteCheck()
				isblackCheck = False
				p = Point(x1,y1)
				q = Point(x2,y2)
				sq = Rectangle(p,q)
				sq.setWidth(10)
				sq.setOutline('yellow')
				sq.draw(win)
				esc = 0
				count = count+1
				piece = 0
				set()
	win.getMouse()
	win.close()


def getAvailable(x, i,j,x1,y1,x2,y2):
	global isWhiteCheck
	global isblackCheck

	relativePosOfKing = "NotRelated"
	if x[i][j]%2 == 0:
		kingValue = 12
	else:
		kingValue = 11
		
	for rowIter in range(i + 1, 8):
		if x[rowIter][j] == kingValue:
			#print("inside relatedFromDown")
			relativePosOfKing = "RelatedFromDown"
			break
		elif x[rowIter][j] != 0:
			break
	for rowIter in range(i-1, -1, -1):
		if x[rowIter][j] == kingValue:
			#print("inside relatedFromUp")
			relativePosOfKing = "RelatedFromUp"
			break
		elif x[rowIter][j] != 0:
			break
	for colIter in range(j + 1, 8):
		if x[i][colIter] == kingValue:
			#print("inside relatedFromRight")
			relativePosOfKing = "RelatedFromRight"
			break
		elif x[i][colIter] != 0:
			break
	for colIter in range(j-1, -1, -1):
		if x[i][colIter] == kingValue:
			#print("inside relatedFromLeft")
			relativePosOfKing = "RelatedFromLeft"
			break
		elif x[i][colIter] != 0:
			break
	for rowIter in range(i + 1, 8):
		for colIter in range(j + 1, 8):
			if rowIter - colIter == i - j and x[rowIter][colIter] == kingValue:
				#print("inside relatedFromDownRight")
				relativePosOfKing = "RelatedFromDownRight"
				break
			elif rowIter - colIter == i - j and x[rowIter][colIter] != 0:
				break
		else:
			continue
		break
	for rowIter in range(i-1, -1, -1):
		for colIter in range(j-1, -1, -1):
			if rowIter - colIter == i - j and x[rowIter][colIter] == kingValue:
				#print("inside relatedFromUpLeft")
				relativePosOfKing = "RelatedFromUpLeft"
				break
			elif rowIter - colIter == i - j and x[rowIter][colIter] != 0:
				break
		else:
			continue
		break
	for rowIter in range(i-1, -1, -1):
		for colIter in range(j + 1, 8):
			if rowIter - i == -1 * (colIter - j) and x[rowIter][colIter] == kingValue:
				#print("inside relatedFromUpRight")
				relativePosOfKing = "RelatedFromUpRight"
				break
			elif rowIter - i == -1 * (colIter - j) and x[rowIter][colIter] != 0:
				break
		else:
			continue
		break
	for rowIter in range(i + 1, 8):
		for colIter in range(j-1, -1, -1):
			if rowIter - i == -1 * (colIter - j) and  x[rowIter][colIter] == kingValue:
				#print("inside relatedFromDownLeft")
				relativePosOfKing = "RelatedFromDownLeft"
				break
			elif rowIter - i == -1 * (colIter - j) and x[rowIter][colIter] != 0:
				break
		else:
			continue
		break

	if x[i][j] == 2:
		if y[i][j+1] == 0 and x[i][j+1] == 0:
			y[i][j+1]=1
		if j == 1 and y[i][j+2] == 0 and x[i][j+2] == 0:
			y[i][j+2]=1
		if i < 7:	
			if x[i+1][j+1]%2 == 1:
				y[i+1][j+1]=1
		if i-1>-1:
			if x[i-1][j+1]%2 == 1:
				y[i-1][j+1]=1
		if j == 6 and x[i][j+1] == 0:
			y[i][j+1]=6
		if j == 6 and i+1<8:
			if x[i+1][j+1]%2 == 1:
				y[i+1][j+1]=6
		if j == 6 and i-1>-1:
			if x[i-1][j+1]%2 == 1:
				y[i-1][j+1]=6
	
	if x[i][j] == 1:
		if y[i][j-1] == 0 and x[i][j-1] == 0:
			y[i][j-1]=1
		if j == 6 and y[i][j-2] == 0 and x[i][j-2] == 0:
			y[i][j-2]=1
		if i-1>-1:	
			if x[i-1][j-1]%2 == 0 and x[i-1][j-1] > 0:
				y[i-1][j-1]=1
		if i < 7:
			if x[i+1][j-1]%2 == 0 and x[i+1][j-1] > 0:
				y[i+1][j-1]=1
		if j == 1 and x[i][j-1] == 0:
			y[i][j-1]=7
		if j == 1 and i+1<8:
			if x[i+1][j-1]%2 == 0 and x[i+1][j-1] > 0:
				y[i+1][j-1]=7
		if j == 1 and i-1>-1:
			if x[i-1][j-1]%2 == 0 and x[i-1][j-1] > 0:
				y[i-1][j-1]=7

	if x[i][j] == 6:
		if i-1>=0 and j+2<=7:
			if (y[i-1][j+2] == 0 or x[i-1][j+2]%2 == 1) and (x[i-1][j+2]%2 != 0 or x[i-1][j+2] == 0):
				y[i-1][j+2]=1
		if i+1<=7 and j+2<=7:
			if (y[i+1][j+2] == 0 or x[i+1][j+2]%2 == 1) and (x[i+1][j+2]%2 != 0 or x[i+1][j+2] == 0):
				y[i+1][j+2]=1
		if i-2>=0 and j+1<=7:
			if (y[i-2][j+1] == 0 or x[i-2][j+1]%2 == 1) and (x[i-2][j+1]%2 != 0 or x[i-2][j+1] == 0):
				y[i-2][j+1]=1
		if i+2<=7 and j+1<=7:
			if (y[i+2][j+1] == 0 or x[i+2][j+1]%2 == 1) and (x[i+2][j+1]%2 != 0 or x[i+2][j+1] == 0):
				y[i+2][j+1]=1
		if i-1>=0 and j-2>=0:
			if (y[i-1][j-2] == 0 or x[i-1][j-2]%2 == 1) and (x[i-1][j-2]%2 != 0 or x[i-1][j-2] == 0):
				y[i-1][j-2]=1
		if i+1<=7 and j-2>=0:
			if (y[i+1][j-2] == 0 or x[i+1][j-2]%2 == 1) and (x[i+1][j-2]%2 != 0 or x[i+1][j-2] == 0):
				y[i+1][j-2]=1
		if i-2>=0 and j-1>=0:
			if (y[i-2][j-1] == 0 or x[i-2][j-1]%2 == 1) and (x[i-2][j-1]%2 != 0 or x[i-2][j-1] == 0):
				y[i-2][j-1]=1
		if i+2<=7 and j-1>=0:
			if (y[i+2][j-1] == 0 or x[i+2][j-1]%2 == 1) and (x[i+2][j-1]%2 != 0 or x[i+2][j-1] == 0):
				y[i+2][j-1]=1

	if x[i][j] == 5:
		if i-1>=0 and j+2<=7:
			if (y[i-1][j+2] == 0 or x[i-1][j+2]%2 == 0) and (x[i-1][j+2]%2 != 1 or x[i-1][j+2] == 0):
				y[i-1][j+2]=1
		if i+1<=7 and j+2<=7:
			if (y[i+1][j+2] == 0 or x[i+1][j+2]%2 == 0) and (x[i+1][j+2]%2 != 1 or x[i+1][j+2] == 0):
				y[i+1][j+2]=1
		if i-2>=0 and j+1<=7:
			if (y[i-2][j+1] == 0 or x[i-2][j+1]%2 == 0) and (x[i-2][j+1]%2 != 1 or x[i-2][j+1] == 0):
				y[i-2][j+1]=1
		if i+2<=7 and j+1<=7:
			if (y[i+2][j+1] == 0 or x[i+2][j+1]%2 == 0) and (x[i+2][j+1]%2 != 1 or x[i+2][j+1] == 0):
				y[i+2][j+1]=1
		if i-1>=0 and j-2>=0:
			if (y[i-1][j-2] == 0 or x[i-1][j-2]%2 == 0) and (x[i-1][j-2]%2 != 1 or x[i-1][j-2] == 0):
				y[i-1][j-2]=1
		if i+1<=7 and j-2>=0:
			if (y[i+1][j-2] == 0 or x[i+1][j-2]%2 == 0) and (x[i+1][j-2]%2 != 1 or x[i+1][j-2] == 0):
				y[i+1][j-2]=1
		if i-2>=0 and j-1>=0:
			if (y[i-2][j-1] == 0 or x[i-2][j-1]%2 == 0) and (x[i-2][j-1]%2 != 1 or x[i-2][j-1] == 0):
				y[i-2][j-1]=1
		if i+2<=7 and j-1>=0:
			if (y[i+2][j-1] == 0 or x[i+2][j-1]%2 == 0) and (x[i+2][j-1]%2 != 1 or x[i+2][j-1] == 0):
				y[i+2][j-1]=1

	if x[i][j] == 4:
		for p in range(1,8):
			if 	j+p<8 and x[i][j+p] == 0:
				y[i][j+p] = 1
			if j+p<8 and x[i][j+p]%2 == 1:
				y[i][j+p] = 1
				break
			if j+p<8 and x[i][j+p]%2 == 0 and x[i][j+p] > 0:
				break
		for p in range(1,8):
			if 	j-p>-1 and x[i][j-p] == 0:
				y[i][j-p] = 1
			if j-p>-1 and x[i][j-p]%2 == 1:
				y[i][j-p] = 1
				break
			if j-p>-1 and x[i][j-p]%2 == 0 and x[i][j-p] > 0:
				break
		for p in range(1,8):
			if 	i+p<8 and x[i+p][j] == 0:
				y[i+p][j] = 1
			if i+p<8 and x[i+p][j]%2 == 1:
				y[i+p][j] = 1
				break
			if i+p<8 and x[i+p][j]%2 == 0 and x[i+p][j] > 0:
				break
		for p in range(1,8):
			if 	i-p>-1 and x[i-p][j] == 0:
				y[i-p][j] = 1
			if i-p>-1 and x[i-p][j]%2 == 1:
				y[i-p][j] = 1
				break
			if i-p>-1 and x[i-p][j]%2 == 0 and x[i-p][j] > 0:
				break

	if x[i][j] == 3:
		for p in range(1,8):
			if 	j+p<8 and x[i][j+p] == 0:
				y[i][j+p] = 1
			if j+p<8 and x[i][j+p]%2 == 0 and x[i][j+p] > 0:
				y[i][j+p] = 1
				break
			if j+p<8 and x[i][j+p]%2 == 1:
				break
		for p in range(1,8):
			if 	j-p>-1 and x[i][j-p] == 0:
				y[i][j-p] = 1
			if j-p>-1 and x[i][j-p]%2 == 0 and x[i][j-p] > 0:
				y[i][j-p] = 1
				break
			if j-p>-1 and x[i][j-p]%2 == 1:
				break
		for p in range(1,8):
			if 	i+p<8 and x[i+p][j] == 0:
				y[i+p][j] = 1
			if i+p<8 and x[i+p][j]%2 == 0 and x[i+p][j] > 0:
				y[i+p][j] = 1
				break
			if i+p<8 and x[i+p][j]%2 == 1:
				break
		for p in range(1,8):
			if 	i-p>-1 and x[i-p][j] == 0:
				y[i-p][j] = 1
			if i-p>-1 and x[i-p][j]%2 == 0 and x[i-p][j] > 0:
				y[i-p][j] = 1
				break
			if i-p>-1 and x[i-p][j]%2 == 1:
				break

	if x[i][j] == 8:
		for p in range(1,8):
			if 	j+p<8 and i+p<8 and x[i+p][j+p] == 0:
				y[i+p][j+p] = 1
			if j+p<8 and i+p<8 and x[i+p][j+p]%2 == 1:
				y[i+p][j+p] = 1
				break
			if j+p<8 and i+p<8 and x[i+p][j+p]%2 == 0 and x[i+p][j+p] > 0:
				break
		for p in range(1,8):
			if 	i-p>-1 and j-p>-1 and x[i-p][j-p] == 0:
				y[i-p][j-p] = 1
			if j-p>-1 and i-p>-1 and x[i-p][j-p]%2 == 1:
				y[i-p][j-p] = 1
				break
			if j-p>-1 and i-p>-1 and x[i-p][j-p]%2 == 0 and x[i-p][j-p] > 0:
				break
		for p in range(1,8):
			if 	i+p<8 and j-p>-1 and x[i+p][j-p] == 0:
				y[i+p][j-p] = 1
			if i+p<8 and j-p>-1 and x[i+p][j-p]%2 == 1:
				y[i+p][j-p] = 1
				break
			if i+p<8 and j-p>-1 and x[i+p][j-p]%2 == 0 and x[i+p][j-p] > 0:
				break
		for p in range(1,8):
			if 	i-p>-1 and j+p<8 and x[i-p][j+p] == 0:
				y[i-p][j+p] = 1
			if i-p>-1 and j+p<8 and x[i-p][j+p]%2 == 1:
				y[i-p][j+p] = 1
				break
			if i-p>-1 and j+p<8 and x[i-p][j+p]%2 == 0 and x[i-p][j+p] > 0:
				break

	if x[i][j] == 7:
		for p in range(1,8):
			if 	j+p<8 and i+p<8 and x[i+p][j+p] == 0:
				y[i+p][j+p] = 1
			if j+p<8 and i+p<8 and x[i+p][j+p]%2 == 0 and x[i+p][j+p] > 0:
				y[i+p][j+p] = 1
				break
			if j+p<8 and i+p<8 and x[i+p][j+p]%2 == 1:
				break
		for p in range(1,8):
			if 	j-p>-1 and i-p>-1 and x[i-p][j-p] == 0:
				y[i-p][j-p] = 1
			if j-p>-1 and i-p>-1 and x[i-p][j-p]%2 == 0 and x[i-p][j-p] > 0:
				y[i-p][j-p] = 1
				break
			if j-p>-1 and i-p>-1 and x[i-p][j-p]%2 == 1:
				break
		for p in range(1,8):
			if 	i+p<8 and j-p>-1 and x[i+p][j-p] == 0:
				y[i+p][j-p] = 1
			if i+p<8 and j-p>-1 and x[i+p][j-p]%2 == 0 and x[i+p][j-p] > 0:
				y[i+p][j-p] = 1
				break
			if i+p<8 and j-p>-1 and x[i+p][j-p]%2 == 1:
				break
		for p in range(1,8):
			if 	i-p>-1 and j+p<8 and x[i-p][j+p] == 0:
				y[i-p][j+p] = 1
			if i-p>-1 and j+p<8 and x[i-p][j+p]%2 == 0 and x[i-p][j+p] > 0:
				y[i-p][j+p] = 1
				break
			if i-p>-1 and j+p<8 and x[i-p][j+p]%2 == 1:
				break

	if x[i][j] == 10:
		for p in range(1,8):
			if 	j+p<8 and i+p<8 and x[i+p][j+p] == 0:
				y[i+p][j+p] = 1
			if j+p<8 and i+p<8 and x[i+p][j+p]%2 == 1:
				y[i+p][j+p] = 1
				break
			if j+p<8 and i+p<8 and x[i+p][j+p]%2 == 0 and x[i+p][j+p] > 0:
				break
		for p in range(1,8):
			if 	i-p>-1 and j-p>-1 and x[i-p][j-p] == 0:
				y[i-p][j-p] = 1
			if j-p>-1 and i-p>-1 and x[i-p][j-p]%2 == 1:
				y[i-p][j-p] = 1
				break
			if j-p>-1 and i-p>-1 and x[i-p][j-p]%2 == 0 and x[i-p][j-p] > 0:
				break
		for p in range(1,8):
			if 	i+p<8 and j-p>-1 and x[i+p][j-p] == 0:
				y[i+p][j-p] = 1
			if i+p<8 and j-p>-1 and x[i+p][j-p]%2 == 1:
				y[i+p][j-p] = 1
				break
			if i+p<8 and j-p>-1 and x[i+p][j-p]%2 == 0 and x[i+p][j-p] > 0:
				break
		for p in range(1,8):
			if 	i-p>-1 and j+p<8 and x[i-p][j+p] == 0:
				y[i-p][j+p] = 1
			if i-p>-1 and j+p<8 and x[i-p][j+p]%2 == 1:
				y[i-p][j+p] = 1
				break
			if i-p>-1 and j+p<8 and x[i-p][j+p]%2 == 0 and x[i-p][j+p] > 0:
				break
		for p in range(1,8):
			if 	j+p<8 and x[i][j+p] == 0:
				y[i][j+p] = 1
			if j+p<8 and x[i][j+p]%2 == 1:
				y[i][j+p] = 1
				break
			if j+p<8 and x[i][j+p]%2 == 0 and x[i][j+p] > 0:
				break
		for p in range(1,8):
			if 	j-p>-1 and x[i][j-p] == 0:
				y[i][j-p] = 1
			if j-p>-1 and x[i][j-p]%2 == 1:
				y[i][j-p] = 1
				break
			if j-p>-1 and x[i][j-p]%2 == 0 and x[i][j-p] > 0:
				break
		for p in range(1,8):
			if 	i+p<8 and x[i+p][j] == 0:
				y[i+p][j] = 1
			if i+p<8 and x[i+p][j]%2 == 1:
				y[i+p][j] = 1
				break
			if i+p<8 and x[i+p][j]%2 == 0 and x[i+p][j] > 0:
				break
		for p in range(1,8):
			if 	i-p>-1 and x[i-p][j] == 0:
				y[i-p][j] = 1
			if i-p>-1 and x[i-p][j]%2 == 1:
				y[i-p][j] = 1
				break
			if i-p>-1 and x[i-p][j]%2 == 0 and x[i-p][j] > 0:
				break

	if x[i][j] == 9:
		for p in range(1,8):
			if 	j+p<8 and i+p<8 and x[i+p][j+p] == 0:
				y[i+p][j+p] = 1
			if j+p<8 and i+p<8 and x[i+p][j+p]%2 == 0 and x[i+p][j+p] > 0:
				y[i+p][j+p] = 1
				break
			if j+p<8 and i+p<8 and x[i+p][j+p]%2 == 1:
				break
		for p in range(1,8):
			if 	j-p>-1 and i-p>-1 and x[i-p][j-p] == 0:
				y[i-p][j-p] = 1
			if j-p>-1 and i-p>-1 and x[i-p][j-p]%2 == 0 and x[i-p][j-p] > 0:
				y[i-p][j-p] = 1
				break
			if j-p>-1 and i-p>-1 and x[i-p][j-p]%2 == 1:
				break
		for p in range(1,8):
			if 	i+p<8 and j-p>-1 and x[i+p][j-p] == 0:
				y[i+p][j-p] = 1
			if i+p<8 and j-p>-1 and x[i+p][j-1]%2 == 0 and x[i+p][j-p] > 0:
				y[i+p][j-p] = 1
				break
			if i+p<8 and j-p>-1 and x[i+p][j-p]%2 == 1:
				break
		for p in range(1,8):
			if 	i-p>-1 and j+p<8 and x[i-p][j+p] == 0:
				y[i-p][j+p] = 1
			if i-p>-1 and j+p<8 and x[i-p][j+p]%2 == 0 and x[i-p][j+p] > 0:
				y[i-p][j+p] = 1
				break
			if i-p>-1 and j+p<8 and x[i-p][j+p]%2 == 1:
				break
		for p in range(1,8):
			if 	j+p<8 and x[i][j+p] == 0:
				y[i][j+p] = 1
			if j+p<8 and x[i][j+p]%2 == 0 and x[i][j+p] > 0:
				y[i][j+p] = 1
				break
			if j+p<8 and x[i][j+p]%2 == 1:
				break
		for p in range(1,8):
			if 	j-p>-1 and x[i][j-p] == 0:
				y[i][j-p] = 1
			if j-p>-1 and x[i][j-p]%2 == 0 and x[i][j-p] > 0:
				y[i][j-p] = 1
				break
			if j-p>-1 and x[i][j-p]%2 == 1:
				break
		for p in range(1,8):
			if 	i+p<8 and x[i+p][j] == 0:
				y[i+p][j] = 1
			if i+p<8 and x[i+p][j]%2 == 0 and x[i+p][j] > 0:
				y[i+p][j] = 1
				break
			if i+p<8 and x[i+p][j]%2 == 1:
				break
		for p in range(1,8):
			if 	i-p>-1 and x[i-p][j] == 0:
				y[i-p][j] = 1
			if i-p>-1 and x[i-p][j]%2 == 0 and x[i-p][j] > 0:
				y[i-p][j] = 1
				break
			if i-p>-1 and x[i-p][j]%2 == 1:
				break

	if x[i][j] == 12:
		if 	j+1<8 and i+1<8 and (x[i+1][j+1] == 0 or x[i+1][j+1]%2 == 1):
			f = checkparticularB(i+1,j+1)
			if f == 1:
				y[i+1][j+1] = 1
		
		if 	i-1>-1 and j-1>-1 and (x[i-1][j-1] == 0 or x[i-1][j-1]%2 == 1):
			f = checkparticularB(i-1,j-1)
			if f == 1:
				y[i-1][j-1] = 1
		
		if 	i+1<8 and j-1>-1 and (x[i+1][j-1] == 0 or x[i+1][j-1]%2 == 1):
			f = checkparticularB(i+1,j-1)
			if f == 1:
				y[i+1][j-1] = 1
		
		if 	i-1>-1 and j+1<8 and (x[i-1][j+1] == 0 or x[i-1][j+1]%2 == 1):
			f = checkparticularB(i-1,j+1)
			if f == 1:
				y[i-1][j+1] = 1
		
		if 	j+1<8 and (x[i][j+1] == 0 or x[i][j+1]%2 == 1):
			f = checkparticularB(i,j+1)
			if f == 1:
				y[i][j+1] = 1
		
		if 	j-1>-1 and (x[i][j-1] == 0 or x[i][j-1]%2 == 1):
			f = checkparticularB(i,j-1)
			if f == 1:
				y[i][j-1] = 1
		
		if 	i+1<8 and (x[i+1][j] == 0 or x[i+1][j]%2 == 1):
			f = checkparticularB(i+1,j)
			if f == 1:
				y[i+1][j+1] = 1
		
		if 	i-1>-1 and (x[i-1][j] == 0 or x[i-1][j]%2 == 1):
			f = checkparticularB(i-1,j)
			if f == 1:
				y[i-1][j] = 1
		
		if i == 4 and j == 0 and x[i-1][j] == 0 and x[i-2][j] == 0 and x[i-3][j] == 0 and x[i-4][j] == 4:
			y[i-3][j] = 2
		if i == 4 and j == 0 and x[i+1][j] == 0 and x[i+2][j] == 0 and x[i+3][j] == 4:
			y[i+2][j] = 4

	if x[i][j] == 11:
		if 	j+1<8 and i+1<8 and x[i+1][j+1]%2 == 0:
			f = checkparticularW(i+1,j+1)
			if f == 1:
				y[i+1][j+1] = 1

		if 	i-1>-1 and j-1>-1 and x[i-1][j-1]%2 == 0:
			f = checkparticularW(i-1,j-1)
			if f == 1:
				y[i-1][j-1] = 1
		
		if i+1<8 and j-1>-1 and x[i+1][j-1]%2 == 0:
			f = checkparticularW(i+1,j-1)
			if f == 1:
				y[i+1][j-1] = 1
		
		if i-1>-1 and j+1<8 and x[i-1][j+1]%2 == 0:
			f = checkparticularW(i-1,j+1)
			if f == 1:
				y[i-1][j+1] = 1
		
		if j+1<8 and x[i][j+1]%2 == 0:
			f = checkparticularW(i,j+1)
			if f == 1:
				y[i][j+1] = 1
		
		if j-1>-1 and x[i][j-1]%2 == 0:
			f = checkparticularW(i,j-1)
			if f == 1:
				y[i][j-1] = 1
		
		if i+1<8 and x[i+1][j]%2 == 0:
			f = checkparticularW(i+1,j)
			if f == 1:
				y[i+1][j] = 1
		
		if i-1>-1 and x[i-1][j]%2 == 0:
			f = checkparticularW(i-1,j)
			if f == 1:
				y[i-1][j] = 1

		if i == 4 and j == 7 and x[i-1][j] == 0 and x[i-2][j] == 0 and x[i-3][j] == 0 and x[i-4][j] == 3:
			y[i-3][j] = 3
		if i == 4 and j == 7 and x[i+1][j] == 0 and x[i+2][j] == 0 and x[i+3][j] == 3:
			y[i+2][j] = 5

	safeToMove = True

	if relativePosOfKing != "NotRelated":
		#print("relation with respect to board")
		#print(x)
		#print("for piece")
		#print(x[i][j])
		#print("and position")
		#print(str(i) + " , " + str(j))
		pass

	if relativePosOfKing == "RelatedFromDown":
		for rowIter in range(i-1, -1, -1):
			if x[rowIter][j] in [9 + x[i][j]%2, 3 + x[i][j]%2]:
				#print("piece creating danger")
				#print(x[rowIter][j])
				#print("at position")
				#print(str(rowIter) + " , " + str(j))
				#print("y before modification is")
				#print(y)
				safeToMove = False
				break
			elif x[rowIter][j] != 0:
				break
		if not safeToMove:
			for rowIter in range(0, 8):
				for colIter in range(0, 8):
					if colIter != j:
						y[rowIter][colIter] = 0
	if relativePosOfKing == "RelatedFromUp":
		for rowIter in range(i, 7):
			if x[rowIter][j] in [9 + x[i][j]%2, 3 + x[i][j]%2]:
				#print("piece creating danger")
				#print(x[rowIter][j])
				#print("at position")
				#print(str(rowIter) + " , " + str(j))
				#print("y before modification is")
				#print(y)
				safeToMove = False
				break
			elif x[rowIter][j] != 0:
				break
		if not safeToMove:
			for rowIter in range(0, 8):
				for colIter in range(0, 8):
					if colIter != j:
						y[rowIter][colIter] = 0
	if relativePosOfKing == "RelatedFromRight":
		for colIter in range(j-1, -1, -1):
			if x[i][colIter] in [9 + x[i][j]%2, 3 + x[i][j]%2]:
				#print("piece creating danger")
				#print(x[i][colIter])
				#print("at position")
				#print(str(i) + " , " + str(colIter))
				#print("y before modification is")
				#print(y)
				safeToMove = False
				break
			elif x[i][colIter] != 0:
				break
		if not safeToMove:
			for rowIter in range(0, 8):
				for colIter in range(0, 8):
					if rowIter != i:
						y[rowIter][colIter] = 0
	if relativePosOfKing == "RelatedFromLeft":
		for colIter in range(j+1, 8):
			if x[i][colIter] in [9 + x[i][j]%2, 3 + x[i][j]%2]:
				#print("piece creating danger")
				#print(x[i][colIter])
				#print("at position")
				#print(str(i) + " , " + str(colIter))
				#print("y before modification is")
				#print(y)
				safeToMove = False
				break
			elif x[i][colIter] != 0:
				break
		if not safeToMove:
			for rowIter in range(0, 8):
				for colIter in range(0, 8):
					if rowIter != i:
						y[rowIter][colIter] = 0		
	if relativePosOfKing == "RelatedFromDownRight":
		for rowIter in range(i-1, -1, -1):
			for colIter in range(j-1, -1, -1):
				if rowIter - colIter == i - j and x[rowIter][colIter] in [9 + x[i][j]%2, 7 + x[i][j]%2]:
					#print("piece creating danger")
					#print(x[rowIter][colIter])
					#print("at position")
					#print(str(rowIter) + " , " + str(colIter))
					#print("y before modification is")
					#print(y)
					safeToMove = False
					break
				elif rowIter - colIter == i - j and x[rowIter][colIter] != 0:
					break
			# else:
			# 	continue
			# break
		if not safeToMove:
			for rowIter in range(0, 8):
				for colIter in range(0, 8):
					if rowIter - colIter != i - j:
						y[rowIter][colIter] = 0
	if relativePosOfKing == "RelatedFromUpLeft":
		for rowIter in range(i+1, 8):
			for colIter in range(j+1, 8):
				if rowIter - colIter == i - j and x[rowIter][colIter] in [9 + x[i][j]%2, 7 + x[i][j]%2]:
					#print("piece creating danger")
					#print(x[rowIter][colIter])
					#print("at position")
					#print(str(rowIter) + " , " + str(colIter))
					#print("y before modification is")
					#print(y)
					safeToMove = False
					break
				elif rowIter - colIter == i - j and x[rowIter][colIter] != 0:
					break
			# else:
			# 	continue
			# break
		if not safeToMove:
			for rowIter in range(0, 8):
				for colIter in range(0, 8):
					if rowIter - colIter != i - j:
						y[rowIter][colIter] = 0
	if relativePosOfKing == "RelatedFromUpRight":
		for rowIter in range(i, 8):
			for colIter in range(j-1, -1, -1):
				if rowIter - i == -1 * (colIter - j) and x[rowIter][colIter] in [9 + x[i][j]%2, 7 + x[i][j]%2]:
					#print("piece creating danger")
					#print(x[rowIter][colIter])
					#print("at position")
					#print(str(rowIter) + " , " + str(colIter))
					#print("y before modification is")
					#print(y)
					safeToMove = False
					break
				elif rowIter - i == -1 * (colIter - j) and x[rowIter][colIter] != 0:
					break
			# else:
			# 	continue
			# break
		if not safeToMove:
			for rowIter in range(0, 8):
				for colIter in range(0, 8):
					if rowIter - i != -1 * (colIter - j):
						y[rowIter][colIter] = 0
	if relativePosOfKing == "RelatedFromDownLeft":
		for rowIter in range(i-1, -1, -1):
			for colIter in range(j, 8):
				if rowIter - i == -1 * (colIter - j) and x[rowIter][colIter] in [9 + x[i][j]%2, 7 + x[i][j]%2]:
					#print("piece creating danger")
					#print(x[rowIter][colIter])
					#print("at position")
					#print(str(rowIter) + " , " + str(colIter))
					#print("y before modification is")
					#print(y)
					safeToMove = False
					break
				elif rowIter - i == -1 * (colIter - j) and x[rowIter][colIter] != 0:
					break
			# else:
			# 	continue
			# break
		if not safeToMove:
			for rowIter in range(0, 8):
				for colIter in range(0, 8):
					if rowIter - i != -1 * (colIter - j):
						y[rowIter][colIter] = 0
	
	if (isWhiteCheck or isblackCheck) and x[i][j] not in [11, 12]:
		kingIsCheckedFrom = ""
		for rowIter in range(0, 8):
			for colIter in range(0, 8):
				if (x[rowIter][colIter] == 11 and isWhiteCheck) or (x[rowIter][colIter] == 12 and isblackCheck):
					kingX = rowIter
					kingY = colIter
					break
			else:
				continue
			break

		for rowIter in range(kingX + 1, 8):
			if x[rowIter][kingY] in [9 + x[i][j] % 2, 3 + x[i][j] % 2]:
				kingIsCheckedFrom = kingIsCheckedFrom + "|Down|"
				checkFromX = rowIter
				checkFromY = kingY
				break
			elif x[rowIter][kingY] != 0:
				break
		for rowIter in range(kingX - 1, -1, -1):
			if x[rowIter][kingY] in [9 + x[i][j] % 2, 3 + x[i][j] % 2]:
				kingIsCheckedFrom = kingIsCheckedFrom + "|Up|"
				checkFromX = rowIter
				checkFromY = kingY
				break
			elif x[rowIter][kingY] != 0:
				break
		for colIter in range(kingY + 1, 8):
			if x[kingX][colIter] in [9 + x[i][j] % 2, 3 + x[i][j] % 2]:
				kingIsCheckedFrom = kingIsCheckedFrom + "|Right|"
				checkFromX = kingX
				checkFromY = colIter
				break
			elif x[kingX][colIter] != 0:
				break
		for colIter in range(kingY - 1, -1, -1):
			if x[kingX][colIter] in [9 + x[i][j] % 2, 3 + x[i][j] % 2]:
				kingIsCheckedFrom = kingIsCheckedFrom + "|Left|"
				checkFromX = kingX
				checkFromY = colIter
				break
			elif x[kingX][colIter] != 0:
				break
		for rowIter in range(kingX + 1, 8):
			for colIter in range(kingY + 1, 8):
				if rowIter - colIter == kingX - kingY and x[rowIter][colIter] in [9 + x[i][j] % 2, 7 + x[i][j] % 2]:
					kingIsCheckedFrom = kingIsCheckedFrom + "|DownRight|"
					checkFromX = rowIter
					checkFromY = colIter
					break
				elif rowIter - colIter == kingX - kingY and x[rowIter][colIter] != 0:
					break
			else:
				continue
			break
		for rowIter in range(kingX - 1, -1, -1):
			for colIter in range(kingY - 1, -1, -1):
				if rowIter - colIter == kingX - kingY and x[rowIter][colIter] in [9 + x[i][j] % 2, 7 + x[i][j] % 2]:
					kingIsCheckedFrom = kingIsCheckedFrom + "|UpLeft|"
					checkFromX = rowIter
					checkFromY = colIter
					break
				elif rowIter - colIter == kingX - kingY and x[rowIter][colIter] != 0:
					break
			else:
				continue
			break
		for rowIter in range(kingX + 1, 8):
			for colIter in range(kingY - 1, -1, -1):
				if rowIter - kingX == -1 * (colIter - kingY) and x[rowIter][colIter] in [9 + x[i][j] % 2, 7 + x[i][j] % 2]:
					kingIsCheckedFrom = kingIsCheckedFrom + "|DownLeft|"
					checkFromX = rowIter
					checkFromY = colIter
					break
				elif rowIter - kingX == -1 * (colIter - kingY) and x[rowIter][colIter] != 0:
					break
			else:
				continue
			break
		for rowIter in range(kingX - 1, -1, -1):
			for colIter in range(kingY + 1, 8):
				if rowIter - kingX == -1 * (colIter - kingY) and x[rowIter][colIter] in [9 + x[i][j] % 2, 7 + x[i][j] % 2]:
					kingIsCheckedFrom = kingIsCheckedFrom + "|UpRight|"
					checkFromX = rowIter
					checkFromY = colIter
					break
				elif rowIter - kingX == -1 * (colIter - kingY) and x[rowIter][colIter] != 0:
					break
			else:
				continue
			break
		if kingX+2<8 and kingY+1<8 and x[kingX+2][kingY+1] == 5 + x[i][j] % 2:
			kingIsCheckedFrom = kingIsCheckedFrom + "|Down2Right1|"
		if kingX+2<8 and kingY-1>-1 and x[kingX+2][kingY-1] == 5 + x[i][j] % 2:
			kingIsCheckedFrom = kingIsCheckedFrom + "|Down2Left1|"
		if kingX-2>-1 and kingY+1<8 and x[kingX-2][kingY+1] == 5 + x[i][j] % 2:
			kingIsCheckedFrom = kingIsCheckedFrom + "|Up2Right1|"
		if kingX-2>-1 and kingY-1>-1 and x[kingX-2][kingY-1] == 5 + x[i][j] % 2:
			kingIsCheckedFrom = kingIsCheckedFrom + "|Up2Left1|"
		if kingX+1<8 and kingY+2<8 and x[kingX+1][kingY+2] == 5 + x[i][j] % 2:
			kingIsCheckedFrom = kingIsCheckedFrom + "|Down1Right2|"
		if kingX+1<8 and kingY-2>-1 and x[kingX+1][kingY-2] == 5 + x[i][j] % 2:
			kingIsCheckedFrom = kingIsCheckedFrom + "|Down1Left2|"
		if kingX-1>-1 and kingY+2<8 and x[kingX-1][kingY+2] == 5 + x[i][j] % 2:
			kingIsCheckedFrom = kingIsCheckedFrom + "|Up1Right2|"
		if kingX-1>-1 and kingY-2>-1 and x[kingX-1][kingY-2] == 5 + x[i][j] % 2:
			kingIsCheckedFrom = kingIsCheckedFrom + "|Up1Left2|"

		if kingIsCheckedFrom.count("|") > 2:
			for rowIter in range(0, 8):
				for colIter in range(0, 8):
					y[rowIter][colIter] = 0
		elif kingIsCheckedFrom == "|Down|":
			for rowIter in range(0, 8):
				for colIter in range(0, 8):
					if kingY != colIter or rowIter < kingX or rowIter > checkFromX:
						y[rowIter][colIter] = 0
		elif kingIsCheckedFrom == "|Up|":
			for rowIter in range(0, 8):
				for colIter in range(0, 8):
					if kingY != colIter or rowIter > kingX or rowIter < checkFromX:
						y[rowIter][colIter] = 0
		elif kingIsCheckedFrom == "|Right|":
			for rowIter in range(0, 8):
				for colIter in range(0, 8):
					if kingX != rowIter or colIter < kingY or colIter > checkFromY:
						y[rowIter][colIter] = 0
		elif kingIsCheckedFrom == "|Left|":
			for rowIter in range(0, 8):
				for colIter in range(0, 8):
					if kingX != rowIter or colIter > kingY or colIter < checkFromY:
						y[rowIter][colIter] = 0
		elif kingIsCheckedFrom == "|DownRight|":
			for rowIter in range(0, 8):
				for colIter in range(0, 8):
					if colIter < kingY or rowIter < kingX or kingX - kingY != rowIter-colIter or rowIter > checkFromX or colIter > checkFromY:
						y[rowIter][colIter] = 0
		elif kingIsCheckedFrom == "|UpLeft|":
			for rowIter in range(0, 8):
				for colIter in range(0, 8):
					if colIter > kingY or rowIter > kingX or kingX - kingY != rowIter-colIter or rowIter < checkFromX or colIter < checkFromY:
						y[rowIter][colIter] = 0
		elif kingIsCheckedFrom == "|DownLeft|":
			for rowIter in range(0, 8):
				for colIter in range(0, 8):
					if colIter > kingY or rowIter < kingX or kingX - rowIter != -1 * (kingY-colIter) or rowIter > checkFromX or colIter < checkFromY:
						y[rowIter][colIter] = 0
		elif kingIsCheckedFrom == "|UpRight|":
			for rowIter in range(0, 8):
				for colIter in range(0, 8):
					if colIter < kingY or rowIter > kingY or kingX - rowIter != -1 * (kingY-colIter) or rowIter < checkFromX or colIter > checkFromY:
						y[rowIter][colIter] = 0
		
		elif kingIsCheckedFrom == "|Down2Right1|":
			for rowIter in range(0, 8):
				for colIter in range(0, 8):
					if rowIter != kingX + 2 or colIter != kingY + 1:
						y[rowIter][colIter] = 0
		elif kingIsCheckedFrom == "|Down2Left1|":
			for rowIter in range(0, 8):
				for colIter in range(0, 8):
					if rowIter != kingX + 2 or colIter != kingY - 1:
						y[rowIter][colIter] = 0
		elif kingIsCheckedFrom == "|Up2Right1|":
			for rowIter in range(0, 8):
				for colIter in range(0, 8):
					if rowIter != kingX - 2 or colIter != kingY + 1:
						y[rowIter][colIter] = 0
		elif kingIsCheckedFrom == "|Up2Left1|":
			for rowIter in range(0, 8):
				for colIter in range(0, 8):
					if rowIter != kingX - 2 or colIter != kingY - 1:
						y[rowIter][colIter] = 0
		elif kingIsCheckedFrom == "|Down1Right2|":
			for rowIter in range(0, 8):
				for colIter in range(0, 8):
					if rowIter != kingX + 1 or colIter != kingY + 2:
						y[rowIter][colIter] = 0
		elif kingIsCheckedFrom == "|Down1Left2|":
			for rowIter in range(0, 8):
				for colIter in range(0, 8):
					if rowIter != kingX + 1 or colIter != kingY1 - 2:
						y[rowIter][colIter] = 0
		elif kingIsCheckedFrom == "|Up1Right2|":
			for rowIter in range(0, 8):
				for colIter in range(0, 8):
					if rowIter != kingX - 1 or colIter != kingY + 2:
						y[rowIter][colIter] = 0
		elif kingIsCheckedFrom == "|Up1Left2|":
			for rowIter in range(0, 8):
				for colIter in range(0, 8):
					if rowIter != kingX - 1 or colIter != kingY - 2:
						y[rowIter][colIter] = 0

			
def checkparticularB(i,j):
	c=0
	f=0
	if j+1<8:
		if (i+1 < 8 and x[i+1][j+1] == 1) or (i-1 > -1 and x[i-1][j-1] == 1):
			c = c+1
	if j+1 < 8:
		if (i+1 < 8 and x[i+1][j+1] == 11) or (i-1 > -1 and x[i-1][j+1] == 11) or x[i][j+1] == 11:
			c = c+1
	if j-1 > -1:
		if (i+1 < 8 and x[i+1][j-1] == 11) or (i-1 > -1 and x[i-1][j-1] == 11) or x[i][j-1] == 11:
			c = c+1
	if i+1<8:
		if x[i+1][j] == 11:
			c = c+1
	if i-1>-1:
		if x[i-1][j] == 11:
			c = c+1
	for p in range(1,8):
		if i+p<8 and j+p<8:
			if x[i+p][j+p]%2 == 1 and x[i+p][j+p] != 7 and x[i+p][j+p] != 9:
				break
			if x[i+p][j+p] == 7 or x[i+p][j+p] == 9:
				c = c+1
				break
			if x[i+p][j+p]%2 == 0 and x[i+p][j+p]>0:
				break
	for p in range(1,8):
		if i-p>-1 and j-p>-1:
			if x[i-p][j-p]%2 == 1 and x[i-p][j-p] != 7 and x[i-p][j-p] != 9:
				break
			if x[i-p][j-p] == 7 or x[i-p][j-p] == 9:
				c = c+1
				break
			if x[i-p][j-p]%2 == 0 and x[i-p][j-p]>0:
				break
	for p in range(1,8):
		if i+p<8 and j-p>-1:
			if x[i+p][j-p]%2 == 1 and x[i+p][j-p] != 7 and x[i+p][j-p] != 9:
				break
			if x[i+p][j-p] == 7 or x[i+p][j-p] == 9:
				c = c+1
				break
			if x[i+p][j-p]%2 == 0 and x[i+p][j-p]>0:
				break
	for p in range(1,8):
		if i-p>-1 and j+p<8:
			if x[i-p][j+p]%2 == 1 and x[i-p][j+p] != 7 and x[i-p][j+p] != 9:
				break
			if x[i-p][j+p] == 7 or x[i-p][j+p] == 9:
				c = c+1
				break
			if x[i-p][j+p]%2 == 0 and x[i-p][j+p]>0:
				break
	for p in range(1,8):
		if i+p<8:
			if x[i+p][j]%2 == 1 and x[i+p][j] != 3 and x[i+p][j] != 9:
				break
			if x[i+p][j] == 3 or x[i+p][j] == 9:
				c = c+1
				break
			if x[i+p][j]%2 == 0 and x[i+p][j]>0:
				break
	for p in range(1,8):
		if i-p>-1:
			if x[i-p][j]%2 == 1 and x[i-p][j] != 3 and x[i-p][j] != 9:
				break
			if x[i-p][j] == 3 or x[i-p][j] == 9:
				c = c+1
				break
			if x[i-p][j]%2 == 0 and x[i-p][j]>0:
				break
	for p in range(1,8):
		if j+p<8:
			if x[i][j+p]%2 == 1 and x[i][j+p] != 3 and x[i][j+p] != 9:
				break
			if x[i][j+p] == 3 or x[i][j+p] == 9:
				c = c+1
				break
			if x[i][j+p]%2 == 0 and x[i][j+p]>0:
				break
	for p in range(1,8):
		if j-p>-1:
			if x[i][j-p]%2 == 1 and x[i][j-p] != 3 and x[i][j-p] != 9:
				break
			if x[i][j-p] == 3 or x[i][j-p] == 9:
				c = c+1
				break
			if x[i][j-p]%2 == 0 and x[i][j-p]>0:
				break
	if i+2<8 and j+1<8 and x[i+2][j+1] == 5:
		c=c+1
	if i+2<8 and j-1>-1 and x[i+2][j-1] == 5:
		c=c+1
	if i-2>-1 and j+1<8 and x[i-2][j+1] == 5:
		c=c+1
	if i-2>-1 and j-1>-1 and x[i-2][j-1] == 5:
		c=c+1
	if i+1<8 and j+2<8 and x[i+1][j+2] == 5:
		c=c+1
	if i+1<8 and j-2>-1 and x[i+1][j-2] == 5:
		c=c+1
	if i-1>-1 and j+2<8 and x[i-1][j+2] == 5:
		c=c+1
	if i-1>-1 and j-2>-1 and x[i-1][j-2] == 5:
		c=c+1
	if c == 0:
		f = 1
	return f

def checkparticularW(i,j):
	c=0
	f=0
	if j-1>-1:
		if (i+1 < 8 and x[i+1][j-1] == 2) or (i-1 > -1 and x[i-1][j-1] == 2):
			c = c+1
	if j+1 < 8:
		if (i+1 < 8 and x[i+1][j+1] == 12) or (i-1 > -1 and x[i-1][j+1] == 12) or x[i][j+1] == 12:
			c = c+1
	if j-1 > -1:
		if (i+1 < 8 and x[i+1][j-1] == 12) or (i-1 > -1 and x[i-1][j-1] == 12) or x[i][j-1] == 12:
			c = c+1
	if i+1<8:
		if x[i+1][j] == 12:
			c = c+1
	if i-1>-1:
		if x[i-1][j] == 12:
			c = c+1
	for p in range(1,8):
		if i+p<8 and j+p<8:
			if x[i+p][j+p]%2 == 0 and x[i+p][j+p] != 8 and x[i+p][j+p] != 10 and x[i+p][j+p] != 0:
				break
			if x[i+p][j+p] == 8 or x[i+p][j+p] == 10:
				c = c+1
				break
			if x[i+p][j+p]%2 == 1:
				break
	for p in range(1,8):
		if i-p>-1 and j-p>-1:
			if x[i-p][j-p]%2 == 0 and x[i-p][j-p] != 8 and x[i-p][j-p] != 10 and x[i-p][j-p] != 0:
				break
			if x[i-p][j-p] == 8 or x[i-p][j-p] == 10:
				c = c+1
				break
			if x[i-p][j-p]%2 == 1:
				break
	for p in range(1,8):
		if i+p<8 and j-p>-1:
			if x[i+p][j-p]%2 == 0 and x[i+p][j-p] != 8 and x[i+p][j-p] != 10 and x[i+p][j-p] != 0:
				break
			if x[i+p][j-p] == 8 or x[i+p][j-p] == 10:
				c = c+1
				break
			if x[i+p][j-p]%2 == 1:
				break
	for p in range(1,8):
		if i-p>-1 and j+p<8:
			if x[i-p][j+p]%2 == 0 and x[i-p][j+p] != 8 and x[i-p][j+p] != 10 and x[i-p][j+p] != 0:
				break
			if x[i-p][j+p] == 8 or x[i-p][j+p] == 10:
				c = c+1
				break
			if x[i-p][j+p]%2 == 1:
				break
	for p in range(1,8):
		if i+p<8:
			if x[i+p][j]%2 == 0 and x[i+p][j] != 4 and x[i+p][j] != 10 and x[i+p][j] != 0:
				break
			if x[i+p][j] == 4 or x[i+p][j] == 10:
				c = c+1
				txt4 = Text(Point(825,500), "White's move")
				break
			if x[i+p][j]%2 == 1:
				break
	for p in range(1,8):
		if i-p>-1:
			if x[i-p][j]%2 == 0 and x[i-p][j] != 4 and x[i-p][j] != 10 and x[i-p][j] != 0:
				break
			if x[i-p][j] == 4 or x[i-p][j] == 10:
				c = c+1
				break
			if x[i-p][j]%2 == 1:
				break
	for p in range(1,8):
		if j+p<8:
			if x[i][j+p]%2 == 0 and x[i][j+p] != 4 and x[i][j+p] != 10 and x[i][j+p] != 0:
				break
			if x[i][j+p] == 4 or x[i][j+p] == 10:
				c = c+1
				break
			if x[i][j+p]%2 == 1:
				break
	for p in range(1,8):
		if j-p>-1:
			if x[i][j-p]%2 == 0 and x[i][j-p] != 4 and x[i][j-p] != 10 and x[i][j-p] != 0:
				break
			if x[i][j-p] == 4 or x[i][j-p] == 10:
				c = c+1
				break
			if x[i][j-p]%2 == 1:
				break
	if i+2<8 and j+1<8 and x[i+2][j+1] == 6:
		c=c+1
	if i+2<8 and j-1>-1 and x[i+2][j-1] == 6:
		c=c+1
	if i-2>-1 and j+1<8 and x[i-2][j+1] == 6:
		c=c+1
	if i-2>-1 and j-1>-1 and x[i-2][j-1] == 6:
		c=c+1
	if i+1<8 and j+2<8 and x[i+1][j+2] == 6:
		c=c+1
	if i+1<8 and j-2>-1 and x[i+1][j-2] == 6:
		c=c+1
	if i-1>-1 and j+2<8 and x[i-1][j+2] == 6:
		c=c+1
	if i-1>-1 and j-2>-1 and x[i-1][j-2] == 6:
		c=c+1
	if c == 0:
		f = 1
	return f

def hideAvailable():
	for i in range(8):
		for j in range(8):
			if y[i][j] > 0:
				sq3 = Rectangle(Point(0+(i*80),0+(j*80)),Point(80+(i*80),80+(j*80)))
				sq3.setWidth(7)
				sq3.setOutline('white')
				sq3.draw(win)

def showAvailable():
	for i in range(8):
		for j in range(8):
			if y[i][j] != 0:
				sq3 = Rectangle(Point(0+(i*80),0+(j*80)),Point(80+(i*80),80+(j*80)))
				sq3.setWidth(7)
				sq3.setOutline(color_rgb(57,255,20))
				sq3.draw(win)
			if y[i][j] != 0 and x[i][j] > 10:
				sq3 = Rectangle(Point(0+(i*80),0+(j*80)),Point(80+(i*80),80+(j*80)))
				sq3.setWidth(7)
				sq3.setOutline('red')
				sq3.draw(win)

def blackAvail(i,j):
	count = 0 
	if 	j+1<8 and i+1<8 and (x[i+1][j+1] == 0 or x[i+1][j+1]%2 == 1):
		f = checkparticularB(i+1,j+1)
		if f == 1:
			count = count+1
		
	if 	i-1>-1 and j-1>-1 and (x[i-1][j-1] == 0 or x[i-1][j-1]%2 == 1):
		f = checkparticularB(i-1,j-1)
		if f == 1:
			count = count+1
		
	if 	i+1<8 and j-1>-1 and (x[i+1][j-1] == 0 or x[i+1][j-1]%2 == 1):
		f = checkparticularB(i+1,j-1)
		if f == 1:
			count = count+1
		
	if 	i-1>-1 and j+1<8 and (x[i-1][j+1] == 0 or x[i-1][j+1]):
		f = checkparticularB(i+1,j+1)
		if f == 1:
			count = count+1
		
	if 	j+1<8 and (x[i][j+1] == 0 or x[i][j+1]%2 == 1):
		f = checkparticularB(i,j+1)
		if f == 1:
			count = count+1
		
	if 	j-1>-1 and (x[i][j-1] == 0 or x[i][j-1]%2 == 1):
		f = checkparticularB(i,j-1)
		if f == 1:
			count = count+1
		
	if 	i+1<8 and (x[i+1][j] == 0 or x[i+1][j]%2 == 1):
		f = checkparticularB(i+1,j)
		if f == 1:
			count = count+1
		
	if 	i-1>-1 and (x[i-1][j] == 0 or x[i-1][j]%2 == 1):
		f = checkparticularB(i-1,j)
		if f == 1:
			count = count+1
	if count == 0:
		sq2 = Rectangle(Point(0,0),Point(1000,670))
		sq2.setFill('black')
		sq2.draw(win)
		sq2 = Image(Point(500,335),"logo.gif")
		sq2.draw(win)
		txt9 = Text(Point(500,600), "Player 2's checkmate\nPlayer 1 wins")
		txt9.setSize(30)
		txt9.setTextColor(color_rgb(57,255,20))
		txt9.draw(win)		
		win.getMouse()
		win.close()
	
def whiteAvail(i,j):
	count = 0
	if 	j+1<8 and i+1<8 and x[i+1][j+1]%2 == 0:
		f = checkparticularW(i+1,j+1)
		if f == 1:				
			count = count+1

	if 	i-1>-1 and j-1>-1 and x[i-1][j-1]%2 == 0:
		f = checkparticularW(i-1,j-1)
		if f == 1:
			count = count+1
		
	if i+1<8 and j-1>-1 and x[i+1][j-1]%2 == 0:
		f = checkparticularW(i+1,j-1)
		if f == 1:
			count = count+1
		
	if i-1>-1 and j+1<8 and x[i-1][j+1]%2 == 0:
		f = checkparticularW(i-1,j+1)
		if f == 1:
			count = count+1
		
	if j+1<8 and x[i][j+1]%2 == 0:
		f = checkparticularW(i,j+1)
		if f == 1:
			count = count+1
		
	if j-1>-1 and x[i][j-1]%2 == 0:
		f = checkparticularW(i,j-1)
		if f == 1:
			count = count+1
		
	if i+1<8 and x[i+1][j]%2 == 0:
		f = checkparticularW(i+1,j)
		if f == 1:
			count = count+1
		
	if i-1>-1 and x[i-1][j]%2 == 0:
		f = checkparticularW(i-1,j)
		if f == 1:
			count = count+1
	if count == 0:
		sq2 = Rectangle(Point(0,0),Point(1000,670))
		sq2.setFill('black')
		sq2.draw(win)
		sq2 = Image(Point(500,335),"logo.gif")
		sq2.draw(win)
		txt9 = Text(Point(500,600), "Player 1's checkmate\nPlayer 2 wins")
		txt9.setSize(30)
		txt9.setTextColor(color_rgb(57,255,20))
		txt9.draw(win)		
		win.getMouse()
		win.close()

def cansaveW(i,j):
	c = 0
	if j+1<8:
		if (x[i+1][j+1] == 1 and x[i+1][j+1]%2 == 0 and x[i+1][j+1] < 0):
			c = c+1
		if x[i][j+1] == 1:
			c = c+1
	if j+1<8:
		if (x[i-1][j+1] == 1 and x[i-1][j+1]%2 == 0 and x[i-1][j+1] < 0):
			c = c+1
		if x[i][j+1] == 1:
			c = c+1
	for p in range(1,8):
		if i+p<8 and j+p<8:
			if x[i+p][j+p]%2 == 1 and x[i+p][j+p] != 7 and x[i+p][j+p] != 9:
				break
			if x[i+p][j+p] == 7 or x[i+p][j+p] == 9:
				c = c+1
				break
			if x[i+p][j+p]%2 == 0 and x[i+p][j+p]<0:
				break
	for p in range(1,8):
		if i-p>-1 and j-p>-1:
			if x[i-p][j-p]%2 == 1 and x[i-p][j-p] != 7 and x[i-p][j-p] != 9:
				break
			if x[i-p][j-p] == 7 or x[i-p][j-p] == 9:
				c = c+1
				break
			if x[i-p][j-p]%2 == 0 and x[i-p][j-p]<0:
				break
	for p in range(1,8):
		if i+p<8 and j-p>-1:
			if x[i+p][j-p]%2 == 1 and x[i+p][j-p] != 7 and x[i+p][j-p] != 9:
				break
			if x[i+p][j-p] == 7 or x[i+p][j-p] == 9:
				c = c+1
				break
			if x[i+p][j-p]%2 == 0 and x[i+p][j-p]<0:
				break
	for p in range(1,8):
		if i-p>-1 and j+p<8:
			if x[i-p][j+p]%2 == 1 and x[i-p][j+p] != 7 and x[i-p][j+p] != 9:
				break
			if x[i-p][j+p] == 7 or x[i-p][j+p] == 9:
				c = c+1
				break
			if x[i-p][j+p]%2 == 0 and x[i-p][j+p]<0:
				break
	for p in range(1,8):
		if i+p<8:
			if x[i+p][j]%2 == 1 and x[i+p][j] != 3 and x[i+p][j] != 9:
				break
			if x[i+p][j] == 3 or x[i+p][j] == 9:
				c = c+1
				break
			if x[i+p][j]%2 == 0 and x[i+p][j]<0:
				break
	for p in range(1,8):
		if i-p>-1:
			if x[i-p][j]%2 == 1 and x[i-p][j] != 3 and x[i-p][j] != 9:
				break
			if x[i-p][j] == 3 or x[i-p][j] == 9:
				c = c+1
				break
			if x[i-p][j]%2 == 0 and x[i-p][j]<0:
				break
	for p in range(1,8):
		if j+p<8:
			if x[i][j+p]%2 == 1 and x[p][j+p] != 3 and x[p][j+p] != 9:
				break
			if x[i][j+p] == 3 or x[i][j+p] == 9:
				c = c+1
				break
			if x[i][j+p]%2 == 0 and x[i][j+p]<0:
				break
	for p in range(1,8):
		if j-p>-1:
			if x[i][j-p]%2 == 1 and x[i][j-p] != 3 and x[i][j-p] != 9:
				break
			if x[i][j-p] == 3 or x[i][j-p] == 9:
				c = c+1
				break
			if x[i][j-p]%2 == 0 and x[i][j-p]<0:
				break
	if i+2<8 and j+1<8 and x[i+2][j+1] == 5:
		c=c+1
	if i+2<8 and j-1>-1 and x[i+2][j-1] == 5:
		c=c+1
	if i-2>-1 and j+1<8 and x[i-2][j+1] == 5:
		c=c+1
	if i-2>-1 and j-1>-1 and x[i-2][j-1] == 5:
		c=c+1
	if i+1<8 and j+2<8 and x[i+1][j+2] == 5:
		c=c+1
	if i+1<8 and j-2>-1 and x[i+1][j-2] == 5:
		c=c+1
	if i-1>-1 and j+2<8 and x[i-1][j+2] == 5:
		c=c+1
	if i-1>-1 and j-2>-1 and x[i-1][j-2] == 5:
		c=c+1
	return c
	
def cansaveB(i,j):
	c = 0
	if j-1>-1:
		if (x[i+1][j-1] == 2 and x[i+1][j-1]%2 == 1):
			c = c+1
		if x[i][j-1] == 1:
			c = c+1
	if j-1>-1:
		if (x[i-1][j-1] == 1 and x[i-1][j-1]%2 == 0):
			c = c+1
		if x[i][j-1] == 1:
			c = c+1
	for p in range(1,8):
		if i+p<8 and j+p<8:
			if x[i+p][j+p]%2 == 0 and x[i+p][j+p] != 8 and x[i+p][j+p] != 10 and x[i+p][j+p] != 0:
				break
			if x[i+p][j+p] == 8 or x[i+p][j+p] == 10:
				c = c+1
				break
			if x[i+p][j+p]%2 == 1:
				break
	for p in range(1,8):
		if i-p>-1 and j-p>-1:
			if x[i-p][j-p]%2 == 0 and x[i-p][j-p] != 8 and x[i-p][j-p] != 10 and x[i-p][j-p] != 0:
				break
			if x[i-p][j-p] == 8 or x[i-p][j-p] == 10:
				c = c+1
				break
			if x[i-p][j-p]%2 == 1:
				break
	for p in range(1,8):
		if i+p<8 and j-p>-1:
			if x[i+p][j-p]%2 == 0 and x[i+p][j-p] != 8 and x[i+p][j-p] != 10 and x[i+p][j-p] != 0:
				break
			if x[i+p][j-p] == 8 or x[i+p][j-p] == 10:
				c = c+1
				break
			if x[i+p][j-p]%2 == 1:
				break
	for p in range(1,8):
		if i-p>-1 and j+p<8:
			if x[i-p][j+p]%2 == 0 and x[i-p][j+p] != 8 and x[i-p][j+p] != 10 and x[i-p][j+p] != 0:
				break
			if x[i-p][j+p] == 8 or x[i-p][j+p] == 10:
				c = c+1
				break
			if x[i-p][j+p]%2 == 1:
				break
	for p in range(1,8):
		if i+p<8:
			if x[i+p][j]%2 == 0 and x[i+p][j] != 4 and x[i+p][j] != 10 and x[i+p][j] != 0:
				break
			if x[i+p][j] == 4 or x[i+p][j] == 10:
				c = c+1
				break
			if x[i+p][j]%2 == 1:
				break
	for p in range(1,8):
		if i-p>-1:
			if x[i-p][j]%2 == 0 and x[i-p][j] != 4 and x[i-p][j] != 10 and x[i-p][j] != 0:
				break
			if x[i-p][j] == 4 or x[i-p][j] == 10:
				c = c+1
				break
			if x[i-p][j]%2 == 1:
				break
	for p in range(1,8):
		if j+p<8:
			if x[i][j+p]%2 == 0 and x[i][j+p] != 4 and x[i][j+p] != 10 and x[i][j+p] != 0:
				break
			if x[i][j+p] == 4 or x[i][j+p] == 10:
				c = c+1
				break
			if x[i][j+p]%2 == 1:
				break
	for p in range(1,8):
		if j-p>-1:
			if x[i][j-p]%2 == 0 and x[i][j-p] != 4 and x[i][j-p] != 10 and x[i][j-p] != 0:
				break
			if x[i][j-p] == 4 or x[i][j-p] == 10:
				c = c+1
				break
			if x[i][j-p]%2 == 1:
				break
	if i+2<8 and j+1<8 and x[i+2][j+1] == 6:
		c=c+1
	if i+2<8 and j-1>-1 and x[i+2][j-1] == 6:
		c=c+1
	if i-2>-1 and j+1<8 and x[i-2][j+1] == 6:
		c=c+1
	if i-2>-1 and j-1>-1 and x[i-2][j-1] == 6:
		c=c+1
	if i+1<8 and j+2<8 and x[i+1][j+2] == 6:
		c=c+1
	if i+1<8 and j-2>-1 and x[i+1][j-2] == 6:
		c=c+1
	if i-1>-1 and j+2<8 and x[i-1][j+2] == 6:
		c=c+1
	if i-1>-1 and j-2>-1 and x[i-1][j-2] == 6:
		c=c+1
	return c

def whiteCheck():
	isCheck = False
	e = 0
	for j in range(8):
		for i in range(1,8):
			if x[i][j] == 11:
				g=i
				h=j
	if g+1<8 and h+2<8:
		if x[g+1][h+2] == 6:
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			e = cansaveW(g+1,h+2)
			if e == 0:
				whiteAvail(g,h)
			
	if g+1<8 and h-2>-1:
		if x[g+1][h-2] == 6:
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			e = cansaveW(g+1,h-2)
			if e == 0:
				whiteAvail(g,h)
			
	if g+2<8 and h+1<8:
		if x[g+2][h+1] == 6:
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			e = cansaveW(g+2,h+1)
			if e == 0:
				whiteAvail(g,h)
			
	if g+2<8 and h-1>-1:
		if x[g+2][h-1] == 6:
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			e = cansaveW(g+2,h-1)
			if e == 0:
				whiteAvail(g,h)
			
	if g-1>-1 and h+2<8:
		if x[g-1][h+2] == 6:
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			e = cansaveW(g-1,h+2)
			if e == 0:
				whiteAvail(g,h)
			
	if g-1>-1 and h-2>-1:
		if x[g-1][h-2] == 6:
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			e = cansaveW(g-1,h-2)
			if e == 0:
				whiteAvail(g,h)
			
	if g-2>-1 and h+1<8:
		if x[g-2][h+1] == 6:
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			e = cansaveW(g-2,h+1)
			if e == 0:
				whiteAvail(g,h)
			
	if g-2>-1 and h-1>-1:
		if x[g-2][h-1] == 6:
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			e = cansaveW(g-2,h-1)
			if e == 0:
				whiteAvail(g,h)
			
	if g-1>-1 and h-1>-1:
		if x[g-1][h-1] == 2:
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			e = cansaveW(g-1,h-1)
			if e == 0:
				whiteAvail(g,h)
			
	if g+1<8 and h-1>-1:
		if x[g+1][h-1] == 2:
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			e = cansaveW(g+1,h-1)
			if e == 0:
				whiteAvail(g,h)
			
	for p in range(1,8):
		if 	h+p<8:
			if (x[g][h+p] == 4 or x[g][h+p] == 10):
				sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
				sq3.setWidth(7)
				sq3.setOutline('red')
				sq3.draw(win)
				isCheck = True
				for y in range(1,p):	
					e = e + cansaveW(g,h+y)
				if e == 0:
					whiteAvail(g,h)
			
			break
		if h+p<8 and x[g][h+p]%2 == 1:
			break
		if h+p<8 and x[g][h+p]%2 == 0 and x[g][h+p] > 0 and x[g][h+p] != 4 and x[g][h+p] != 10:
			break
	for p in range(1,8):
		if 	h-p>-1 and (x[g][h-p] == 4 or x[g][h-p] == 10):
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			for y in range(1,p):	
				e = e + cansaveW(g,h-y)
			if e == 0:
				whiteAvail(g,h)
			
			break
		if h-p>-1 and x[g][h-p]%2 == 1:
			break
		if h-p>-1 and x[g][h-p]%2 == 0 and x[g][h-p] > 0 and x[g][h-p] != 4 and x[g][h-p] != 10:
			break
	for p in range(1,8):
		if 	g+p<8 and (x[g+p][h] == 4 or x[g+p][h] == 10):
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			for y in range(1,p):	
				e = e + cansaveW(g+y,h)
			if e == 0:
				whiteAvail(g,h)
			
			break
		if g+p<8 and x[g+p][h]%2 == 1:
			break
		if g+p<8 and x[g+p][h]%2 == 0 and x[g+p][h] > 0 and x[g+p][h] != 4 and x[g+p][h] != 10:
			break
	for p in range(1,8):
		if 	g-p>-1 and (x[g-p][h] == 4 or x[g-p][h] == 10):
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			for y in range(1,p):	
				e = e + cansaveW(g-y,h)
			if e == 0:
				whiteAvail(g,h)
			
			break
		if g-p>-1 and x[g-p][h]%2 == 1:
			break
		if g-p>-1 and x[g-p][h]%2 == 0 and x[g-p][h] > 0 and x[g-p][h] != 4 and x[g-p][h] != 10:
			break
	for p in range(1,8):
		if 	h+p<8 and g+p<8 and (x[g+p][h+p] == 8 or x[g+p][h+p] == 10):
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			for y in range(1,p):	
				e = e + cansaveW(g+y,h+y)
			if e == 0:
				whiteAvail(g,h)
			
			break
		if h+p<8 and g+p<8 and x[g+p][h+p]%2 == 1:
			break
		if h+p<8 and g+p<8 and x[g+p][h+p]%2 == 0 and x[g+p][h+p] > 0 and x[g+p][h+p] != 8 and x[g+p][h+p] != 10:
			break
	for p in range(1,8):
		if 	h-p>-1 and g-p>-1 and (x[g-p][h-p] == 8 or x[g-p][h-p] == 10):
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			for y in range(1,p):	
				e = e + cansaveW(g-y,h-y)
			if e == 0:
					whiteAvail(g,h)
			break
		if h-p>-1 and g-p>-1 and x[g-p][h-p]%2 == 1:
			break
		if h-p>-1 and g-p>-1 and x[g-p][h-p]%2 == 0 and x[g-p][h-p] > 0 and x[g-p][h-p] != 8 and x[g-p][h-p] != 10:
			break
	for p in range(1,8):
		if 	g+p<8 and h-p>-1 and (x[g+p][h-p] == 8 or x[g+p][h-p] == 10):
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			for y in range(1,p):	
				e = e + cansaveW(g+y,h-y)
			if e == 0:
				whiteAvail(g,h)
			
			break
		if g+p<8 and h-p>-1 and x[g+p][h-p]%2 == 1:
			break
		if g+p<8 and h-p>-1 and x[g+p][h-p]%2 == 0 and x[g+p][h-p] > 0 and x[g+p][h-p] != 8 and x[g+p][h-p] != 10:
			break
	for p in range(1,8):
		if 	g-p>-1 and h+p<8 and (x[g-p][h+p] == 8 or x[g-p][h+p] == 10):
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			for y in range(1,p):	
				e = e + cansaveW(g-y,h+y)
			if e == 0:
				whiteAvail(g,h)
			
			break
		if g-p>-1 and h+p<8 and x[g-p][h+p]%2 == 1:
			break
		if g-p>-1 and h+p<8 and x[g-p][h+p]%2 == 0 and x[g-p][h+p] > 0 and x[g-p][h+p] != 8 and x[g-p][h+p] != 10:
			break
	return isCheck

def blackCheck():
	isCheck = False
	e = 0
	for j in range(8):
		for i in range(8):
			if x[i][j] == 12:
				g=i
				h=j
	if g+1<8 and h+2<8:
		if x[g+1][h+2] == 5:
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			e = cansaveW(g+1,h+2)
			if e == 0:
				blackAvail(g,h)
	if g+1<8 and h-2>-1:
		if x[g+1][h-2] == 5:
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			e = cansaveW(g+1,h-2)
			if e == 0:
				blackAvail(g,h)
	if g+2<8 and h+1<8:
		if x[g+2][h+1] == 5:
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			e = cansaveW(g+2,h+1)
			if e == 0:
				blackAvail(g,h)
	if g+2<8 and h-1>-1:
		if x[g+2][h-1] == 5:
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			e = cansaveW(g+2,h-1)
			if e == 0:
				blackAvail(g,h)
	if g-1>-1 and h+2<8:
		if x[g-1][h+2] == 5:
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			e = cansaveW(g-1,h+2)
			if e == 0:
				blackAvail(g,h)
	if g-1>-1 and h-2>-1:
		if x[g-1][h-2] == 5:
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			e = cansaveW(g-1,h-2)
			if e == 0:
				blackAvail(g,h)
	if g-2>-1 and h+1<8:
		if x[g-2][h+1] == 5:
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			e = cansaveW(g-2,h+1)
			if e == 0:
				blackAvail(g,h)
	if g-2>-1 and h-1>-1:
		if x[g-2][h-1] == 5:
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			e = cansaveW(g-2,h-1)
			if e == 0:
				blackAvail(g,h)
	if g-1>-1 and h+1<8:
		if x[g-1][h+1] == 1:
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			e = cansaveW(g-1,h+1)
			if e == 0:
				blackAvail(g,h)
	if g+1<8 and h+1<8:
		if x[g+1][h+1] == 1:
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			e = cansaveW(g+1,h+1)
			if e == 0:
				blackAvail(g,h)
	for p in range(1,8):
		if 	h+p<8 and (x[g][h+p] == 3 or x[g][h+p] == 9):
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			for y in range(1,p):	
				e = e + cansaveW(g,h+y)
			if e == 0:
				blackAvail(g,h)
			break
		if h+p<8 and x[g][h+p]%2 == 0 and x[g][h+p] > 0:
			break
		if h+p<8 and x[g][h+p]%2 == 1 and x[g][h+p] != 3 and x[g][h+p] != 9:
			break
	for p in range(1,8):
		if 	h-p>-1 and (x[g][h-p] == 3 or x[g][h-p] == 9):
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			for y in range(1,p):	
				e = e + cansaveW(g,h-y)
			if e == 0:
				blackAvail(g,h)
			break
		if h-p>-1 and x[g][h-p]%2 == 0 and x[g][h-p] > 0:
			break
		if h-p>-1 and x[g][h-p]%2 == 1 and x[g][h-p] != 3 and x[g][h-p] != 9:
			break
	for p in range(1,8):
		if 	g+p<8 and (x[g+p][h] == 3 or x[g+p][h] == 9):
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			for y in range(1,p):	
				e = e + cansaveW(g+y,h)
			if e == 0:
				blackAvail(g,h)
			break
		if g+p<8 and x[g+p][h]%2 == 0 and x[g+p][h] > 0:
			break
		if g+p<8 and x[g+p][h]%2 == 1 and x[g+p][h] != 3 and x[g+p][h] != 9:
			break
	for p in range(1,8):
		if 	g-p>-1 and (x[g-p][h] == 3 or x[g-p][h] == 9):
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			for y in range(1,p):	
				e = e + cansaveW(g-y,h)
			if e == 0:
				blackAvail(g,h)
			break
		if g-p>-1 and x[g-p][h]%2 == 0 and x[g-p][h]:
			break
		if g-p>-1 and x[g-p][h]%2 == 1 and x[g-p][h] != 3 and x[g-p][h] != 9:
			break
	for p in range(1,8):
		if 	h+p<8 and g+p<8 and (x[g+p][h+p] == 7 or x[g+p][h+p] == 9):
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			for y in range(1,p):	
				e = e + cansaveW(g+y,h+y)
			if e == 0:
				blackAvail(g,h)
			break
		if h+p<8 and g+p<8 and x[g+p][h+p]%2 == 0 and x[g+p][h+p] > 0:
			break
		if h+p<8 and g+p<8 and x[g+p][h+p]%2 == 1 and x[g+p][h+p] != 7 and x[g+p][h+p] != 9:
			break
	for p in range(1,8):
		if 	h-p>-1 and g-p>-1 and (x[g-p][h-p] == 7 or x[g-p][h-p] == 9):
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			for y in range(1,p):	
				e = e + cansaveW(g-y,h-y)
			if e == 0:
				blackAvail(g,h)
			break
		if h-p>-1 and g-p>-1 and x[g-p][h-p]%2 == 0 and x[g-p][h-p] > 0:
			break
		if h-p>-1 and g-p>-1 and x[g-p][h-p]%2 == 1 and x[g-p][h-p] != 7 and x[g-p][h-p] != 9:
			break
	for p in range(1,8):
		if 	g+p<8 and h-p>-1 and (x[g+p][h-p] == 7 or x[g+p][h-p] == 9):
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			for y in range(1,p):	
				e = e + cansaveW(g+y,h-y)
			if e == 0:
				blackAvail(g,h)
			break
		if g+p<8 and h-p>-1 and x[g+p][h-p]%2 == 0 and x[g+p][h-p] > 0:
			break
		if g+p<8 and h-p>-1 and x[g+p][h-p]%2 == 1 and x[g+p][h-p] != 7 and x[g+p][h-p] != 9:
			break
	for p in range(1,8):
		if 	g-p>-1 and h+p<8 and (x[g-p][h+p] == 7 or x[g-p][h+p] == 9):
			sq3 = Rectangle(Point(0+(g*80),0+(h*80)),Point(80+(g*80),80+(h*80)))
			sq3.setWidth(7)
			sq3.setOutline('red')
			sq3.draw(win)
			isCheck = True
			for y in range(1,p):	
				e = e + cansaveW(g-y,h+y)
			if e == 0:
				blackAvail(g,h)
			break
		if g-p>-1 and h+p<8 and x[g-p][h+p]%2 == 0 and x[g-p][h+p] > 0:
			break
		if g-p>-1 and h+p<8 and x[g-p][h+p]%2 == 1 and x[g-p][h+p] != 7 and x[g-p][h+p] != 9:
			break
	return isCheck
	
def getAllAvailableMoves(boardArray, color):
	boardArrayNp = np.array(boardArray)
	##print(boardArrayNp)
	listOfBoards = []
	for i in range(8):
		for j in range(8):
			if color == 'Black' and boardArrayNp[i][j] in [2,4,6,8,10,12]:
				getAvailable(boardArrayNp,i, j, 0, 0, 0, 0)
			elif color == 'White' and boardArrayNp[i][j] in [1,3,5,7,9,11]:
				getAvailable(boardArrayNp,i, j, 0, 0, 0, 0)
			piece = boardArrayNp[i][j]
			for y_i in range(8):
				for y_j in range(8):
					boardArrayCopy = boardArrayNp.copy()
					if y[y_i][y_j] != 0:
						boardArrayCopy[y_i][y_j] = piece
						boardArrayCopy[i][j] = 0
						y[y_i][y_j] = 0
						listOfBoards.append(boardArrayCopy)

	return listOfBoards

def resetMinMax():
	global maxWeight
	global minWeight
	maxWeight = -99999
	minWeight = 99999

# def minimax(board, depth, color):
# 	global maxWeight
# 	global minWeight
# 	# global checkMateW
# 	# global checkMateB
# 	# #print('Called for ')
# 	# #print(board)
# 	# #print('with depth ')
# 	# #print(depth)
# 	# #print('and color')
# 	# #print(color)
# 	# #print(maxWeight)
# 	# #print(minWeight)
# 	tempboard = np.copy(board)

# 	if (tuple(map(tuple, board)), depth, color) in BoardMoveWeightDict:
# 		weight, move = BoardMoveWeightDict[(tuple(map(tuple, board)), depth, color)]
# 		return weight, move
# 	else:
# 		#BoardMoveWeightDict[positionPawnW] = [positionPawnB, 200]

# 		if depth == 0 or checkmateW == 1 or checkmateB == 1:
# 			##print('returning weight' + str(calculateTotalWeight(tempboard)))
# 			weight = calculateTotalWeight(tempboard)
# 			BoardMoveWeightDict[(tuple(map(tuple, board)), depth, color)] = [weight, tempboard]
# 			#np.save(fileName, BoardMoveWeightDict)
# 			return weight, tempboard

# 		listOfMoves = getAllAvailableMoves(tempboard, color)
# 		# #print('for position ')
# 		# #print(tempboard)
# 		# #print('available moves are')
# 		# #print(listOfMoves)
# 		if color == "White":
# 			for move in listOfMoves:
# 				weight, tboard = minimax(move, depth - 1, "Black")
# 				#maxWeight = max(maxWeight, weight)
# 				if weight > maxWeight:
# 					##print('inside white if')
# 					maxWeight = weight
# 					tempboard = move
# 			# 		#print('changed tempboard to ')
# 			# 		#print(tempboard)
# 			# #print('returning from white ')
# 			# #print(tempboard)
# 			weightToReturn = maxWeight
# 			maxWeight = -99999
# 			BoardMoveWeightDict[(tuple(map(tuple, board)), depth, color)] = [weightToReturn, tempboard]
# 			#np.save(fileName, BoardMoveWeightDict)
# 			return weightToReturn, tempboard

# 		elif color == "Black":
# 			for move in listOfMoves:
# 				weight, tboard = minimax(move, depth - 1, "White")
# 				##print(weight)
# 				#minWeight = min(minWeight, weight)
# 				if weight < minWeight:
# 					##print('inside black if')
# 					minWeight = weight
# 					tempboard = move
# 			# 		#print('changed tempboard to ')
# 			# 		#print(tempboard)
# 			# #print('returning from black ')
# 			# #print(tempboard)
# 			weightToReturn = minWeight
# 			minWeight = 99999
# 			BoardMoveWeightDict[(tuple(map(tuple, board)), depth, color)] = [weightToReturn, tempboard]
# 			#np.save(fileName, BoardMoveWeightDict)
# 			return weightToReturn, tempboard

### Trial section for minimax #########################################################################

#board = []

def minimaxRoot(depth, board, isMaximizing):
    #possibleMoves = getAllAvailableMoves(tempboard, color)
    color = "White" if isMaximizing else "Black"
    possibleMoves = getAllAvailableMoves(board, color)
    bestMove = -9999
    secondBest = -9999
    thirdBest = -9999
    bestMoveFinal = None
    for move in possibleMoves:
        #board.append(move)
        value = max(bestMove, minimaxFromRoot(depth - 1, move, not isMaximizing))
        #board.pop()
        if( value > bestMove):
            #print("Best score: " ,str(bestMove))
            #print("Best move: ",str(bestMoveFinal))
            #print("Second best: ", str(secondBest))
            thirdBest = secondBest
            secondBest = bestMove
            bestMove = value
            bestMoveFinal = move
    return bestMoveFinal

# def minimaxFromRoot(depth, board, is_maximizing):
# 	color = "White" if is_maximizing else "Black"
# 	if (tuple(map(tuple, board)), depth, color) in BoardWeightDict:
# 		weight = BoardWeightDict[(tuple(map(tuple, board)), depth, color)]
# 		return  move
# 	else:
# 		#BoardWeightDict[positionPawnW] = [positionPawnB, 200]
# 	    if(depth == 0):
# 	        return -1 * calculateTotalWeight(board)
# 	    possibleMoves = getAllAvailableMoves(board, color)
# 	    if(is_maximizing):
# 	        bestMove = -9999
# 	        for move in possibleMoves:
# 	            #board.append(move)
# 	            bestMove = max(bestMove,minimaxFromRoot(depth - 1, move, not is_maximizing))
# 	            #board.pop()
# 	        BoardWeightDict[(tuple(map(tuple, board)), depth, color)] = bestMove
# 	        return bestMove
# 	    else:
# 	        bestMove = 9999
# 	        for move in possibleMoves:
# 	            #board.append(move)
# 	            bestMove = min(bestMove, minimaxFromRoot(depth - 1, move, not is_maximizing))
# 	            #board.pop()
# 	        BoardWeightDict[(tuple(map(tuple, board)), depth, color)] = bestMove
# 	        return bestMove


def minimaxRootAB(depth, board, isMaximizing):
    #possibleMoves = getAllAvailableMoves(tempboard, color)
    color = "White" if isMaximizing else "Black"
    possibleMoves = getAllAvailableMoves(board, color)
    bestMove = -9999
    bestMoveFinal = None
    for move in possibleMoves:
        #board.append(move)
        value = max(bestMove, minimaxFromRootAB(depth - 1, move, -10000, 10000, not isMaximizing))
        #board.pop()
        if( value > bestMove):
            #print("Best score: " ,str(bestMove))
            #print("Best move: ",str(bestMoveFinal))
            #print("Second best: ", str(secondBest))
            bestMove = value
            bestMoveFinal = move
    return bestMoveFinal

def minimaxFromRootAB(depth, board, alpha, beta, is_maximizing):
	color = "White" if is_maximizing else "Black"
	if (tuple(map(tuple, board)), depth, alpha, beta, color) in BoardWeightDictAB:
		weight = BoardWeightDictAB[(tuple(map(tuple, board)), depth, alpha, beta, color)]
		return  weight
	else:
		#BoardWeightDict[positionPawnW] = [positionPawnB, 200]
	    if(depth == 0):
	        return -1 * calculateTotalWeight(board)
	    possibleMoves = getAllAvailableMoves(board, color)
	    if(is_maximizing):
	        bestMove = -9999
	        for move in possibleMoves:
	            #board.append(move)
	            bestMove = max(bestMove,minimaxFromRootAB(depth - 1, move, alpha, beta, not is_maximizing))
	            alpha = max(alpha, bestMove)
	            if beta <= alpha:
	            	BoardWeightDictAB[(tuple(map(tuple, board)), depth, alpha, beta, color)] = bestMove
	            	return bestMove
	            #board.pop()
	        BoardWeightDictAB[(tuple(map(tuple, board)), depth, alpha, beta, color)] = bestMove
	        return bestMove
	    else:
	        bestMove = 9999
	        for move in possibleMoves:
	            #board.append(move)
	            bestMove = min(bestMove, minimaxFromRootAB(depth - 1, move, alpha, beta, not is_maximizing))
	            beta = min(beta, bestMove)
	            if beta <= alpha:
	            	BoardWeightDictAB[(tuple(map(tuple, board)), depth, alpha, beta, color)] = bestMove
	            	return bestMove
	            #board.pop()
	        BoardWeightDictAB[(tuple(map(tuple, board)), depth, alpha, beta, color)] = bestMove
	        return bestMove

### Trial section for minimax #########################################################################

def convertToWeights(boardArray):
	boardArrayNp = np.array(boardArray)
	boardArrayNp[boardArrayNp == 3] = 50
	boardArrayNp[boardArrayNp == 4] = -50
	boardArrayNp[boardArrayNp == 5] = 30
	boardArrayNp[boardArrayNp == 6] = -30
	boardArrayNp[boardArrayNp == 7] = 30
	boardArrayNp[boardArrayNp == 8] = -30
	boardArrayNp[boardArrayNp == 9] = 90
	boardArrayNp[boardArrayNp == 10] = -90
	boardArrayNp[boardArrayNp == 11] = 900
	boardArrayNp[boardArrayNp == 12] = -900
	boardArrayNp[boardArrayNp == 1] = 10
	boardArrayNp[boardArrayNp == 2] = -10

	return boardArrayNp

# def calculateTotalWeight(boardArray):
# 	boardArray = convertToWeights(boardArray)
# 	boardArrayNp = np.array(boardArray)
# 	sum = np.sum(boardArrayNp)

# 	return sum


def calculateTotalWeight(boardArray):
	boardArray = convertToWeights(boardArray)
	boardArrayNp = np.array(boardArray)
	sum = 0
	positionKingW = np.array([[-3.0, -3.0, -3.0, -3.0, -4.0, -1.0, 2.0, 2.0], 
							  [-4.0, -4.0, -4.0, -4.0, -3.0, -2.0, 2.0, 3.0],
							  [-4.0, -4.0, -4.0, -4.0, -3.0, -2.0, 0.0, 1.0],
							  [-5.0, -5.0, -5.0, -5.0, -4.0, -2.0, 0.0, 0.0],
							  [-5.0, -5.0, -5.0, -5.0, -4.0, -2.0, 0.0, 0.0],
							  [-4.0, -4.0, -4.0, -4.0, -3.0, -2.0, 0.0, 1.0],
							  [-4.0, -4.0, -4.0, -4.0, -3.0, -2.0, 2.0, 3.0], 
							  [-3.0, -3.0, -3.0, -3.0, -2.0, -1.0, 2.0, 2.0]])

	positionKingB = np.array([[2.0, 2.0, -1.0, -2.0, -3.0, -3.0, -3.0, -3.0], 
							  [3.0, 2.0, -2.0, -3.0, -4.0, -4.0, -4.0, -4.0],
							  [1.0, 2.0, -2.0, -3.0, -4.0, -4.0, -4.0, -4.0],
							  [0.0, 2.0, -2.0, -4.0, -5.0, -5.0, -5.0, -5.0],
							  [0.0, 2.0, -2.0, -4.0, -5.0, -5.0, -5.0, -5.0],
							  [1.0, 2.0, -2.0, -3.0, -4.0, -4.0, -4.0, -4.0],
							  [3.0, 2.0, -2.0, -3.0, -4.0, -4.0, -4.0, -4.0], 
							  [2.0, 2.0, -1.0, -2.0, -3.0, -3.0, -3.0, -3.0]])


	positionQueenW = np.array([[-2.0, -1.0, -1.0, -0.5, 0.0, -1.0, -1.0, -2.0],
							   [-1.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, -1.0],
							   [-1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.5, -1.0],
							   [-0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
							   [-0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
							   [-1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
							   [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0], 
							   [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]])

	positionQueenB = np.array([[-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
							   [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
							   [-1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
							   [-0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
							   [-0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
							   [-1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
							   [-1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0], 
							   [-2.0, -1.0, -1.0, 0.0, -0.5, -1.0, -1.0, -2.0]])


	positionRookW = np.array([[0.0, 0.5, -0.5, -0.5, -0.5, -0.5, -0.5, 0.0],
							  [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
							  [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
							  [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5],
							  [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5],
							  [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
							  [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
							  [0.0, 0.5, -0.5, -0.5, -0.5, -0.5, -0.5, 0.0]])

	positionRookB = np.array([[0.0, -0.5, -0.5, -0.5, -0.5, -0.5, 0.5, 0.0],
							  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
							  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
							  [0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
							  [0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
							  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
							  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 
							  [0.0, -0.5, -0.5, -0.5, -0.5, -0.5, 0.5, 0.0]])


	positionBishopeW = np.array([[-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
							     [-1.0, 0.0, 0.5, 0.5, 0.0, 1.0, 0.5, -1.0],
							     [-1.0, 0.0, 0.5, 0.5, 1.0, 1.0, 0.0, -1.0],
							     [-1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.5],
							     [-1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.5],
							     [-1.0, 0.0, 0.5, 0.5, 1.0, 1.0, 0.0, -1.0],
							     [-1.0, 0.0, 0.5, 0.5, 0.0, 1.0, 0.5, -1.0], 
							     [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]])

	positionBishopeB = np.array([[-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
							     [-1.0, 0.5, 1.0, 0.0, 0.5, 0.5, 0.0, -1.0],
							     [-1.0, 0.0, 1.0, 1.0, 0.5, 0.5, 0.0, -1.0],
							     [-1.5, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.5],
							     [-1.5, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.5],
							     [-1.0, 0.0, 1.0, 1.0, 0.5, 0.5, 0.0, -1.0],
							     [-1.0, 0.5, 1.0, 0.0, 0.5, 0.5, 0.0, -1.0], 
							     [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]])

	positionKinghtW = np.array([[-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
							    [-4.0, -2.0, 0.0, 0.5, 0.0, 0.5, -2.0, -4.0],
							    [-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0],
							    [-3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.5, -3.5],
							    [-3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.5, -3.5],
							    [-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0],
							    [-4.0, -2.0, 0.0, 0.5, 0.0, 0.5, -2.0, -4.0], 
							    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]])

	positionKnightB = np.array([[-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
							    [-4.0, -2.0, 0.5, 0.0, 0.5, 0.0, -2.0, -4.0],
							    [-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0],
							    [-3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0],
							    [-3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0],
							    [-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0],
							    [-4.0, -2.0, 0.5, 0.0, 0.5, 0.0, -2.0, -4.0], 
							    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]])


	positionPawnW = np.array([[0.0, 5.0, 1.0, 0.5, 0.0, 0.5, 0.5, 0.0],
							  [0.0, 5.0, 1.0, 0.5, 0.0, -0.5, 1.0, 0.0],
							  [0.0, 5.0, 2.0, 1.0, 0.0, -1.0, 1.0, 0.0],
							  [0.0, 5.0, 3.0, 2.5, 2.0, 0.0, -2.0, 0.0],
							  [0.0, 5.0, 3.0, 2.5, 2.0, 0.0, -2.0, 0.0],
							  [0.0, 5.0, 2.0, 1.5, 0.0, -1.0, 1.0, 0.0],
							  [0.0, 5.0, 1.0, 0.5, 0.0, -0.5, 1.0, 0.0], 
							  [0.0, 5.0, 1.0, 0.5, 0.0, 0.5, 0.5, 0.0]])

	positionPawnB = np.array([[0.0, 0.5, 0.5, 0.0, 0.5, 1.0, 5.0, 0.0],
							  [0.0, 1.0, -0.5, 0.0, 0.5, 1.0, 5.0, 0.0],
							  [0.0, 1.0, -1.0, 0.0, 1.0, 2.0, 5.0, 0.0],
							  [0.0, -2.0, 0.0, 2.0, 2.5, 3.0, 5.0, 0.0],
							  [0.0, -2.0, 0.0, 2.0, 2.5, 3.0, 5.0, 0.0],
							  [0.0, 1.0, -1.0, 0.0, 1.5, 2.0, 5.0, 0.0],
							  [0.0, 1.0, -0.5, 0.0, 0.5, 1.0, 5.0, 0.0], 
							  [0.0, 0.5, 0.5, 0.0, 0.5, 1.0, 5.0, 0.0]])
	
	positionDict = {
					1 : positionPawnW,
					2 : positionPawnB,
					3 : positionRookW,
					4 : positionRookB,
					5 : positionKinghtW,
					6 : positionKnightB,
					7 : positionBishopeW,
					8 : positionBishopeB,
					9 : positionQueenW,
					10 : positionQueenB,
					11 : positionKingW,
					12 : positionKingB
	 				}

	for i in range(0, 7):
		for j in range(0, 7):
			if x[i][j] != 0:
				sum = sum + boardArrayNp[i][j] * positionDict[x[i][j]][i][j]

	return sum

def board():
	for j in range(4):
		for i in range(8):
			x = i%2
			if x==0:
				pt2 = Point(0+(i*80), 0+(160*j))
				pt3 = Point(80+(i*80), 80+(160*j))
				sq = Rectangle(pt2,pt3)
				sq.setFill('white')
				sq.draw(win)
			else:
				pt2 = Point(0+(i*80), 0+(160*j))
				pt3 = Point(80+(i*80), 80+(160*j))
				sq = Rectangle(pt2,pt3)
				sq.setFill('grey')
				sq.draw(win)	
		for i in range(8):
			x = i%2
			if x==1:
				pt2 = Point(0+(i*80), 80+(160*j))
				pt3 = Point(80+(i*80), 160+(160*j))
				sq = Rectangle(pt2,pt3)
				sq.setFill('white')
				sq.draw(win)
			else:
				pt2 = Point(0+(i*80), 80+(160*j))
				pt3 = Point(80+(i*80), 160+(160*j))
				sq = Rectangle(pt2,pt3)
				sq.setFill('grey')
				sq.draw(win)

	for i in range(8):
		txt = Text(Point(650,40+(i*80)),i+1)
		txt.draw(win)

	for i in range(8):
		txt = Text(Point(40+(i*80),650),i+1)
		txt.draw(win)
	position()
			
def pawn(i,j,c):
	pt4 = Point(40+(i*80), 40+(j*80))
	pawn = Circle(pt4, 25)
	pawn.setWidth(5)
	if c%2 == 1:
		pawn.setFill('white')
	else:
		pawn.setFill('black')	
	pawn.draw(win)

def rook(i,j,c):
	rook = Polygon(Point((i*80)+60, (j*80)+70),
				   Point((i*80)+20, (j*80)+70),
				   Point((i*80)+20, (j*80)+40),
				   Point((i*80)+10, (j*80)+40),
				   Point((i*80)+10, (j*80)+20),
				   Point((i*80)+20, (j*80)+20),
				   Point((i*80)+20, (j*80)+30),
				   Point((i*80)+30, (j*80)+30),
				   Point((i*80)+30, (j*80)+20),	
				   Point((i*80)+50, (j*80)+20),
				   Point((i*80)+50, (j*80)+30),
				   Point((i*80)+60, (j*80)+30),
				   Point((i*80)+60, (j*80)+20),
				   Point((i*80)+70, (j*80)+20),
				   Point((i*80)+70, (j*80)+40),
				   Point((i*80)+60, (j*80)+40))
	rook.setWidth(5)
	if c%2 == 1:
		rook.setFill('white')
	else:
		rook.setFill('black')
	rook.draw(win)

def knight(i,j,c):
	knight = Polygon(Point((i*80)+70,(j*80)+70),
					 Point((i*80)+20,(j*80)+70),
					 Point((i*80)+40,(j*80)+30),
					 Point((i*80)+20,(j*80)+40),
					 Point((i*80)+20,(j*80)+25),
					 Point((i*80)+60,(j*80)+5))
	knight.setWidth(5)
	if c%2 == 1:
		knight.setFill('white')
	else:
		knight.setFill('black')
	knight.draw(win)

def bishop(i,j,c):
	bishop = Polygon(Point((i*80)+60,(j*80)+70),
					 Point((i*80)+20,(j*80)+70),
					 Point((i*80)+10,(j*80)+50),
					 Point((i*80)+40,(j*80)+20),
					 Point((i*80)+70,(j*80)+50),)
	bishop.setWidth(5)
	if c%2 == 1:
		bishop.setFill('white')
	else:
		bishop.setFill('black')
	bishop.draw(win)
	cir = Circle(Point((i*80)+40,(j*80)+15),5)
	cir.setWidth(5)
	if c%2 == 1:
		cir.setFill('white')
	else:
		cir.setFill('black')
	cir.draw(win)

def king(i,j,c):
	king = Polygon(Point((i*80)+60,(j*80)+70),
				   Point((i*80)+20,(j*80)+70),
				   Point((i*80)+10,(j*80)+30),
				   Point((i*80)+20,(j*80)+40),
				   Point((i*80)+25,(j*80)+25),
				   Point((i*80)+30,(j*80)+40),
				   Point((i*80)+40,(j*80)+20),
				   Point((i*80)+50,(j*80)+40),
				   Point((i*80)+55,(j*80)+25),
				   Point((i*80)+60,(j*80)+40),
				   Point((i*80)+70,(j*80)+30))
	king.setWidth(5)
	if c%2 == 1:
		king.setFill('white')
	else:
		king.setFill('black')
	king.draw(win)
	ln = Line(Point((i*80)+40,(j*80)+20),Point((i*80)+40,(j*80)+10))
	ln1 = Line(Point((i*80)+35,(j*80)+15),Point((i*80)+46,(j*80)+15))
	ln.setWidth(5)
	ln.setOutline('black')
	ln.draw(win)
	ln1.setWidth(5)
	ln1.setOutline('black')
	ln1.draw(win)

def queen(i,j,c):
	queen = Polygon(Point((i*80)+60,(j*80)+70),
				   Point((i*80)+20,(j*80)+70),
				   Point((i*80)+10,(j*80)+30),
				   Point((i*80)+20,(j*80)+40),
				   Point((i*80)+40,(j*80)+20),
				   Point((i*80)+60,(j*80)+40),
				   Point((i*80)+70,(j*80)+30))
	queen.setWidth(5)
	if c%2 == 1:
		queen.setFill('white')
	else:
		queen.setFill('black')
	queen.draw(win)
	cir = Circle(Point((i*80)+40,(j*80)+15),5)
	cir.setWidth(5)
	if c%2 == 1:
		cir.setFill('white')
	else:
		cir.setFill('black')
	cir.draw(win)

def position():
	for i in range(8):
		for j in range(8):
			if x[i][j] == 1 or x[i][j] == 2:
				pawn(i,j,x[i][j])
			elif x[i][j] == 3 or x[i][j] == 4:
				rook(i,j,x[i][j])
			elif x[i][j] == 5 or x[i][j] == 6:
				knight(i,j,x[i][j])
			elif x[i][j] == 7 or x[i][j] == 8:
				bishop(i,j,x[i][j])
			elif x[i][j] == 9 or x[i][j] == 10:
				queen(i,j,x[i][j])
			elif x[i][j] == 11 or x[i][j] == 12:
				king(i,j,x[i][j])						

main()



