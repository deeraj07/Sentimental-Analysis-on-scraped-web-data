import requests
from bs4 import BeautifulSoup
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
url = 'https://www.naukri.com/machine-learning-data-science-jobs-in-chennai?k=machine%20learning%20data%20science&l=chennai&functionAreaIdGid=5&ctcFilter=6to10&ctcFilter=10to15&ctcFilter=15to25&qbusinessSize=213&jobPostType=1'

response = requests.get(url,headers=header)
src = response.content
soup = BeautifulSoup(src, 'lxml')
print(soup)