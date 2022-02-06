from tkinter import font
from matplotlib.pyplot import close
from moviepy.editor import *
from moviepy.editor import VideoFileClip
import tkinter
from pyparsing import col;

def removeaudio():
    filenew=filenewdes.get()
    file=filedes.get()
    media = VideoFileClip(file)
    new_clip = media.without_audio()
    if(not filenew):
        new_clip.write_videofile(file)
        new_clip.close()
    else:
        new_clip.write_videofile(filenew+".mp4")
        new_clip.close()

def getaudio():
    # audfile=input("Plese enter the complete path of the video file from which you want to seperate the audio from you want to enter (write extension in the end like filename.mp4) : ");
    audfile=filedes.get()
    filenew=filenewdes.get()
    videoclip = VideoFileClip(audfile)
    audioclip = videoclip.audio
    audioclip.write_audiofile(filenew+".mp3")

def changeangle():
    filenew=filenewdes.get()
    file=filedes.get()
    deg=int(angle.get())
    new_clip=VideoFileClip(file).rotate(deg)
    new_clip.write_videofile(filenew+".mp4")
    new_clip.close()
    


win=tkinter.Tk(screenName='AV operations')
win.title("Audio Video Operations")
win.geometry("520x720")

#taking input of file names

tkinter.Label(win,text='Enter the address of the video ',padx=10).grid(row=0,column=0,sticky='w')#taking input of the video file 
filedes=tkinter.Entry(win)
filedes.grid(row=0,column=1)
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
angle=tkinter.Entry(win).grid(row=7,column=1)
b=tkinter.Button(win,text='Change Angle',bg="cyan",command=getaudio,padx=5,pady=5).grid(row=8,column=0,sticky='w')

win.mainloop()

#to add - change angle of video and add video and audio