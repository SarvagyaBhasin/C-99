import time
import calendar
import os
import shutil

path='D:/AISN/CLASS 7'
days=645
seconds=time.time()-(days*24*60*60)
if os.path.exists(path):
    listoffiles=os.listdir(path)
    os.remove(path)
    
else :
    print('file not found')