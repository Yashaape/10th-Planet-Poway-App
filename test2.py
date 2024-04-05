from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.uix.label import Label

KV = '''
<ChatScreen>:
    name: 'chat_screen'

    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            title: 'Chat'
            left_action_items: [["arrow-left", lambda x: app.change_screen('main')]]

        ScrollView:
            MDList:
                id: chat_messages

        BoxLayout:
            padding: '10dp'
            spacing: '10dp'

            MDTextField:
                id: message_input
                hint_text: 'Type your message'
                mode: 'fill'

            MDIconButton:
                icon: 'send'
                on_release: app.send_message(message_input.text)
'''

Builder.load_string(KV)


class ChatScreen(MDScreen):
    pass

class MyApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        # Create instances of screens
        self.main_screen = Label(text="This is the main screen")
        self.chat_screen = ChatScreen()

        # Add screens to the screen manager
        self.screen_manager.add_widget(self.main_screen)
        self.screen_manager.add_widget(self.chat_screen)

        return self.screen_manager

    def change_screen(self, screen_name):
        self.screen_manager.current = screen_name

    def send_message(self, message):
        # Code to send the message and update the UI
        # You need to implement this according to your requirements
        print("Sending message:", message)


if __name__ == '__main__':
    MyApp().run()
