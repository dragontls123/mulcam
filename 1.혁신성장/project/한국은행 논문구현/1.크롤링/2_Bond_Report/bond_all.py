# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 11:25:48 2020

@author: molo6
"""

import pdftotext
import re 
import pandas as pd
import requests
from bs4 import BeautifulSoup

dl_url=[]
date_tag = []
for i in range(24,128):
    url=f"https://finance.naver.com/research/debenture_list.nhn?&page={i}"
    resp=requests.get(url)
    soup=BeautifulSoup(resp.text)
    li=soup.select('div.box_type_m tr td.file ')
    # date_li = soup.select('div.box_type_m tr td.date ')
    date_li = soup.findAll("td", {"style" : "padding-left:5px"})
    
    for l in li:
        k=l.find('a')
        dl_url.append({
            'link':k.get('href'),
        })
    for k in date_li:
        date_tag.append(k.text)
for i in range(len(dl_url)): 
  mpb = requests.get(dl_url[i]['link']) #request.get을 통해 url을 저장
  with open('C:\\Users\\molo6\\Desktop\\NAVER\\bond\\{}.pdf'.format(i), 'wb') as f: #url파일들을 지정된 폴더로 다운받는다.
    f.write(mpb.content)

base_cd = r"C:\Users\molo6\Desktop\NAVER\bond\{}.pdf"

for i in range(0, 3098): # 2448에서 error가 남 한번 끊고 range 바꿔주고 돌리기 (텍스트 폴더에도 2448파일 만들어야함)
    print(i)
    with open(base_cd.format(i), "rb") as f:
        pdf = pdftotext.PDF(f)
    try:    
        with open(r'C:\Users\molo6\Desktop\NAVER\bond_txt\{}.txt'.format(i), 'w', encoding='utf-8') as f:
            f.write("\n\n".join(pdf))
    except:
        print("error {}".format(i))
        pass

def tidy_sentences(section):
    sentence_enders = re.compile(r'((?<=[함음됨임봄짐움])(\s*\n|\.|;)|(?<=다)\.)\s*')
    splits = list((m.start(), m.end()) for m in re.finditer(sentence_enders, section))
    starts = [0] + [i[1] for i in splits]
    ends = [i[0] for i in splits]
    sentences = [section[start:end] for start, end in zip(starts[:-1], ends)]
    for i, s in enumerate(sentences):
        sentences[i] = (s.replace('\n', ' ').replace(' ', ' ')) + '.'
    text = '\n'.join(sentences) if len(sentences) > 0 else ''
    return text


k = [] # txt폴더에서 저장된 data 불러오기
for i in range(0,3098):
    filename = r'C:\Users\molo6\Desktop\NAVER\bond_txt\{}.txt'.format(i)
    k.append(filename)
len(k)
print(k[0])

text_li = []
for i in range(len(k)):
    with open(k[i],'r',encoding='UTF-8') as file_object:
        contents = file_object.read()
        text_li.append(contents)

new_text_li = []
for i in text_li:
    new_text_li.append(tidy_sentences(i).strip())

df_text = pd.DataFrame(new_text_li, columns=['text'])
df_date = pd.DataFrame(date_tag, columns=['date'])
df_date = df_date.reset_index()
df_date = df_date['date']
df_mpb = pd.concat([df_date, df_text], axis=1)

import pickle

with open('bond_data.pickle','wb') as f: #저장
    pickle.dump(df_mpb , f)
    
with open('bond_data.pickle', 'rb') as f: #불러오기
    data = pickle.load(f)


