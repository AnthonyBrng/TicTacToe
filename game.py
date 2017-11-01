from gamemanager import Gamemanager

g = Gamemanager()

while g.getWinner() == None:
	g.start()

else:
	print("Game Over")
	if g.getWinner() == "Draw":
		print("Its a Draw!")
	else:
		print("Plalyer " , g.getWinner(), " has won !")
	exit()
