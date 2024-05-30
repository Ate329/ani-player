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
    
    while True:
        # Search for torrents
        torrents = torrent_search.search_torrents(title, episode_number)
        if not torrents:
            print("No torrents found.")
            return

        # Display available torrents
        print("Available torrents:")
        for i, torrent in enumerate(torrents):
            print(f"{i + 1}. {torrent['title']}")

        # Ask user to select a torrent
        choice = input("Enter the number of the torrent to download: ")
        if not choice.isdigit():
            print("Invalid choice. Please enter a number.")
            continue

        choice = int(choice)
        if choice < 1 or choice > len(torrents):
            print("Invalid choice. Please enter a valid number.")
            continue

        selected_torrent = torrents[choice - 1]
        print(f"Selected torrent: {selected_torrent['title']}")

        # Download and stream the selected torrent
        success = torrent_manager.download_and_stream(selected_torrent['magnet_link'])
        if success:
            break
        else:
            print("Please select another torrent.")


if __name__ == "__main__":
    main()
