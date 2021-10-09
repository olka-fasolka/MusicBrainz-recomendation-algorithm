from mutagen.id3 import ID3
import pandas as pd
import numpy as np
import tqdm

from services.AcousticBrainzService import AcousticBrainzService
from services.FileManager import FileManager


if __name__ == "__main__":
    FM = FileManager()
    ABS = AcousticBrainzService()
    dataset_ID = "fc881bc5-1eef-4281-809b-a8913be38775"
    dataset = ABS.get_dataset_by_ID(dataset_ID)
    recordings_ids = dataset['classes'][0]['recordings']
    #print(dataset)

    row_list_high = []
    row_list_low = []

    #FM.upload_songs_to_dataset(dataset_ID)

    i=0

    for recording_id in recordings_ids:
        print(recording_id)
        try: 
            recording = ABS.get_recording_by_ID(recording_id)
            #print(recording)
            row_list_low.append([recording.MBID, recording.title, recording.artist, recording.key, recording.scale, recording.bpm, recording.loudness, 
            recording.spectral_centroid_mean, recording.spectral_centroid_var, recording.dynamic_complexity])
            row_list_high.append([recording.MBID, recording.title, recording.artist, recording.danceability, recording.femininity, 
            recording.acousticness, recording.sadness, recording.brightness, recording.instrumental])
            i+=1
            print(i)
        except (RuntimeError, KeyError):
            print("Catched Error")
            continue
        
        df_low = pd.DataFrame(row_list_low, columns=['MBID','title','artist','key','scale','bpm','loudness','dynamic_complexity','spectral_centroid_mean','spectral_centroid_var'])
        df_high = pd.DataFrame(row_list_high, columns=['MBID','title','artist','danceability','femininity','acousticness','sadness','brightness','instrumentality'])
        # print(df_low)
        # print("\n\n")
        # print(df_high)
        df_low.to_csv("data_low.csv")
        df_high.to_csv("data_high.csv")





    