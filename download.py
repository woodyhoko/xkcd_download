import wget
import requests
from bs4 import BeautifulSoup

# 191 selector => #comic > a > img
# 404 404 error
# 1037 no comic
# 1331 special case
# 2067 special case
try os.mkdir("data")
with open("details.txt", "a") as f:
	for i in range(2067,2218):
		url = "http://xkcd.com/"+str(i)
		resp = requests.get(url)
		if resp.status_code == 404:
			continue
		soup = BeautifulSoup(resp.text, "html.parser")
		selector = "#middleContainer"
		img = soup.select(selector)[0]
		try :
			link = img.contents[5].img['srcset'][:-2]
			print '\n', i, '\t', link
			wget.download("http:"+link,out="./data/"+str(i)+"_"+link.split('/')[-1].replace("_2x",""))
		except :
			if len(img.contents[12])>2:
				link = img.contents[12].split(':')[-1]
			else :
				link = img.contents[5].img['src']
			print '\n', i, '\t', link
			wget.download("http:"+link,out="./data/"+str(i)+"_"+link.split('/')[-1].replace("_2x",""))
		f.write("number : "+str(i)+"\n")
		f.write("title : "+link.split('/')[-1].replace("_2x",""))		
		f.write("link : http:"+link)
		try :
			f.write("description : \n\t"+img.find(id='transcript').contents[0].encode("utf-8").replace("\n","\n\t") + "\n")
		except :
			try :
				f.write("subtitle : "+img.contents[5].img['title'].encode("utf-8")+"\n")
			except : 
				f.write("\n")
		f.write("="*30+"\n")
