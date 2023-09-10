import json
from novel import Novel

novels = {
    'ri': 'https://readnovelfull.me/renegade-immortal/',
    'pot': 'https://readnovelfull.me/pursuit-of-the-truth/',
    'issth': 'https://readnovelfull.me/i-shall-seal-the-heavens/',
    'awe': 'https://readnovelfull.me/a-will-eternal/'
}

for acronym, link in novels.items():
    with open(f'json/{acronym}.json', 'w', encoding='utf-8') as _json:
        json.dump(Novel(link).processed_data, _json, indent=4)
