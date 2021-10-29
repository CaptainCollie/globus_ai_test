from docx2python import docx2python
import re


def parse_word(path_to):
    text = docx2python(path_to).body
    profession_line = []
    for table in text:
        for row in table:
            for cell in row:
                if 'Stillingskategori' in cell:
                    profession_line.extend(row)
    result = []
    for cell in profession_line:
        tmp = re.findall(r'(?<=\d )[a-zA-Z]+', ''.join(cell))
        if tmp:
            result.extend(tmp)

    return result


if __name__ == '__main__':
    path_to = 'files/source_document_for_multiple_needs__roles_with_positions_amount.docx'
    print(parse_word(path_to))
