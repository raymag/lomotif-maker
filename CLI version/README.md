# MMK
A simple script that converts images and a song into a video clip using the python and the FFMPEG tool.

## Installing
To use this script you have to download the **FFMPEG** tool which can be found in the official [website](https://www.ffmpeg.org/).  
For it to work properly, it's necessary to include the **FFMPEG** executable in the **PATH** environment variable.

Now you can clone this repository with the following:
```bash
git clone https://github.com/raymag/mmk
```

## How to use it?
Now that you have everything installed, you can finally run the script.  
There are only too features in **MMK**:
- Rename .jpg files to a logical and organized name.
- Merge renamed .jpg files and a .mp3 song into a videoclip.

Remmember that's **necessary** to run the first command to the run the second command.  
By the way, we **strongly** recommend that you put all wanted images into a single directory.  
To rename all .jpg files with mmk, all you need to do is run the following command replacing path with the path to the
directory where all .jpg files are:  
```bash
python mmk.py rename path
```
Note that renamed files will be moved to a new directory which is described in the end of the process. Now that you have prepared
all .jpg files you can merge everything into the videoclip by running the following statement and replacing img_path for the directory
of the renamed images and audio_path for the path to the song.  
```bash
python mmk.py make-movie img_path img_path
```
The final product will be a new file called ```movie.avi``` in a new directory.
