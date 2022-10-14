# args - [start time in seconds] [number of clips needed]
# randomly extracts clips


from fileinput import filename
from math import floor
from pydoc import cli
from random import randrange
from moviepy.editor import VideoFileClip
from moviepy.video.fx import crop
from sys import argv


number_of_clips = 1
if len(argv) > 1:
    number_of_clips = int(argv[1]) if (int(argv[1]) < 10) else 10

video = VideoFileClip("./shorts_gen/video.mp4")
video_length = video.duration


for i in range(number_of_clips):
    clip_length = randrange(10, 50)
    start = randrange(0, floor(video_length-clip_length))
    clip = video.subclip(start, start+clip_length)
    clip_width = clip.w
    print(clip_width)
    cropwidth = clip_width//3
    print("crop width ", cropwidth)

    croppedclip = crop.crop(clip, x1=cropwidth, width=cropwidth)
    filename = str(i)+'.mp4'
    croppedclip.write_videofile('./shorts_gen/clips/'+filename)
