# cleans up the file system by deleting downloaded and generated videos

import os
import shutil

clips_folder = './shorts_gen/clips'
for filename in os.listdir(clips_folder):
    file_path = os.path.join(clips_folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))
if (os.path.exists('./shorts_gen/video.mp4')):
    os.remove('./shorts_gen/video.mp4')

if (os.path.exists('./shorts_gen/upload_video.py-oauth2.json')):
    os.remove('./shorts_gen/upload_video.py-oauth2.json')
