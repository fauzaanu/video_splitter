# Adapted from https://stackoverflow.com/questions/37317140/cutting-out-a-portion-of-video-python
import os
from moviepy.editor import VideoFileClip

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
start_pos = 0
end_pos = split_every_secs

# for testing..
# print(f"""
# duration {full_duration}
# files  {amount_of_files}
# """)


for i in range(1,amount_of_files+1):
    subclip = clip.subclip(start_pos, end_pos)
    subclip.write_videofile(f"converted/clip_{i}.mp4")

    start_pos = end_pos
    end_pos = start_pos+split_every_secs

#