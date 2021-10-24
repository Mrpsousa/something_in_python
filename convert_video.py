import os
from subprocess import call

path = './' #video path

files = os.listdir(path)

for i, file in enumerate(files):
    call([f'ffmpeg -y -i {path}/{file} -c:v libx264 -crf 24 output/{file[:-4]}.mp4'], shell=True) #convert to mp4
  