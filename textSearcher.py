# -*- coding: utf-8 -*-
'''
Created on Sat Dec  5 15:14:35 2020

@author: tanaka
'''

import re
import glob
import codecs
import datetime

print("文章検索を開始します。")
print("結果ファイルが出力されない際は何らかの問題が発生しています。")

#  設定ファイルの読み込み
conLd = codecs.open('config.txt','r', 'utf-8')
conLdlines = conLd.readlines()
conLd.close()

for i, conLine in enumerate(conLdlines):
    if conLine.find('path') >= 0:
        path = re.findall(':.*',  conLine[:-1])[0].strip(':').strip()
        
    if conLine.find('recursive') >= 0:
        recurisive = re.findall(':.*',  conLine[:-1])[0].strip(':').strip()
        if recurisive == '1':
            rec = '\\**\\'
            
    if conLine.find('fileName') >= 0:
        fileName = re.findall(':.*',  conLine[:-1])[0].strip(':').strip()
        
    if conLine.find('No-fileMatch') >= 0:
        noMatch = re.findall(':.*',  conLine[:-1])[0].strip(':').strip()

#  検索ワードの読み込み
sWords = []
sLd = codecs.open('search_list.txt','r', 'utf-8')
sLdlines = sLd.readlines()
sLd.close()

for i, conLine in enumerate(sLdlines):
    sWords.append(conLine.strip())

file = 'result/result_' + datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '.txt'
fileobj = codecs.open(file, 'w', encoding = 'utf_8')    
    
#  検索のメイン処理
filePath = path +  rec + fileName
files = glob.glob(filePath, recursive=True)

print('検索対象ファイル条件　：',filePath, file=fileobj)

if noMatch =='1' :
    print('※検索ワードを含むファイルは検索対象外。\r\n', file=fileobj)

match = 0
for word in sWords:
    print('\r\n検索文字列： ', word, file=fileobj)
    for sFile in files:
        if noMatch =='1' and sFile.find(word) >=0 :
            continue
        ld = codecs.open(sFile,'r','utf-8')
        ldlines = ld.readlines()
        ld.close()
        for i, line in enumerate(ldlines): 
            if line.find(word) >= 0:
               print(sFile, '(', i+1, ')', line.strip(), file=fileobj)
               match +=1 

#  完了表示
print('\r\n',match,'件　一致しました。', file=fileobj)
fileobj.close()

