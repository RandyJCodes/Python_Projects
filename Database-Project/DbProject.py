#
# Python: 3.9.5
#
# Author: Randall Jackson
#
#
# Purpose: First Db I have built in Python using sqlite3.
# The goal of this project is to create a db and insert files into
# it with different file extensions. It will then pull the files that
# have '.txt' file extensions and display them in IDLE shell.



import sqlite3
import os

conn = sqlite3.connect('No1.db') #Creates a db named 'No1.db'/ connects to it if it has already been made.
fileList = ('information.docx', 'Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')


with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txt( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_txtdocs TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('No1.db')

with conn:
    for fName in fileList:
        if fName.endswith(".txt") is True: #If the fname is a .txt file type, add it to the db and print it. 
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_txt(col_txtdocs) VALUES(?)", (fName,))
            print(fName)
    conn.commit()
conn.close()
        
        



