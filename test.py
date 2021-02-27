from pprint import pprint, pformat
from requests.sessions import Session

import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

s = Session()
scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    credentials = flow.run_console()
    print(credentials)
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

    live_ids = [x['channel']['yt_channel_id'] for x in getLive()['live']]
    responses = [youtube.channels().list(part="statistics", id=x).execute() for x in live_ids]
    viewcounts = [(x['items'][0]['id'],x['items'][0]['statistics']['viewCount']) for x in responses]
    pprint(viewcounts)

def getLive():
    return s.get('https://api.holotools.app/v1/live').json()

if __name__ == "__main__":
    main()