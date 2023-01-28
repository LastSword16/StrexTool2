import os
# Anamenü
print (''' 
------------------------------------------------ |
WELCOME TO STREXTOOL                             |
1)Sherlock                                       |
2)TheFatRat                                      | 
3)Ufonet                                         |
4)Impulse                                        |
5)CyberPish                                      |
------------------------------------------------ |
[+]Discord:Strex#0010                            |
[+]Github:https://github.com/LastSword16         |
------------------------------------------------ |   
Choose any number and wait for it to install     |
To learn the tools, type the name of the tool    |
--------------------------------------------------
''')
sayisec =input('Choose any Number:')
if(sayisec == '1'):
      os.system('git clone https://github.com/sherlock-project/sherlock.git')
if(sayisec == '2'):
    os.system('git clone https://github.com/screetsec/TheFatRat.git')
if(sayisec == '3'):
    os.system('git clone https://github.com/epsylon/ufonet.git')
if(sayisec == '4'):
    os.system('git clone https://github.com/LimerBoy/Impulse.git')
if(sayisec == '5'):
    os.system('git clone https://github.com/Cyber-Dioxide/CyberPhish.git')
else:
    print('1.2.3.4.5 You dialed a number other than that, please try another number')
# TOOLLARIN BİLGİLERİ
Sherlock = 'Enter a name and Wait and all the social media accounts of the name you entered in front of you'
TheFatRat = 'A program for creating a rat'
UfoNet = 'Create a Botnet attack and disrupt websites'
Impulse = 'Most Methods are in sms bomb etc.'
CyberPish = 'Classic Phishing Program'
