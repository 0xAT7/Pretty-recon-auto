
#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import argparse
from colorama import Fore, Style
import time
import sys

# arguments
parser_arg_menu = argparse.ArgumentParser(prog='tool', formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=40)
)
parser_arg_menu.add_argument(
"-l" , "--sublist" , help="List contains subdomains Ex: endpoints.txt",
metavar=""
)

parser_arg_menu.add_argument(
"-sn" , "--scanname" , help="Give the Scan a Name Ex: Google",
metavar=""
)

arg_menu = parser_arg_menu.parse_args()
list_file = arg_menu.sublist
scan_name = arg_menu.scanname


def login():
    url = "https://prettyrecon.com/login/"
    r = session.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    csrftoken = soup.find('input', attrs={'name': 'csrfmiddlewaretoken'})['value']
    data = {"csrfmiddlewaretoken": csrftoken, "email": email, "password": password}
    headers = {'Referer': 'https://prettyrecon.com/login/'}
    r = session.post(url=url, data=data, headers=headers, allow_redirects=False)
    r = session.get(url="https://prettyrecon.com/dashboard")
    if "Welcome" in str(r.content):
        print(Fore.GREEN +"[*] You're Successfully Authenticated" + Style.RESET_ALL)


def readList(filePath):
    with open(filePath, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        output = "\r\n".join(lines)
        return(output)


def subScan():
    url = "https://prettyrecon.com/tools/custom_subdomains/"
    r = session.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    csrftoken = soup.find('input', attrs={'name': 'csrfmiddlewaretoken'})['value']
    headers = {"Referer": "https://prettyrecon.com/tools/custom_subdomains/"}
    data = {"csrfmiddlewaretoken": csrftoken, "scan_name": scanName, "targets": subsList}
    r = session.post(url=url, headers=headers, data=data)
    print(Fore.GREEN + "[*] Subdomains Added Successfully with Scan Name: " + Fore.CYAN + scanName + Style.RESET_ALL)



if __name__=='__main__':
    try:
        if arg_menu.sublist:
            #Calling Functions
            session = requests.Session()
            login()
            subsList = readList(list_file)
            scanName = scan_name
            subScan()

            # Calc Time taken
            t1 = time.perf_counter()
            t2 = time.perf_counter() - t1
            print(f'Total time taken: {t2:0.2f} seconds')

        else:
            print(Fore.YELLOW + '[*] Usage: python3 prettyRecon.py -l google.txt -sn Google' + Style.RESET_ALL)
    except:
        sys.exit()
