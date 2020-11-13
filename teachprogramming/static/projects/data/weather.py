"""
Concept for getting hourly weather data into python.

It may be possible to download 4gb (compressed) of a years worth of data and mirror it locally on school servers.
The files are named from weather station id numbers. It would be good to see these on a map.

TODO:
Investigate how to put multiple flags on a browser map - this could be a precursor to data layers? maybe heatmap?
Investigate offline generation of map images too
Can we put pins in a map where the weather stations are available?
What can we do historically? - there is data here back to 1900
My example below only extracts temperature - is there more we can do? wind direction?
"""

import os
import csv
import re
import datetime
import logging
from pprint import pprint
from collections import namedtuple

log = logging.getLogger(__name__)

LatLon = namedtuple('LatLon', ('lat', 'lon'))


def load_neic_csv_into_data(filename, data):
    """
    Parser for
    * [National Centers for Environmental Information (US)](https://www.ncei.noaa.gov/)
        * [global hourly](https://www.ncei.noaa.gov/data/global-hourly/)

    Weather station id list?
    https://www.metoffice.gov.uk/hadobs/hadisdh/data/PosthomogIDPHAt_anoms8110_goodsHadISDH.4.2.0.2019f_JAN2020.txt
    """
    log.debug(f'load {filename}')
    with open(filename, encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in csv_reader:
            # Parse data
            timestamp = datetime.datetime.strptime(row['DATE'], '%Y-%m-%dT%H:%M:%S')
            latlon = LatLon(lat=float(row['LATITUDE']), lon=float(row['LONGITUDE']))
            tmp = float(re.match(r'([-+]\d{4}),\d', row['TMP']).group(1)) / 10
            tmp = tmp if tmp < 100 else None
            # Add to dataset
            data.setdefault(timestamp, {})[latlon] = {
                'tmp': tmp,
            }


def get_csv_files(path):
    for filename in os.listdir(path):
        if filename.endswith('.csv'):
            yield os.path.join(path, filename)


def open_browser(latlon):
    lat, lon = latlon
    zoom = 10
    url = f'https://www.google.co.uk/maps/@{lat},{lon},{zoom}z'
    log.info(f'Opening webbrowser at {url}')
    import webbrowser
    webbrowser.open(url)  # [, new=0[, autoraise=True]]


# Comamnd Line -----------------------------------------------------------------

def get_args():
    import argparse
    parser = argparse.ArgumentParser(
        description="""
        load neic csv weather data
        """,
        epilog=""" """
    )

    parser.add_argument('path', action='store', help='file path where the csv datafiles are located', default='./')
    parser.add_argument('-v', '--verbose', action='store_true', help='', default=False)

    args = vars(parser.parse_args())
    return args


# Main -------------------------------------------------------------------------


def main():
    args = get_args()
    logging.basicConfig(level=logging.DEBUG if args['verbose'] else logging.INFO)

    data = {}
    for filename in get_csv_files(args['path']):
        load_neic_csv_into_data(filename, data)

    pprint(data)
    latlon = data.values().__iter__().__next__().keys().__iter__().__next__()
    open_browser(latlon)


if __name__ == "__main__":
    main()
