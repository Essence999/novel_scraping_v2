from re import sub
from driver import Driver
from scrapping import Scrapping


class Novel():
    def __init__(self, link):
        driver = Driver(link)

        self.link = link
        self.chapters_titles = driver.chapters_titles

        self.url_chapters = self.generate_url_chapters()
        self.total_chapters = len(self.chapters_titles)
        self.processed_data = Scrapping(
            self.url_chapters, self.chapters_titles).processed_data

    def __str__(self) -> str:
        return f'''Link: {self.link}
    Quantidade de Capítulos: {self.total_chapters}
    {self.chapters_titles[0]}'''

    def generate_url_chapters(self) -> list:
        chapters_titles_url = self.formart_chapters_list()
        url_chapters = []
        for chapter in chapters_titles_url:
            url_chapters.append(''.join([self.link, chapter, '/']))
        return url_chapters

    def formart_chapters_list(self):
        self.chapters_titles = self.chapters_titles.split('\n')
        url_chapters = []
        for chapter_title in self.chapters_titles:
            chapter_title = self.formart_title(chapter_title)
            url_chapters.append(chapter_title)
        return url_chapters

    def formart_title(self, title=str):
        title = sub(r'[^a-zA-Z0-9\s-]', '', title)
        title = sub(r'\s+', ' ', title)
        title = title.lower().replace(' ', '-')
        while '--' in title:
            title = title.replace('--', '-')
        if len(title) > 100:
            title = title[:100]
        if title.endswith('-'):
            title = title[:-1]
        return title
