import getopt, sys
from update_check import isUpToDate

from lib import *

# Debug
err = "[  ERROR  ]  "
alert = "[  ALERT  ]  "

# Check update
if isUpToDate(__file__, "https://github.com/PointVirguIe/Map-my-Web-trafic/main.py") == False:
   print(alert + "There is an newer version on Github. Please download the new version.")

def main(argv):
    if sys.argv[1] == "-h":
       pass
    if sys.argv[1] == "-rm":
       pass
    if sys.argv[1] == "-a":
       pass
    if sys.argv[1] == "-ls":
       pass
    if sys.argv[1] == "-R":
       pass