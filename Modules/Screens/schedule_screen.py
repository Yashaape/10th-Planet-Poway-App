from kivymd.uix.screen import MDScreen

from kivy.lang import Builder

KV = '''
<ScheduleScreen>:
    name: 'schedule_screen'
    BoxLayout:
        orientation: 'vertical'
        Image:
            source: '10thPlanetPowaySchedule.png'
            size_hint_y: None  # Fixing the height
            height: root.height * 0.89  # Adjust the height as per your requirement
            
'''

Builder.load_string(KV)


class ScheduleScreen(MDScreen):
    pass
