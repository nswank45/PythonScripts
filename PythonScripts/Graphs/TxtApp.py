import kivy   
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


kivy.require("1.10.1")


class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 2 

        self.add_widget(Label(text='IP:'))  # widget #1, top left
        self.ip = TextInput(multiline=False)  # defining self.ip...
        self.add_widget(self.ip) # widget #2, top right

        self.add_widget(Label(text='Port:'))
        self.port = TextInput(multiline=False)
        self.add_widget(self.port)

        self.add_widget(Label(text='Username:'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.join = Button(text="Join")   
        self.add_widget(Label())  # just take up the spot.
        self.add_widget(self.join)
        


class BowlingApp(App):

    def build(self):
        return ConnectPage()

if __name__== "__main__":
    BowlingApp().run()