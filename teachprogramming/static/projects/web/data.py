## -*- coding: utf-8 -*-

# This is crazy old project
# Could be reworked with 
# https://www.rapidseedbox.com/blog/snscrape
# https://github.com/JustAnotherArchivist/snscrape " A social networking service scraper in Python "


import os
import re
import datetime
import json
import base64
import time
from itertools import chain

#try:
import urllib.request
urlopen = urllib.request.urlopen
from urllib.parse import quote
#except ImportError:
#    from urllib2 import urlopen


#try:
import html  # python3
#except ImportError:
#    from HTMLParser import HTMLParser  # python2 fallback
#    class html():
#        unescape = HTMLParser().unescape
        #escape = HTMLParser().escape


def _safe_encode_url(url):
    return base64.urlsafe_b64encode(url.encode('utf8')).decode('utf8')


def get_url(url, cache_path='cache', cache_seconds=60*60*100):
    if cache_path:
        cache_filename = os.path.join(cache_path, _safe_encode_url(url))
        if os.path.exists(cache_filename) and (os.stat(cache_filename).st_mtime > time.time() - cache_seconds):
            print('Cache: ' + url)
            with open(cache_filename, 'r') as filehandle:
                return filehandle.read()  #.decode('utf8')
    print('External: ' + url)
    data = urlopen(url).read().decode('utf8')
    if data and cache_path:
        try:
            os.makedirs(cache_path)
        except:
            pass
        with open(cache_filename, 'w') as filehandle:
            filehandle.write(data)  # .encode('utf8')
    return data


def get_json(*args, **kwargs):
    return json.loads(get_url(*args, **kwargs))


def postcode_to_lat_long(postcode):
    data = get_json(f'http://api.postcodes.io/postcodes/{quote(postcode)}')
    return {
        'latitude': data['result'].get('latitude'),
        'longitude': data['result'].get('longitude'),
    }


def get_user_tweets(username):
    """
    OLD!
    Will not work with current twitter - have to use API - (hope without authentication?)
    """
    TWITTER_URL = 'http://twitter.com/'

    twitter_html = get_url(TWITTER_URL + username)
    tweets = []
    for tweet_match, time_match, link_match in zip(
        re.finditer(r'tweet-text.*?>(.*?)<\/p>', twitter_html),
        re.finditer(r'data-time="(.*?)"', twitter_html),
        re.finditer(r'data-permalink-path="(.*?)"', twitter_html),
    ):
        tweet_html = html.unescape(tweet_match.group(1))
        tweet_html_stripped = re.sub(r'<.*?>', '', tweet_html)
        tweets.append({
            'title': tweet_html_stripped,
            'description': tweet_html,
            'unicode': html.unescape(tweet_html_stripped),
            'datetime': datetime.datetime.fromtimestamp(int(time_match.group(1))),
            'link': TWITTER_URL + link_match.group(1),
        })
    return tweets


def get_ebay_items(search):
    """
    OLD
    Page has changed - can't be used - suspect apikey required
    """
    EBAY_ITEMS_URL = 'http://www.ebay.co.uk/sch/i.html?LH_Auction=1&_nkw='
    ebay_html = get_url(EBAY_ITEMS_URL + search)

    items = []
    for title_match, price_match in zip(
        re.finditer(r'<h3 class="lvtitle"><a href="(.*?)\?.*?>(.*?)</a>\s*</h3>', ebay_html),
        #re.finditer(r'timeMs="(\d*?)"', ebay_html),
        #re.finditer(r'imgurl="(.*?)"', ebay_html),  # \s*class="img load-img"
        re.finditer(r'lvprice.*?([.\d]*)</span', ebay_html, flags=re.DOTALL + re.MULTILINE),
    ):
        items.append({
            'title': title_match.group(2),
            'description': price_match.group(1),
            'datetime': datetime.datetime.now(),
            'link': title_match.group(1),
            'image': '',
        })
    return items


def get_local_crime(latlon_dict):
    API = 'https://data.police.uk/api/'
    crime_items = get_json(API +
        'crimes-at-location?lat={latitude}&lng={longitude}'.format(**latlon_dict)
    )
    crimes = []
    for crime in crime_items:
        crimes.append({
            'title': crime['category'],
            'description': '',
            'datetime': datetime.datetime.strptime(crime['month'], '%Y-%m'),
            'link': API + 'outcomes-for-crime/' + crime['persistent_id']
        })
    return crimes


def get_tube_disruptions(line):
    data = get_json('https://api.tfl.gov.uk/Line/'+line)
    return [{
        'title': '{} Disruptions'.format(line),
        'description': '',
        'link': '',
        'datetime': datetime.datetime.now(),
    }]


def get_local_weather(postcode):
    return []


def format_rss(rss_items, **kwargs):
    RSS_DATE_FORMAT = '%a, %d %b %Y %H:%M:%S %z'  # RSS specification pubDate must follow RFC822:

    kwargs.setdefault('title', '')
    kwargs.setdefault('description', '')
    kwargs.setdefault('link', '')
    kwargs.setdefault('pubDate', datetime.datetime.now().strftime(RSS_DATE_FORMAT))

    def format_rss_item(rss_item):
        rss_item['pubDate'] = rss_item['datetime'].strftime(RSS_DATE_FORMAT)
        return u"""
            <item>
                <title>{title}</title>
                <description>{description}</description>
                <link>{link}</link>
                <pubDate>{pubDate}</pubDate>
            </item>
        """.format(**rss_item)

    return u"""<?xml version="1.0" encoding="utf-8"?>
        <rss version="2.0">
        <channel>
            <title>{title}</title>
            <description>{description}</description>
            <link>{link}</link>
            <language>en-us</language>
            <lastBuildDate>{pubDate}</lastBuildDate>
            <pubDate>{pubDate}</pubDate>

            {ITEMS}

        </channel>
        </rss>
    """.format(
        ITEMS='\n\n'.join(map(format_rss_item, rss_items)),
        **kwargs
    )


def save_csv(items, filename='data.csv', **kwargs):
    print('Output: ' + filename)
    import csv
    FIELDNAMES = ('title', 'description', 'link', 'datetime')
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        writer.writeheader()
        for item in items:
            writer.writerow({field: item.get(field, '') for field in FIELDNAMES})  #.encode('utf8')


def save_rss(items, filename='data.xml', **kwargs):
    print('Output: ' + filename)
    rss_string = format_rss(items, **kwargs)
    with open(filename, 'w') as filehandle:
        filehandle.write(rss_string)  #.encode('utf8')


if __name__ == "__main__":
    items = chain(
        #get_user_tweets('calaldees'),
        get_local_crime(postcode_to_lat_long('ct1 1ys')),
        get_tube_disruptions('piccadilly'),
        #get_ebay_items('kenshin')[:5],
        #get_local_weather('CT1 1YS')
    )
    items = sorted(items, key=lambda item: item.get('datetime'), reverse=True)
    save_csv(items)
    save_rss(items)
