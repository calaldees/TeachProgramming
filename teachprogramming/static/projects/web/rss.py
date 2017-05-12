import os
import re
import datetime
import json
import base64
import time

try:
    import urllib.request
    urlopen = urllib.request.urlopen
except ImportError:
    import urllib2
    urlopen = urllib2.urlopen

try:
    import html  # python3
except ImportError:
    from HTMLParser import HTMLParser  # python2 fallback
    class html():
        unescape = HTMLParser().unescape
        #escape = HTMLParser().escape


def _safe_encode_url(url):
    return base64.urlsafe_b64encode(url.encode('utf8')).decode('utf8')


def get_url(url, cache_path='cache', cache_seconds=60*60):
    if cache_path:
        cache_filename = os.path.join(cache_path, _safe_encode_url(url))
        if os.path.exists(cache_filename) and (os.stat(cache_filename).st_mtime > time.time() - cache_seconds):
            with open(cache_filename, 'r') as filehandle:
                return filehandle.read().decode('utf8')
    data = urlopen(url).read().decode('utf8')
    if data and cache_path:
        try:
            os.makedirs(cache_path)
        except:
            pass
        with open(cache_filename, 'w') as filehandle:
            filehandle.write(data.encode('utf8'))
    return data


def get_json(*args, **kwargs):
    return json.loads(get_url(*args, **kwargs))


def postcode_to_lat_long(postcode):
    data = get_json('http://api.postcodes.io/postcodes/{}'.format(postcode))
    return {
        'latitude': data['result'].get('latitude'),
        'longitude': data['result'].get('longitude'),
    }


def get_user_tweets(username):
    TWITTER_URL = 'http://twitter.com/'

    twitter_html = get_url(TWITTER_URL + username)
    tweets = []
    for tweet_match, time_match, link_match in zip(
        re.finditer(r'tweet-text.*?>(.*?)<\/p>', twitter_html),
        re.finditer(r'data-time="(.*?)"', twitter_html),
        re.finditer(r'data-permalink-path="(.*?)"', twitter_html),
    ):
        tweet_html = tweet_match.group(1)
        tweet_html_stripped = re.sub(r'<.*?>', '', tweet_html)
        tweets.append({
            'title': tweet_html_stripped,
            'description': tweet_html,
            'unicode': html.unescape(tweet_html_stripped),
            'datetime': datetime.datetime.fromtimestamp(int(time_match.group(1))),
            'link': TWITTER_URL + link_match.group(1),
        })
    return tweets


def get_local_crime(latlon_dict):
    crimes = []
    for crime in get_json('https://data.police.uk/api/crimes-at-location?lat={latitude}&lng={longitude}'.format(**latlon_dict)):
        crimes.append({
            'title': crime['category'],
            'description': '',
            'datetime': datetime.datetime.strptime(crime['month'], '%Y-%m'),
            'link': '',
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


def save_rss(rss_items, filename='rss.xml', **kwargs):
    rss_items = sorted(rss_items, key=lambda rss_item: rss_item.get('datetime'), reverse=True)
    rss_string = format_rss(rss_items, **kwargs)
    with open(filename, 'w') as filehandle:
        filehandle.write(rss_string.encode('utf8'))


if __name__ == "__main__":
    save_rss(
        get_user_tweets('calaldees') +
        get_local_crime(postcode_to_lat_long('ct1 1ys')) +
        get_tube_disruptions('piccadilly')
        #get_local_weather('CT1 1YS')
    )
