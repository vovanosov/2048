import pygame, pygame.mixer
import random
import time

def inter (x1, y1, x2, y2, db1, db2):
	if x1 > x2 - db1 and x1 < x2 + db2 and y1 > y2 - db1 and y1 < y2 + db2:
		return 1
	else:
		return 0

def inter1 (x1, y1, x2, y2, db1, db2, ds):
	if x1 > x2 - db1 and x1 < x2 + db2 and y2 < ds + y1:
		return 1
	else:
		return 0
		
def inter2 (x1, y1, x2, y2, db1, db2, db3):
	if x1 > x2 - db1 and x1 < x2 + db2 and y1 > y2 - db3 and y1 < y2 + db3:
		return 1
	else:
		return 0

#hello

pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((1280,720),pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)
screen = pygame.Surface((1280,720))
card = pygame.image.load("./data/card.png")
give = pygame.image.load("./data/give.png")
money = pygame.image.load("./data/money.png")
cancel = pygame.image.load("./data/cancel.png")
prevr = pygame.image.load("./data/prevr.png")
new = pygame.image.load("./data/new.png")
new1 = pygame.image.load("./data/new1.png")
option = pygame.image.load("./data/option.png")
option1 = pygame.image.load("./data/option1.png")
exit = pygame.image.load("./data/exit.png")
exit1 = pygame.image.load("./data/exit1.png")
sound = pygame.image.load("./data/sound.png")
musika = pygame.image.load("./data/musika.png")
onn = pygame.image.load("./data/on.png")
offf = pygame.image.load("./data/off.png")
breakk = pygame.image.load("./data/break.png")
break1 = pygame.image.load("./data/break1.png")

money.set_colorkey((0,255,0))

Begin = False
ind = 0
numb = 0

a = []
xg = []
xg1 = 200
yg = []
x = 0
y = 0
for i in range (0,4):
	xg1 += 100
	xg.append (xg1)
	yg.append (100)

xcard = []
ycard = []
xc = -11940
for i in range (0,200):
	xc = xc + 60
	xcard.append (xc)
	ycard.append (310)
	a1 = random.randint (1,6)
	a1 = 2**a1
	a.append(a1)
	
counter = 0

off = True
on = False
off1 = True
on1 = False

def music():
	pygame.mixer.init()
	pygame.mixer.music.load("./data/music.mp3")
	pygame.mixer.music.play(loops=-1)
	
f = open("./data/kol.txt", "r")
numb = f.read()
f.close()

numb2 = int(numb)

ost = 0

buttonn = 0

music()
nastr = False

