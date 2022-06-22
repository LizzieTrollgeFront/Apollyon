try:
    import aminofix
    import colorama
    import pyfiglet
    from colorama import Fore, Style, init
    import threading
    init()
    print("\033[1;32;40m[*] Loading...")
except:
    print("\033[1;31;40m[⨉] You do not have all the necessary modules installed. Please install them and try again.")

client = aminofix.Client()
print(Fore.LIGHTYELLOW_EX + "[✓] Successfully loaded in!")

print(Fore.MAGENTA)

pyfiglet.print_figlet("Apollyon", font="colossal")

email = input(Fore.MAGENTA + "[?] Email: ")
password = input(Fore.MAGENTA + "[?] Password: ")

try:
    client.login(email=email, password=password)
    print(Fore.LIGHTYELLOW_EX + "[✓] Successfully logged in!")
except aminofix.exceptions.InvalidPassword:
    print(Fore.LIGHTRED_EX + "[⨉] Invalid Password. Try again with a correct password.")
except aminofix.exceptions.UnsupportedEmail:
    print(Fore.LIGHTRED_EX + "[⨉] Your email is unsupported. Please try again with a different email.")
except aminofix.exceptions.InvalidEmail:
    print(Fore.LIGHTRED_EX + "[⨉] Your email is invalid. Try again with a correct email.")
except aminofix.exceptions.AccountDisabled:
    print(Fore.LIGHTRED_EX + "[⨉] This account has been disabled. Try a different account.")
except aminofix.exceptions.AccountDoesntExist:
    print(Fore.LIGHTRED_EX + "[⨉] This account does not exist. Please recheck the info you inputted and try again.")
except aminofix.exceptions.InvalidAccountOrPassword:
    print(Fore.LIGHTRED_EX + "[⨉] Invalid email or password. Please try again.")


print(Fore.MAGENTA)
coml = input("[*] Target Community Link: ")
comID = client.get_from_code(coml).comId
print(Fore.LIGHTYELLOW_EX + "[✓] Community found!")
client.join_community(comID)
subc = aminofix.SubClient(comId=comID, profile=client.profile)


print(Fore.MAGENTA)
title = input("[*] Title: ")
content = input("[*] Content: ")

def wisp():
    while True:
        try:
            subc.post_wiki(title, content, imageList=[open("Screenshot_20220621-042223.png", 'rb')])
            print(Fore.LIGHTGREEN_EX + "[✓] Wiki sent!")
        except:
            print(Fore.LIGHTRED_EX + "[⨉] Unable to send wiki.")


threads = []

for i in range(1000):
    t = threading.Thread(target=wisp)
    t.daemon = True
    threads.append(t)

for i in range(1000):
    threads[i].start()

for i in range(1000):
    threads[i].join()