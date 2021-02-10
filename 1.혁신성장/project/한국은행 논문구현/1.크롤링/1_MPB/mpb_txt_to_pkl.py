# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 09:51:22 2020

@author: molo6
"""

import re
import pandas as pd
import requests
from bs4 import BeautifulSoup

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
for i in range(0,264):
    filename = r'C:\Users\molo6\Desktop\NAVER\mpb\mpb_txt\{}.txt'.format(i)
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

date_list = [] # tag리스트를 저장
for i in range(5,34):
    url = 'https://www.bok.or.kr/portal/bbs/B0000245/list.do?menuNo=200761'
    query = {
        'pageIndex' : i
      }
    resp = requests.get(url, query).text
    soup = BeautifulSoup(resp, 'html.parser') #resp.conetent 로 뽑으면 Tag형태로 나오기 때문에 content를 쓰지 않고 리스트 형태로 전환 (날짜만 뽑기 위해)
    tag = soup.select('div span.titlesub')
    date_list.extend(tag)
    
date_1 = [] # join함수를 써서 list->str로 변환 
for t in date_list:
  date_1.append('\n'.join(t))
len(date_1)

date_2 = date_1[7:-8] # 기존의 날짜로 정리(필요없는 날짜 슬라이스를 통해 정리)

date_3 = [] #0000.00.00 으로 가져오기 위해 split date_2를 수정
for d in range(len(date_2)): 
  date_3.append(date_2[d].split('('))

date_4 = [] #0000.00.00 으로 가져오기 위해 slice
for t in date_3:
  date_4.append(t[2][:-1])

date_5 = []
for d in date_4:
  if d[-1] == '.':
    date_5.append(d[:-1])
  else:
    date_5.append(d)

len(date_5)
df_date = pd.DataFrame(date_5, columns=['date'])
df_date = df_date.drop([0,1,2,274,273,272,271,270,269,268,267])
df_date = df_date.reset_index()
df_date = df_date['date']
df_mpb = pd.concat([df_date, df_text], axis=1)

import pickle

with open('MIB_data.pickle','wb') as f: #저장
    pickle.dump(df_mpb , f)
    
with open('MIB_data.pickle', 'rb') as f: #불러오기
    data = pickle.load(f)
