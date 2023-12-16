from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.scrollview import MDScrollView
import os

# Get the current directory of the module
module_dir = os.path.dirname(os.path.realpath(__file__))

# Load the kv file using a relative path
kv_path = os.path.join(module_dir, 'content_navigation_drawer.kv')
Builder.load_file(kv_path)


class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
