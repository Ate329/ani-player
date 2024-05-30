import requests
import json


def get_access_token():
    with open('token.json') as token_file:
        token_info = json.load(token_file)
    return token_info['access_token']


def search_anime(anime_name):
    query = '''
    query ($search: String) {
      Media (search: $search, type: ANIME) {
        id
        
        title {
          romaji
          english
          native
        }
        
        description
        genres
        episodes
        
        streamingEpisodes {
          title
        }
      }
    }
    '''
    variables = {'search': anime_name}
    url = 'https://graphql.anilist.co'
    headers = {'Authorization': f'Bearer {get_access_token()}'}
    response = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)

    if response.status_code != 200:
        print(f"AniList API request failed with status code {response.status_code}.")
        print(response.text)
        return None

    data = response.json()
    if 'errors' in data:
        print(f"AniList API returned errors:")
        print(data['errors'])
        return None

    return data


def display_episode_info(anime):
    data = anime
    
    anime_data = data['data']['Media']
    anime_title = anime_data['title']['english']
    episode_count = anime_data['episodes']
    
    if 'streamingEpisodes' in anime_data:
        episodes = anime_data['streamingEpisodes']
        for episode in episodes:
            print(f"{episode['title']}")
    else:
        print("Episode titles not available for this anime.")


if __name__ == "__main__":
    print("You are not suppose to run this module individually")
    anime_name = input("Enter the name of the anime: ")
    anime = search_anime(anime_name)
    if anime:
        display_episode_info(anime)
