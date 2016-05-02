import requests
import BeautifulSoup
import datetime
import operator

url1 = 'http://www.nlng.com/nignlng/home.aspx'


def worded(url):
    wordlist=[]
    i=4
    raw= requests.get(url).text
    soups=BeautifulSoup.BeautifulSoup(raw)
    output=open('dicco'+'.txt','w')
    for a in soups.findAll('span',{'class': "menu-item-text"}):
        new= a.string
        news=new.lower().split()



        for each_word in news:
            wordlist.append(each_word)
            output.write(each_word +'\n')


    print wordlist


worded(url1)

