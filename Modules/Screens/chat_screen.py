from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivy.properties import ObjectProperty
from kivy.metrics import dp
from kivy.clock import Clock


KV = '''
<ChatScreen>:
    name: 'chat_screen'

    ScrollView:
        size_hint_y: None
        height: root.height - 40 - message_input.height  # Adjust the height as needed
        do_scroll_x: False
        
        MDBoxLayout:
            id: message_container
            orientation: 'vertical'
            padding: dp(10)
            size_hint_y: None
            height: self.minimum_height
            adaptive_height: True

    MDBoxLayout:
        size_hint_y: None
        height: "30dp"  # Height of the MDTextField or any other component below the scroll view

        MDTextField:
            id: message_input
            multiline: True
            hint_text: 'Type your message'
            max_height: "500dp" # stops Textbox growth after 24 lines.
            mode: 'fill'

        MDIconButton:
            id: send_button
            icon: 'send'
            on_press: root.on_send()
'''

Builder.load_string(KV)


class ChatScreen(MDScreen):
    message_input = ObjectProperty(None)
    message_container = ObjectProperty(None)

    def send_message(self, message):
        # Create a rounded label for the sent message
        message_label = MDLabel(
            text=message,
            size_hint=(None, None),
            size=(dp(200), dp(50)),  # Adjust size as needed
            pos_hint={'right': 1},
            valign='top',
            font_style='Body1',
            theme_text_color='Custom',
            text_color=(1, 1, 1, 1),  # White text color
            padding=(dp(10), dp(5))  # Adjust padding as needed
        )

        # Add the message label to the message container
        self.ids.message_container.add_widget(message_label)

        # Clear the text input after sending the message
        self.ids.message_input.text = ""

        # prints to terminal, Useful for debugging
        print("Sent message:", message)

        # Handle response after sending the message
        self.handle_response()

    def handle_message(self, message):
        # Create a label for the received message
        received_message_label = MDLabel(
            text=message,
            size_hint=(None, None),
            size=(dp(200), dp(50)),  # Adjust size as needed
            pos_hint={'left': 1},
            valign='top',
            font_style='Body1',
            theme_text_color='Custom',
            text_color=(1, 1, 1, 1),  # White text color
            padding=(dp(10), dp(5))  # Adjust padding as needed
        )

        # Add the received message label to the message container
        self.ids.message_container.add_widget(received_message_label)

    def on_send(self):
        message = self.ids.message_input.text
        self.send_message(message)

    def handle_response(self):
        response = input("Enter response: ")
        self.handle_message(response)


