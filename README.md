# ani-player
ani-player is a Python script that allows users to search for and download anime episodes using magnet links from popular torrent websites. It provides a simple command-line interface for searching anime titles and selecting specific episodes to download and stream using the webtorrent-cli tool.

## Features

- Search for anime titles and episodes using AniList API integration.
- Display available torrents for selected episodes from Nyaa.si.
- Check the initial download speed of torrents before downloading.
- Download and stream (VLC) selected torrents using webtorrent-cli.

## Requirements

- Python 3.x
- pip (Python package manager)
- Node.js (for webtorrent-cli)
- webtorrent-cli (installation instructions [here](https://webtorrent.io/desktop/) and for most Linux distros it can be downloaded through the package managers directly)

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Ate329/ani-player.git
    ```

2. Install Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Install Node.js and webtorrent-cli according to the instructions provided on the [webtorrent](https://webtorrent.io/desktop/) website.

## Usage

1. Run the `main.py` script:

    ```bash
    python main.py
    ```

2. Enter the name of the anime you want to search for.
3. Enter the episode number you want to download.
4. Choose from the available torrents and enter the corresponding number.
   
## Example

Here's an example of how to use the script:

```shell
python main.py
Enter the name of the anime: Naruto
Anime: NARUTO
Number of episodes: 220
Episode 1 - Enter: Naruto Uzumaki!
Episode 2 - My Name is Konohamaru!
Episode 3 - Sasuke and Sakura: Friends or Foes?
Episode 4 - Pass or Fail: Survival Test
Episode 5 - You Failed! Kakashis Final Decision
Episode 6 - A Dangerous Mission! Journey to the Land of Waves!
Episode 7 - The Assassin of the Mist!
...
Enter the episode number to download: 1
1. [Almighty] Boruto - Naruto Next Generations 256-273 [Set 17][BD 1920x1080 x264 10bit FLAC][Dual Audio][Multiple Subs]
2. [Yameii] Naruto - 001 [English Dub] [iTunes WEB-DL 1080p] [1F520D83] (Naruto)
3. Boruto: Naruto Next Generations Episode 265-273 [Dual Audio][1080p] (English Dub, Japanese Dub)
4. Boruto: Naruto Next Generations Episode 256-264 [Dual Audio][1080p] (English Dub, Japanese Dub)
Enter the number of the torrent to download: 2 
Selected torrent: [Yameii] Naruto - 001 [English Dub] [iTunes WEB-DL 1080p] [1F520D83] (Naruto)
Checking initial speed of torrents. Please wait...
Download speed is too slow (0.00 KB/s).
Enter 'y' to choose another torrent, or any other key to continue with the current torrent: y
```

## To-Do
- [ ] Enhance torrents searching results.
- [ ] Select exact anime title before searching.
- [ ] AniList API sync saved/favourite animes.
- [ ] AniList API update watched animes/episodes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
