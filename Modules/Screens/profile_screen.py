from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivy.lang import Builder
from kivy.metrics import dp

KV = '''
<ProfileScreen>:
    id: profile_screen
    name: 'profile_screen'

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(20)
        
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            
            Image:
                source: 'Generic_Blank_Avatar.png'  # Replace '.png' with the actual path to your image
                size_hint_y: None
                height: dp(300)  # Adjust the height as needed
                pos_hint: {'center_x': 0.5}
                allow_stretch: True  # Adjusts the aspect ratio to fit the space

            MDTextField:
                id: name_label
                hint_text: "Name"
                mode: "rectangle"
                size_hint_y: None
                height: dp(40)
                readonly: True
                helper_text_mode: "on_focus"
                helper_text: "Enter your name"

            MDTextField:
                id: email_label
                hint_text: "Email"
                mode: "rectangle"
                size_hint_y: None
                height: dp(40)
                readonly: True
                helper_text_mode: "on_focus"
                helper_text: "Enter your email"

            MDDropDownItem:
                id: belt_rank_field
                text: "Belt Rank"
                on_release: root.menu.open()

            Widget:
                size_hint_y: None
                height: dp(20)
'''

Builder.load_string(KV)


class ProfileScreen(MDScreen):
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

    def set_user_info(self, user_info):
        # Access MDLabel widgets and set their text to user info
        self.ids.name_label.text = user_info.get('first_name', '') + ' ' + user_info.get('last_name', '')
        self.ids.email_label.text = user_info.get('email', '')

