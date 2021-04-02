import random
import sys
money = 100
print("  ██████  ███▄    █     ▄████▄   ▄▄▄        ██████  ██▓ ███▄    █  ▒█████  ")
print("▒██    ▒  ██ ▀█   █    ▒██▀ ▀█  ▒████▄    ▒██    ▒ ▓██▒ ██ ▀█   █ ▒██▒  ██▒")
print("░ ▓██▄   ▓██  ▀█ ██▒   ▒▓█    ▄ ▒██  ▀█▄  ░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒██░  ██▒")
print("  ▒   ██▒▓██▒  ▐▌██▒   ▒▓▓▄ ▄██▒░██▄▄▄▄██   ▒   ██▒░██░▓██▒  ▐▌██▒▒██   ██░")
print("▒██████▒▒▒██░   ▓██░   ▒ ▓███▀ ░ ▓█   ▓██▒▒██████▒▒░██░▒██░   ▓██░░ ████▓▒░")
print("▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒    ░ ░▒ ▒  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ")
print("░ ░▒  ░ ░░ ░░   ░ ▒░     ░  ▒     ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░  ░ ▒ ▒░ ")
print("░  ░  ░     ░   ░ ░    ░          ░   ▒   ░  ░  ░   ▒ ░   ░   ░ ░ ░ ░ ░ ▒  ")
print("      ░           ░    ░ ░            ░  ░      ░   ░           ░     ░ ░  ")
print("                       ░                                                   ")

resulta=random.randrange(1, 50) 
if resulta == [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50]:
	resultared = ("true")
else:
	resultared = ("false")
if resulta == [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49]:
	reslutabalck = ("true")
else:
	reslutabalck = ("false")
def bet(bet,money):
	print("votre porte feuilleet de", money,"$")
	bet = int(input("mise($):"))
	if bet > money:
		print("sold insufisant")
		sys.exit()
	else: 
		money -= bet
		print("votre sold et de",money,"$")
bet(1,money)


def num(num,money):
	num= int(input("num(0-49):"))
	if num > 49:
		print("combre doit aitre comprie entre 0 et 49")
		sys.exit()
	else:
		if resulta == num:
			money = bet*2
			print (resulta)
			print("you win")
			print("votre mise a été doublé")
			print(money)
		else:
			print(resulta)
			print("you loose")

def color ():
	col= input("color red or black:")
	if col == ("red"):
		if resultared == ("true"):
			print("you win")
			money = moeny+bet*2
		else:
			print("you loose")
			money = moeny-bet
			pass
	else:
		if col == ("black"):
			if reslutabalck == ("true"):
				print("you win")
				money = moeny+bet*2
			else:
				if reslutabalck == ("false"):
					print("you loose")
					money = moeny-bet
				pass
			pass
		pass

choi = input("num or color:")
if choi == ("num"):
	num(1,money)
else:
	if choi == ("color"):
		color()
	else:
		print("choix non encadrer")
		sys.exit()
		pass
	pass



	
