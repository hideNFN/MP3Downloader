from __future__ import unicode_literals
import yt_dlp
import os

def mp3dwn():
    print("MP3 Downloader v1.00 de hideNFN\n \n")

    foldercurent = os.getcwd()
    datafolder = foldercurent + "\\data"
    folderffmpeg = datafolder + "\\ffmpeg"
    ffmpegcheck = folderffmpeg + "\\ffmpeg.exe"
    ffprobecheck = folderffmpeg + "\\ffprobe.exe"

    if os.path.exists(datafolder) is False and os.path.exists(folderffmpeg) is False:
        print("Se creeaza folderele necesare...")
        os.mkdir(datafolder)
        os.mkdir(folderffmpeg)
    if os.path.exists(datafolder) is False:
            print("Se creeaza folderul necesar...")
            os.mkdir(datafolder)
    if os.path.exists(folderffmpeg) is False:
            print("Se creeaza folderul necesar...")
            os.mkdir(folderffmpeg)

    if os.path.exists(ffmpegcheck) is True and os.path.exists(ffprobecheck) is True:
        print("A fost gasita instalarea de ffmpeg.")
    else:
        print('Instalarea de ffmpeg nu a fost gasita, va rog sa downloadati ffmpeg si sa introduceti ffmpeg.exe si ffprobe.exe in folderul "ffmpeg"')

    os.chdir(datafolder)
    
    while True:
        print("\nIntrodu URL-ul continutului media pe care doresti sa il downloadezi in format MP3:\n")

        
        linkmp3 = input()

        try:
            ydlp_opts = {
                "ffmpeg_location": "ffmpeg\\",
                "outtmpl": "%(title)s.%(ext)s",
                "format": "bestaudio/best",
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }],
            }
            with yt_dlp.YoutubeDL(ydlp_opts) as ydlp:
                ydlp.download([linkmp3])
        except:
            print("Eroare.")
mp3dwn()
#pyinstaller mp3downloader.py -F