import os
from tkinter import *
from tkinter import filedialog
import downloaderBE as be

inp = ""
filepath = ""
canDownload = False

#This method sends the URL to isDownloadable method in downloaderBE 
# and display the message according to the response returned from the method.
#Invoked when Go button is pressed.
def checkForDownload():
    global inp, canDownload
    deleteLastLabel()
    inp = urlTextBox.get()
    msgLabel = Label(root,text = "Checking if downloadable", font ='arial 15 bold', pady=20, bg="#4f3d40", foreground="#fff")
    msgLabel.pack(padx= 150, pady=(5,0), side= TOP, anchor="w")
    root.update()
    canDownload = be.isDownloadable(inp)
    msgLabel.destroy()
    if (canDownload):
        startDownLoad()
    else:
        msgLabel = Label(root,text = "Unable to download. Please check the URL/Source, and try again!", font ='arial 15 bold', pady=20, bg="#4f3d40", foreground="#fff")
        msgLabel.pack(padx= 150, pady=(5,0), side= TOP, anchor="w")

#This method sends the directory path to downloadeFile method in downloaderBE 
#Since it can be directly invoked by download button, thus it checks first if it is
# downloadable file or not and thus displays the message of download being in progress or completed.
def startDownLoad():
    global urlTextBox
    deleteLastLabel()
    if canDownload:
        downloadLabel = Label(root,text = "Download In Progress...", font ='arial 15 bold', pady=20, bg="#4f3d40", foreground="#fff")
        downloadLabel.pack(padx= 150, pady=(5,0), side= TOP, anchor="w")
        root.update()
        be.downloadFile(filepath)
        urlTextBox.delete(0,'end')
        downloadLabel.destroy()
        downloadLabel = Label(root,text = "Download Completed!", font ='arial 15 bold', pady=20, bg="#4f3d40", foreground="#fff")
        downloadLabel.pack(padx= 150, pady=(5,0), side= TOP, anchor="w")
    else:
        checkForDownload()

#This method deleted the last download status when Download/Go button is clicked again.
def deleteLastLabel():
    for label in root.winfo_children():
        if type(label) == Label :
            text = label["text"] 
            if text == "Download Completed!" or "Unable to download" in text:
                label.destroy()

#This method helps the user to choose a new directory when Chage directory button is clicked.
def changeDirectory():
    global textEntry, filepath
    textEntry.set(filedialog.askdirectory())
    filepath = textEntry.get()

#MAIN BODY
root = Tk()
root.geometry('1000x500')
root.resizable(0,0)
root.title("File Downloader")
root.config(bg="#4f3d40")

# UI for Heading
Label(root,text = 'An Easy File Downloader Application For You', font ='arial 20 bold', pady=20, bg="#4f3d40", foreground="#fff").pack()

# UI for Give Downloadable URL
# Label 
urlLabel = Label(root,text = 'Paste your download URL here:', font ='arial 12 bold', pady=10, bg="#4f3d40", foreground="#fff")
urlLabel.pack(padx= 150, pady=(5,0), side= TOP, anchor="w")

#Entry/Textbox to fill in URL
textEntry = StringVar()
urlTextBox = Entry(root,textvariable = textEntry, width=93)
urlTextBox.pack(padx= 150, side= TOP, anchor="w")

#Go Button
btnCheck = Button(root, text="Go", command=checkForDownload, bg="#fff", fg="#4f3d40", width=10)
btnCheck.pack(padx= 150,pady=(8,2) ,side= TOP, anchor="w")

#Get Path to downloads folder
path = os.path.join(os.path.expanduser('~'), 'downloads')

# UI for Change Directory
#Label
urlLabel = Label(root,text = 'Your File will download here:', font ='arial 12 bold', bg="#4f3d40", foreground="#fff")
urlLabel.pack(padx= 150, pady=(20,8), side= TOP, anchor="w")

#Entry/Textbox to display chosen path 
textEntry = StringVar()
textEntry.set(path)
pathTextBox = Entry(root,textvariable = textEntry, width=93)
pathTextBox.configure(state='disabled')
pathTextBox.pack(padx= 150, side= TOP, anchor="w")

#Change directory Button
btnPathChange = Button(root, text="Change Directory", command=changeDirectory, bg="#fff", fg="#4f3d40")
btnPathChange.pack(padx= 150,pady=(8,2) ,side= TOP, anchor="w")

#Download Button
btnDownload = Button(root, text="Download My File", command=startDownLoad, bg="#fff", fg="#4f3d40")
btnDownload .pack(padx= 150,pady=(8,2) ,side= TOP, anchor="w")

root.mainloop()
