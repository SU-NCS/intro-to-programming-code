#conda install -c conda-forge pyfiglet
#conda install -c anaconda termcolor
import sys
import termcolor
import pyfiglet

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected


termcolor.cprint(pyfiglet.figlet_format('Becky Peltz', font='acrobatic'),
       'white', 'on_magenta')