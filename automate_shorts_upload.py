from email.policy import default
import os
import sys
import json
if (len(sys.argv) < 3):
    print(
        "usage: automated.py [YOUTUBE_VIDEO_LINK] [NUMBER_OF_SHORTS_CLIPS_TO_GENERATE]")
    sys.exit()

os.system("python ./shorts_gen/video_downloader.py {}".format(
    sys.argv[1]))  # download video

os.system("python ./shorts_gen/clip_extractor.py {}".format(
    sys.argv[2]))  # generage shorts clips

f = open('./shorts_gen/video_defaults.json')
defaults = json.load(f)
print("title ", defaults['title'])
# upload clips
for filename in os.listdir('./shorts_gen/clips'):
    print('python ./shorts_gen/upload_video.py --file=\"./shorts_gen/clips/{}\" --title=\"{}\" --description=\"{}\" --keywords=\"{}\" --category=\"{}\" --privacyStatus=\"{}\"'
          .format(filename, defaults['title'], defaults['description'], defaults['keywords'], defaults['category'], defaults['privacyStatus']))
    os.system(
        'python ./shorts_gen/upload_video.py --file=\"./shorts_gen/clips/{}\" --title=\"{}\" --description=\"{}\" --keywords=\"{}\" --category=\"{}\" --privacyStatus=\"{}\"'
        .format(filename, defaults['title'], defaults['description'], defaults['keywords'], defaults['category'], defaults['privacyStatus']))


os.system('python ./shorts_gen/cleaner.py')  # clean up


# for easy testing from command line
# python upload_video.py --file="./clips/0.mp4" --title="Best of Reaction Moments" --description="?? Subscribe for more of the funniest & best new videos: n n #reels #shorts #tiktok #funny" --keywords="tik tok,tik toks,ethiopia tik tok,tiktok memes,ethiopia,tik tok memes,tik tok video,best tik tok memes,cringe tik toks,funny tiktok memes,tik tok funny video,funny tik tok memes,ethiopia film,funny tik tok videos,monstro,ethiopia woman,ethiopia music,ethiopia movie,ethiopia funny,ethiopia video,ethiopia comedy,tik tok compilation,tik toks that radiate vine energy,funny tik tok compilation,reels,shorts" --category="22" --privacyStatus="public"
