import argparse
import requests, json
import sys
from sys import argv
import os

parser = argparse.ArgumentParser()

parser.add_argument ("-link", help= "track link", type=str, dest='target', required=True )

args = parser.parse_args()

red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

print (red+"""
JioSaavn Downloader Script
                                                      v 1.0
"""+red)
print (lgreen+bold+"         <===[[ made by github.com/nisarga-developer]]===> \n"+clear)
print (yellow+bold+"   <---(( https://nisarga-developer.github.io/ ))--> \n"+clear)


link = args.target

api = "https://jiosaavn-api-v3.vercel.app/link?link="

try:
        data = requests.get(api+link).json()
        sys.stdout.flush()
        a = lgreen+bold+"[$]"
        b = cyan+bold+"[$]"
        print (a, "[Download Link:", data['media_urls'])
        print(red+"<--------------->"+red)
        print (" "+yellow)

except KeyboardInterrupt:
        print ('Terminating, Bye'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[~]"+" check your internet connection!"+clear)
sys.exit(1)