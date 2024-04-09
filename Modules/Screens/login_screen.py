from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

KV = '''
<LoginScreen>:
    Image:
        source: '10thPlanetPoway.png'
        size_hint_y: None #allows setting a fixed height
        height: dp(250)
        pos_hint: {"top": 1.0} #aligns top of image to top

    ClickableTextFieldRound:
        id: clickable_text_field_round
        size_hint: None, None
        width: "300dp"
        hint_text: "Password"
        pos_hint: {"center_x": .5, "center_y": .35}

'''
Builder.load_string(KV)


class LoginScreen(MDScreen):
    pass