while Begin == False:
	for j in pygame.event.get():
		if j.type == pygame.KEYUP and j.key == pygame.K_ESCAPE:
			Begin = True
		if j.type == pygame.MOUSEBUTTONUP:
			x,y = j.pos
			
		
	
	screen.fill ((0,140,0))
	screen.blit(new, (1000,300))
	screen.blit(option, (1000,400))
	screen.blit(exit, (1000,500))
	if j.type == pygame.MOUSEBUTTONDOWN:
		x, y = j.pos
		if inter2 (x, y, 1000, 300, 1, 200, 40):
			if off1 == True:
				pygame.mixer.init()
				neww = pygame.mixer.Sound('./data/neww.wav')
				neww.play()
			screen.blit(new1, (1000,300))
			ind = 0
			numb = 0

			a = []
			xg = []
			xg1 = 200
			yg = []
			x = 0
			y = 0
			for i in range (0,4):
				xg1 += 100
				xg.append (xg1)
				yg.append (100)

			xcard = []
			ycard = []
			xc = -11940
			for i in range (0,200):
				xc = xc + 60
				xcard.append (xc)
				ycard.append (310)
				a1 = random.randint (1,6)
				a1 = 2**a1
				a.append(a1)
				
			counter = 0
				
			f = open("./data/kol.txt", "r")
			numb = f.read()
			f.close()

			numb2 = int(numb)

			ost = 0

			
			
			
		if inter2 (x, y, 1000, 400, 1, 200, 40):
			if off1 == True:
				pygame.mixer.init()
				optionn = pygame.mixer.Sound('./data/options.wav')
				optionn.play()
			screen.blit(option1, (1000,400))
			nastr = True
			
		if inter2 (x, y, 1000, 500, 1, 200, 40):
			Begin = True
			screen.blit(exit1, (1000,500))
			
		x = y = 0
	
	
		
	for i in range (0,200):
		for k in range (0,4):
			screen.blit(give, (xg[k],yg[k]))
		
			if inter (xg[k], yg[k], x, y, 80, 1) and xcard[i] >= 60:
				class animation (): #Animation of map movement
					while ind != 1:
						for t2 in pygame.event.get():
							if t2.type == pygame.KEYUP and t2.key == pygame.K_ESCAPE:
								break
								 
						if inter (xcard[i], ycard[i], xg[k], yg[k], 50,50):
							ycard[i] = yg[k]
							xcard[i] = xg[k]
							yg[k] = ycard[i] + 79
							ind += 1
							
								
						if xcard[i] != xg[k]:
							if xcard[i] < xg[k]:
								xcard[i] += 7
						
						if ycard[i] > yg[k]:
							ycard[i] -= 7
						if ycard[i] < yg[k]:
							ycard[i] += 7
								
								
						screen.fill ((0,140,0))
						
						for t5 in range (0,200): #loading all cards
							
							if xcard[t5] >= 60:
								screen.blit(card, (xcard[t5],ycard[t5]))
							
									
						for t3 in range (0,4):
							screen.blit(give, (xg[t3],yg[t3]))
							
						num = pygame.font.SysFont('monospace', 50)
						number = num.render('' + str(numb) , True, (255, 150, 0))
						screen.blit(money, (1000,50))
						screen.blit(number, (1050,45))
						screen.blit(cancel, (800,300))
						screen.blit(new, (1000,300))
						screen.blit(option, (1000,400))
						screen.blit(exit, (1000,500))
						window.blit(screen, (0,0))
						pygame.display.update()
						
				animation()
				
				if off1 == True:
					pygame.mixer.init()
					cardd = pygame.mixer.Sound('./data/card.wav')
					cardd.play()
					
				ind = 0
					
				#if ind == True:
				ycard[i] = yg[k] - 79
				xcard[i] = xg[k]
				#yg[k] = ycard[i] + 79
				x = y = 0
				
				for i2 in range (0,200):
					screen.blit(card, (xcard[i],ycard[i]))
					if xcard[i2] < 60:
						xcard[i2] += 60
	
		for jj in range (0,200):
			if inter (xcard[jj], ycard[jj], xcard[i], ycard[i], 80, 80) and ycard[jj] < ycard[i]: #odinakovie carti clojenie
				if a[i] == a[jj] and ycard[i] > ycard[jj]:
					class animation2 (): #animation of adding cards
						while ycard[i] != ycard[jj]:
							for r2 in pygame.event.get():
								if r2.type == pygame.KEYUP and r2.key == pygame.K_ESCAPE:
									break
							ycard[i] -= 1
							for k2 in range (0,4):
								if yg[k2] == ycard[jj] + 158 and xg[k2] == xcard[jj]:
									xg[k2] = 10000
							screen.fill ((0,140,0))
							
							for t5 in range (0,200):
								if xcard[t5] > 60:
									screen.blit(prevr, (xcard[t5],ycard[t5]))
								if xcard[t5] == 60:
									screen.blit(card, (xcard[t5],ycard[t5]))
								
										
							for t3 in range (0,4):
								screen.blit(give, (xg[t3],yg[t3]))
								
							num = pygame.font.SysFont('monospace', 50)
							number = num.render('' + str(numb) , True, (255, 150, 0))
							screen.blit(money, (1000,50))
							screen.blit(number, (1050,45))
							screen.blit(cancel, (800,300))
							screen.blit(new, (1000,300))
							screen.blit(option, (1000,400))
							screen.blit(exit, (1000,500))
							window.blit(screen, (0,0))
							pygame.display.update()
							
					animation2()
						
					if off1 == True:
						pygame.mixer.init()
						coin = pygame.mixer.Sound('./data/coin.wav')
						coin.play()
					
					numb2 += 1
					numb = int(numb2)
					
					f = open("./data/kol.txt", "w")
					f.write(str(numb))
					f.close()
					
					xcard[i] = 30000
					ycard[i] = -30000
					a[jj] = a[jj] * 2
					for k2 in range (0,4):
						if xg[k2] == 10000:
							xg[k2] = xcard[jj]
						if yg[k2] == ycard[jj] + 158 and xg[k2] == xcard[jj]:
							yg[k2] -= 79
							
							
							
		
		if inter (x, y, 800, 300, 1, 80) and numb2 >= 50: #cancel a card
			
			for nas in range (0,200):
				if xcard[nas] == 60:
					nass = nas
			class animation3 (): #Animation of map movement
				while 1:
					for d2 in pygame.event.get():
						if d2.type == pygame.KEYUP and d2.key == pygame.K_ESCAPE:
							break
							 
					#if inter (xcard[nass], ycard[nass], 800, 300, 50,50):
					if xcard[nass] == 800:
						ycard[nass] = 300
						break
					
							
					if xcard[nass] != 800:
						
						if xcard[nass] < 800:
							xcard[nass] += 5
					
					if ycard[nass] > 300:
						ycard[nass] -= 5
					if ycard[nass] < 300:
						ycard[nass] += 5
							
							
					screen.fill ((0,140,0))
					
					for t5 in range (0,200):
						
						if xcard[t5] >= 60:
							screen.blit(card, (xcard[t5],ycard[t5]))
						
					for t3 in range (0,4):
						screen.blit(give, (xg[t3],yg[t3]))
						
					num = pygame.font.SysFont('monospace', 50)
					number = num.render('' + str(numb) , True, (255, 150, 0))
					screen.blit(money, (1000,50))
					screen.blit(number, (1050,45))
					screen.blit(cancel, (800,300))
					screen.blit(new, (1000,300))
					screen.blit(option, (1000,400))
					screen.blit(exit, (1000,500))
					window.blit(screen, (0,0))
					pygame.display.update()
				
			animation3()
			
			if off1 == True:
				pygame.mixer.init()
				otm = pygame.mixer.Sound('./data/otmena.wav')
				otm.play()
			
			x = y = 0
			xcard[nass] = -30000
			numb2 -= 50
			numb = int(numb2)
			
			f = open("./data/kol.txt", "w")
			f.write(str(numb))
			f.close()
			
			for nas2 in range (0,200):
				if xcard[nas2] < 60:
					xcard[nas2] += 60
		
			
		if a[i] > 10:
			myfont = pygame.font.SysFont('monospace', 25)
		if a[i] < 10:
			myfont = pygame.font.SysFont('monospace', 25)
		if a[i] > 100:
			myfont = pygame.font.SysFont('monospace', 17)
			
			
		string = myfont.render('' + str(a[i]) , True, (255, 0, 255))
		
		if xcard[i] >= 60:
			screen.blit(card, (xcard[i],ycard[i]))
		
		if xcard[i] >= 60:
			if a[i] > 10 and a[i] < 1000:
				screen.blit(string, (xcard[i]+10,ycard[i]+25))
			if a[i] < 10:
				screen.blit(string, (xcard[i]+17,ycard[i]+25))
			if a[i] > 1000:
				screen.blit(string, (xcard[i]+5,ycard[i]+25))
				
				
		for k2 in range (0,4):
			if yg[k2] >= 653:
				xg[k2] = -10000
				
		
		
	if inter2 (x, y, 1000, 400, 1, 200, 40):
		while nastr == True:
			for op in pygame.event.get():
				if op.type == pygame.MOUSEMOTION:
					x,y = op.pos
				if op.type == pygame.MOUSEBUTTONDOWN:
					x,y = op.pos
					
					if inter (825, 150, x, y, 185, 1): #off music
						if off1 == True or on == False:
							pygame.mixer.init()
							pygame.mixer.music.load("./data/options.wav")
							pygame.mixer.music.play()
						x = y = 0
						on = True
							
					if on == True:
						if inter (640, 150, x, y, 185, 1): #on music
							
							pygame.mixer.init()
							if off1 == True:
								optionn = pygame.mixer.Sound('./data/options.wav')
								optionn.play()
							music()
							on = False
							
					if inter (825, 350, x, y, 185, 1): # off sound
						off1 = False
						x = y = 0
					if inter (640, 350, x, y, 185, 1): # on sound
						off1 = True
						pygame.mixer.init()
						optionn = pygame.mixer.Sound('./data/options.wav')
						optionn.play()
						x = y = 0
						
					if inter (1150, 10, x, y, 100, 1):
						nastr = False
				
					
				
			screen.fill ((0,140,0))
			screen.blit(musika, (270,150))
			screen.blit(sound, (270,350))
			screen.blit(breakk, (1150,10))
			
			if inter (640, 150, x, y, 185, 1): #on music
				screen.blit(onn, (640,150))
			if inter (640, 350, x, y, 185, 1): #on sound
				screen.blit(onn, (640,350))
			if inter (825, 350, x, y, 185, 1): #off sound
				screen.blit(offf, (825,350))
			if inter (825, 150, x, y, 185, 1): #off music
				screen.blit(offf, (825,150))
			if inter (1150, 10, x, y, 100, 1): #break
				screen.blit(break1, (1150,10))
			
			
			window.blit(screen, (0,0))
			pygame.display.update()
				
	myfont = pygame.font.SysFont('monospace', 50)
	number = myfont.render('' + str(numb) , True, (255, 150, 0))
	
	screen.blit(money, (1000,50))
	screen.blit(number, (1050,45))
	screen.blit(cancel, (800,300))
	
	
	window.blit(screen, (0,0))
	pygame.display.update()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	