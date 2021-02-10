# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 19:33:32 2020

@author: molo6
"""

import requests
from bs4 import BeautifulSoup
from tika import parser #https://github.com/chrismattmann/tika-python 이용하였다.
from os import listdir #listdir-directory에 있는 모든 파일을 가져온다
from os.path import isfile, join # isfile 지정된 경로의 파일명만 얻기
import os


total_list = [] # 설정된 page의 tag list

for i in range(6,33): 
    url = 'https://www.bok.or.kr/portal/bbs/B0000245/list.do?menuNo=200761'
    query = {
        'pageIndex' : i # page number
      }
    resp = requests.get(url, query)
    soup = BeautifulSoup(resp.content, 'lxml')
    tag = soup.select('div.fileGoupBox a') #tag
    
    total_list.extend(tag) 
    print(total_list)
    
    pdf_list = [] #.pdf를 가지는 리스트를 가져온다.
    for idx,t in enumerate(total_list):
      if total_list[idx].attrs['title'][-3:] == 'pdf': #.attrs['title']을 활용해서 title의 .pdf파일이 들어간 리스트를 뽑아낸다.
        pdf_list.append(total_list[idx]) 
    print(pdf_list)

pdf_href_list = [] 
for i in pdf_list:
    pdf_href_list.append(i.attrs['href']) # .attrs['href']를 사용해서 url주소만 가져온다.
print(pdf_href_list)

site = 'https://www.bok.or.kr'

url = []
for i in range(len(pdf_href_list)): 
    url.append(site + pdf_href_list[i]) # site + url을 통해서 pdf파일이 다운 가능하게 한다.
print(url)

for i in range(len(url)): 
  mpb = requests.get(url[i]) #request.get을 통해 url을 저장
  with open('C:\\Users\\molo6\\Desktop\\NAVER\\mpb\\{}.pdf'.format(i), 'wb') as f: #url파일들을 지정된 폴더로 다운받는다.
    f.write(mpb.content)

def pdf2txt (source_folder, output_folder) :#pdf파일을 text파일로 변경해 주는 함수
    # 지정 폴더 내 파일 목록 조회 (파일만)
    # in ~~~ 는 폴더 내 다른 서브퓰더가 있는 경우를 처리하기 위함.
    pdf_files = [f for f in listdir(source_folder) if isfile(join(source_folder, f))] 
    
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for pdf in pdf_files :
        pdf_filepath = source_folder + pdf
        
        try:    
            pdf_filepath = source_folder + pdf
            # pdf 파일을 text로 변환
            print(pdf_filepath)
            parsedPDF = parser.from_file(pdf_filepath)["content"]

        except Exception as e:
            parsedPDF = ' '
            print(f'{pdf} 에러 : {e}')
        
        ouput_filepath = (output_folder + pdf).replace('.pdf', '.txt')
        with open(ouput_filepath, 'w', encoding='utf-8') as f :
            print(ouput_filepath)
            f.write(parsedPDF)
            f.close()

base = os.getcwd() # 현재 작업 폴더 얻기
source = os.path.join(base, 'C:\\Users\\molo6\\Desktop\\NAVER\\mpb\\') #Pdf파일 저장되어 있는 폴더
output = os.path.join(base, 'C:\\Users\\molo6\\Desktop\\NAVER\\mpb_txt\\')#Txt파일로 폴더 지정
pdf2txt(source, output) #pdf->text 파일로 변경


    

    
    