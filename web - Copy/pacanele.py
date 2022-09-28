import random
import sys

linia1 = ("🍓",7,"🍇")
linia2 = ("🍓",7,"🍇")
linia3 = ("🍓",7,"🍇")

castig1 = (7,7,7)
castig2 =('🍓','🍓','🍓')
castig3 = ('🍇','🍇','🍇')

x = random.choice(linia1)
y = random.choice(linia2)
z = random.choice(linia3)

final = (x,y,z)
print(final)

if final == castig1 :
    print("Ai castigat premiul cel mare ( castig 10.000 )")
    dublaj = str(input("doresti sa dublezi?"))
    while "da" in dublaj:
    	rsn = str(input(" 'R' sau 'N' ?"))
    	rosieneagra = ['R','N']
    	d = random.choice(rosieneagra)
    	print(d)
    	stop = ('stop')
    	if rsn == d:
    		print("ai castigat 2x suma castigata")
    	elif rsn == stop:
    		print("felicitari pt suma castigata")
    		sys.exit()
    	else:
    		sys.exit()
    else:
    	sys.exit()
    	
    	
    
elif final == castig2 :
    print("castig 2000")
    dublaj = str(input("doresti sa dublezi?"))
    while "da" in dublaj:
    	rsn = str(input(" 'R' sau 'N' ?"))
    	rosieneagra = ['R','N']
    	d = random.choice(rosieneagra)
    	print(d)
    	stop1 = ('stop')
    	if rsn == d:
    		print("ai castigat 2x suma castigata")
    	elif rsn == stop1:
    		print("felicitari pt suma castigata")
    		sys.exit()
    	else:
    		sys.exit()
    else:
    	sys.exit()
    	
    	
    	
elif final == castig3 :
    print("castig 1000")
    dublaj = str(input("doresti sa dublezi?"))
    while "da" in dublaj:
    	rsn = str(input(" 'R' sau 'N' ?"))
    	rosieneagra = ['R','N']
    	d = random.choice(rosieneagra)
    	print(d)
    	stop2 = ('stop')
    	if rsn == d:
    		print("ai castigat 2x suma castigata")
    	elif rsn == stop2:
    		sys.exit()
    		print("felicitari pt suma castigata")
    	else:
    		sys.exit()
    else:
    	sys.exit()
    	
else:
    print("mai incearca")