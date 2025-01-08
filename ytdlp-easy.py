import os
import subprocess

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

ytLink = input("enter YouTube link:\n")
clearTerminal()

vOrA = int(input("what do you want to download?\n[1] video only\n[2] audio only\n[3] video and audio (default):\n"))
clearTerminal()

if vOrA == 1 or vOrA == 3:
    videoFormat = input("select video format:\n[1] mp4\n[2] webm\n[3] mkv\n[4] avi\n")

if vOrA == 2:
    audioFormat = input("select audio format:\n[1] mp3\n[2] m4a\n[3] wav\n[4] ogg\n[5] flac\n[6] aac\n")

clearTerminal()

resolution = ["144", "240", "360", "480", "720", "1080", "1440", "2160", "4320"]
videoFormats = ["mp4", "webm", "mkv", "avi"]
audioFormats = ["mp3", "m4a", "wav", "ogg", "flac", "aac"]

if vOrA == 1 or vOrA == 3:
    selectedResolution = input("select video resolution you want to download:\n[1] 144p\n[2] 240p\n[3] 360p\n[4] 480p (SD)\n[5] 720p (HD)\n[6] 1080p (Full HD) - default\n[7] 1440p (2K)\n[8] 2160p (4K)\n[9] 4320p (8K) - rarely available\n")
    clearTerminal()

downloadLocation = int(input(f"select download location:\n[1] current folder - {os.getcwd()}\n[2] different location\n"))
clearTerminal()

if downloadLocation == 2:

    currentDir = os.getcwd()
    count = 0

    print(f"subfolders of {currentDir}:\n")

    folders = [folder for folder in os.listdir(currentDir) if os.path.isdir(os.path.join(currentDir, folder))]
    
    for folder in folders:
        count+=1
        print(f"[{count}]📁 {folder}")


    ouputPath = input("\nselect a folder or enter full path to the desired location:\n")

    if ouputPath.isdigit() and  ouputPath <= str(len(folders)):
        ouputPath = os.path.join(currentDir, folders[int(ouputPath)-1])
        clearTerminal()
        print(f"download started and will be saved to {ouputPath}")

    elif not ouputPath.isdigit():
        if os.path.isdir(ouputPath):
            ouputPath = ouputPath
            clearTerminal()
            print(f"download started and will be saved to {ouputPath}")
        else:
            print("invalid output folder")
        
    elif ouputPath >= str(len(folders)):
        print("invalid output folder!")
else:
    ouputPath = os.getcwd()

cmd = f'yt-dlp "{ytLink}" -o "{ouputPath}{os.sep}%(title)s.'

if vOrA == 1 or vOrA == 3:
    cmd += videoFormats[int(videoFormat)-1] + '" '
else:
    cmd += audioFormats[int(audioFormat)-1] + '" '

if vOrA == 1:
    cmd += f'-f "bv*[height<={resolution[int(selectedResolution)-1]}]"'

if vOrA == 2:
    cmd += f'-f "ba"'

if vOrA == 3:
    cmd += f'-f "bestvideo[height={resolution[int(selectedResolution)-1]}]+bestaudio" --merge-output-format {videoFormats[int(videoFormat)-1]}'

subprocess.call(cmd, shell=True)