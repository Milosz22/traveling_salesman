from tkinter import *
from app_functions import *

root = Tk()

#buttons
myButton1 = Button(root, text="Load graph from file", padx=50, pady=50, font=50, command=load_graph_from_file(
    "example_in.txt"))
myButton2 = Button(root, text="Save christofides graph to file", padx=50, pady=50, font=50,
                   command=save_christo_graph_to_file(load_graph_from_file("example_in.txt"),
                                                      "example_out.txt"))
myButton3 = Button(root, text="End process", padx=50, pady=50, font=50, command=end_app)
myButton1.grid(row=1)
myButton2.grid(row=2)
myButton3.grid(row=3)

root.mainloop()
