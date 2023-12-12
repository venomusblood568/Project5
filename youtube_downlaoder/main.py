import os 
import urllib.request
from pytube import YouTube
from tqdm import tqdm

def download_video(url,save_path):
    try:
        #call of the youtube url
        yt = YouTube(url)

        #This Python code filters the available streams of a YouTube video (`yt` object) to include only progressive streams with the file extension "mp4".
        streams = yt.streams.filter(progressive=True, file_extension="mp4")

        #for streaming in the highest quality possible
        highest_res_stream = streams.get_highest_resolution()

        #for getting th video tilte for file name and showing the file in terminal as well
        video_title = yt.title

        #for printing the title before downloading the video
        print(f"Downloading: {video_title}")

        #saving the video in folder with the same name and with the extension of mp4
        full_file_path = os.path.join(save_path, f"{video_title}.mp4")

        #for hightest resolution
        total_size = highest_res_stream.filesize

        #progressive bar conditions
        with tqdm(unit="B",unit_scale=True,unit_divisor=1024,mininterval=1,total=total_size,desc="Progress") as bar:
            urllib.request.urlretrieve(highest_res_stream.url,filename=full_file_path,reporthook=lambda blocknum,blocksize,bytes_read: bar.update(blocksize))

        #finally for printing the name of file and a task complete message
        print(f"\n Video '{video_title}' downloaded successfully")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    video_url = input("Enter youtube url: ")
    save_path = input("Enter the full path for video save: ")

    download_video(video_url,save_path)