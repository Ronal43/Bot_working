import sys
import subprocess
import string
import re

def runBash(commandLine):
    process = subprocess.Popen(commandLine, shell=True, stdout=subprocess.PIPE)
    out = process.stdout.read().strip()
    return out


def cd():
    return runbash("cd rabotayet/Bot_working")
    return runbash("git add . ")
    return runbash("git commit -m 'New commit'")
    return runbash("git push origin master")

def cd():

if __name__=="__main__":
    sys.exit(main())
