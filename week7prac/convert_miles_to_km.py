"""
CP1404 Practical
Erik Cronin
Miles to Kilometres Converter
"""
from kivy.app import App
from kivy.lang import Builder

conversion_rate = 1.60934

class MilesToKilometresApp(App):
    def build(self):
        self.title = "Miles to Kilometres Conversion"
        self.root = Builder.load_file('convert_miles_to_km.kv')
        return self.root

    def handle_increment(self, change):
        value = int(self.root.ids.miles.text) + change
        self.root.ids.miles.text = value

MilesToKilometresApp().run()