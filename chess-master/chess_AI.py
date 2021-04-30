import numpy as np

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

def calculateTotalWeight(boardArray):
	boardArray = convertToWeights(boardArray)
	boardArrayNp = np.array(boardArray)
	sum = np.sum(boardArrayNp)

	return sum

def getAvailable(x,i,j,x1,y1,x2,y2):
	#print(x[i][j])
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

def checkparticularB(i,j):
	c=0
	f=0
	if j+1<8:
		if x[i+1][j+1] == 1 or x[i-1][j+1] == 1:
			c = c+1
	if j+1 < 8:
		if x[i+1][j+1] == 11 or x[i-1][j+1] == 11 or x[i][j+1] == 11:
			c = c+1
	if j-1 > -1:
		if x[i+1][j-1] == 11 or x[i-1][j-1] == 11 or x[i][j-1] == 11:
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
	if c == 0:
		f = 1
	return f

def checkparticularW(i,j):
	c=0
	f=0
	if j-1>-1:
		if x[i+1][j-1] == 2 or x[i-1][j-1] == 2:
			c = c+1
	if j+1 < 8:
		if x[i+1][j+1] == 12 or x[i-1][j+1] == 12 or x[i][j+1] == 12:
			c = c+1
	if j-1 > -1:
		if x[i+1][j-1] == 12 or x[i-1][j-1] == 12 or x[i][j-1] == 12:
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

def getAllAvailableMoves(boardArray, color):
	boardArrayNp = np.array(boardArray)
	#print(boardArrayNp)
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

checkMateW = 0
checkMateB = 0
maxWeight = -99999
minWeight = 99999

def resetMinMax():
	global maxWeight
	global minWeight
	maxWeight = -99999
	minWeight = 99999

def minimax(board, depth, color):
	global maxWeight
	global minWeight
	# print('Called for ')
	# print(board)
	# print('with depth ')
	# print(depth)
	# print('and color')
	# print(color)
	# print(maxWeight)
	# print(minWeight)
	tempboard = np.copy(board)
	if depth == 0 or checkMateW == 1 or checkMateB == 1:
		#print('returning weight' + str(calculateTotalWeight(tempboard)))
		return calculateTotalWeight(tempboard), tempboard

	listOfMoves = getAllAvailableMoves(tempboard, color)
	# print('for position ')
	# print(tempboard)
	# print('available moves are')
	# print(listOfMoves)
	if color == "White":
		for move in listOfMoves:
			weight, tboard = minimax(move, depth - 1, "Black")
			#maxWeight = max(maxWeight, weight)
			if weight > maxWeight:
				#print('inside white if')
				maxWeight = weight
				tempboard = move
		# 		print('changed tempboard to ')
		# 		print(tempboard)
		# print('returning from white ')
		# print(tempboard)
		weightToReturn = maxWeight
		maxWeight = -99999
		return weightToReturn, tempboard

	elif color == "Black":
		for move in listOfMoves:
			weight, tboard = minimax(move, depth - 1, "White")
			#print(weight)
			#minWeight = min(minWeight, weight)
			if weight < minWeight:
				#print('inside black if')
				minWeight = weight
				tempboard = move
		# 		print('changed tempboard to ')
		# 		print(tempboard)
		# print('returning from black ')
		# print(tempboard)
		weightToReturn = minWeight
		minWeight = 99999
		return weightToReturn, tempboard

def minimaxAlphaBetaPruning(board, depth, alpha, beta, color):
	if depth == 0 or checkMateW == 1 or checkMateB == 1:
		return calculateTotalWeight(board)

	listOfMoves = getAllAvailableMoves(board, color)
	if color == "White":
		maxWeight = -99999
		for move in listOfMoves:
			weight = minimaxAlphaBetaPruning(move, depth - 1, alpha, beta, "Black")
			maxWeight = max(maxWeight, weight)
			alpha = max(alpha, weight)
			if beta <= alpha:
				break
		return maxWeight

	elif color == "Black":
		minWeight = 99999
		for move in listOfMoves:
			weight = minimaxAlphaBetaPruning(move, depth - 1, alpha, beta, "White")
			minWeight = min(minWeight, weight)
			beta = min(beta, weight)
			if beta <= alpha:
				break
		return minWeight

