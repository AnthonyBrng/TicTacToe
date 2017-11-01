

class Board:

	def __init__(self):
		self.board = [0] * 9

	def printBoard(self):
		for i in range(0,3):
			rowwins = self.board[i*3:3*(i+1)]
			print(rowwins)


	def setMove(self, move, player):
		self.board[3*int(move[0])+int(move[1])] = player

	def getBoardValue(self, row, col):
		return self.board[3*row+col] 


	


