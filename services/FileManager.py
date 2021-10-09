import os
from mutagen.id3 import ID3
import requests
from services.AcousticBrainzService import AcousticBrainzService

class FileManager: 

    def upload_songs_to_dataset(self, dataset_ID, directory): 
        ABS = AcousticBrainzService()
        for filename in os.listdir(directory): 
            filepath = directory + "/" + filename
            recording_ID = self.read_UUID(filepath)
            ABS.add_recording_to_dataset(recording_ID, dataset_ID, "songs")
            print(recording_ID)


    
    def read_UUID(self, filepath): 
        audio = ID3(filepath)
        MBID = ''
        for frame in audio.getall("UFID"):
            MBID = str(frame.data, 'utf-8')
        return MBID





