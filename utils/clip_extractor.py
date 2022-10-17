# args - [start time in seconds] [number of clips needed]
# randomly extracts clips


from fileinput import filename
from math import floor
from os import system
import os
from random import randrange
from moviepy.editor import VideoFileClip
from moviepy.video.fx import crop
from sys import argv

if (len(argv) < 5):
    print(
        "usage: clip_extractor.py [NUMBER_OF_CLIPS] [VIDEO_PATH] [CLIPS_DESTINATION_PATH] [CLIP_MIN_DURATION] [CLIP_MAX_DURATION] [OVERWRITE?]")

number_of_clips = int(argv[1])
video_path = argv[2]
clips_destination = argv[3]
min_dur = int(argv[4])
max_dur = int(argv[5])
overwrite = argv[6].lower() == 'true'

video = VideoFileClip(video_path)

video_length = video.duration

clip_length = randrange(min_dur, max_dur)
j = 0
for i in range(number_of_clips):
    start = randrange(0, floor(video_length-clip_length))
    clip = video.subclip(start, start+clip_length)
    filename = str(i)+'.mp4'
    if (overwrite):
        clip.write_videofile(clips_destination+filename)
    else:
        print("entered here")
        while (True):
            k = i+j
            print("k : ", k)
            filename = str(k)+'.mp4'
            print("filename : ", filename)
            if (not os.path.exists(clips_destination+filename)):
                break
            j += 1
        clip.write_videofile(clips_destination+filename)
