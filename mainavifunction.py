from tkinter import font
from matplotlib.pyplot import close
from moviepy.editor import *
from moviepy.editor import VideoFileClip
import tkinter
from tkinter import ttk

from pyparsing import col;
def removeaudio():
    file=input("Plese enter the complete path of the video file you want to enter : ");
    dec=input("Do you want to overwrite the file or create a new file(write OVERWRITE or NEW) : ");
    if(dec=="OVERWRITE"):
        media = VideoFileClip(file);
        new_clip = media.without_audio();
        new_clip.write_videofile(file);
        new_clip.close();
    elif(dec=="NEW"):
        media = VideoFileClip(file);
        new_clip = media.without_audio();
        filenew=input("Please enter the name of new file : ");
        new_clip.write_videofile(filenew+"mp4");
        new_clip.preview(fps=60, audio=False);

def getaudio():
    audfile=input("Plese enter the complete path of the video file from which you want to seperate the audio from you want to enter (write extension in the end like filename.mp4) : ");
    videoclip = VideoFileClip(audfile);
    audioclip = videoclip.audio;
    audioclip.write_audiofile("newaud.mp3");

win=tkinter.Tk(screenName='AV operations')
win.title("Audio Video Operations")
win.geometry("520x720")
win.iconphoto(False,tkinter.PhotoImage(file="logo.jpg")) #giving error sometimes and working sometimes
#removeaudio
tkinter.Label(win,text='Audio Remover ',font=('Arial',22),fg="#0000FF", pady= 20,padx=10).grid(row=0,sticky='w')
tkinter.Label(win,text='Enter the address of the video ',padx=10).grid(row=1,column=0,sticky='w')
file=tkinter.Entry(win,).grid(row=1,column=1)
b=tkinter.Button(win,text='Remove Audio',bg="cyan",command=removeaudio,padx=10).grid(row=2,column=0,sticky='w') #add checkbox to ask if user wants to overwrite the old file or make a new file

separator = ttk.Separator(win, orient='horizontal')
separator.place(relx=0.47, rely=0, relwidth=0.2, relheight=1)

#remove video and get mp3
tkinter.Label(win,text='Video Remover ',font=('Arial',22),fg="#5D1049",pady= 20,padx=10).grid(row=3,sticky='w')
tkinter.Label(win,text='Enter the address of the video you want to perform operations on - ',padx=10).grid(row=4,column=0,sticky='w')
file=tkinter.Entry(win).grid(row=4,column=1)
b=tkinter.Button(win,text='Remove Video',bg="cyan",command=getaudio,padx=10).grid(row=5,column=0,sticky='w')

#change the angle of video
tkinter.Label(win,text='Change Angle of Video ',font=('Arial',22),fg="#720D5D",pady= 20,padx=10).grid(row=6,sticky='w')
tkinter.Label(win,text='Enter the address of the video',padx=10).grid(row=7,column=0,sticky='w')
file=tkinter.Entry(win).grid(row=7,column=1)
b=tkinter.Button(win,text='Change Angle',bg="cyan",command=getaudio,padx=10).grid(row=8,column=0,sticky='w')

win.mainloop()

#to add - change angle of video and add video and audio