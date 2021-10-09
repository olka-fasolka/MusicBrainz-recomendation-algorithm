import requests
from mutagen.id3 import ID3
import json
import time
import pandas as pd
import numpy as np

from models.Recording import Recording 

class AcousticBrainzService: 
    api_url = "https://acousticbrainz.org/api/v1/" 
    token = "Token Vodr3Zu7XahC1rVvcRTkWf1OeazNoIfPxUyelcvX"
    
    def get_dataset_by_ID(self, dataset_ID):
        url = self.api_url + "datasets/" + dataset_ID
        response = requests.get(url)
        return response.json()

    def get_recording_data_by_ID(self, recording_id, level):
        url = self.api_url + recording_id + '/' + level+ '-level'
        response = requests.get(url)
        if response.ok:
            return response.json()
        else:
            raise RuntimeError("Not Found")
        

    def get_recording_by_ID(self, recording_id):
        json_high = self.get_recording_data_by_ID(recording_id, 'high')
        json_low = self.get_recording_data_by_ID(recording_id, 'low')

        #metadata
        title = json_high['metadata']['tags']['title'][0]
        artist =  json_high['metadata']['tags']['artist'][0]

        #low level data
        key = json_low['tonal']['key_key']
        scale = json_low['tonal']['key_scale']
        bpm = json_low['rhythm']['bpm']
        loudness = json_low['lowlevel']['average_loudness']
        spectral_centroid_mean = json_low['lowlevel']['spectral_centroid']['mean']
        spectral_centroid_var = json_low['lowlevel']['spectral_centroid']['var']
        dyn_com = json_low['lowlevel']['dynamic_complexity']

        #high level data
        danceability = json_high['highlevel']['danceability']['all']['danceable']
        gender = json_high['highlevel']['gender']['all']['female']
        acousticness = json_high['highlevel']['mood_acoustic']['all']['acoustic']
        happiness = json_high['highlevel']['mood_happy']['all']['happy']
        brightness = json_high['highlevel']['timbre']['all']['bright']
        instrumental = json_high['highlevel']['voice_instrumental']['all']['instrumental']

        return Recording(recording_id, title, artist, key, scale, bpm, loudness, spectral_centroid_mean, spectral_centroid_var, dyn_com, 
        danceability, gender, acousticness, happiness, brightness, instrumental)

    def add_recording_to_dataset(self, recording_id, dataset_id, class_name): 
        url = self.api_url + 'datasets/' + dataset_id + '/recordings' 
        json_request = {"class_name": class_name, "recordings": [recording_id]}
        headers = {'Authorization': self.token, 'Content-Type':'application/json'}
        requests.put(url, json=json_request, headers=headers)

    