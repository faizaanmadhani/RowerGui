#Baseline code necessary for Adding Pages/Windows to a TKinter Application Using Python 3/3.4.1/3.6.0.
#import Modules and Dependencies
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

#Import tkinter
#Case t in tkinter, and change "from tkinter import ttk" to "import ttk" for Python 2/2.6.0/2.7.1 Optimization
import tkinter as tk
from tkinter import ttk

import urllib
import json

import numpy as np

#Graph Style (Refer to ttk module directories for different styles to use).
LARGE_FONT= ("Verdana", 12)
style.use("ggplot")

#Create Graph plot
f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

#Initialize real time animation function for Propulsive Force Graph
def animate(i):
    pullData = open("FpGraphData.txt","r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))

    a.clear()
    a.plot(xList, yList)

e = Figure(figsize=(5,5), dpi=100)
d = f.add_subplot(111)

#Initialize real time animation function for Efficiency Graph
# def animate(i):
#     pullData = open("EfGraphData.txt","r").read()
#     dataList = pullData.split('\n')
#     xList = []
#     yList = []
#     for eachLine in dataList:
#         if len(eachLine) > 1:
#             x, y = eachLine.split(',')
#             xList.append(int(x))
#             yList.append(int(y))
#
#     d.clear()
#     d.plot(xList, yList)

#Begin Pages Initialization
class MainActivity(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        #tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "RowerGUI")


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, FpGraph):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text=("""Alpha Application. Use at your own risk"""), font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Agree",
                            command=lambda: controller.show_frame(FpGraph))
        button1.pack()

        button2 = ttk.Button(self, text="Disagree",
                            command=quit)
        button2.pack()



class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()



#Force Propulsive Graph Page Initialization
class FpGraph(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Propulsive Force vs Time Graph!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        # button2 = ttk.Button(self, text="Efficiency Graph",
        #                     command=lambda: controller.show_frame(EfGraph))
        # button2.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

#Efficiency Time graph Page Initialization (CURRENTLY THROWS AN ERROR -- TO BE DEBUGGED)
# class EfGraph(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Efficiency vs Time Graph!", font=LARGE_FONT)
#         label.pack(pady=10,padx=10)
#
#         button1 = ttk.Button(self, text="Back to Home",
#                             command=lambda: controller.show_frame(StartPage))
#         button1.pack()
#
#         #Canvas Element where graph rests
#         canvas = FigureCanvasTkAgg(e, self)
#         canvas.show()
#         canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
#
#         toolbar = NavigationToolbar2TkAgg(canvas, self)
#         toolbar.update()
#         canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

#Run Event Loop
app = MainActivity()
#Initialization of animation function -- scans file every 1 second
ani = animation.FuncAnimation(f, animate, interval=1000)
#Execute main loop and initiate event driven async prorgram.
app.mainloop()
