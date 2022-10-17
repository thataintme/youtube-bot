from math import floor
import os
from random import random, randrange
from secrets import choice
from sys import argv
from video_comp_from_search import videos_search
from moviepy.editor import VideoFileClip, concatenate_videoclips

if (len(argv) < 4):
    print(
        "usage: auto_search_compile.py [SEARCH_QUERY] [MAX_VIDEOS_TO_USE] [MAX_LENGTH-OUTPUT] [CLIPS_MIN_LENGTH] [CLIPS_MAX_LENGTH]")


search_query = argv[1]
max_number_of_videos = int(argv[2])
max_length_output = int(argv[3])
clip_min_len = int(argv[4])
clip_max_len = int(argv[5])


video_links = videos_search.get_video_links_from_search(
    search_query, max_number_of_videos)

# download videos
j = 0
for i in video_links:
    os.system("python ./utils/video_downloader.py {} {} {}.mp4".format(i,
              "./video_comp_from_search/videos", j))
    j += 1

# # now make compilations
max_number_of_clips = max_length_output // clip_max_len

clips = []
for i in range(max_number_of_clips):
    r = choice(list(range(j-1)))
    video_path = "./video_comp_from_search/videos/{}.mp4".format(r)
    video = VideoFileClip(video_path)

    clip_duration = randrange(clip_min_len, clip_max_len)
    start = randrange(0, floor(video.duration - clip_duration))
    clip = video.subclip(start, start+clip_duration)
    clips.append(clip)

    print("clips elements: ", len(clips))

output = concatenate_videoclips(clips)
output.write_videofile("./output.mp4")
