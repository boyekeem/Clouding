import urllib

vid = "http://yify.tv/watch-daddys-home-online-free-yify/"

def download(url):
    response = urllib.urlopen(url)
    kay = response.read()
    kayformat= str(kay)

    fx= open("kaylocation.html", "w")
    fx.write(kayformat)

    fx.close()

    fx1= open("kaylocation.html", "r")
    new = fx1.read()
    print(new)
    fx1.close()
download(vid)





