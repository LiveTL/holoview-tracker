from pprint import pprint, pformat
from requests.sessions import Session

import os

s = Session()
f = open("thing.txt", "w", encoding="utf-8")

def main():
    getLiveResponse = getLive()
    f.write(str(getLiveResponse))
    idviews = [(x['channel']['yt_channel_id'], x['live_viewers']) for x in getLiveResponse['live']]
    pprint(idviews)

def getLive():
    return s.get('https://api.holotools.app/v1/live').json()

if __name__ == "__main__":
    main()