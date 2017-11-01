
from board import Board
from player import Player
import os

class Gamemanager:


	def __init__(self):
		self.board = [0] * 9
		self.players = []
		self.currentTurn = 1
		self.toggle = -1 
		self.getPlayerNames()
		self.winner = None
		self.clear = lambda : os.system('clear')
		self.clear()

	def askTurn(self):
		self.printBoard()
		print(self.players[self.currentTurn-1], "'s turn!")
		return (input("row: "), input("col: "))
		pass
			

	def isValidMove(self, move):
		try:
			row = int(move[0])
			col = int(move[1])
		except ValueError:
			return False
		cond1 = row in range(0,3) and col in range(0,3)	
		cond2 = cond1 and self.board[3*row+col]  == 0
		return cond2


	def setTurn(self,move):
		self.board[3*int(move[0])+int(move[1])] = self.currentTurn
		if self.isWon():
			self.winner = self.players[self.currentTurn-1]
			return
		elif 0 not in self.board:
			self.winner = "Draw"
			return
		self.toggle *= -1
		self.currentTurn += self.toggle


	def printBoard(self):
		self.clear()
		iconMap = lambda x: [" ", "X", "O"][x]
		print("     0     1     2")
		print("  -------------------")
		#each row
		for i in range(0,3):
			row = self.board[i*3:3*(i+1)]
			print(i,"| ", iconMap(row[0]), " | ", iconMap(row[1]), " | ", iconMap(row[2]), " |")
			print("  -------------------")

		 

	def isWon(self) :
		wins = []
		for i in range(0,3):
			wins.append(set(self.board[i*3:3*(i+1)]))
			wins.append(set(self.board[i::3]))
			wins.append(set(self.board[::4]))
			wins.append(set(self.board[2:-2:2]))
		
		return not [s for s in wins if len(s) == 1 and s.pop() != 0] == []


	def getPlayerNames(self):
		self.players.append(input("Name of Player1: "))
		self.players.append(input("Name of Player2: "))


	def getWinner(self):
		return self.winner

	def start(self):
		self.clear()
		move = self.askTurn()
		while not self.isValidMove(move):
			print("Invalid Move! Try again!")
			move = self.askTurn()
		self.setTurn(move)

