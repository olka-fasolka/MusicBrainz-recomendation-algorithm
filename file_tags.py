from mutagen.mp3 import MP3
from mutagen.id3 import ID3

import mutagen
import eyed3

def read_title(filepath): 
    audio = ID3(filepath)
    title = audio['TIT2']
    return title



if __name__ == "__main__":
    filepath = "magisterka/audio/sanah.mp3"

    # file = eyed3.load(filepath)
    # for frame in file.tag.frameiter(["TXXX"]):
    #     print(f"{frame.description}: {frame.text}")
    # # get a specific tag
    # artist_id = file.tag.user_text_frames.get("MusicBrainz Artist Id").text
    # print(artist_id)

    audio = ID3(filepath)
    for frame in audio.getall("UFID"):
        print(str(frame.data, 'utf-8'))
        
    # get a specific tag
    #artist_id = audio["TXXX:MusicBrainz Artist Id"].text[0]