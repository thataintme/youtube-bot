import os
from pytube import YouTube, exceptions
from sys import argv
# args - (link to youtube video)
if (len(argv) < 4):
    print(
        "usage: video_downloader.py [VIDEO_LINK] [DESTINATION_FOLDER_PATH] [DESTINATION_FILE_NAME]")


link = argv[1]
destination = argv[2]
filename = argv[3]
print(argv)
yt = YouTube(link)
print("title: ", yt.title)
print("views: ", yt.views)
yd = yt.streams.get_highest_resolution()
try:
    yd.download(destination, filename)
except Exception as e:
    if (os.path.exists(destination+filename)):
        os.remove(destination+filename)
