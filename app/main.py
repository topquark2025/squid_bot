from kivy.app import App
from kivy.uix.label import Label
from gps_helper import GPSListener
from utils import send_location_to_server

class MyApp(App):
    def build(self):
        self.label = Label(text="GPS 추적 중...")
        self.gps = GPSListener(callback=self.on_location)
        self.gps.start()
        return self.label

    def on_location(self, lat, lon):
        self.label.text = f"위치: {lat}, {lon}"
        send_location_to_server(lat, lon)

if __name__ == '__main__':
    MyApp().run()
