import requests
from mutagen.id3 import ID3
import json
import time
import pandas as pd
import numpy as np

from models.Recording import Recording 

class AcousticBrainzService: 
    api_url = "https://acousticbrainz.org/api/v1/" 
    
    def get_dataset_by_ID(self, dataset_ID):
        url = self.api_url + "datasets/" + dataset_ID
        response = requests.get(url)
        return response.json()

    def get_recording_data_by_ID(self, recording_id):
        url = self.api_url + recording_id + "/high-level"
        response = requests.get(url)
        return response.json()

    def get_recording_by_ID(self, recording_id):
        json = self.get_recording_data_by_ID(recording_id)
        title = json['metadata']['tags']['title'][0]
        artist =  json['metadata']['tags']['artist'][0]
        danceability = json['highlevel']['danceability']['all']['danceable']
        return Recording(recording_id, title, artist, danceability)

    