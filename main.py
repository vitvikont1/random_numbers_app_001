from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import random


class LoginScreen(GridLayout):
    """Test kivy App"""
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 1
        self.padding = [200]
        self.spacing = [10, 10]
        self.lbl = Label(text='Info')
        self.add_widget(self.lbl)
        self.btn = Button(text='Click',
                          on_press=self.btn_press)
        self.add_widget(self.btn)

    def btn_press(self, instance):
        self.update_label()
        instance.text = "On press"

    def update_label(self):
        self.lbl.text = str(random.randint(1, 100))


class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()