x0 = [4,0,2,0,1,0,3,0]
x1 = [6,2,0,0,1,0,0,5]
x2 = [8,2,0,0,0,0,1,7]
x3 = [10,2,0,0,0,0,1,9]
x4 = [12,2,0,0,0,0,1,11]
x5 = [8,2,0,0,0,0,1,7]
x6 = [6,2,0,0,0,0,1,5]
x7 = [4,2,0,0,0,0,1,3]

# x0 = [0,3,0,0,0,0,0,0]
# x1 = [0,0,0,0,0,0,11,0]
# x2 = [0,0,3,0,0,0,0,0]
# x3 = [0,0,0,0,0,0,0,0]
# x4 = [0,12,0,0,0,0,0,0]
# x5 = [5,0,0,0,0,0,0,0]
# x6 = [0,0,0,0,0,0,0,0]
# x7 = [0,0,0,0,0,0,0,0]

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

# listOfMoves = getAllAvailableMoves(x, 'Black')
# print(listOfMoves)

# resetMinMax()
# weight, board = minimax(x, 2, 'Black')
# print(board)

resetMinMax()
weight, board = minimax(x, 2, 'Black')
print(board)
resetMinMax()


# resetMinMax()
# weight, board = minimax(x, 4, 'White')
# print(board)
# resetMinMax()
# weight, board = minimax(board, 4, 'Black')
# print(board)
# resetMinMax()
# weight, board = minimax(board, 4, 'White')
# print(board)
# resetMinMax()
# weight, board = minimax(board, 4, 'Black')
# print(board)
# resetMinMax()
# weight, board = minimax(board, 4, 'White')
# print(board)
# resetMinMax()
# weight, board = minimax(board, 4, 'Black')
# print(board)
# resetMinMax()
# weight, board = minimax(board, 4, 'White')
# print(board)
# resetMinMax()
# weight, board = minimax(board, 4, 'Black')
# print(board)
# resetMinMax()
# weight, board = minimax(board, 4, 'White')
# print(board)
# resetMinMax()
# weight, board = minimax(board, 2, 'Black')
# print(board)
# resetMinMax()
# weight, board = minimax(board, 2, 'White')
# print(board)
# resetMinMax()
# weight, board = minimax(board, 2, 'Black')
# print(board)
# resetMinMax()
# weight, board = minimax(board, 2, 'White')
# print(board)
# resetMinMax()
# weight, board = minimax(board, 2, 'Black')
# print(board)
# resetMinMax()
# weight, board = minimax(board, 2, 'White')
# print(board)
# resetMinMax()
# weight, board = minimax(board, 2, 'Black')
# print(board)
# resetMinMax()
# weight, board = minimax(board, 2, 'White')
# print(board)
# resetMinMax()
# weight, board = minimax(board, 2, 'Black')
# print(board)
# resetMinMax()
# weight, board = minimax(board, 2, 'White')
# print(board)
# resetMinMax()
# weight, board = minimax(board, 2, 'Black')
# print(board)
# resetMinMax()
# weight, board = minimax(board, 2, 'White')
# print(board)
# resetMinMax()
# weight, board = minimax(board, 2, 'Black')
# print(board)
# resetMinMax()
# weight, board = minimax(board, 2, 'White')
# print(board)
# resetMinMax()
# weight, board = minimax(board, 2, 'Black')
# print(board)
# resetMinMax()
# weight, board = minimax(board, 2, 'White')
# print(board)
# resetMinMax()
# weight, board = minimax(board, 2, 'Black')
# print(board)
# resetMinMax()
# weight, board = minimax(board, 2, 'White')
# print(board)
# resetMinMax()
# weight, board = minimax(board, 2, 'Black')
# print(board)
# resetMinMax()
