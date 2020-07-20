# -*- coding: utf-8 -*-

import shutil
import os
import pdb
import random
import string
import codecs
import re
import matplotlib.image as mpimg # mpimg 用于读取图片
import base64

# from urllib.parse import quote, unquote


ocString = re.compile(r'@"[^"]+"')

ocFileFilterArr = ["MJExtension","Pods","DesFile","CDSSTeam","SpecialLiver","SDWebImage","MJRefresh","IQKeyboardManager","BRPickerView","BarrageRenderer","AFNetworking","YYText","SocketRocket","Masonry","XDPagesView"]

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

    sourceArr = getSoureData(files) #资源文件
    dataSouceReChange(sourceArr)

    # sourceArr = getSoureHeadHM(files)#字符串加密
    # print("sourceArr:" + str(sourceArr))
    # ergodicM(sourceArr)



def getSoureHeadHM(files):#过滤 遍历获取.h.m所有文件。  第一层元祖(.h .m)第二层:所有的元祖集合
    sourceArr = []
    for fileName in files:#遍历所有文件
        # print("address:" + fileName)
        if not ".h" in fileName:#不是.h的文件continue
            # print("fileName is not .h" + fileName)
            continue

        # if "Pods" in fileName: #is cocoapod
        #     # print("fileName is pods" + fileName)
        #     continue
        status = False
        for fileStr in ocFileFilterArr:
            if fileStr in fileName:
                status = True
                break

        if status:
            # print("不混淆:" + fileName)
            continue;

        # print("混淆:" + fileName)


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
     
        patternMArr = re.findall(ocString,sourceM)
        # print("strArr:" + str(patternMArr))
        for ocstr in patternMArr:
            ocstrReplace = ocstr  ###增加部分
            patternStr = ""
            print("ocstr:" + ocstrReplace)
            for i,ch in enumerate(ocstrReplace):###算法在里面
                print("ch:" + ch)
                if i == 0 or i == 1 or i == len(ocstrReplace) - 1:
                    print("wulue")
                    continue
                if i == 2 :
                    patternStr = patternStr  + charupper(ch) + "^*^" + randomStr() + "ppdya" + "^*^"
                elif i == len(ocstrReplace) - 2:
                    patternStr = patternStr  + "^*^" + randomStr() + "ppdya" + "^*^" + charupper(ch)
                else:
                    patternStr = patternStr  + charupper(ch)
                
                # if ch == '\\':
                #     patternStr = patternStr + randomStr() + '*'
                    # continue
                
                # if random.randint(1,10) > 6 :
                #    patternStr = patternStr + "trp:o*yq"
            # patternStr = patternStr + "trp:o*yq" #加后缀
            # print("patternStr:" + patternStr)
            # patternStr = ''.join(map(chr,map(lambda x:ord(x)^32,patternStr)))  #url编码
            # print("patternStr:" + patternStr)
            patternStr = "[VisagChangshintienWestinghouse PoekzVojvodinaTallahassee:@\"" + patternStr + "\"]"
            # print("patternStr:" + patternStr)
            sourceM = sourceM.replace(ocstr,patternStr)
            # print("sourceM" + sourceM)

        with codecs.open(filePathM, 'w', 'utf-8') as t:
            try:
                t.write(sourceM)
                t.close() 
            except :
                print("fileHHHname:" + filePathH)
                continue

      
        		# print("x:" + x)


        # print("pattern:" + str(patternMArr))
    

def randomStr():#随机1位的字符串
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return salt


def getSoureData(files):#资源文件
    sourceArr = []
    for fileName in files:#遍历所有文件
        # print("fileName:" + fileName)
        if "Assets"   in fileName:#
            print("Assets.xcassets no work!!!")
            continue
        if ".png"   in fileName:#
            sourceArr.append(fileName)
        if ".jpg" in fileName:
            sourceArr.append(fileName)
            continue
        if ".jpeg" in fileName:
            sourceArr.append(fileName)
            continue
       
    print("sourceArr:" + str(sourceArr))
    return sourceArr


def dataSouceReChange(files):#资源文件存在
    for fileName in files:
        sourceM = ""
        with open(fileName, 'rb') as f:
            try:
                sourceM = f.read() 
                sourceM = base64.b64encode(sourceM)
                f.close()
                print("json1111:" + sourceM)
            except :
                print("fileMMMname:" + fileName)
                continue
        
        patternStr = ""
        for i,ch in enumerate(sourceM):###算法在里面
            if i == 0 :
                patternStr = patternStr  + charupper(ch) + "^*^" + randomStr() + "ppdya" + "^*^"
            elif i == len(sourceM) - 1:
                patternStr = patternStr  + "^*^" + randomStr() + "ppdya" + "^*^" + charupper(ch)
            else:
                patternStr = patternStr  + charupper(ch)

        print("jia mi qian :" + sourceM)
        print("jia mi hou :" + patternStr)
        # patternStr = patternStr + randomStr() #加后缀
        # patternStr = quote(patternStr) #url编码
        # print("patternStr:" + patternStr)
        with open(fileName, 'wb') as t:
            try:
                t.write(patternStr)
                t.close()
                print("finishSucc" )
            except :
                print("fileHHHname:" + fileName)
                continue


    


def randomStr():#随机1位的字符串
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return salt


def charupper(ch):
    if "a"<= ch <= "z":
        return  ch.upper()
    elif"A" <= ch <= "Z":
        return ch.lower()
    else:
        return ch


if __name__ == "__main__":
	main()

