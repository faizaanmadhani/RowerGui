#Baseline code necessary for Adding Pages/Windows to a TKinter Application Using Python.

import Tkinter as tk
from Tkinter import ttk

LARGE_FONT = ("Verdana", 12)

#Build Container for GUI
class mainActivity(tk.Tk):

    def __init__(self, *args, **kwargs):


        #Top Left Corner icon and text input and styling. Lines 14-18
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self.default= #insert .ico icon here)
        tk.Tk.wm_title(self, "Rower Application")

        #initialize container
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

    self.frames = {}

    for F in (StartPage, PageOne):

    frame = F(container, self)

    self.frames[F] = frame

    #Initialize Grid/Cell Size. Sticky parameter defines north-south-east-west (u-d-l-r)
    frame.grid(row = 0, column = 0, sticky = "nsew")

    self.show_frame(StartPage)

    def show_frame(self, cont) :

        frame = self.frames[cont]
        frame.tkraise()

#Change this function to manipulate execution when page changes
def qf(param):
    print(param)

#Add an initial Page
class StartPage(tk.Frame) :

    def __init__(self, parent, controller) :
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Start Page", font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        #Add Button to allow user to move to seperate Page
        button1 = ttk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show__frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self, text="Visit Page 2",
                                command=lambda: controller.show__frame(PageTwo))
        button2.pack()


#Add another page
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    label = tk.Label(self, text = "Page One", font = LARGE_FONT)
    label.pack(pady=10,padx=10)

    button1 = ttk.Button(self, text="Back to Home",
                        command=lambda: controller.show__frame(StartPage))
    button1.pack()

    button2 = ttk.Button(self, text="Visit Page 2",
                        command=lambda: controller.show__frame(PageTwo))
    button2.pack()

class PageTwo(tk.Frame) :

    def __init__(self, parent, controller) :
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Start Page", font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        #Add Button to allow user to move to seperate Page
        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show__frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page One",
                                command=lambda: controller.show__frame(PageOne))
        button2.pack()



app = mainActivity()
app.mainloop()
