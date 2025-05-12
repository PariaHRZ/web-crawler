import requests
from bs4 import BeautifulSoup
import time
import os
from datetime import datetime

def fetch_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Erreur: {response.status_code} pour {url}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête pour {url}: {e}")
        return None

def parse_links(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.startswith('http'):
            links.append(href)
    return links

def crawl(seed_url, max_pages=10):
    visited = set()
    to_visit = [seed_url]
    all_links = set()
    
    while to_visit and len(visited) < max_pages:
        current_url = to_visit.pop(0)
        if current_url in visited:
            continue
        
        print(f"Visiting: {current_url}")
        html_content = fetch_page(current_url)
        if html_content:
            links = parse_links(html_content)
            to_visit.extend(links)
            visited.add(current_url)
            all_links.update(links)
        
        time.sleep(1)  # Pause pour ne pas surcharger le serveur
    
    print(f"Crawling terminé. {len(visited)} pages visitées.")
    return all_links

def save_links_to_file(links, directory='output'):
    try:
        os.makedirs(directory, exist_ok=True)
        now = datetime.now()
        filename = f'crawled_links_{now.strftime("%d-%m-%Y_%H-%M-%S")}.txt'
        filepath = os.path.join(directory, filename)
        with open(filepath, 'w') as file:
            for link in links:
                file.write(link + '\n')
        print(f"Liens sauvegardés dans '{filepath}'")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde des liens : {e}")

if __name__ == "__main__":
    seed_url = "https://example.com"  # Remplace par l'URL à crawler
    links = crawl(seed_url, max_pages=20)  # Nombre de pages à visiter
    save_links_to_file(links)
