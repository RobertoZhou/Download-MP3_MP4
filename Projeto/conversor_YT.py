from pytubefix import YouTube

print("Insira a URL dos vídeos que gostaria de baixar")
print("OBS: Para baixar mais de um vídeo, separe-os com um espaço")

urls_videos = input("URL: ")
url = urls_videos.split()  # Divide a string em uma lista de URLs usando espaço como delimitador


for video in url:
    yt = YouTube(video)
    ys = yt.streams.get_highest_resolution()
    ys.download(output_path=r"ytdownload")



