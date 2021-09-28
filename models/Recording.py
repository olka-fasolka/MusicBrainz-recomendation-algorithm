import requests
from mutagen.id3 import ID3
import json
import time
import pandas as pd
import numpy as np

class Recording: 

    def __init__(self, MBID, title, artist, danceability): 
        self.MBID = MBID
        self.title = title, 
        self.artist = artist
        self.danceability = danceability

    def __str__(self): 
        return f'Recording data: \n title: {self.title} \n artist: {self.artist} \n danceability: {self.danceability}'
