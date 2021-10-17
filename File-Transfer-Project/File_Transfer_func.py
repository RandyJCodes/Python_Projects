# Function Scripts for the File transfer Project

import os
from tkinter import filedialog
from tkinter import *
import tkinter as tk
import time
import shutil

import File_Transfer_main
import File_Transfer_gui

def center_window(self, w, h): # pass in the tikinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

#User will set where the source files are
def addFolderSrc(self):
   folderpath = tk.filedialog.askdirectory()
   self.txt_src.insert(END,folderpath)
   
   
#user will set destination path
def addFolderDst(self):
   folderpath = tk.filedialog.askdirectory()
   self.txt_dst.insert(END,folderpath)
   
        



def fileCheck(self):
    #Set Variables to be passed into the fileCheck Function
    #Seconds is = to the number of seconds in 24 hours
    seconds = 24 * 60 * 60
    # variables for now and the past 24 hours
    now = time.time()
    before = now - seconds
    source = self.txt_src.get()
    destination = self.txt_dst.get()
    for filename in os.listdir(source):
        source_filename = os.path.join(source,filename)
        modtime = os.path.getmtime(source_filename)
        if modtime > before:
            destination_filename = os.path.join(destination,filename)
            shutil.move(source_filename, destination_filename)
    
    


if __name__ == "__main__":
    pass
