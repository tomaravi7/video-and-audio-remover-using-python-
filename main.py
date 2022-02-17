from tkinter import StringVar, font
from matplotlib.pyplot import close, title
from moviepy.editor import *
from moviepy.editor import VideoFileClip
import tkinter
from tkinter import filedialog,messagebox
from pyparsing import col;

def getpath():
    global selfile
    selfile = StringVar()
    selfile = filedialog.askopenfilename( initialdir=selfile,
    title = "Select a file", filetypes = [(".mp4", "*.mp4")])
    selfile=title.get()
    tkinter.Label(win,text=selfile,padx=10).grid(row=0,column=4)
def removeaudio():
    filenew=filenewdes.get()
    file=selfile
    media = VideoFileClip(file)
    new_clip = media.without_audio()
    if(not filenew):
        new_clip.write_videofile(file)
        new_clip.close()
    else:
        new_clip.write_videofile(filenew+".mp4")
        new_clip.close()

def getaudio():
    audfile=selfile
    filenew=filenewdes.get()
    videoclip = VideoFileClip(audfile)
    audioclip = videoclip.audio

    if(not filenew):
        newaudfile = audfile.replace(".mp4", ".mp3")
        audioclip.write_audiofile(newaudfile)
    else:
        audioclip.write_audiofile(filenew+".mp3")
        

def changeangle():
    filenew=filenewdes.get()
    file=selfile
    deg=int(angle.get())
    new_clip=VideoFileClip(file).rotate(deg)
    if(not filenew):
        new_clip.write_videofile(file+".mp4")
        new_clip.close()
    else:
        new_clip.write_videofile(filenew+".mp4")
        new_clip.close()



win=tkinter.Tk(screenName='AV operations')
win.title("Audio Video Operations")
win.geometry("1020x720")

#taking input of file names

tkinter.Label(win,text='Enter the address of the video ',padx=10).grid(row=0,column=0,sticky='w')#taking input of the video file 
b = tkinter.Button(win,width = 15,text= "Browse",command = getpath).grid(row=0,column=2)
tkinter.Label(win,text='Enter the name of new file (Skip if you want to overwite the file) ',padx=10).grid(row=1,column=0,sticky='w')#taking input where to store new file if not overwriting
filenewdes=tkinter.Entry(win)
filenewdes.grid(row=1,column=1,sticky='e')


#removeaudio
tkinter.Label(win,text='Mute a Video',font=('Arial',22),fg="#0000FF", pady= 20,padx=10).grid(row=2,sticky='w')
b=tkinter.Button(win,text='Mute',bg="cyan",command=removeaudio,padx=5,pady=5).grid(row=3 ,column=0,sticky='w') #check if newfile name working or not


#remove video and get mp3
tkinter.Label(win,text='Extract Audio From a Video File',font=('Arial',22),fg="#5D1049",pady= 20,padx=10).grid(row=4,sticky='w')
b=tkinter.Button(win,text='Extract Audio',bg="cyan",command=getaudio,padx=5,pady=5).grid(row=5,column=0,sticky='w')

#change the angle of video
tkinter.Label(win,text='Change Angle of Video ',font=('Arial',22),fg="#720D5D",pady= 20,padx=10).grid(row=6,sticky='w')
tkinter.Label(win,text='Enter the angle you want to rotate the video',padx=10).grid(row=7,column=0,sticky='w')
angle=tkinter.Entry(win)
angle.grid(row=7,column=1)
b=tkinter.Button(win,text='Change Angle',bg="cyan",command=changeangle,padx=5,pady=5).grid(row=8,column=0,sticky='w')

win.mainloop()

#to add - video and audio merger try making classes
#diagnose and solve not responding issues