import config

import os
import time
import sys
import platform
import psutil

hostsPath = config.hostsPath

hostsFile = open(hostsPath)
hostsFileRead = open(hostsPath).readlines()


def findTextLine(text):
    x = None
    for i, line in enumerate(open(hostsPath), 1):
        if text in line:
            x = i
    return(x)


waitTime = int(config.time)
if "#timetillend" in open(hostsPath).read():
    lineNum = findTextLine("#timetillend")
    fileToExtract = open(hostsPath).readlines()
    lineOftime = fileToExtract[lineNum - 1]
    newTime = int(lineOftime.split("#timetillend", 1)[1])
    print("Your time is still " + str(newTime) + " minute(s) until timer completes")
    waitTime = newTime


input("This program will restart all web browsers. Press enter to continue.")

def killByProcessName(name):
    PROCNAME = 'python.exe'
    for proc in psutil.process_iter():
        if proc.name == PROCNAME:
            p = psutil.Process(proc.pid)
            if not 'SYSTEM' in p.username:
                proc.kill()

    #print("Not found process: " + name)


def closeBrowsers():
    #print(os.name)
    browsersToClose = config.webBrowsers

    if platform.system() == "Darwin":
        print("macos")
        i=0
        while i < len(browsersToClose):
            if browsersToClose[i] in (p.name() for p in psutil.process_iter()):
                print(browsersToClose[i] + " is running")
                os.system("killall " + browsersToClose[i].replace(" ", '\\ ' ))
                print("Closed " + browsersToClose[i])
            i+=1

    if platform.system() == "Windows":
        i=0
        while i < len(browsersToClose):
            if browsersToClose[i] in (p.name() for p in psutil.process_iter()):
                print(browsersToClose[i] + " is running")
                os.system("TASKKILL /F /IM " + browsersToClose[i])
                print("Closed " + browsersToClose[i])
            i+=1

closeBrowsers()


toBlock = config.blockSites
print("These sites will be blocked.")
print(toBlock)

def compileList():
    i=0
    compiledDump = "#blockSites\n"
    while i < len(toBlock):
        compiledDump += "127.0.0.1 " + toBlock[i] + "\n"
        compiledDump += "127.0.0.1 www." + toBlock[i] + "\n"
        i+=1

    compiledDump += "#timetillend"+ str(waitTime) +"\n"
    compiledDump += "#endBlockSites\n"
    return(compiledDump)


def removeLines():
    if "#blockSites" in open(hostsPath).read() and "#endBlockSites" in open(hostsPath).read():
        oldLines = hostsFileRead
        newLines = ""

        startDelete = findTextLine("#blockSites") - 1
        endDelete = findTextLine("#endBlockSites")

        deleteThese = list(range(startDelete, endDelete))

        i = 0

        while i < len(oldLines):
            if i not in deleteThese:
                newLines += oldLines[i]
            i+=1

        raw = open(hostsPath, "r+")
        raw.seek(0)
        raw.truncate()
        raw.write(newLines)



def addBlockList():
    removeLines()
    x = open(hostsPath, "a")
    toWrite = compileList()


    x.write(toWrite)


def countdown(t):
    t*=60
    print("Time till finished:")
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('00:00\nBlock ended.')



addBlockList()
countdown(waitTime)
removeLines()
