from re import sub
import asyncio
import aiohttp
from bs4 import BeautifulSoup


class Scrapping():
    def __init__(self, url_chapters, chapter_titles):
        self.url_chapters = url_chapters
        self.chapter_titles = chapter_titles
        self.chapters_stats = []

        asyncio.run(self.run())
        self.processed_data = self.chapters_stats

    async def run(self):
        await self.get_text_of_chapters()
        self.calculate_average_per_chapter()

    async def get_text_of_chapters(self):
        urls = self.url_chapters

        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_chapter_text(session, url) for url in urls]
            self.chapters_stats = await asyncio.gather(*tasks)

    async def fetch_chapter_text(self, session, url):
        async with session.get(url) as response:
            response_text = await response.text()
            chapter_html = BeautifulSoup(response_text, "html.parser")
            chapter_html = chapter_html.find("div", id="chr-content")

            chapter_text = chapter_html.get_text(separator=' ', strip=True)

            extracted_data_dict = self.extract_data_from_chapter(chapter_text)
            return extracted_data_dict

    def extract_data_from_chapter(self, chapter_text=str):
        extracted_data_dict = {
            'words': len(chapter_text.split()),
            'characters': len(chapter_text),
            'no spaces': len(sub(r'\s', '', chapter_text)),
            'no punctuation': len(sub(r'[^a-zA-Z0-9\s]', '', chapter_text)),
            'no both': len(sub(r'[^a-zA-Z0-9]', '', chapter_text))
        }
        return extracted_data_dict

    def calculate_all_sum(self):
        total_sum = {
            'words': 0,
            'characters': 0,
            'no spaces': 0,
            'no punctuation': 0,
            'no both': 0
        }

        for stats in self.chapters_stats:
            for key, value in stats.items():
                total_sum[key] += value
        return total_sum

    def calculate_average_per_chapter(self):
        total_sum = self.calculate_all_sum()
        average_per_chapter = {
            'words': 0,
            'characters': 0,
            'no spaces': 0,
            'no punctuation': 0,
            'no both': 0
        }
        total = len(self.chapters_stats)
        for key, value in total_sum.items():
            average_per_chapter[key] = value / total

        self.add_title_to_dicts()

        last = {'all chapters sum': total_sum}, {
            'average per chapter': average_per_chapter}
        self.chapters_stats.insert(0, last)

    def add_title_to_dicts(self):
        for i, title in enumerate(self.chapter_titles):
            self.chapters_stats[i] = {'title': title, **self.chapters_stats[i]}
