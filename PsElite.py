from time import sleep
import os
import time
data_list = []
word_list = []
characters = []

def License():
    print("")
    ramz = input("\033[93mLICENSE : \033[92m")
    while ramz == 'HyBroJoinWechannel~>>T.me/Persian_Elite<<~ByMen':
        os.system("clear")
        break
    while ramz != 'HyBroJoinWechannel~>>T.me/Persian_Elite<<~ByMen':
        print("\033[94mEror! please join ~> T.me/Persian_Elite")

logo = """

\033[92m          _____             _        \033[96m _____ _ _ _
\033[92m         |  _  |___ ___ ___|_|___ ___\033[96m|   __| |_| |_ ___
\033[92m         |   __| -_|  _|_ -| | . |   \033[96m|   __| | |  _| -_|
\033[92m         |__|  |___|_| |___|_|__,|_|_\033[96m|_____|_|_|_| |___|
"""

def add(word, met):
    if word == 's':
        pass
    elif word == 'S':
        pass
    else:
        if met == 'data':
            data_list.append(word)
        elif met == 'word':
            word_list.append(word)
        elif met == 'characters':
            characters.append(word)

time = time.asctime(time.localtime(time.time()))

def kobs():
    print("")
    os.system("clear")
    print(logo)
    print("\t\t\t\033[91m       ", time)
    print("")
    print("")
    sleep(1)
    print(" \033[97mLoading [\033[96m■■\033[97m□□□□□□□□ 20%]")
    sleep(2)
    os.system("clear")
    print(logo)
    print("\t\t\t\033[96m       ", time)
    print("")
    print("")
    print("\033[97m Loading [\033[96m■■■■\033[97m□□□□□□ 40%]")
    sleep(2)
    os.system("clear")
    print(logo)
    print("\t\t\t\033[93m       ", time)
    print("")
    print("")
    print("\033[97m Loading [\033[96m■■■■■■\033[97m□□□□ 60%]")
    sleep(2)
    os.system("clear")
    print(logo)
    print("\t\t\t\033[94m       ", time)
    print("")
    print("")
    print(" \033[97mLoading [\033[96m■■■■■■■■\033[97m□□ 80%]")
    sleep(2)
    os.system("clear")
    print(logo)
    print("\t\t\t\033[95m       ", time)
    print("")
    print("")
    print("\033[92m Loading [ \033[96m■■■■■■■■■■ \033[92m\033[93m100%\033[92m ]")
    sleep(2)
    os.system("clear")
    print(logo)
    print("\nOK :) ~> \033[92mT.me/Persian_Elite\n\033[93m[\033[92m✓\033[93m] Successfully completed")

def get_data():
    print ("\033[96m[\033[91m!\033[96m] \033[1;35m  s = skip       n or N = No                \033[93mAuthor ~> MetiAlion\033[1;m"+'\n')
    add(input("[\033[96m+\033[93m] \033[1;32mName: \033[93m"), 'data')
    add(input("[\033[96m+\033[93m] \033[92mLast Name: \033[93m"), 'data')
    add(input("[\033[96m+\033[93m] \033[92mAge :\033[93m "), 'data')
    job = input("[\033[96m+\033[93m] \033[92mJob : \033[93m")
    if len(job) == 6:
        add(job, 'word')
        add(job, 'data')
    elif len(job) > 6:
        add(job, 'word')
        add(job, 'data')
    else:
        add(job, 'data')
    birthday = input("[\033[96m+\033[93m] \033[92mBirthday (zzzz/yy/xx) : \033[93m")
    if birthday == 's':
        pass
    elif birthday == 'S':
        pass
    else:
        if '/' in birthday:
            birthday_s = birthday.split("/")
            if len(birthday_s) == 3:
                add(birthday_s[0]+birthday_s[0], 'word')
                add(birthday_s[2], 'data')
            else:
                pass
        else:
            pass
    while True:
        x = input("[\033[96m+\033[93m] \033[92mPhone Number { \033[94mfor next < n > \033[92m} : \033[93m")
        if x == 'n':
            break
        elif x == 'N':
            break
        else:
            if len(x) == 6:
                add(x, 'word')
                add(x, 'data')
            elif len(x) > 6:
                add(x, 'word')
                add(x, 'data')
            elif len(x) < 6:
                add(x, 'data')
    while True:
        x = input("[\033[96m+\033[93m] \033[92mOther { \033[94mfor next < n > \033[92m} : \033[93m")
        if x == 'n':
            break
        elif x == 'N':
            break
        else:
            if len(x) == 6:
                add(x, 'word')
                add(x, 'data')
            elif len(x) > 6:
                add(x, 'word')
                add(x, 'data')
            elif len(x) < 6:
                add(x, 'data')
    while True:
        x = input("[\033[96m+\033[93m] \033[92mMore ● \033[91m@,*,!,#,% ... \033[92m● { \033[94mn = Enter \033[92m} : \033[93m")
        if x == 'n':
            break
        elif x == 'N':
            break
        else:
            add(x, 'characters')

banner = '''\033[92m

             ____________________________________________________
            /                                                    \      
           |    _____________________________________________     |     
           |   |                                             |    |
           |   |  \033[95mC:\> \033[96mpython PsElite.py                     \033[92m|    |
           |   |   \033[97mOK Starting...                            \033[92m|    |
           |   |   \033[97m■■■■■■■■□99%                              \033[92m|    |
           |   |   \033[97mSuccessfully completed (:                 \033[92m|    |
           |   |                                             |    |
           |   |  \033[95m>> \033[96mcat Password_List.lst                   \033[92m|    |
           |   |   \033[90mpassssytix                                \033[92m|    |
           |   |   \033[90mPasswordOne                               \033[92m|    |
           |   |   \033[90mPassword27                                \033[92m|    |
           |   |   \033[90mPasswordiodj62                            \033[92m|    |
           |   |   \033[90mPassword9277                              \033[92m|    |
           |   |   \033[90mPassword1400                              \033[92m|    |
           |   |_____________________________________________|    |
           |                                                      |
            \_____________________________________________________/
                   \_______________________________________/


  \033[34m< ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■  >


\033[31m              ●  Telegram : @Persian_Elite
              ●  YouTube  : Persian Elite
              ●  Insta    : instagram.com/Persian.Elite


  \033[34m< ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■  >

'''

def generat_save():
    f = open('Password_List.lst', 'a')
    for wr in word_list:
        f.write(wr+'\n')
    for da1 in data_list:
        for da2 in data_list:
            for chra in characters:
                f.write(da1+da2+'\n')
                f.write(da1+chra+da2+'\n')
    f.close()
    print ("\033[1;37m\nPassword List Maked in < \033[93mPassword_List.lst \033[97m> ~>  \033[34m T.me/Persian_Elite \033[1;m"+'\n')
def kobs636():
    print("\033[93m")
    os.system("clear")
    print("■■□□□□□□□□ 20%")
    time.sleep(2)
    os.system("clear")
    print("■■■■□□□□□□ 40%")
    time.sleep(1)
    os.system("clear")
    print("■■■■■■□□□□ 60%")
    time.sleep(2)
    os.system("clear")
    print("■■■■■■■■□□ 80%")
    time.sleep(1)
    os.system("clear")
    print("■■■■■■■■■■ 100%")
    time.sleep(1)
    os.system("clear")
    print("OK (:")

if __name__ == '__main__':
    License()
    print (banner)
    get_data()
    kobs()
    generat_save()

