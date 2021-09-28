from mutagen.id3 import ID3
import pandas as pd
import numpy as np

from services.AcousticBrainzService import AcousticBrainzService

def read_UUID(filepath): 
    audio = ID3(filepath)
    for frame in audio.getall("UFID"):
        print(str(frame.data, 'utf-8'))


if __name__ == "__main__":
    ABS = AcousticBrainzService()
    dataset_ID = "30ee0678-9d04-45d9-a793-4dd8282ef6b4"
    dataset = ABS.get_dataset_by_ID(dataset_ID)
    recordings_ids = dataset['classes'][0]['recordings']
    #print(dataset)

    row_list = []

    for recording_id in recordings_ids: 
        recording = ABS.get_recording_by_ID(recording_id)
        print(recording)
        row_list.append([recording.MBID,recording.title, recording.artist, recording.danceability])
        #print(recording_data)
    
    df = pd.DataFrame(row_list, columns=['MBID', 'title', 'artist', 'danceability'])
    print(df)



    