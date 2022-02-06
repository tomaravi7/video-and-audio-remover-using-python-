from tkinter import *
from tkinter import filedialog,messagebox

FotaGui = Tk()


def file_path():
        
        global filepath
        filepath = StringVar()
        #Fetch the file path of the hex file browsed.
        if(filepath == ""):
            filepath = filedialog.askopenfilename( initialdir = os.getcwd() ,
                 title = "select a file", filetypes = [("vid files", "*.mp4")])
        else:
            filepath = filedialog.askopenfilename( initialdir=filepath,
                 title = "select a file", filetypes = [("vid files", "*.mp4")])


def generate():
        
        if filepath == "":
            messagebox.showinfo('Information','please browse')
        else:
            filepathlabel.config(text=filepath)

Browsebutton = Button(FotaGui,width = 15,text= "BROWSE",command = file_path)
Browsebutton.pack()
Generatebutton = Button(FotaGui,text="Generate",command = generate)
Generatebutton.pack()
filepathlabel = Label(FotaGui,text = "hex file path:",font = ('Times 10'))
filepathlabel.pack()
FotaGui.mainloop()