import Tkinter as tk

class mainActivity(tk.Tk):

    def__init__(self, *args, **kwargs):

    tk.Tk.__init__(self, *args, **kwargs)
    container = tk.Frame(self)

    container.pack(side="top", fill="both", expand=True)

    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    self.frames = ()

    frame = StartPage(container, self)






