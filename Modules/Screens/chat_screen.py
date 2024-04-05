from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

KV = '''
<ChatScreen>:
    name: 'chat_screen'

    BoxLayout:
        orientation: 'vertical'
        
        BoxLayout:
            padding: '10dp'
            spacing: '10dp'

            MDTextField:
                id: message_input
                hint_text: 'Type your message'
                mode: 'fill'

            MDIconButton:
                icon: 'send'
                on_press: root.send_message(message_input.text)

'''

Builder.load_string(KV)


class ChatScreen(MDScreen):

    def send_message(self, message):
        # Code to send the message and update the UI
        # You need to implement this according to your requirements
        print("Sending message:", message)
