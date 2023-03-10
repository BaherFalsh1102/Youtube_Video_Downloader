# (1) import the required modules
# ------------------------------
# Tkinter is a standard GUI library
# pytube used for downloading videos from youTube

from tkinter import *
from pytube import YouTube

# (2) Create Display Window
# ------------------------------
# Create display window
# Tk() used to initialize tkinter to create display window
# geometry() used to set the window’s width and height
# resizable(0,0) set the fix size of window
# title() used to give the title of window
# Label() widget use to display text that users can’t able to modify.
# root is the name of the window
# text which we display the title of the label
# font in which our text is written
# pack organized widget in block

root = Tk()
root.geometry('500x300')
root.configure(bg="#202033")
root.resizable(0,0)
root.title(" B-Sigma | youtube video downloader ")

Label(root,
      text  = 'Youtube Video Downloader',
      font  = 'arial 20 bold'
      ).pack()

# (3) Create Field to Enter Link
# ------------------------------
# link is a string type variable that stores the youtube video link that the user enters.
link = StringVar()

Label(root,
      text  = 'Paste Link Here:',
      font  = 'arial 15 bold'
      ).place(x= 160 , y = 60)

# Entry() widget is used when we want to create an input text field.
# textvariable used to retrieve the value of current text variable to the entry widget.
# place() use to place the widget at a specific position

link_enter = Entry(root,
                   width = 70,
                   textvariable = link
                   ).place(x = 32, y = 100)

# (4) Create Function to Start Downloading
# ------------------------------
def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root,
          text = 'DOWNLOADED',
          font = 'arial 15'
          ).place(x= 180 , y = 160)

# bg sets the background color
# command is used to call the function

Button(root,
       text = 'DOWNLOAD',
       font = 'arial 15 bold',
       bg = 'pale violet red',
       padx = 2,
       command = Downloader
       ).place(x=185 ,y = 230)

root.mainloop()

