# Author: Randall Jackson
# Python 3.9.5
# Tested in Win 10
#
#
# Purpose: Create an HTML page and allows the user to update the body under
# the header with anything they want to add to the body. 

from tkinter import *
import tkinter as tk
import webbrowser

#Python File Write. Creates the webpage if user does not have it, and opens it when
# the script is run
f = open("python-site1.html", "w")
f.write("""<html>\
               <body>\
                   <h1>Stay tuned for our amazing summer sale!</h1>
               </body>
           </html>""")

url = "python-site1.html"
f= open(url)
webbrowser.open_new_tab(url)

def loadGui(self):
    self.txt_body = tk.Entry(self.master,text='')
    self.txt_body.grid(row=1, column=0,columnspan=2,padx=(10,0),pady=(20,10),sticky=W)
    self.btn_changeBody = tk.Button(self.master,width=10,height=1,text="Update Body...",command=lambda: appendSite(self))
    self.btn_changeBody.grid(row=1,column=3,padx=(5,0),pady=(20,10),sticky=W)

def center_window(self, w, h): # pass in the tikinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

# Frame is the Tkinter frame class that this class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(300,200) #(Height,width)
        self.master.maxsize(300,200)

        center_window(self, 300,200)
        self.master.title('Update Body')
        self.master.configure(bg="#F0F0F0")
        loadGui(self)

def appendSite(self):
    # First we need to get what the user inputs into the txt field.
    body = self.txt_body.get()
    f = open("python-site1.html", "w")
    f.write("""<html>\
               <body>\
                   <h1>Stay tuned for our amazing summer sale!</h1>
                   {}
               </body>
           </html>""".format(body))
    url = "python-site1.html"
    f= open(url)
    webbrowser.open_new_tab(url)
    


    

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()



