from app_functions import *
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.graphics import Rectangle
from kivy.uix.label import Label


class Background(FloatLayout):
    def __init__(self, **kwargs):
        super(Background, self).__init__(**kwargs)
        layout = FloatLayout()
        with self.canvas:
            self.rect = Rectangle(source='background.jpg', pos=layout.pos, size=self.size)
        self.text = Label(text='Photo by <a href="https://unsplash.com/@anniespratt?utm_source=unsplash&utm_medium'
                               '=referral&utm_content=creditCopyText">Annie Spratt</a> on <a '
                               'href="https://unsplash.com/photos/Uk3t05ndSng?utm_source=unsplash&utm_medium=referral'
                               '&utm_content=creditCopyText">Unsplash</a>',
                          font_size=5, pos=(693, 3), color=(0, 0, 0), text_size=(2000, 600))

        myButton1 = Button(text="Load graph from file", font_name='Verdana.ttf', size_hint=(.5, .15), font_size=23,
                           pos_hint={'x': .25, 'y': .65}, background_color=(0.3, 0.6, 1, 1))
        myButton1.bind(on_press=self.callback1)

        myButton2 = Button(text="Save christofides graph to file", font_name='Verdana.ttf', size_hint=(.6, .15),
                           font_size=23, pos_hint={'x': .2, 'y': .45}, background_color=(0.3, 0.6, 1, 1))
        myButton2.bind(on_press=self.callback2)

        myButton3 = Button(text="End process", font_name='Verdana.ttf', font_size=23, size_hint=(.4, .15),
                           pos_hint={'x': .3, 'y': .25}, background_color=(0.3, 0.6, 1, 1))
        myButton3.bind(on_press=self.callback3)

        layout.add_widget(myButton1)
        layout.add_widget(myButton2)
        layout.add_widget(myButton3)
        layout.add_widget(self.text)
        self.add_widget(layout)

    def callback1(self, event):
        load_graph_from_file_coordinates("generate_graph_2.txt")

    def callback2(self, event):
        save_christo_graph_to_file(load_graph_from_file_coordinates("generate_graph_2.txt"), "example_out.txt")

    def callback3(self, event):
        end_app()

    def resize(self, *_):
        widgets = self.children[:]
        self.canvas.clear()
        self.clear_widgets()
        with self.canvas:
            self.rect = Rectangle(source='background.jpg', pos=self.pos, size=self.size)
        for widget in widgets:
            self.add_widget(widget)

    on_size = resize


class MyApp(App):

    def build(self):
        return Background()


root = MyApp()
root.run()

if __name__ == '__main__':
    MyApp().run()
