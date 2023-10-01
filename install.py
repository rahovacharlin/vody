##code
import os
import sys
import time
import string

W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'

def vody():
	os.system("clear")
	print(logo)
	print('')
	print('   %sRaha misy manome ny zavatra ansee kinga miteny hoe!%s'%(G,G))
	print("  \033[97;1mvaliny \033[97;1m: " + dada)
	print(banner)
	print('')
	print("   \033[97;1mVita tompoko ry \033[92;1m" + USER1)
	print("   \033[97;1mMipetraka any \033[92;1m" + USER2 )
	print('')
	print(' \033[91;1m[0] \033[97;1mExit ')
	user6=input(" \033[91;1m[√] \033[97;1mchoose :  ")
	if user6 in ["0", "00"]:
		os.system("clear")
		exit()
	else:
		vody()
	
	
def xox(z):
	for e in z + '':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.1)
banner=("""
   \033[93;1m_     _  _______  _______   _____  
  (_)   (_)(_______)(__ _ __) (_____) 
  (_)   (_)   (_)      (_)   (_)___(_)
  (_)   (_)   (_)      (_)   (_______)
   (_)_(_)  __(_)__    (_)   (_)   (_)
    (___)  (_______)   (_)   (_)   (_)""")
logo=("""
  \033[92;1m┌───────────────────────────────────────────────────┐
  \033[91;1m│  \033[92;1m┌─────────────────────────────────────────────┐  \033[91;1m│
  \033[91;1m│  \033[91;1m│  \033[92;1m┌───────────────────────────────────────┐  \033[91;1m│  \033[91;1m│
  \033[91;1m│  \033[91;1m│  \033[91;1m│   \033[91;1m[🌺] \033[96;1mAUTHOR   : \033[95;1mRAHOVA CHARLIN      \033[91;1m│  \033[91;1m│  \033[91;1m│
  \033[91;1m│  \033[91;1m│  \033[91;1m│   \033[91;1m[🌺] \033[92;1mGITHUB   : \033[94;1mR4H0V4-CH4RL1N      \033[91;1m│  \033[91;1m│  \033[91;1m│ 
  \033[91;1m│  \033[91;1m│  \033[91;1m│   \033[91;1m[🌺] \033[93;1mCOUNTRY  : \033[93;1mMADAGASCAR          \033[91;1m│  \033[91;1m│  \033[91;1m│ 
  \033[91;1m│  \033[91;1m│  \033[91;1m│   \033[91;1m[🌺] \033[94;1mTOOLS    : \033[92;1mINSTALL ALL PKG     \033[91;1m│  \033[91;1m│  \033[91;1m│ 
  \033[91;1m│  \033[91;1m│  \033[91;1m│   \033[91;1m[🌺] \033[95;1mVERSION  : \033[96;1m2.0                 \033[91;1m│  \033[91;1m│  \033[91;1m│
  \033[91;1m│  \033[91;1m│  \033[92;1m└───────────────────────────────────────┘  \033[91;1m│  \033[91;1m│
  \033[91;1m│  \033[92;1m└─────────────────────────────────────────────┘  \033[91;1m│
  \033[92;1m└───────────────────────────────────────────────────┘""")
os.system('clear')
print(logo)
print("                     \033[97;1m\033[1;41m🌺 Anaranao 🌺\033[1;0m")
print("")
USER1 =input("    \033[95;1m🌺🌺⫸   ")
print("")
print("                 \033[1;47m🌺 aiza no mipetraka 🌺\033[1;0m")
print("")
USER2 =input("    \033[95;1m🌺🌺⫸   ")
print("")
print(" \033[91;1m[•]  \033[92;1mMisaotra tompoko !")
user=input(" \033[91;1m[•]  \033[97mpress enter to install all package")
os.system('apt update')
os.system('apt upgrade')
os.system('pkg install python -y')
os.system('pkg install python2 -y')
os.system('pkg istall python3 -y')
os.system('pkg install python-dev')
os.system('pkg install python-pip')
os.system('pkg install wget')
os.system('pkg install nano -y')
os.system('pkg install bs4')
os.system('pip install bs4')
os.system('pkg install requests')
os.system('pip install requests')
os.system('pkg install futures')
os.system('pip install futures')
os.system('pkg install mechanize')
os.system('pkg install rich')
os.system('pip install rich')
os.system('pip install mechanize')
os.system('pkg install curl -y')
os.system('pkg install openssl -y')
os.system('pkg install openssh -y')
os.system('pkg install java -y')
os.system('pkg install fish -y')
os.system('pkg install cowsay -y')
os.system('pkg install php -y')
os.system('pkg install figlet -y')
os.system('pkg install ruby -y')
os.system('clear')
print(logo)
print('')
xox('   %sRaha misy manome ny zavatra ansee kinga miteny hoe!%s'%(G,G))
print('')
dada=input("  \033[97;1mvaliny \033[97;1m: ")
print(banner)
print('')
print("   \033[97;1mVita tompoko ry \033[92;1m" + USER1)
print("   \033[97;1mMipetraka any \033[92;1m" + USER2 )
print('')
print(' \033[91;1m[0] \033[97;1mExit ')
user6=input(" \033[91;1m[√] \033[97;1mchoose :  ")
if user6 in ["0", "00"]:
	os.system("clear")
	exit()
else:
	vody()