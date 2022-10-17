from operator import indexOf
import os
from random import random
import urllib.request
import re
import sys
if (len(sys.argv) < 3):
    print(
        "usage: videos_search.py [SEARCH_QUERY_AS_STRING] [MAX_NUMBER_OF_LINKS]")
    sys.exit()
search_keyword = sys.argv[1]
max_number_videos = int(sys.argv[2])


def get_video_links_from_search(search_keyword, max_number_videos):
    search_keyword = search_keyword.replace(" ", "+")
    html = urllib.request.urlopen(
        "https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    set_video_ids = list(set(video_ids))
    # got the list of videos
    # now creating random numbers to use as indices
    ran = random()
    ran_digits_list = list(
        set(list(str(ran)[str(ran).index(".")+1::])))
    ran_digits_list = [int(x) for x in ran_digits_list[:max_number_videos:]]

    video_links = []
    for i in ran_digits_list:
        video_link = "https://www.youtube.com/watch?v=" + set_video_ids[i]
        video_links.append(video_link)
        # os.system(
        #     "python ./video_comp_from_search/video_downloader.py {} {}.mp4".format(video_link, set_video_ids[i]))

    return video_links


print(get_video_links_from_search(search_keyword, max_number_videos))
