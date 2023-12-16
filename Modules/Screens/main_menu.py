from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
import os

# Get the current directory of the module
module_dir = os.path.dirname(os.path.realpath(__file__))

# Load the kv file using a relative path
kv_path = os.path.join(module_dir, 'main_menu.kv')
Builder.load_file(kv_path)


class MainMenuScreen(MDScreen):
    pass
