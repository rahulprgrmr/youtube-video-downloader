import sys
from youtube import YouTubeDownloader

def main():
    url: str = input("Paste the YouTube video link to download: ")
    print(url)
    ytd: YouTubeDownloader = YouTubeDownloader(url)
    ytd.download_and_save()
    

if __name__ == '__main__':
    main()