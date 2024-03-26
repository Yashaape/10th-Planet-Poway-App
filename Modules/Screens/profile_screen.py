from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
import os

# Get the current directory of the module
module_dir = os.path.dirname(os.path.realpath(__file__))

# Load the kv file using a relative path
kv_path = os.path.join(module_dir, 'profile_screen.kv')
screen = Builder.load_file(kv_path)


class ProfileScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        items = [
            {
                "viewclass": "OneLineListItem",
                "text": color,
                "height": dp(56),
                "on_release": lambda x=color: self.set_item(x),
            } for color in ['White', 'Blue', 'Purple', 'Brown', 'Black']
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.belt_rank_field,
            items=items,
            position="center",
            width_mult=4,
        )

    def set_item(self, text_item):
        self.ids.belt_rank_field.set_item(text_item)
        self.menu.dismiss()
