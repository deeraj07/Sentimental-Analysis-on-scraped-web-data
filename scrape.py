# importing the modules
import requests
import sys
from bs4 import BeautifulSoup
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
import pandas as pd
col_list = ["URL_ID","URL"]
df = pd.read_csv("intern.csv",usecols=col_list)
t = df["URL"]
print(len(t))
for i in range(170):
    sys.stdout= open("D:\OneDrive\Desktop\work\inter"+str(i)+".txt", "w+")
    y= t.iloc[i]
    url = y
    response = requests.get(url,headers=header)
    src = response.content.decode('utf-8')
    soup = BeautifulSoup(src, 'lxml')
    job_elements = soup.find_all("p")
    head = soup.find_all("h1") #title
    for j in head:
        print(j.text)
    for link in job_elements:
        print(link.text)
    sys.stdout.close()
