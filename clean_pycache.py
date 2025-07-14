import os
import sys
import shutil

target = sys.argv[1]


def clean_cache(target):
    files = os.listdir(target)
    for file in files:
        full_path = os.path.join(target, file)
        if file == "__pycache__":
            shutil.rmtree(full_path)
        elif os.path.isdir(full_path):
            clean_cache(full_path)

        

clean_cache(target)