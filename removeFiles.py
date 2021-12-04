import os;
import time;
import shutil;

days=time.time();
userTime=input("Enter the time");
path=input("Enter the path of folder in which files have to be deleted");
if os.path.exists(path):
    files=os.listdir(path);

    for f in files:
      file=open(f,"r");
      if(os.stat(f).st_ctime>days):
          try:
              os.remove(f);
          except:
              shutil.rmtree();
    
    

