import requests
from bs4 import BeautifulSoup
import csv

def extract_data(soup):
    titres = soup.find_all('h1')
    liens = soup.find_all('a')
    paragraphes = soup.find_all('p')
    atik = soup.find_all('div', class_='lnv-featured-article-lg')
    

    lyen_imaj = []
    for div in atik:
        imaj = div.find('img')
        if imaj:
            src_value = imaj.get('src')
            lyen_imaj.append(src_value)

    titres_texte = [titre.get_text(strip=True) for titre in titres]
    liens_texte = [lien.get('href').strip() for lien in liens]
    paragraphes_texte = [paragraphe.get_text(strip=True) for paragraphe in paragraphes]

    return titres_texte, liens_texte, paragraphes_texte, lyen_imaj

def write_to_csv(filename, headers, data):
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for header, values in zip(headers, data):
            writer.writerow([header])
            for value in values:
                writer.writerow([value])

def main():
    url = 'https://lenouvelliste.com/'
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        headers = ['TIT', 'LYEN', 'DESKRIPSYON', 'LYEN IMAJ']
        data = extract_data(soup)
        write_to_csv('result.csv', headers, data)

if __name__ == "__main__":
    main()
