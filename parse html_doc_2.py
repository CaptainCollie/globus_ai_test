import re
import datetime
from bs4 import BeautifulSoup


def parse_html(path_to):
    soup = BeautifulSoup(open(path_to, 'r'), 'lxml')
    rows = soup.find_all(class_='MsoNormal')
    rows = list(map(lambda x: x.text, rows))
    matched = []
    for row in rows:
        tmp = re.findall(r'(?<=Frist for svar )\d{,2}.\d{,2}.kl \d{,2}.\d{,2}', row)
        if tmp:
            matched.extend(tmp)
    result = []
    for time in matched:
        tmp = [i.replace('.kl', '') for i in time.split()]
        day, month = list(map(int, tmp[0].split('.')))
        hour, min = list(map(int, tmp[1].split('.')))
        d = datetime.datetime(year=datetime.date.today().year, month=month, day=day, hour=hour, minute=min)
        d = d.strftime('%Y-%m-%dT%H:%M:%S')
        result.append(d)
    return result


if __name__ == '__main__':
    path_to = 'files/source_for_extract_deadline_date_time.html'
    print(*parse_html(path_to))
