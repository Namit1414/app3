from kivy.utils import get_color_from_hex
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDIconButton, MDRaisedButton
from kivy.lang import Builder
from Helpers import KV
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.toast import toast
from kivy.core.window import Window


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class ThirdWindow(Screen):
    pass


class FourthWindow(Screen):
    pass


class FifthWindow(Screen):
    pass


class sixthWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class MainApp(MDApp):
    def build(self):
        #Window.clearcolor = (0, 0, 0, 1)
        # self.theme_cls.primary_palette = "Blue"
        # self.theme_cls.theme_style = 'Dark'
        return
    def dialog(self):
        butt= MDRaisedButton(text="AB YAHAN CLICK KAR",on_release=self.dialog2)
        self.dialog10 = MDDialog(title='Mana Kara Tha Na',
                               text=" Sun Liya Kar Baat "
                                    "Ab Neeche Click Kar"
                                    " Aur Iss Baar Sirf Upar Wale Cake Ko Touch Kariyo"
                               , size_hint=(0.7, 1), auto_dismiss='FALSE',buttons=[butt])

        self.dialog10.open()
        pass
    def dialog2(self, obj):
        self.dialog10.dismiss()
        pass


    def show_MDDialog(self):
        self.theme_cls.primary_palette = "Amber"
        button1 = MDRaisedButton(text='ORANGE', font_size=(15), on_release=self.close_dialog)
        button2 = MDRaisedButton(text='THANK YOU', font_size=(15), on_release=self.change_color)
        button3 = MDIconButton(icon="close", user_font_size="23sp", on_release=self.close_dialog2)
        self.dialog = MDDialog(title='HAPPY BIRTHDAY BRUHHHHHHH',
                               text="IT HAS BEEN AN AWESOME "
                                    "JOURNEY AND WILL ALWAYS BE ONE"
                                    " THANK YOU FOR ALWAYS BEING THERE FOR ME"
                               , size_hint=(0.7, 1), auto_dismiss='FALSE',
                               buttons=[button3, button1, button2])

        self.dialog.open()

    def close_dialog(self, obj):
        toast('Close card')
        pass

    def close_dialog2(self, obj):
        self.dialog.dismiss()
        pass

    def change_color(self, obj):
        self.theme_cls.primary_palette = "Blue"


MainApp().run()
