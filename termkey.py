risk ='"'
terabaap = "extra-keys = [['F1','F2','F3','F4','F5','F6','F12'],['ESC','TAB','CTRL','ALT','-','DOWN','UP']]"
#
damage = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
#
shift = "extra-keys = [['ESC','/','-','HOME','UP','END'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT']]"
 
from colorama import Fore

print(Fore.WHITE + '__________________________________________') 

TGREEN =  '\033[32m'
print (TGREEN + "✓TERMKEY:Termux Additional Keyboard")
#Green because "we are so called Hackers."")
print(Fore.CYAN + "             Coded by: Devil Techno")
print(Fore.WHITE + '__________________________________________') 
def mainMenu():
	print("1.  Only Arrow keys")
	print("2.  Arrow keys + Page UP & DOWN")
	print("3.  Arrow Keys + PGUP & PGDN + Function keys")
	print("4.  Reset Add. Keyboard")
	print("")
	print("5.  Exit")
	while True: 
		try:
			selection=int(input("[>] Select any option:"))
			if selection==1:
				one()
			elif selection==2:two()
			elif selection==3:three()
			elif selection==4:four()
			elif selection==5:
				break
			else:
				    print("[!]Are you High? Select Only 1-3 or 4 !")
		except ValueError:print("[!]WTF!? Enter only option 1-3 or 4 !")
		exit
				
def one():
	   print:("KEYBOARD OPTION ONE")
	   anykey=input(f"COPY & PASTE IN NEW TAB:>> mkdir $HOME/.termux/ ;echo {risk}{shift}{risk} >> $HOME/.termux/termux.properties && termux-reload-settings && sleep 1 &&logout")
	   mainMenu()
					
def two():
		print:("KEYBOARD OPTION TWO")
		anykey=input(f"COPY & PASTE IN NEW TAB:>> mkdir $HOME/.termux/ ;echo {risk}{damage}{risk} >> $HOME/.termux/termux.properties && termux-reload-settings && sleep 1 &&logout")
		mainMenu()
					
def three():
		print:("KEYBOARD OPTION THREE")
		anykey=input(f"COPY & PASTE IN NEW TAB:>> mkdir $HOME/.termux/ ;echo {risk}{terabaap}{risk} >> $HOME/.termux/termux.properties && termux-reload-settings && sleep 1 &&logout")
		mainMenu()

def four():
	import os
	os.system('rm -r $HOME/.termux')
	mainMenu()				
#main routine
mainMenu()