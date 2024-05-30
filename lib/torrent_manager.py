import os
import time
import psutil
import subprocess


def download_and_stream(magnet_link, save_path='downloads'):
    os.makedirs(save_path, exist_ok=True)

    while True:
        # Define the webtorrent command
        command = f'webtorrent download "{magnet_link}" --out "{save_path}" --quiet'

        # Start the webtorrent process
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Check speed before starting the download
        wait_time = 10  # Wait time in seconds
        download_speed = get_download_speed(process, wait_time)

        # Define minimum acceptable speed (adjust as needed)
        min_speed = 1024 * 1024  # 1 MB/s

        if download_speed < min_speed:
            print(f"Download speed is too slow ({download_speed / 1024:.2f} KB/s).")
            choice = input("Enter 'y' to choose another torrent, or any other key to continue with the current torrent: ")
            if choice.lower() == 'y':
                process.terminate()
                return
            else:
                break
        else:
            break

    print(f"Initial speed: {download_speed / 1024:.2f} KB/s")

    # If the speed is acceptable, start streaming with VLC
    stream_command = f'webtorrent download "{magnet_link}" --out "{save_path}" --vlc'
    stream_process = subprocess.Popen(stream_command, shell=True)
    stream_process.communicate()


def get_download_speed(process, wait_time):
    start_time = time.time()
    initial_bytes = psutil.net_io_counters().bytes_recv

    while time.time() - start_time < wait_time:
        time.sleep(1)

    final_bytes = psutil.net_io_counters().bytes_recv
    total_bytes = final_bytes - initial_bytes

    # Calculate the download speed in bytes/second
    download_speed = total_bytes / wait_time

    return download_speed


if __name__ == "__main__":
    print("You are not supposed to run this module individually")
    magnet_link = input("Enter the magnet link: ")
    download_and_stream(magnet_link)
