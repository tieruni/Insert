# -*- coding: utf-8 -*-

import shutil
import os
import pdb
import random
import string
import codecs
import re

pattern = re.compile(r'(?:\+|-)\s*\([^()]+\).*')#need ?: oc func
ocfunc = re.compile(r'.*;/{0,}.*\n')
ocproperty = re.compile(r'^(@property).*')#有问题
numMax = 25

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
            if "DS_Store" not in filePath:
                filelist.append(filePath)
                           
    return filelist


def main():
    print("this main run")
    dir = os.getcwd() + "/Demo"
    files = getResourcePath(dir)
    sourceArr = getSoureHeadHM(files)
    ergodicM(sourceArr)
    print("=====================sucesssul!!!!=========================")


def getSoureHeadHM(files):#过滤 遍历获取.h.m所有文件。  第一层元祖(.h .m)第二层:所有的元祖集合
    sourceArr = []
    for fileName in files:#遍历所有文件
        if not ".h" in fileName:#不是.h的文件continue
            # print("fileName is not .h" + fileName)
            continue

        if "Pods" in fileName: #is cocoapod
            # print("fileName is pods" + fileName)
            continue

        fileNameText = os.path.splitext(fileName)
        # print("fileNameText:" + fileNameText[0]);
        fileNameM = fileNameText[0] + ".m"
        if fileNameM in files:#.h.m同一个文件目录下情况,正常情况要遍历整个项目找到.m
            tupe = (fileName,fileNameM)
            sourceArr.append(tupe)
            continue
        else:
            print(".h .m不是同一文件夹暂不处理:" + fileNameM);
    # print("sourceArr:" + str(sourceArr))
    return sourceArr

def ergodicM(sourceArr):#遍历.M的所有方法替换成
    for tupes in sourceArr:
        filePathH = tupes[0]
        filePathM = tupes[-1]
        sourceM = ""
        with codecs.open(filePathM, 'r', 'utf-8') as f:
            try:
                sourceM = f.read() 
                f.close()
            except :
                print("fileMMMname:" + filePathM)
                continue
        implementationArr = sourceM.split("@implementation")
        if len(implementationArr) > 2:
            print(".m有两个以上implementation暂不处理:" + filePathM + '\r\n' + str(re.findall(pattern,sourceM)));#.m有两个以上implementation暂不处理
            continue;
        patternMArr = re.findall(pattern,sourceM)
        # print("pattern:" + str(patternMArr))
        sourceH = ""
        with codecs.open(filePathH, 'r', 'utf-8') as f:
            try:
                sourceH = f.read()
                f.close()  
            except :
                print("fileHHHname:" + filePathH)
                continue

        interfaceBack = sourceH.split("@interface")[-1]#@interface后

        interfacePre = sourceH.split("@interface")[0]#@interface前
        interfaceCon = interfaceBack.split("@end")[0]#interface内容
        endBack = interfaceBack.split("@end")[-1]#end后

        patternHArr = re.findall(pattern,interfaceCon)#.h方法名
        for ocfuncH in patternHArr:
            interfaceCon = interfaceCon.replace(ocfuncH,'')#删除.h interface 方法名


        for ocfuncM in patternMArr:#遍历.m 文件oc方法;
            # print("ocfuncMMMMM:" + ocfuncM);
            ocfuncM = ocfuncM.split("//")[0]#分割注释
            ocfuncM = ocfuncM.split("{")[0]#分割{括号
            interfaceCon = interfaceCon + '\r\n' + ocfuncM + ";//ttest my"#遍历.m所有方法名加在interfaceCon内容中

        strH = interfacePre + '\r\n' + "@interface" + interfaceCon + '\r\n' + "@end" + '\r\n' + endBack #还原操作
        # print("strH:" + strH)
        with codecs.open(filePathH, 'w', 'utf-8') as t:
            try:
                t.write(strH)
                t.close() 
            except :
                print("fileHHHname:" + filePathH)
                continue
           



if __name__ == "__main__":
	main()