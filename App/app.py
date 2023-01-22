import time
from functools import partial
from kivy.clock import Clock

from app_functions import *
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.graphics import Rectangle
from kivy.uix.label import Label
from threading import Thread

G = graph(load_graph_from_file_coordinates("generate_graph_2.txt"), coordinates=1)

def time_it(Gr):
    start = time.time()
    christofides(Gr)
    end = time.time()
    return end - start


sec = time_it(G) * 2.5


class Background(FloatLayout):
    def __init__(self, **kwargs):
        super(Background, self).__init__(**kwargs)
        layout = FloatLayout()
        with self.canvas:
            self.rect = Rectangle(source="background.jpg", pos=layout.pos, size=self.size)
        self.text = Label(text='Photo by <a href="https://unsplash.com/@anniespratt?utm_source=unsplash&utm_medium'
                               '=referral&utm_content=creditCopyText">Annie Spratt</a> on <a '
                               'href="https://unsplash.com/photos/Uk3t05ndSng?utm_source=unsplash&utm_medium=referral'
                               '&utm_content=creditCopyText">Unsplash</a>',
                          font_size=5, pos=(693, 3), color=(0, 0, 0), text_size=(2000, 600))

        self.myButton1 = Button(text="Load Map", font_name='Verdana.ttf', size_hint=(.4, .15), font_size=23,
                                pos_hint={'x': .3, 'y': .65+0.05}, background_color=(0.3, 0.6, 1, 1))
        self.myButton1.bind(on_press=self.callback1)

        self.myButton2 = Button(text="View Route", font_name='Verdana.ttf', size_hint=(.4, .15),
                                font_size=23, pos_hint={'x': .3, 'y': .25+0.05}, background_color=(0.3, 0.6, 1, 1))
        self.myButton2.bind(on_press=self.callback2)

        self.myButton3 = Button(text="Exit", font_name='Verdana.ttf', font_size=23, size_hint=(.4, .15),
                                pos_hint={'x': .3, 'y': .05+0.05}, background_color=(0.3, 0.6, 1, 1))
        self.myButton3.bind(on_press=self.callback3)

        self.myButton4 = Button(text="Find Route", font_name='Verdana.ttf', font_size=23, size_hint=(.4, .15),
                                pos_hint={'x': .3, 'y': .45+0.05}, background_color=(0.3, 0.6, 1, 1))
        self.myButton4.bind(on_press=self.callback4)

        layout.add_widget(self.myButton1)
        layout.add_widget(self.myButton2)
        layout.add_widget(self.myButton3)
        layout.add_widget(self.myButton4)
        layout.add_widget(self.text)
        self.add_widget(layout)

    def callback1(self, event):
        self.myButton1.disabled = True
        self.myButton2.disabled = True
        self.myButton3.disabled = True
        thread = Thread(target=load_graph_from_file_coordinates, args=("generate_graph_2.txt",))
        thread.start()

        Clock.schedule_once(partial(self.disable, thread), sec)

    def disable(self, thread, what):
        if not thread.is_alive():
            self.myButton1.disabled = False
            self.myButton2.disabled = False
            self.myButton3.disabled = False
            return False

    def callback2(self, event):
        draw_graph()


    def callback3(self, event):
        end_app()

    def callback4(self, event):
        load_client_vertices_and_save_to_file("adress.txt")

    def resize(self, *_):
        widgets = self.children[:]
        self.canvas.clear()
        self.clear_widgets()
        with self.canvas:
            self.rect = Rectangle(source="background.jpg", pos=self.pos, size=self.size)
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
