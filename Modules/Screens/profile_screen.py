from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivy.properties import ObjectProperty

KV = '''
<ProfileScreen>:
    name: 'profile_screen'
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(20)

        MDLabel:
            text: "Profile"
            halign: 'center'
            font_style: 'H4'

        MDLabel:
            id: name_field
            text: "Name"
            mode: "rectangle"

        MDLabel:
            id: email_field
            text: "Email"
            mode: "rectangle"

        MDDropDownItem:
            id: belt_rank_field
            text: "Belt Rank"
            on_release: root.menu.open()
'''
Builder.load_string(KV)


class ProfileScreen(MDScreen):
    screen_manager = ObjectProperty()
    menu = None

    def on_enter(self):
        if not self.menu:
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
