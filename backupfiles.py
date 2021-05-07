import time
import os
import shutil

path=input('pls give path here:')
days=99
days=time.time()

print(days)

exist=os.path.exists(path)
print(exist)

if (exist==True):
    show=os.walk(path)
    print(show)

    joining=os.path.join(path)
    print(joining)

    ctime=os.stat(path)
    ctime1=ctime.st_ctime
    print(ctime1)

    if(time!=ctime):
        check=path.isfile()
        if(check==True):
           os.remove(path)
        else:
          os.open(path)
          os.remove(path.file)
    else:
        print('no file is greater than 99 days')
else:
    print('no such path or directory')



