# downloader.py
import os
import subprocess
import sys

def download_video(url: str, save_folder: str = "downloads"):
    """
    Downloads an embedded or direct video using yt-dlp.
    Saves the file in the 'downloads' folder, named by video title.
    """
    os.makedirs(save_folder, exist_ok=True)
    output_template = os.path.join(save_folder, "%(title)s.%(ext)s")

    command = [
        sys.executable, "-m", "yt_dlp",
        "-f", "best",
        "-o", output_template,
        url
    ]

    try:
        print("\n Starting download — please wait...\n")
        subprocess.run(command, check=True)
        print(f"\n Download completed. Files are in: {os.path.abspath(save_folder)}\n")
    except subprocess.CalledProcessError:
        print(" Error: yt-dlp failed to download. Check the URL or try another site.")
    except Exception as e:
        print(f"⚠ Unexpected error: {e}")

if __name__ == "__main__":
    print("=== Universal Video Downloader ===")
    video_url = input("Enter the video URL: ").strip()
    if not video_url:
        print("No URL provided. Exiting.")
        sys.exit(1)
    download_video(video_url)

