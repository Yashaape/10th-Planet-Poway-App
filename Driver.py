from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class PowayApp(MDApp):
    def build(self):
        return MDLabel(text="10Th Planet Poway", halign="center")

PowayApp().run()
