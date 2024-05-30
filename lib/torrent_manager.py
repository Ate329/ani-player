import os
import time
import subprocess


def download_and_stream(magnet_link, save_path='downloads'):
    global wait_time
    
    # Ensure the save path exists
    os.makedirs(save_path, exist_ok=True)

    # Download and stream the torrent using webtorrent
    command = f'webtorrent "{magnet_link}" --out "{save_path}" --vlc'
    process = subprocess.Popen(command, shell=True)

    # Check speed after some time (adjust wait time as needed)
    wait_time = 5  # Wait 5 seconds before checking speed
    time.sleep(wait_time)

    download_speed = get_download_speed(process)
    
    # Define minimum acceptable speed (adjust as needed)
    min_speed = 1024 * 1024  # 1 MB/s

    if download_speed < min_speed:
        print(f"Download speed is too slow ({download_speed} bytes/s). Try another torrent?")
        choice = input("Enter y to choose another torrent, or any other key to continue: ")
        if choice.lower() == 'y':
            process.terminate()  # Stop the slow download
            return  # Exit the function to prompt for another torrent

    # Wait for the webtorrent process to complete
    process.communicate()


def get_download_speed(process):
    # Get process connections
    connections = process.connections()
    
    # Filter TCP connections for download direction
    download_connections = [conn for conn in connections if conn.status == 'ESTABLISHED' and conn.laddr.port != process.connections()[0].laddr.port]
    
    # Get total bytes sent by all download connections
    total_sent = sum(conn.bytes_sent for conn in download_connections)
    
    # Return download speed in bytes/second
    return total_sent / wait_time


if __name__ == "__main__":
    print("You are not suppose to run this module individually")
    magnet_link = input("Enter the magnet link: ")
    download_and_stream(magnet_link)
