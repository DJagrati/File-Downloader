from tkinter import *
from tkinter import ttk

inp = ""
def retrieve_input():
    global inp
    inp = urlTextBox.get("1.0","end-1c")
    if inp == 'Jagrati':
        msgLabel = Label(root,text = 'Jagssss!!!', font ='arial 20 bold', pady=20, bg="#4f3d40", foreground="#fff")
    else:
        msgLabel = Label(root,text = 'Armaannnn!!!!', font ='arial 20 bold', pady=20, bg="#4f3d40", foreground="#fff")
    msgLabel.pack()

root = Tk()

root.geometry('900x500')
root.resizable(0,0)
root.title("File Downloader")
root.config(bg="#4f3d40")

Label(root,text = 'An Easy File Downloader Application For You', font ='arial 20 bold', pady=20, bg="#4f3d40", foreground="#fff").pack()

urlLabel = Label(root,text = 'Paste your URL Here:', font ='arial 12', pady=10, bg="#4f3d40", foreground="#fff")
urlLabel.pack(padx= 150, pady=(10,2), side= TOP, anchor="w")

urlTextBox = Text(root, height=1, width=70)
urlTextBox.pack(padx= 150, side= TOP, anchor="w")

btnDownload = Button(root, text="Download", command=retrieve_input, bg="#fff", fg="#4f3d40")
btnDownload.pack(padx= 150,pady=(10,2) ,side= TOP, anchor="w")


root.mainloop()
print("Yayy ::: ", len(inp))
