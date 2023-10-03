import requests
from bs4 import BeautifulSoup
import json

def extract_all_mp4_hd_urls(game_url):
    """
    Given a game URL, extracts all data-mp4-hd-source values and returns them as a list.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(game_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Search for all elements with a 'data-mp4-hd-source' attribute
    video_elements = soup.find_all(attrs={"data-mp4-hd-source": True})
    
    # Extract all the data-mp4-hd-source values
    urls = [video["data-mp4-hd-source"] for video in video_elements]
    return urls

def extract_mp4_url(game_url):
    """
    Given a game URL, extracts the first data-mp4-source value.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(game_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Search for the first element with a 'data-mp4-source' attribute
    video_element = soup.find(attrs={"data-mp4-hd-source": True})
    if video_element:
        return video_element["data-mp4-hd-source"]
    return None

def main():
    # read in from file urls.txt and store each url into the game_urls list
    game_urls = []

    with open('urls.txt', 'r') as f:
        for line in f:
            game_urls.append(line.strip())
    
    games_data = {}
        
    for game_url in game_urls:
        game_name = game_url.split("/")[-2] # Just an example to extract game name from URL, might need adjustments
        mp4_hd_urls = extract_all_mp4_hd_urls(game_url)
        
        if mp4_hd_urls:
            games_data[game_name] = mp4_hd_urls
            print(f"Found mp4 for game: {game_name}")
        else:
            print(f"Could not find mp4 for game: {game_name}")
    
    with open("games.json", "w") as jsonfile:
        json.dump(games_data, jsonfile, indent=4)

if __name__ == "__main__":
    main()
