import os
import subprocess


def download_and_stream(magnet_link, save_path='downloads'):
    # Ensure the save path exists
    os.makedirs(save_path, exist_ok=True)

    # Download and stream the torrent using webtorrent
    command = f'webtorrent "{magnet_link}" --out "{save_path}" --vlc'
    process = subprocess.Popen(command, shell=True)

    # Wait for the webtorrent process to complete
    process.communicate()


if __name__ == "__main__":
    print("You are not suppose to run this module individually")
    magnet_link = input("Enter the magnet link: ")
    download_and_stream(magnet_link)
