import os
import sys
import shutil

target = sys.argv[1]


folders = os.listdir(target)

for folder in folders:
    full_path = os.path.join(target, folder)
    folders_ = []
    if os.path.isdir(full_path):
        folders_ = os.listdir(full_path)
 
    for folder_ in folders_:
        if folder_ == "__pycache__":

            pcache_path = os.path.join(full_path, folder_)

            shutil.rmtree(pcache_path)

