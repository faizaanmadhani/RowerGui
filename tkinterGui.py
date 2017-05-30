#Baseline code necessary for Adding Pages/Windows to a TKinter Application Using Python 3/3.4.1/3.6.0.
#import Modules and Dependencies
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

#Import tkinter
#Case t in tkinter, and change "from tkinter import ttk" to "import ttk" for Python 2/2.6.0/2.7.1 Optimization
import Tkinter as tk
import ttk
LARGE_FONT=("Verdana", 12)
style.use("ggplot")

#Create Graph plot
f= Figure()
canvas = FigureCanvas(f)
a = f.add_subplot(1, 1, 1)


#Initialize real time animation function for Propulsive Force Graph
def animate(i):
    pullData = open("FpGraphData","r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))
    a.clear()
    a.plot(xList,yList)

#Initialize Main Activity for GUI
#Build Container for GUI
class mainActivity (tk.Tk):
    def _init_(self,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

#Initialize Icon. Insert ico file in here soon
        tk.Tk.iconbitmap(self, default="icon.ico")
        tk.Tk.wm_title(self, "Main GUI")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column = 0, sticky="nsew")
        self.show_frame(StartPage)


    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
def qf():
    print("Main Page Here")

#Begin Pages Initialization
# class StartPage(tk.Frame):
#     def _init_(self, parent, controller):
#         tk.Frame.__init__(self,parent)
#         label = tk.Label(self, text="Start Page", font=LARGE_FONT)
#         label.pack(pady=10, padx=10)
#
#         button = ttk.Button(self, text="Visit Page 1", command=lambda :controller.show_frame(PageOne))
#         button.pack()
#         buttona = ttk.Button(self, text="Visit Page 2", command=lambda :controller.show_frame(PageTwo))
#         buttona.pack()
#         buttonb = ttk.Button(self, text="Visit Graph Page", command=lambda :controller.show_frame(PageThree))
#         buttonb.pack()
# class PageOne(tk.Frame):
#     def _init_(self, parent, controller):
#         tk.Frame.__init__(self,parent)
#         label = tk.Label(self, text="Page One", font=LARGE_FONT)
#         label.pack(pady=10, padx=10)
#
#         button1 = ttk.Button(self, text="Back to Home", command=lambda :controller.show_frame(StartPage))
#         button1.pack()
#
# class PageTwo(tk.Frame):
#     def _init_(self, parent, controller):
#         tk.Frame.__init__(self,parent)
#         label = tk.Label(self, text="Page Two", font=LARGE_FONT)
#         label.pack(pady=10, padx=10)
#
#         button1 = ttk.Button(self, text="Back to Home", command=lambda :controller.show_frame(StartPage))
#         button1.pack()


class PageThree(tk.Frame):
    def _init_(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Graph Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home", command=lambda :controller.show_frame(StartPage))
        button1.pack()

        #Canvas where Graph Rests
        f.set_canvas
        canvas = FigureCanvasTkAgg(f,self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

#Run Event Loop
app= mainActivity()
ani = animation.FuncAnimation(f,animate, interval=1000)
app.mainloop()
