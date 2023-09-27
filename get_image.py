from bs4 import BeautifulSoup
import random
import requests
import re
import sys


post_list = []
url_list = []
start_page=3950
end_page=4001
fetched_page = []

def getUrl():
    # https://www.ptt.cc/bbs/Beauty/index2600.html
    while True:
        page_num = random.randint(start_page,end_page);
        if (not(page_num in fetched_page)):
            fetched_page.append(page_num)
            break
        if ((end_page - start_page + 1) == len(fetched_page)):
            return

    url = "https://www.ptt.cc/bbs/Beauty/index"+str(page_num)+'.html'
    headers = {
    'Cookie': 'over18=1'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text,'html.parser')
    f = open("url_list.txt", "a")

    
    for a_tag in soup.select('a'):
        # format
        # <a href="/bbs/Beauty/M.1471237548.A.EAB.html">[正妹] 體育主播</a>
        match = re.search(r'<a href="/bbs/Beauty/M(.*?)">\[正妹\]',str(a_tag))
        if match:
            article_url = 'https://www.ptt.cc/bbs/Beauty/M'+match.group(1)
            url_list.append(article_url)
    
    for url in url_list:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text,'html.parser')
        for a_tag in soup.select('a'):
            # format
            # <a href="http://i.imgur.com/e5UD40k.jpg" rel="nofollow" target="_blank">http://i.imgur.com/e5UD40k.jpg</a>
            match = re.search(r'<a href="http(s)?://(i\.)?imgur\.com/(.*?)\.jpg"',str(a_tag))
            if match:
                image_url = 'https://imgur.com/'+match.group(3)+'.jpg'
                f.write(image_url+'\n')

try:
    if len(sys.argv) == 1 :
        getUrl()
    else :
        times = int(sys.argv[1])
        for i in range(times) :
            print('x')
except Exception as e:
    print(e)
