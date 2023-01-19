import requests
from bs4 import BeautifulSoup
import pprint

for i in range(0,5):
    res = requests.get('https://news.ycombinator.com/news?p='+str(i+1))
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.titleline')
    subtext = soup.select('.subtext')
    def sorted_stories_v(hnlist):
        return sorted(hnlist, key=lambda k:k['votes'], reverse=True)
    def create_custom_hn(links, subtext):
        hn=[]
        for idx, item in enumerate(links):
            title = links[idx].getText()
            href = links[idx].get('href', None)
            votes = subtext[idx].select('.score')
            if len(votes):
                points = int(votes[0].getText().replace(' points', ''))
                if points > 99:
                    hn.append({'title': title, 'link': href, 'votes': points})
        return sorted_stories_v(hn)
    pprint.pprint(create_custom_hn(links, subtext))

'''res = requests.get('https://news.ycombinator.com/news')

soup = BeautifulSoup(res.text, 'html.parser')

#find all the data in non string format
#print(soup)

#find all the data of body format
#print(soup.body.contents)

#find all the given tag in soup object
#print(soup.find_all('a')) #a is for links in the site 
#print(soup.find_all('div')) #div tags is  in the site
# 
# for finding the title tag in our soup object we use
# print(soup.title)
# if use soup.a it will give the first link in the site
# same for soup.find_all('a') it will give all the links in the site
# if I write soup.find(id='score_25000000') it will show data  of the link

#soup.select('a') #it will give all the links in the site
#soup.select('.score') #it will give all the score in the site
#soup.select('#score_25000000') #here in #score # stands for ID .#it will give the score of the link


# now we will find score more than 100 in the site
#print(soup.select('.storylink')) #here it will show headline of the stories in the link
links = soup.select('.titleline')
subtext = soup.select('.subtext')
#print(votes[0])


def sorted_stories_v(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn=[]
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        votes = subtext[idx].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points', ''))
            if points > 99:
#            print(points)
                hn.append({'title': title, 'link': href, 'votes': points})
    return sorted_stories_v(hn)

pprint.pprint(create_custom_hn(links, subtext))'''