# -*- coding:utf-8 -*-
# 区分在少了一个int转化
import json
import os

def calcuTotalScore():
    with open('person.json',encoding='utf-8') as f:
        jsoncontent = json.load(f)
        print(jsoncontent['userName'],'的总分是：',(jsoncontent['chineseScore']+jsoncontent['englishScore']))
        f.close()
    os.remove('person.json')
    with open('person.txt','r',encoding='utf-8') as f:
        lines = f.readlines()
        print(lines[0].strip(),'的总分是：',(lines[1].strip()+lines[2].strip()))
        f.close()
    os.remove('person.txt')


def writePersonInfo(userName, chineseScore, englishScore):
    personInfo = {'userName':userName,'chineseScore':int(chineseScore),'englishScore':int(englishScore)}
    with open('person.json','w+',encoding='utf-8') as f:
        json.dump(personInfo,f)
    with open('person.txt','w+',encoding='utf-8') as f:
        f.writelines(userName+'\n'+chineseScore+'\n'+englishScore+'\n')
    calcuTotalScore()

def main():
    userName = input('Enter your name: ')
    chineseScore = input('Enter your chinese score: ')
    englishScore = input('Enter your english score: ')
    writePersonInfo(userName,chineseScore,englishScore)

if __name__ == '__main__':
    main()
