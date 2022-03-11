import os
from pathlib import Path
from tkinter import *
from tkinter import filedialog
import downloaderBE as be

inp = ""
filepath = ""
canDownload = False

def checkForDownload():
    global inp, canDownload
    msgLabel = Label(root)
    inp = urlTextBox.get()
    canDownload = be.isDownloadable(inp)
    if (canDownload):
        displaytext = "Starting Download"
        be.startDownload(filepath)
    else:
        displaytext = "Unable to download. Please check the URL/Source, and try again!"
        flag = 1

    if msgLabel.winfo_exists:
        msgLabel.destroy
    msgLabel = Label(root,text = displaytext, font ='arial 15 bold', pady=20, bg="#4f3d40", foreground="#fff")
    msgLabel.pack(padx= 150, pady=(5,0), side= TOP, anchor="w")
    root.after(3000, msgLabel.destroy)

def startDownLoad():
    global urlTextBox
    if canDownload:
        be.startDownload(filepath)
        urlTextBox.delete(0,'end')
        msgLabel = Label(root,text = "Download Completed!", font ='arial 15 bold', pady=20, bg="#4f3d40", foreground="#fff")
        msgLabel.pack(padx= 150, pady=(5,0), side= TOP, anchor="w")
    else:
        checkForDownload()


def changeDirectory():
    global textEntry, filepath
    textEntry.set(filedialog.askdirectory())
    filepath = textEntry.get()


root = Tk()
root.geometry('1100x500')
root.resizable(0,0)
root.title("File Downloader")
root.config(bg="#4f3d40")

# UI for Heading
Label(root,text = 'An Easy File Downloader Application For You', font ='arial 20 bold', pady=20, bg="#4f3d40", foreground="#fff").pack()

# UI for Give Downloadable URL 
urlLabel = Label(root,text = 'Paste your download URL here:', font ='arial 12 bold', pady=10, bg="#4f3d40", foreground="#fff")
urlLabel.pack(padx= 150, pady=(5,0), side= TOP, anchor="w")

textEntry = StringVar()
urlTextBox = Entry(root,textvariable = textEntry, width=93)
urlTextBox.pack(padx= 150, side= TOP, anchor="w")


btnCheck = Button(root, text="Go", command=checkForDownload, bg="#fff", fg="#4f3d40", width=10)
btnCheck.pack(padx= 150,pady=(8,2) ,side= TOP, anchor="w")

#Get Path to downloads folder
path = os.path.join(os.path.expanduser('~'), 'downloads')

# UI for Change Directory
urlLabel = Label(root,text = 'Your File will download here:', font ='arial 12 bold', bg="#4f3d40", foreground="#fff")
urlLabel.pack(padx= 150, pady=(20,8), side= TOP, anchor="w")
textEntry = StringVar()
textEntry.set(path)
pathTextBox = Entry(root,textvariable = textEntry, width=93)
pathTextBox.configure(state='disabled')
pathTextBox.pack(padx= 150, side= TOP, anchor="w")

btnPathChange = Button(root, text="Change Directory", command=changeDirectory, bg="#fff", fg="#4f3d40")
btnPathChange.pack(padx= 150,pady=(8,2) ,side= TOP, anchor="w")

btnDownload = Button(root, text="Download My File", command=startDownLoad, bg="#fff", fg="#4f3d40")
btnDownload .pack(padx= 150,pady=(8,2) ,side= TOP, anchor="w")


root.mainloop()
print("Yayy ::: ", filepath)
