from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDIconButton, MDRaisedButton
from kivymd.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.toast import toast
from kivymd.uix.tab import MDTabsBase
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty



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


class Tab1(FloatLayout, MDTabsBase):
    pass


class Tab2(FloatLayout, MDTabsBase):
    pass

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()


class MainApp(MDApp):
    icons = "heart",
    data = {
        'heart': 'I KNOW I AM A BIT BEKAAR',
        'hand-heart': 'ON MESSAGING OFTEN BUT',
        'heart-circle-outline': ' I WANT U TO KNOW THAT',
        'emoticon-excited': 'I WILL ALWAYS BE THERE...',
        'heart-circle': 'THANK U FOR EVERYTHING',
        'emoticon-happy': 'U HAVE DONE',
        'heart-pulse': 'FOR ME',
    }

    def build(self):
        return

    def callback(self, instance):
        toast("HAPPY BIRTHDAY TO YOU MISHTI")
        pass


    def dialog(self):
        butt = MDRaisedButton(text="AB YAHAN CLICK KAR", on_release=self.dialog2,
                              pos_hint={'center_x': 0.5, 'center_y': 0.4})
        self.dialog10 = MDDialog(title='Mana Kara Tha Na',
                                 text=" Sun Liya Kar Baat "
                                      "Ab Neeche Click Kar"
                                 , size_hint=(0.7, 1), auto_dismiss='FALSE', buttons=[butt])

        self.dialog10.open()
        pass

    def dialog2(self, obj):
        self.dialog10.dismiss()
        pass

    def show_MDDialog(self):
        self.theme_cls.primary_palette = "Amber"
        button1 = MDRaisedButton(text=':)', font_size=(15), on_release=self.close_dialog,
                                 pos_hint={'center_x': 0.5, 'center_y': 0.4})
        button2 = MDRaisedButton(text='THANK YOU', font_size=(15), on_release=self.change_color,
                                 pos_hint={'center_x': 0.5, 'center_y': 0.4})
        button3 = MDIconButton(icon="close", user_font_size="23sp", on_release=self.close_dialog2,
                               pos_hint={'center_x': 0.5, 'center_y': 0.4})
        self.dialog = MDDialog(title='HAPPY BIRTHDAY BRUHHHHHHH',
                               text="IT HAS BEEN AN AWESOME"
                                    " JOURNEY AND "
                                    "WILL ALWAYS BE ONE"
                                    " THANK YOU FOR "
                                    "ALWAYS BEING "
                                    "THERE FOR ME", size_hint=(0.9, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5},
                               auto_dismiss='FALSE',
                               buttons=[button3, button1, button2])

        self.dialog.open()
        pass

    def call(self):
        toast('HAPPY BIRTHDAY BROOO')
        pass

    def close_dialog(self, obj):
        toast('HAPPY BIRTHDAY')
        pass

    def close_dialog2(self, obj):
        self.dialog.dismiss()
        self.theme_cls.primary_palette = "DeepOrange"
        self.theme_cls.primary_hue="A200"
        pass

    def change_color(self, obj):
        self.theme_cls.primary_palette = "Blue"
        toast('CHL NA BAE')
        pass







MainApp().run()
