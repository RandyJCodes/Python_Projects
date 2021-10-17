# Author: Randall Jackson
# Python 3.9.5
# Tested in Windows 10 
#
# Purpose: A program that can transfer files
# from one folder, to another based on last modified date. 
from tkinter import *
import tkinter as tk
import shutil
import os
import time

import File_Transfer_gui
import File_Transfer_func

# Frame is the Tkinter frame class that this class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(300,200) #(Height,width)
        self.master.maxsize(300,200)

        File_Transfer_func.center_window(self, 300,200)
        self.master.title('File Transfer')
        self.master.configure(bg="#F0F0F0")
        File_Transfer_gui.loadGui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

    
    
