from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivy.properties import ObjectProperty
from kivy.metrics import dp
from kivy.clock import Clock


KV = '''
<ChatScreen>:
    name: 'chat_screen'
    
    MDBoxLayout:
        orientation: 'vertical'  # Orientation of the layout ('horizontal' or 'vertical')
        spacing: '10dp'  # Spacing between children widgets
        padding: '20dp'  # Padding around the layout
        size_hint: (1, 0.8)  # Make the first MDBoxLayout take up 90% of the screen's height
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}  # Center the MDBoxLayout horizontally
        
        ScrollView:
            padding: dp(20)
            size_hint_y: None
            height: self.parent.height - 40  # Adjust the height to fit the parent MDBoxLayout
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
        # Schedule the handle_response method to be called after a delay
        Clock.schedule_once(self.handle_response, 0.1)

    def handle_response(self, dt):
        response = input("Enter response: ")
        self.handle_message(response)


class AllLevelsScreen(ChatScreen):
    pass


class YouthAges4to8Screen(ChatScreen):
    pass


class YouthAges9to15Screen(ChatScreen):
    pass


class AdultFundamentalsScreen(ChatScreen):
    pass
