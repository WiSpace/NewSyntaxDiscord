# imports
import re
import random
import pyperclip
import argparse
from msvcrt import getch

from syntax import tokens
from colors import Colors

# args
parser = argparse.ArgumentParser(description='Create new syntax for Discord! How to use: Go to syntax.py and in the tokens dictionary, the key is the regular expression and the value is the color that the regular expression will be colored with. In colors.py all colors for code.')
parser.add_argument('path', type=str, help='Input file')
parser.add_argument('-e', default="utf-8", type=str, help='Input file encoding')

args = parser.parse_args()

# color print
def pr_e(color, text):
    return f"[2;"+color+"m"+text+"[0m"

# get code
with open(args.path, args.e) as f:
    code = f.read()

for reg, color in tokens.items():
    # find all regular expressions
    regex = re.findall(reg, code)
    
    # traversing list
    for i in regex:
        # replace element to colored element
        code = code.replace(i, pr_e(color, i))

# copy to clipboard
pyperclip.copy('```ansi\n'+code+"\n```")

# exit
print("Нажми Ctrl+V в Discord")
getch()
