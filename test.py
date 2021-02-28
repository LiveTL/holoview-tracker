from pprint import pprint, pformat
from requests.sessions import Session

import os
from time import sleep
from datetime import datetime

s = Session()
f = open("out.txt", "a", encoding="utf-8")

def main():
    while True:
        line = str((datetime.now().strftime('%Y-%m-%d %H:%M:%S'), [(x['channel']['name'],x['channel']['yt_channel_id'], x['live_viewers']) for x in getLive()['live']]))
        print(line)
        f.write('\n' + line)
        f.flush()
        sleep(5)

def getLive():
    return s.get('https://api.holotools.app/v1/live').json()

if __name__ == "__main__":
    main()