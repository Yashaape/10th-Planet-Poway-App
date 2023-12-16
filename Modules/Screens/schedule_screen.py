from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

import os

# Get the current directory of the module
module_dir = os.path.dirname(os.path.realpath(__file__))

schedule = """
MDScreen:
    Image:
        source: '10thPlanetPowaySchedule.png'

"""
Builder.load_string(schedule)


class ScheduleScreen(MDScreen):
    pass
