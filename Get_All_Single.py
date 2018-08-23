import requests
from bs4 import BeautifulSoup as bs

#first stages, find all Hardwell's single via wikipedia, and store them in a list named 'songs'

r=requests.get('https://en.wikipedia.org/wiki/Hardwell_discography')
soup=bs(r.content,'html.parser')

#get the Tag object, and search down to the specific tag we want

singles=soup.find_all("span",text='Singles')
single=singles[1]
table=single.parent
real_table=table.next_sibling.next_sibling
childs=real_table.contents
tbody=childs[3]

#now we find the minumal unit to repeat searching

trs=tbody.contents
length=len(trs)
i=4
songs=[]
while i<=length:
    ths=trs[i].contents
    if ths[1].contents[0]=="\"":
        songs.append(ths[1].contents[1].string)
    else:
        text=ths[1].contents[0].replace("\"","").rstrip()
        songs.append(text)
    i=i+2

#first stage complete, now we successfully store all singles in 'songs', next we are going to search them one by one on music.163.com and store these singles as a new personal tracklist

