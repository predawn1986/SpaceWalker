import re
import requests

base_url = 'https://maoyan.com/board/4?offset='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/68.0.3440.106 Safari/537.36'
}
pattern = re.compile(r'<dd>.*?</dd>', re.S)
pattern_title = re.compile(r'<p class="name">.*?title="(.*?)".*?</p>', re.S)
pattern_actor = re.compile(r'<p.*?class="star"(.*?)</p>', re.S)
pattern_date = re.compile(r'<p.*?class="releasetime">.*?：(.*?)</p>', re.S)
pattern_score_integer = re.compile(r'<i class="integer">(.*?)</i>', re.S)
pattern_score_fraction = re.compile(r'<i class="fraction">(.*?)</i>', re.S)
pattern_image = re.compile(r'<img data-src="(.*?)".*?>', re.S)


def get_info():
    offset = 0
    for i in range(10):
        offset = offset * 10
        content = get_page(offset)
        if content != 'Error':
            results = re.findall(pattern, content)
            if results:
                for result in results:
                    title = re.findall(pattern_title, result)
                    actor = re.findall(pattern_actor, result)
                    date = re.findall(pattern_date, result)
                    score_integer = re.findall(pattern_score_integer, result)
                    score_fraction = re.findall(pattern_score_fraction, result)
                    image = re.findall(pattern_image, result)
                    with open('maoyan_top_100.txt', 'a+', encoding='utf-8') as f:
                        f.write(title[0] + ' ' + actor[0].replace('\n', '').replace('>', '').strip() + ' ' + date[0]
                                + ' ' + str(score_integer[0] + score_fraction[0]) + ' ' + image[0] + '\n')
        else:
            with open('maoyan_top_100.txt', 'a+') as f:
                f.write('offset ' + str(offset) + ' can not get film.')


def get_page(offset):
    url = base_url + str(offset)
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.text
    else:
        return "Error"


if __name__ == '__main__':
    get_info()

