# GUI for File Transfer Project
from tkinter import *
import tkinter as tk

import File_Transfer_main
import File_Transfer_func

#Gui will have a 2 browse buttons for searching for source and destination folders
def loadGui(self):
    self.btn_browsesrc = tk.Button(self.master,width=10,height=2,text='Browse...',command=lambda: File_Transfer_func.addFolderSrc(self))
    self.btn_browsesrc.grid(row=0,column=0,padx=(5,0),pady=(20,10),sticky=W)
    self.btn_browsedst = tk.Button(self.master,width=12,height=2,text='Browse...',command=lambda: File_Transfer_func.addFolderDst(self))
    self.btn_browsedst.grid(row=1,column=0,padx=(5,0),pady=(20,10),sticky=W)
    self.btn_fchck = tk.Button(self.master,width=12,height=2,text='File Check',command=lambda: File_Transfer_func.fileCheck(self))
    self.btn_fchck.grid (row=2,column=0,padx=(5,0),pady=(20,10),sticky=W)

    self.txt_src = tk.Entry(self.master,text='')
    self.txt_src.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_dst = tk.Entry(self.master,text='')
    self.txt_dst.grid(row=2,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)



if __name__ == "__main__":
    pass
