from plyer import gps

class GPSListener:
    def __init__(self, callback):
        self.callback = callback

    def start(self):
        gps.configure(on_location=self.on_location)
        gps.start(minTime=1000, minDistance=1)

    def on_location(self, **kwargs):
        lat = kwargs.get('lat')
        lon = kwargs.get('lon')
        if self.callback:
            self.callback(lat, lon)
