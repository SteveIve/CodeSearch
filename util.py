import csv
import random
import sys
import xml.etree.ElementTree as ET

from tqdm import tqdm


def load_xml(path, encoding="UTF-8"):
    with open(path, "r", encoding=encoding) as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
    return lines


def filter_closed_negative(seq: list[str]):
    i = 0
    while i < len(seq):
        progress_bar(i, len(seq), "filtering")
        line = seq[i]
        if line.find("ClosedDate=") > -1:
            del seq[i]
        elif line.find('Score="-') > -1:
            del seq[i]
        else:
            i += 1
    return seq


def save_xml(lines: list[str], path):
    with open(path, 'w', encoding='utf-8') as file:
        for line in tqdm(lines, desc="saving as xml"):
            file.write(line + "\n")


def progress_bar(index, total, desc='processing'):
    # TODO wrong here
    print('\r', end='')
    num = int(index / total * 100)
    por_num = int(num * 0.5)
    print("{}: {}%: ".format(desc, num), "▋" * por_num, end="")
    sys.stdout.flush()


def save_as_csv(lines: list[str], path, question_only):
    line_num = len(lines)
    with open(path, 'w', encoding='utf-8', newline='') as f_write:
        csv_writer = csv.writer(f_write)
        for i in tqdm(range(line_num), desc="converting into csv"):
            line = lines[i]
            post = dict(ET.fromstring(line).attrib)
            if question_only:
                csv_writer.writerow([i, post['Title']])
                continue
            csv_writer.writerow([i, post['Id'], post['PostTypeId'],
                                 -1 if 'AcceptedAnswerId' not in post.keys() else post['AcceptedAnswerId'],
                                 post['CreationDate'],
                                 post['Score'], post['ViewCount'], post['Body'],
                                 -1 if 'OwnerUserId' not in post.keys() else post['OwnerUserId'],
                                 -1 if 'LastEditorUserId' not in post.keys() else post['LastEditorUserId'],
                                 -1 if 'LastEditDate' not in post.keys() else post['LastEditDate'],
                                 post['LastActivityDate'],
                                 post['Title'], post['Tags'], post['AnswerCount'], post['CommentCount'],
                                 -1 if 'FavoriteCount' not in post.keys() else post['FavoriteCount'],
                                 post['ContentLicense']])
            # TODO: Hard-coded..need fix
            continue
        f_write.flush()


def sample_k_from_list(k: int, lines: list[str]):
    lines = random.sample(lines, k)
    return lines
