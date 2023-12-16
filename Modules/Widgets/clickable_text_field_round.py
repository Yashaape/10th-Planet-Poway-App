from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.properties import StringProperty
from kivy.lang import Builder
import os

# Get the current directory of the module
module_dir = os.path.dirname(os.path.realpath(__file__))

# Load the kv file using a relative path
kv_path = os.path.join(module_dir, 'clickable_text_field_round.kv')
Builder.load_file(kv_path)


class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()
    username = StringProperty()
    username_hint_text = StringProperty()