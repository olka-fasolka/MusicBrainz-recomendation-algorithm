import os
from mutagen.id3 import ID3
import requests
from services.AcousticBrainzService import AcousticBrainzService
from tqdm import tqdm

class FileManager: 

    def upload_songs_to_dataset(self, dataset_ID): 
        ABS = AcousticBrainzService()

        thisdir = os.getcwd()

        for r, d, f in tqdm(os.walk(thisdir)): 
            for file in f: 
                if file.endswith(".mp3"): 
                    filepath=os.path.join(r,file)
                    recording_ID = self.read_UUID(filepath)
                    ABS.add_recording_to_dataset(recording_ID, dataset_ID, "all")
                    print("uploaded: ",recording_ID)
            

    
    def read_UUID(self, filepath): 
        audio = ID3(filepath)
        MBID = ''
        for frame in audio.getall("UFID"):
            MBID = str(frame.data, 'utf-8')
        return MBID





