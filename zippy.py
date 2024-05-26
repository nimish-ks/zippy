import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup, NavigableString
import argparse
import os


def parse_algorithm(algorithm):
    try:
        res = {
            'exclude': True,
            'sizes': [],
            'restRatio': 0.4
        }
        parts = algorithm.split(" ")

        if parts[0] == "+":
            res['exclude'] = False

        res['restRatio'] = float(parts[-1])

        for i in range(1, len(parts) - 1):
            res['sizes'].append(int(parts[i]))

        return res
    except:
        defaultRes = {
            'exclude': True,
            'sizes': [1, 1, 2],
            'restRatio': 0.4
        }
        return defaultRes


def bionify_word(word, algorithm, common_words):
    def is_common(word):
        return word.lower() in common_words

    index = len(word) - 1
    num_bold = 1

    if len(word) <= 3 and algorithm['exclude']:
        if is_common(word):
            return word

    if index < len(algorithm['sizes']):
        num_bold = algorithm['sizes'][index]
    else:
        num_bold = int(len(word) * algorithm['restRatio'])

    return f"<b>{word[:num_bold]}</b>{word[num_bold:]}"


def bionify_text(text, algorithm, common_words):
    res = ""
    for word in text.split(" "):
        res += bionify_word(word, algorithm, common_words) + " "
    return res.strip()


def bionify_node(node, algorithm, common_words):
    if node is None or (isinstance(node, str) and node.strip() == "") or node.name in ["script", "style"]:
        return
    if isinstance(node, NavigableString):
        bionified_html = bionify_text(node, algorithm, common_words)
        new_soup = BeautifulSoup(bionified_html, 'html.parser')
        node.replace_with(new_soup)
    else:
        for child in list(node.children):
            bionify_node(child, algorithm, common_words)


def bionify_ebook(input_path, output_path, algorithm_str):
    book = epub.read_epub(input_path)
    common_words = ["the", "be", "to", "of", "and", "a", "an", "it", "at", "on", "he", "she", "but", "is", "my"]
    algorithm = parse_algorithm(algorithm_str)
    
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        soup = BeautifulSoup(item.get_body_content(), 'html.parser')
        if soup.body is not None:
            bionify_node(soup.body, algorithm, common_words)
            item.set_content(str(soup))
    
    epub.write_epub(output_path, book)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bionify ePub eBooks.")
    parser.add_argument('input', help="Input ePub file path")
    parser.add_argument('output', help="Output ePub file path")
    parser.add_argument('--algorithm', default="- 0 1 1 2 0.4", help="Bionification algorithm")
    args = parser.parse_args()

    bionify_ebook(args.input, args.output, args.algorithm)
