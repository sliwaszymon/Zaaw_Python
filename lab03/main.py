import PyPDF2
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


class PDFConnector:
    file1_path: str
    file2_path: str
    output_file_path: str

    def __init__(self, file1_path: str, file2_path: str, output_file_path: str | None = None) -> None:
        self.file1_path = file1_path
        self.file2_path = file2_path
        self.output_file_path = output_file_path

    def __call__(self):
        pdf_writer = PyPDF2.PdfWriter()
        with open(self.file1_path, 'rb') as pdf1:
            pdf1_reader = PyPDF2.PdfReader(pdf1)
            for page_num in range(len(pdf1_reader.pages)):
                pdf_writer.add_page(pdf1_reader.pages[page_num])

        with open(self.file2_path, 'rb') as pdf2:
            pdf2_reader = PyPDF2.PdfReader(pdf2)
            for page_num in range(len(pdf2_reader.pages)):
                pdf_writer.add_page(pdf2_reader.pages[page_num])
        if self.output_file_path:
            output_name = self.output_file_path
        else:
            output_name = 'connected'
        with open(f'{output_name}.pdf', 'wb') as connected_file:
            pdf_writer.write(connected_file)


def zad1() -> None:
    connector = PDFConnector('pdf1.pdf', 'pdf2.pdf')
    connector()
    connector2 = PDFConnector('pdf2.pdf', 'pdf1.pdf', 'connected2')
    connector2()


def zad2() -> None:
    scrapper = Scrapper("https://pl.wikipedia.org/wiki/Python")
    scrapper()


def main() -> None:
    zad1()
    zad2()


if __name__ == '__main__':
    main()
