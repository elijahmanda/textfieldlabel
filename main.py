from kivymd.app import MDApp
from kivy.lang import Builder

kv = '''
#:import toast kivymd.toast.toast
MDBoxLayout : 
    id : box
    orientation : 'vertical'
    padding : '20dp'
    spacing : '20dp'

    MDLabel :
        text : 'Enter some text'
        halign : 'center'
        font_size : 100
    MDTextField :
        id : field
        hint_text : 'enter some text'
        color_active : [0,1,0,1]
        font_size : 30
        size_hint_x : None
        width : box.width - 10
        pos_hint : {'center_x': .5}
    MDRoundFlatButton :
        text : 'See your inputted text'
        md_bg_color : [0,0,1,1]
        on_release : toast(field.text)
        size_hint : None, None
        height : '100dp'
        width : box.width - 10
        pos_hint : {'center_x': .5}
    Widget :
'''

class TextFieldLabel(MDApp):
    def build(self):
        return Builder.load_string(kv)

TextFieldLabel().run()