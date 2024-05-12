from bs4 import BeautifulSoup
from pathlib import Path

input_file_path = Path.cwd() / "web_scraping"/ "pyladies_locations.html"

html = open(input_file_path, encoding='utf8').read()
soup = BeautifulSoup(html, 'html.parser')

locations = soup.find_all('div', class_='chapter_location')
# locationsの数をprintする
print(f'Number of locations: {len(locations)}')

with open(Path.cwd() / "web_scraping"/'contact_info.txt', 'w') as fout:
    for location in locations:
        # chapter_locationを探す
        name = location.find('h3', class_='chpts chapter-name')

        address = location.find('a', class_='icon-mail4')
        if address is None:
            mail = "メールアドレスがありません"
        else:
            mail = address["href"].removeprefix("mailto:")

        fout.write(f'{name.text.strip()}:{mail}')
        fout.write('\n')
