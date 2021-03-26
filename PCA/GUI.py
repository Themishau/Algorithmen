# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
from analyze import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import asyncio
import threading


class Model:
    def __init__(self):
        self.data = None
        self.plot_data = None

        self.input_path = None
        self.output_path = None


    def dataLoadedAndAvailable(self):
        if (self.data == None):
            return False
        else:
            return True

    #import the data into the data framework
    async def prepare_data(self):
        self.plot_data = await preprare_data(self.data)

    #reads the files
    async def read_data(self):
        if (self.input_path == None):
            messagebox.showerror( 'Error', 'no path!')
            return
        self.data = await readData(self.input_path)

    #gets the data out of the files


    async def start(self):
        await self.read_data()
        await self.prepare_data()


class Controller():
    def __init__(self):

        #init tk
        self.root = tk.Tk()

        #init window size
        self.root.geometry("500x650+200+200")
        self.root.resizable(0, 0)
        #counts running threads
        self.runningAsync = 0

        #init model and viewer
        self.model = Model()
        self.view = View(self.root)

        self.view.main.mainStartButton.bind("<Button>", self.start)
        self.view.main.quitButton.bind("<Button>", self.closeprogram)

    def run(self):
        self.root.title("show plot")
        #sets the window in focus
        self.root.deiconify()
        self.root.mainloop()

    def start(self, event):
        try:
            self.model.input_path = self.view.main.input_path.get()
        except:
            messagebox.showerror( 'Error', 'no input path')
            return

        try:
            self.model.output_path = self.view.main.output_path.get()
        except:
            messagebox.showerror( 'Error', 'no output path')
            return

        self.do_tasks()

    def closeprogram(self, event):
        self.root.destroy()

    def closeprogrammenu(self):
        self.root.destroy()

    def do_tasks(self):
        """ Function/Button starting the asyncio part. """
        threading.Thread(target= self.async_load_data, args=()).start()

    def async_load_data(self):
        loop = asyncio.new_event_loop()
        self.runningAsync = self.runningAsync + 1
        loop.run_until_complete(self.model.start())
        loop.close()
        self.runningAsync = self.runningAsync - 1
        #create plot
        self.createplot(self.model.plot_data['lines'].to_list(),self.model.plot_data['iParseBlockStatementsOpen'].to_list())

    def createplot(self, datax, datay):
        fig = plt.figure()
        ax = fig.add_subplot(111)

        ax.plot(datax, datay)
        fig.savefig(self.model.output_path + 'dfdataPLOT.png')
        #plt.ylabel('some numbers')
        #plt.show()

        self.model.plot_data.to_csv( self.model.output_path + 'dfdataSORTED.csv', header=True, quotechar=' ', index=True, sep=';', mode='a', encoding='utf8')
        #self.view.plt.plot([1, 2, 3, 4])
        #self.view.plt.ylabel('some numbers')
        #self.view.plt.show()



class Main(tk.Frame):
    def __init__(self, root, **kw):

        super().__init__(**kw)
        self.mainFrame = tk.Frame(root)
        self.mainFrame.grid(sticky="NSEW")

        #textfield
        self.input = tk.Label(self.mainFrame, text="Enter input path ")
        self.input.grid(row = 0, column = 0, sticky = tk.N, pady = 2, columnspan = 4)

        #entry
        self.input_path = tk.Entry(self.mainFrame, width=80)
        self.input_path.insert(0, 'E:/OneDrive/1_Daten_Dokumente_Backup/1_Laptop_Backup_PC/Programmieren_Python/algorithmn/Algorithmen/PCA Hauptkomponentenanalyse/input.txt')
        self.input_path.grid(row = 1, column = 0, sticky = tk.N, pady = 2, columnspan = 4)

        #textfield
        self.output = tk.Label(self.mainFrame, text="Enter outputpath")
        self.output.grid(row = 2, column = 0, sticky = tk.N, pady = 2, columnspan = 4)

        #entry
        self.output_path = tk.Entry(self.mainFrame, width=80)
        self.output_path.insert(0,'E:/OneDrive/1_Daten_Dokumente_Backup/1_Laptop_Backup_PC/Programmieren_Python/algorithmn/Algorithmen/PCA Hauptkomponentenanalyse/')
        self.output_path.grid(row = 3, column = 0, sticky = tk.N, pady = 2, columnspan = 4)

        #button quit
        self.quitButton = tk.Button(self.mainFrame, text="Quit", width=30, borderwidth=5, bg='#FBD975')
        self.quitButton.grid(row = 7, column = 2, sticky = tk.N, pady = 0)

        #button start
        self.mainStartButton = tk.Button(self.mainFrame, text="Start", width=30, borderwidth=5, bg='#FBD975')
        self.mainStartButton.grid(row = 7, column = 1, sticky = tk.N, pady = 0)



class View():
    def __init__(self, parent):
        self.plt = Figure(figsize=(5, 5), dpi=100)
        self.plt.add_subplot(111).plot([0,1, 2, 3, 4],[0,1,20,3,50])
        self.frame = tk.Frame(parent)
        self.frame.grid(sticky="NSEW")
        self.main = Main(parent)

        self.canvas = FigureCanvasTkAgg(self.plt, master=self.frame)
        self.canvas.get_tk_widget().grid(row = 3, column = 0, sticky = tk.N, pady = 2, columnspan = 4)
        self.canvas.draw()