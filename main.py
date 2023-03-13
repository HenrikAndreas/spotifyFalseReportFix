import requests
import json
from time import sleep
from datetime import datetime

from tokenAcquire import TokenAcquire

CLIENT_ID = ""
CLIENT_SECRET = ""
AUTH_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = "https://api.spotify.com/v1/playlists/"

USER_ID = "1134655235"
PLAYLIST_ID="" # Official spotify playlist id

def main():
    print("\n\n-_-_-_ Spotify Abuse Fix Kit _-_-_-\n\n")

    name = input("Enter name of playlist: ")
    description = input("Enter description of playlist: ")

    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })

    tokenAcquire = TokenAcquire(headless=True)
    tokenAcquire.start()

    access_token = ""

    while True:

        headers = {
            'Authorization': 'Bearer {token}'.format(token=access_token)
        }

        playlist_data = requests.get(BASE_URL+PLAYLIST_ID+'?fields=name', headers=headers)
        
        try:
            if playlist_data.json()['name'] != "Depressive | Sad Metal":
                print("[{0}]: - The playlist has been falsely reported!".format(datetime.now().strftime("%H:%M:%S")))              

                print("\t\t>>> Reverting playlist to original...")
                data = json.dumps({
                    "name": name,
                    "description": description,
                    "public": True
                })

                update_playlist = requests.put(BASE_URL+PLAYLIST_ID, data=data, headers=headers)
                print("\t\t>>> Successfully updated playlist!")
            else:
                print("[{0}]: Everything seems ok".format(datetime.now().strftime("%H:%M:%S")))
        except:
            print("[{0}]: {1}".format(datetime.now().strftime("%H:%M:%S"), playlist_data.json()['error']['message']))
            access_token = tokenAcquire.getToken()


        sleep(70)

    return


if __name__ == "__main__":
    main()
