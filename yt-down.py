import yt_dlp
import sys



def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now post-processing ...')

    
ydl_opts = {
    'format': '18',
    'outtmpl': '/media/pi/61ED-724C/%(playlist)s/%(title)s.%(ext)s',
    'progress_hooks': [my_hook],
}

url = sys.argv[1]


with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
