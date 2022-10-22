from math import floor
import os
from random import randrange
from secrets import choice
from sys import argv
from video_comp_from_search import videos_search
from moviepy.editor import VideoFileClip, concatenate_videoclips
import json

if (len(argv) != 6):
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
choice_videos = list(range(j))
new_choice_videos = choice_videos.copy()
for i in choice_videos:
    if (not os.path.exists("./video_comp_from_search/videos/{}.mp4".format(i))):
        new_choice_videos.remove(i)

for i in range(max_number_of_clips):
    r = choice(new_choice_videos)
    video_path = "./video_comp_from_search/videos/{}.mp4".format(r)
    video = VideoFileClip(video_path)

    clip_duration = randrange(clip_min_len, clip_max_len)
    start = randrange(0, floor(video.duration - clip_duration))
    clip = video.subclip(start, start+clip_duration)
    clips.append(clip)

    clip.write_videofile(
        "./video_comp_from_search/clips/clipnNumber{}FromFile{}.mp4".format(i, r))

output = concatenate_videoclips(clips, method='compose')
output.write_videofile("./output.mp4")

f = open("./video_comp_from_search/video_defaults.json")
defaults = json.load(f)

print('python ./utils/upload_video.py --file=\"output.mp4\" --title=\"{}\" --description=\"{}\" --keywords=\"{}\" --category=\"{}\" --privacyStatus=\"{}\"'.format(
    defaults['title'], defaults['description'], defaults['keywords'], defaults['category'], defaults['privacyStatus']))
os.system('python ./utils/upload_video.py --file=\"output.mp4\" --title=\"{}\" --description=\"{}\" --keywords=\"{}\" --category=\"{}\" --privacyStatus=\"{}\"'.format(
    defaults['title'], defaults['description'], defaults['keywords'], defaults['category'], defaults['privacyStatus']))
