## ex2_movie actor挑戰題：
## 請取得 The Darkest Minds (2018) 這部電影的所有演員

from requests_html import HTMLSession
session = HTMLSession()
response = session.get('https://www.imdb.com/movies-coming-soon/2018-08/?ref_=cs_dt_nx')
#print(response) # status_code, example: 200, 404...
elements = response.html.find('[itemtype="http://schema.org/Movie"]')[1].find('[itemprop="actors"] span a')
for element in elements:
    print(element.text)
