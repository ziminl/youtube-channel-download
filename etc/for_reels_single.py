import yt_dlp

url = 'https://www.youtube.com/shorts/kW3udWiKSYU'

ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',  
        'preferedformat': 'mp4', 
    }],
    'outtmpl': '%(title)s.%(ext)s',
    'noplaylist': True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
