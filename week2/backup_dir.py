#!/usr/bin/env python3

import os
import subprocess
from multiprocessing import Pool

root_dir = "/root/python/Google-Troubleshooting-Debugging/week2/data/prod"
backup_root = "/root/python/Google-Troubleshooting-Debugging/week2/data/prod_backup"

# create backup directory if it doesn't exist

if not os.path.isfile(backup_root):  
    os.mkdir(backup_root) 


#for subdir, dirs, files in os.walk(root_dir):
    #print(src_dir)
    #print(dirs)
    #print(dirs)
    #for file in files:
    #print(subdir)
    #print(dirs)
    #for source_dir in dirs:
        #print(source_dir)
    #rsync -zavh [Source-Files-Dir] [Destination]


# Copy or sync files locally: 
# rsync -zvh [Source-Files-Dir] [Destination]
# 
# Copy or sync directory locally: 
# rsync -zavh [Source-Files-Dir] [Destination]

# Copy files and directories recursively locally: 
# rsync -zrvh [Source-Files-Dir] [Destination]

    

for root, dirs, files in os.walk("/root/python/Google-Troubleshooting-Debugging/week2/data/prod", topdown=False):
   for name in dirs:
      #print(os.path.join(root, name))
      #print(os.path.join(backup_root, name))
      src = os.path.join(root, name)
      dest = os.path.join(backup_root, name)
      print(src)
      print(dest)
      subprocess.call(["rsync", "-zrvh", src, dest])

   for name in files:
      print(os.path.join(root, name))
      print(os.path.join(backup_root, name))
      







