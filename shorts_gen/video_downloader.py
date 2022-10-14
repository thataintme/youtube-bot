from pytube import YouTube
from sys import argv
# args - (link to youtube video)

link = argv[1]
print(argv)
yt = YouTube(link)
print("title: ", yt.title)
print("views: ", yt.views)
yd = yt.streams.get_highest_resolution()
yd.download('./shorts_gen', 'video.mp4')
