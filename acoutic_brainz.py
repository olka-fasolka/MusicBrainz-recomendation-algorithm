from mutagen.id3 import ID3
import pandas as pd
import numpy as np

from services.AcousticBrainzService import AcousticBrainzService
from services.FileManager import FileManager


if __name__ == "__main__":
    FM = FileManager()
    ABS = AcousticBrainzService()
    dataset_ID = "00ff3304-aea8-4ff1-a4da-8d9b2df8951f"
    dataset = ABS.get_dataset_by_ID(dataset_ID)
    recordings_ids = dataset['classes'][0]['recordings']
    #print(dataset)

    row_list_high = []
    row_list_low = []

    #FM.upload_songs_to_dataset(dataset_ID, "magisterka/audio/Pure Love Disc 1")

    FM.upload_songs_to_dataset(dataset_ID, "magisterka/audio/2009 - Fearless")

    # for recording_id in recordings_ids: 
    #     recording = ABS.get_recording_by_ID(recording_id)
    #     #print(recording)
    #     row_list_low.append([recording.MBID, recording.title, recording.artist, recording.key, recording.scale, recording.bpm, recording.loudness, 
    #     recording.spectral_centroid_mean, recording.spectral_centroid_var, recording.dynamic_complexity])
    #     row_list_high.append([recording.MBID, recording.title, recording.artist, recording.danceability, recording.femininity, 
    #     recording.acousticness, recording.sadness, recording.brightness, recording.instrumental])
    #     #print(recording_data)
    
    # df_low = pd.DataFrame(row_list_low, columns=['MBID','title','artist','key','scale','bpm','loudness','dynamic_complexity','spectral_centroid_mean','spectral_centroid_var'])
    # df_high = pd.DataFrame(row_list_high, columns=['MBID','title','artist','danceability','femininity','acousticness','sadness','brightness','instrumentality'])
    # print(df_low)
    # print("\n\n")
    # print(df_high)
    #df.to_csv("data.csv")



    