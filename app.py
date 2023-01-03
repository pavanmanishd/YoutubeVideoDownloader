from pytube import YouTube
from tkinter import *
from tkinter import ttk

def download():
    global entry
    #Get the link from entry
    videoLink= entry.get()
    video = YouTube(videoLink)
    video = video.streams.get_highest_resolution()
    try:
        video.download()
    except:
        label.configure(text="There has been an error in downloading!")
    label.configure(text="Download is Completed.")


win= Tk()

#Set the geometry of Tkinter frame
win.geometry("750x250")

#Initialize a Label to display the User Input
label=Label(win, text="Enter Video Link Here", width=100,font=("Georgia"),height=2)
label.pack()

#Create an Entry widget to accept User Input
entry= Entry(win, width= 40,font='Arial 15')
entry.focus_set()
entry.pack(padx=10,pady=5)

#Create a Button to validate Entry Widget
ttk.Button(win, text= "Download",width= 30, command= download).pack(padx=10,pady=30)

win.mainloop()