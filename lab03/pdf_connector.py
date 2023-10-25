import PyPDF2


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


if __name__ == '__main__':
    connector = PDFConnector('pdf1.pdf', 'pdf2.pdf')
    connector()
    connector2 = PDFConnector('pdf2.pdf', 'pdf1.pdf', 'connected2')
    connector2()
