import requests
from bs4 import BeautifulSoup
import sys, argparse
import bcolors
import os

def banner():
    print("""
        ░██████╗░██╗████████╗░░░░░░███████╗██╗███╗░░██╗██████╗░███████╗██████╗░
        ██╔════╝░██║╚══██╔══╝░░░░░░██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗
        ██║░░██╗░██║░░░██║░░░█████╗█████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
        ██║░░╚██╗██║░░░██║░░░╚════╝██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
        ╚██████╔╝██║░░░██║░░░░░░░░░██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║
        ░╚═════╝░╚═╝░░░╚═╝░░░░░░░░░╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝
                                                                    Code by NG          
        """)

if len(sys.argv) > 1:
    banner()
    if (sys.argv[1] == '-u'):
        try:
           input_url = sys.argv[2]
           if (os.path.exists(input_url) == True):
            parser = argparse.ArgumentParser()
            parser.add_argument("-u", required=True)
            args = parser.parse_args()

            input_file = open(input_url, "r")
            input_file_line = input_file.readlines()
            print(bcolors.BITALIC + "Searching for '.git' hidden-Directories")
            for file_url in input_file_line:
                try:
                    url = file_url.strip()
                    url_dir = url + ".git"
                    print('Full URL',url_dir , requests.get(url_dir).status_code)
                    if(requests.get(url_dir).status_code == 200):
                        input_code= requests.get(url_dir).text

                        soup = BeautifulSoup(input_code, 'html.parser')
                        links = [a.attrs.get('href') for a in soup.select('a')]

                        print(bcolors.OKMSG + "All available Dir in hidden dir")
                        for i in range(len(links)):
                            print(links[i])
                    else:
                        print(bcolors.ERRMSG + 'Git repository not available publically')
                except:
                    print(bcolors.ERRMSG + 'This is not valid URL ' + url)

           elif (os.path.exists(input_url) == False):
                   parser = argparse.ArgumentParser()
                   parser.add_argument("-u", required=True)
                   args = parser.parse_args()

                   print(bcolors.BITALIC + "Searching for '.git' hidden-Directories")

                   https_url = "http://" + input_url
                   url_dir = https_url + ".git"
                   print('Full URL', url_dir)
                   input_code = requests.get(url_dir).text

                   soup = BeautifulSoup(input_code, 'html.parser')
                   links = [a.attrs.get('href') for a in soup.select('a')]

                   print(bcolors.OKMSG + "All available Dir in hidden dir")
                   for i in range(len(links)):
                       print(links[i])


        except:
            print('Please enter python gitfinder.py -u <valid URL where you want to check .git hidden Dir >')

    elif ((sys.argv[1] == '-h') | (sys.argv[1] == '--help')):
        print(bcolors.BOLD + 'usage: gitfinder.py [-h] -u URL' '\n' 'OPTIONS:' '\n' '-h,--help    '
                             'show this help message and exit' '\n''-u URL,   --URL valid URL where you want to check .git hidden Dir')
else:
    banner()
    print(bcolors.ERR + 'Please select at-least 1 option from -u or -h, with a valid URL')
