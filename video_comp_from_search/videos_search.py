import urllib.request
import re
import sys
if (len(sys.argv) < 2):
    print("usage: videos_search.py [SEARCH_QUERY_AS_STRING]")
    sys.exit()
search_keyword = sys.argv[1]
html = urllib.request.urlopen(
    "https://www.youtube.com/results?search_query=" + search_keyword)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
for i in range(7):
    print("https://www.youtube.com/watch?v=" + video_ids[i])
