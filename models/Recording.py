class Recording: 

    def __init__(self, MBID, title, artist, key, scale, bpm, loudness, dynamic_complexity, spectral_centroid_mean, spectral_centroid_var, 
    danceability, femininity, acousticness, sadness, brightness, instrumental):
        self.MBID = MBID
        self.title = title 
        self.artist = artist

        self.key = key
        self.scale = scale
        self.bpm = bpm
        self.loudness = loudness
        self.dynamic_complexity = dynamic_complexity
        self.spectral_centroid_mean = spectral_centroid_mean
        self.spectral_centroid_var = spectral_centroid_var


        self.danceability = danceability
        self.femininity = femininity
        self.acousticness = acousticness
        self.sadness = sadness
        self.brightness = brightness
        self.instrumental = instrumental

    def __str__(self): 
        return f'Recording data: \n title: {self.title} \n artist: {self.artist} \n danceability: {self.danceability}'
