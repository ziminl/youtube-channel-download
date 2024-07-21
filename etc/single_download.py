
##pip install yt-dlp


import yt_dlp

def download_best_resolution(url, output_path='.'):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Download the video
            ydl.download([url])
            print(f'Download completed! The video is saved to {output_path}')
    
    except Exception as e:
        print(f'An error occurred: {e}')

# Example usage
if __name__ == "__main__":
    video_url = 'https://youtu.be/WaZHX6RhGLs?si=fdPAT9UoT5PjwVv1'
    download_best_resolution(video_url)


