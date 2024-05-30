from lib import anilist_api
from lib import torrent_search
from lib import torrent_manager


def main():
    query = input("Enter the name of the anime: ")
    anime_data = anilist_api.search_anime(query)

    # Extract anime information
    anime_info = anime_data['data']['Media']
    title = anime_info['title']['romaji']
    episodes = anime_info.get('episodes', 'Unknown')
    
    print(f"Anime: {title}")
    print(f"Number of episodes: {episodes}")
    
    anilist_api.display_episode_info(anime_data)

    # Ask user for episode number
    episode_number = input("Enter the episode number to download: ")
    
    # Search for torrents
    torrents = torrent_search.search_torrents(title, episode_number)
    if not torrents:
        print("No torrents found.")
        return
    
    print("Available torrents:")
    for i, torrent in enumerate(torrents):
        print(f"{i + 1}. {torrent['title']}")

    # Ask user to select a torrent
    choice = int(input("Enter the number of the torrent to download: ")) - 1
    if choice < 0 or choice >= len(torrents):
        print("Invalid choice.")
        return

    magnet_link = torrents[choice]['magnet_link']
    print(f"Selected torrent: {torrents[choice]['title']}")
    
    # Download and stream the torrent
    torrent_manager.download_and_stream(magnet_link)


if __name__ == "__main__":
    main()
