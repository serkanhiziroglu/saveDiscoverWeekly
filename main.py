import json
import requests
from authentication import spotify_id, dw_uri
from datetime import date
from refresh import Refresh


class saveSongs:

    def __init__(self):
        self.spotify_id = spotify_id
        self.spotify_token = ""
        self.dw_uri = dw_uri
        self.tracks = ""
        self.newPlaylistId = ""

    def findSongs(self):
        query = 'https://api.spotify.com/v1/playlists/{}/tracks'.format(dw_uri)
        response = requests.get(query, headers={"Content-Type": "application/json",
                                                "Authorization": "Bearer {}".format(self.spotify_token)})

        response_json = response.json()

        for i in response_json["items"]:
            self.tracks += (i["track"]["uri"] + ",")
        self.tracks = self.tracks[:-1]

        # print(self.tracks)

        self.addToPlayList()

    def createPlaylist(self):

        global date
        date = date.today()
        today = date.strftime("%d/%m/%y")
        query = 'https://api.spotify.com/v1/users/{}/playlists'.format(
            spotify_id)

        request_body = json.dumps({
            "name": "DiscoverWeekly: " + today
        })

        response = requests.post(query, data=request_body, headers={"Content-Type": "application/json",
                                                                    "Authorization": "Bearer {}".format(self.spotify_token)})
        response_json = response.json()

        return response_json["id"]

    def addToPlayList(self):

        self.newPlaylistId = self.createPlaylist()

        query = "https://api.spotify.com/v1/playlists/{}/tracks?uris={}".format(
            self.newPlaylistId, self.tracks)

        response = requests.post(query, headers={
                                 "Content-Type": "application/json",
                                 "Authorization": "Bearer {}".format(self.spotify_token)})

        print(response.json)

    def call_refresh(self):
        print("Refreshing")
        refreshCaller = Refresh()
        self.spotify_token = refreshCaller.refresh()

        self.findSongs()


a = saveSongs()
a.call_refresh()
