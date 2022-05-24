import sys 
import os
import platform 
from colorama import Fore

def main(platfroms:str): 
   if platform == platfroms: 
      try: 
         print("wait install...")
         os.system("bash AhutoInstall.sh") 
      except: 
         pass 
   else:
      pass 
   
   try: 

      args = sys.argv[1:100]
      sort_args =  " ".join(args)

      if sort_args == "-h" or sort_args == "--help": 
         print(f""" 

welocome to tools,rename! command down;
rename [New Name] [old file]""")
      else: 
         with open(args[1],mode='r') as readname: 
            read_file = readname.read()

         with open(args[0] , mode='w') as w: 
            os.remove(args[1])
            w.write(read_file) 
   except: 
      pass  
main("linux".lower()) 