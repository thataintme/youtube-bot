# cleans up the file system by deleting downloaded and generated videos

import os
import shutil

videos_folder = './video_comp_from_search/videos'
for filename in os.listdir(videos_folder):
    file_path = os.path.join(videos_folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))
        

videos_folder = './video_comp_from_search/clips'
for filename in os.listdir(videos_folder):
    file_path = os.path.join(videos_folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))