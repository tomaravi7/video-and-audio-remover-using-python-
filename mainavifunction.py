from matplotlib.pyplot import close
from moviepy.editor import *
from moviepy.editor import VideoFileClip
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
    audfile=input("Plese enter the complete path of the video file from which you want to seperate the audio from you want to enter (write extension in the end ) : ");
    videoclip = VideoFileClip(audfile);
    audioclip = videoclip.audio;
    audioclip.write_audiofile("newaud.mp3");
getaudio();
