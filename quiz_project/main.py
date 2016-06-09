#! python3
# multi clipboard project

# mcb.pyw - saves and loads pieces of text to the clipboard
# usage:    py.exe mcb.pyw save <keyword> - saves clipboard to keyword
#           py.exe mcb.pyw <keyword> - loads keyword to clipboard
#           py.exe mcb.pyw list - loads all keywords to clipboard

import shelve, pyperclip, sys

mcb_shelf = shelf.open('mcb')

# todo: save clipboard content
# todo: list keywords and load content.


mcb_shelf.close()