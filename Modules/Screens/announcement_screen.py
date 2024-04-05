from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

KV = '''
<AnnouncementScreen>:
    name: 'announcement_screen'
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: 'announcement_screen'
            halign: 'center'

'''

Builder.load_string(KV)


class AnnouncementScreen(MDScreen):
    pass
