import os

BOOK_PATH = '../books/book.txt' if __name__ == '__main__' else 'books/book.txt'
PAGE_HEIGHT_LINES = 31
PAGE_WIDTH = 39

book: dict[int, str] = {}


def _get_part_text(text: str, start: int) -> tuple[str, int]:
    """
    Функция, возвращающая строку с текстом страницы и ее размер
    :param text: текст книги
    :param start: номер страницы
    :return: (текст страницы, размер страницы) """
    count_lines = 0
    current = start
    while count_lines < PAGE_HEIGHT_LINES and current < len(text):
        end_line = text.find('\n', current, current + PAGE_WIDTH)
        if end_line < 0:
            count_lines += 1
            current += PAGE_WIDTH
            while text[current + 1] != ' ':
                current -= 1
        else:
            count_lines += 1
            current = end_line + 1
    punctuation = {',', '.', '?', '!', ':', ';', '\n'}
    current = min(current, len(text) - 1)
    while text[current] not in punctuation or text[current + 1: current + 2] in punctuation:
        current -= 1
    return text[start: current + 1], current - start


def prepare_book(path: str = BOOK_PATH) -> None:
    with open(path) as f:
        text = f.read()
    page_number = 1
    start = 0
    page_size = 1000
    while start < len(text) and page_size > 0:
        page_text, page_size = _get_part_text(text, start)
        if page_size > 0:
            book[page_number] = page_text
        # print('Book preparing, page:', page_number, '    first symbol:', start, '    page_size:', page_size)
        # if page_number in [1, 100]:
        #     print(book[page_number])
        start += page_size + 1
        page_number += 1


prepare_book(os.path.join(os.getcwd(), BOOK_PATH))
