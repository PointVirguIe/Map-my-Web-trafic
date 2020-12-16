import json, getopt, sys
from update_check import isUpToDate

# Debug
err = "[  ERROR  ]  "
alert = "[  ALERT  ]  "

# Check update
if isUpToDate(__file__, "https://github.com/MajestionMC/Build-Minecraft-Server/main.py") == False:
   print(alert + "There is an newer version on Github. Please download the new version.")

def main(argv):
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print(err + "Please, try: main.py -h") 
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print("\nExample:\tmain.py  -a  spigot  1.16.2  \{ServerName}\n\
             ")
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg

try:
    with open('bin/data.json') as fp:
        data = json.load(fp)
except:
    with open('person.txt', 'w') as json_file:
        json.dump(data_to_dump, json_file)