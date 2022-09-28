# Adapted from https://stackoverflow.com/questions/37317140/cutting-out-a-portion-of-video-python

import os
from moviepy.editor import VideoFileClip
from multiprocessing import Pool, cpu_count

try:
    os.mkdir("converted")
except:
    pass

split_every_secs = 30

# loading video gfg
clip = VideoFileClip("main.mp4")

# get full length of video
full_duration = clip.duration

# get amount of resulting videos so we can end loop at that point : Added +1 as duration is a float and video may not
# actually have ended
amount_of_files = int(full_duration/split_every_secs)

# initial positions


# for testing..
# print(f"""
# duration {full_duration}
# files  {amount_of_files}
# """)


def functionx(x):
    end_pos = x * 30
    start_pos = end_pos-30
    subclip = clip.subclip(start_pos, end_pos)
    subclip.write_videofile(f"converted/clip_{x}.mp4")

if __name__ == '__main__':
    with Pool(cpu_count()) as p:
        count = set()
        for i in range(1, amount_of_files + 1):
            count.add(i)
        print(p.map(functionx,count))