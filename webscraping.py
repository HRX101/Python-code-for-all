import requests#import requests package
from bs4 import BeautifulSoup #import BeautifulSoup package from bs4
res=requests.get("https://www.atree.org/people/adjunct-fellows") #get the path of html
soup=BeautifulSoup(res.content,"html.parser") #get the html content
#print(soup.prettify) #make it in aling
data=soup.find("div",attrs={"class":"container"})
data2=soup.find("div",attrs={"class":"entity"})##find the div value from html
data1="{} {}".format(data,data2)
print(data1)