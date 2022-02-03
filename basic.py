from ast import If
from moviepy.editor import *
x=input("Enter name of the file: ")
videoclip = VideoFileClip(x)
do=int(input("Press 1 for removing audio from video\nPress 2 for rotating video\n:"))

if(do==1):
    new_clip = videoclip.without_audio()
    
elif(do==2):
    deg=int(input("Enter the degree at which you want to rotate :"))
    new_clip=VideoFileClip(x).rotate(deg)
else:
    print("Please enter a correct value")
x=int(input("Press 1 for editing in main file\nPress 2 for editing in copy\n:"))
if(x==1):
    new_clip.write_videofile("sample.mp4")
elif(x==2):
    u=input("Enter name of the new file: ")
    new_clip.write_videofile(u+".mp4")
else:
    print("Please enter a correct value")