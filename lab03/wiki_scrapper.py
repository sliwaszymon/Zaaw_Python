import requests
from bs4 import BeautifulSoup


class Scrapper:
    url: str
    output_file: str

    def __init__(self, url: str, output_file: str | None = None):
        self.url = url
        self.output_file = output_file

    @staticmethod
    def _make_file_title(title: str) -> str:
        return (title.lower().replace(' ', '_').replace(',', '').replace('.', '')
                .replace('ą', 'a').replace('ę', 'e').replace('ó', 'o')
                .replace('ś', 's').replace('ł', 'l').replace('ż', 'z')
                .replace('ź', 'z').replace('ć', 'c').replace('ń', 'n'))

    def __call__(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            prettified_html = soup.prettify()
            if self.output_file:
                name = self.output_file
            else:
                name = self._make_file_title(soup.title.string)

            with open(f"{name}.txt", "w", encoding="utf-8") as text_file:
                text_file.write(prettified_html)
        else:
            print(f"Failed to retrieve the web page. Status code: {response.status_code}")


if __name__ == '__main__':
    scrapper = Scrapper("https://pl.wikipedia.org/wiki/Python")
    scrapper()
