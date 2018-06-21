import os, subprocess

os.chdir("SampleVideos/tempvideo_2")
print("Generating video")
vname = 'video_2'
subprocess.call([
    'ffmpeg', '-framerate',
    str(39.0), '-i', '/file%04d.png', '-r', '30', '../'+vname + '_DeepLabCutlabeled.mp4'])
if deleteindividualframes:
    for file_name in glob.glob("*.png"):
        os.remove(file_name)

os.chdir("../")