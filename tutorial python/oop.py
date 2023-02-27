from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen

class WindowManager(ScreenManager):
    pass

class Home(Screen):
    pass

class MyApp(MDApp):

    def build(self):

        # Create a list of all screen, loop through it and add it to the screenmanager
        # and return the screenmanager.
        self.wm = WindowManager()

        screens = [
            Home(name="home")
        ]

        for screen in screens:
            self.wm.add_widget(screen)

        return self.wm

if __name__=="__main__":
    MyApp().run()