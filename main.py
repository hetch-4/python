#download yt video in mp3 format
from pytube import YouTube
import os

#url input from user
yt = YouTube(str(input("Enter url of video you want to download:")))

# extract audio only
video = yt.streams.filter(only_audio=True).first()

#check for destination to save file 
print("Enter Destination to save file (leave blank for urrent directory)")
destination = str(input(">> ")) or '.'

#download the file 
out_file = video.download(output_path=destination)

#save the file
base, ext = os.path.splittext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)  

#result of success
print(yt.title + " has been succesfully downloaded in .mp3 format.")