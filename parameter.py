#encoding:utf-8


import shutil
import os
import pdb
import random
import string
import codecs
import re

# pattern = re.compile(r'(?:^\+|-)\s*\([^()]+\).*', re.M)#need ?: oc func
# ocfunc_rule = re.compile(r'*/s*.*\/s*;', re.M)
ocfunc_rule = re.compile(r'.*;', re.M)
numMax = 20

def getResourcePath(targetpath):
    # print("=====================Find all Files=========================")
    filelist = []
    # pdb.set_trace()
    os.listdir(targetpath)
    for fileName in os.listdir(targetpath):
        filePath = targetpath + '/' + fileName
        # print(filePath)
        if os.path.isdir(filePath):
            # renameDir(filePath)
            files = getResourcePath(filePath)
            filelist.extend(files)
        else:
            
            if "DS_Store" in filePath:
                print("============" + filePath)
                continue
            elif "Pods" in filePath or "xcworkspace" in filePath or "xcodeproj" in filePath or "Podfile" in filePath:
                continue
            else:
                filelist.append(filePath)            
    return filelist


def main():
    print("this main run")
    dir = os.getcwd() + "/Demo"
    files = getResourcePath(dir)
    for filename in files:
        source = ""
        with codecs.open(filename, 'r', 'utf-8') as f:
            try:
                source = f.read()
                # print(t)  
            except :
                print("filename:" + filename)
                continue
                                   
            if not "@implementation" in source: #.h
                print("no implementation finder")
                continue
            sourceList = source.split("@implementation",1)
            source = sourceList[-1]
            # print("source:"+source)
            ocfuncList = ocfunc_rule.findall(source)
            source = replaceWithOcfuncList(ocfuncList,source)
            source = sourceList[0] + "@implementation " + source
            # print (source)
            f.close()
        with codecs.open(filename, 'w', 'utf-8') as f:
            f.write(source)
            f.close()
            # re.sub("NSString *","NSSString *")
    print("=====================sucesssul!!!!=========================")

def replaceWithOcfuncList(ocfuncList,source):
    ocfuncList = getNonRepeatList(ocfuncList)
    source_all = source
    for str in ocfuncList:
        # pattern = re.compile(str)
        # re.sub(pattern,'str + '\r\n' + ////this my insert////',source)
        if "return" in str:
            print("this is return continue:")
            continue
        elif "@property" in str:
            print("this is return continue:")
            continue
        # elif str.startswith('//'):
        #     print("this is // continue:")
        #     continue
        elif "break" in str:
            print("this is break continue:")
            continue
        elif "continue" in str:
            print("this is continue continue:")
            continue
        elif "//" in str:
            strArr = str.split(";")
            str1 = strArr[0]
            if "//" in str1:
                print("this is // continue")
                continue
                
        num = random.randint(0,99)
        if numMax >= num:
            source_all = source_all.replace(str,str + '     \n\t//////insert//' )
        
    print(source_all)
    return source_all

def getNonRepeatList(data):
    return list(set(data))

if __name__ == "__main__":
	main()