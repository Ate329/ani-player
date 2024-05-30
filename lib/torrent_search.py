import requests
from bs4 import BeautifulSoup


def search_torrents(anime_name, episode_number):
    def fetch_torrents(query):
        url = f"https://nyaa.si/?f=0&c=1_2&q={query}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        torrents = []
        for row in soup.select('tr.default'):
            try:
                title_element = row.select_one('a[href^="/view/"]')
                title = title_element.text.strip() if title_element else 'No title available'
                magnet_link = row.select_one('a[href^="magnet:"]')['href']
                torrents.append({'title': title, 'magnet_link': magnet_link})
            except Exception as e:
                print(f"Error extracting torrent info: {e}")
                print(f"Raw HTML for row: {row}")
                continue

        return torrents


    # Construct different possible search queries
    with_zero_episode_number = f"{int(episode_number):02d}"
    queries = [
        f"{anime_name} {episode_number}",
        f"{anime_name} E{episode_number}",
        f"{anime_name} {with_zero_episode_number}"
        f"{anime_name} E{with_zero_episode_number}"
    ]

    # Fetch torrents for each query and combine results
    all_torrents = []
    for query in queries:
        torrents = fetch_torrents(query)
        all_torrents.extend(torrents)

    # Remove duplicates based on magnet link
    unique_torrents = {torrent['magnet_link']: torrent for torrent in all_torrents}.values()

    return list(unique_torrents)


if __name__ == "__main__":
    print("You are not supposed to run this module individually")
    torrents = search_torrents("Naruto", "1")
    for torrent in torrents:
        print(torrent)
