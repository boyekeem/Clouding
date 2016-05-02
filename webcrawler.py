import requests
import BeautifulSoup


url1 = "http://www.surrey.ac.uk/postgraduate"


name='courselist'
def crawler(url):
    info = requests.get(url)
    PlainTxt = info.text
    soup = BeautifulSoup.BeautifulSoup(PlainTxt)
    n1 =open(name, 'w')

    for n in soup.findAll('h4', {'class': 'h6'}):
  #      href1 = link.get('href')
 #       print(href1)
#        title = link.string
        Pg = n.string
        pgtxt=str(Pg)+ '\n'
        n1.write(pgtxt)
    n1.close()
#    n2=open('name', 'r')
 #   n2.read()
  #  n2.close()










crawler(url1)
a=1
while   a<4:
    a+= 1
    try:
        age = int(2016 - input("enter year pf birth\n"))
        print("you are ",age, " years old")
        break
    except NameError:
        print("use numbers only")
    finally:
        b=3-a
        print(b," tries left")








