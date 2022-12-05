import os
import  signal
import psutil
from sys import *

def process_checker(process_name):
    list=[]
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['name', 'pid', 'username'])
            if process_name.lower() in pinfo['name'].lower():
                list.append(pinfo)


        except(psutil.NoSuchProcess, psutil.ZombieProcess, psutil.AccessDenied):
            pass
    return list

def kill_process(process_name):
    process_info=process_checker(process_name)
    pid=int(process_info[0]["pid"])
    if len(process_info)>=1:
        os.kill(pid, signal.SIGILL)
    else:
       print("no such process is running in your system")

def main():
    if argv[1]=="-h" or argv[1]=="-H":
        print("this script accept process name as input and terminate that process if its running in system ")
        exit()
    if len(argv)<1:
        print("insufficient no of arguments")
        exit()

    kill_process(argv[1])


if __name__=="__main__":
    main()