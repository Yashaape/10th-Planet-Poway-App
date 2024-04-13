from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.image import Image

KV = '''
<ChatScreen>:
    orientation: 'vertical'

    ScrollView:
        MDGridLayout:
            id: message_list
            cols: 1
            size_hint_y: None
            height: self.minimum_height

    MDBoxLayout:
        size_hint_y: None
        height: "30dp"  # Height of the input area

        MDTextField:
            id: message_input
            hint_text: 'Type your message'
            mode: 'fill'

        MDIconButton:
            icon: 'image'
            on_release: app.select_image()
'''

Builder.load_string(KV)


class ChatScreen(MDBoxLayout):
    pass


class TestApp(MDApp):
    def build(self):
        return ChatScreen()

    def select_image(self):
        # Dummy function to simulate selecting an image
        # In a real application, this function should open a file picker or camera interface
        # and handle the selected image appropriately.
        self.add_image_to_chat("10thPlanetPoway.png")

    def add_image_to_chat(self, image_path):
        # Create an Image widget with the selected image
        image_widget = Image(source=image_path)

        # Add the Image widget to the message list
        self.root.ids.message_list.add_widget(image_widget)


if __name__ == "__main__":
    TestApp().run()
