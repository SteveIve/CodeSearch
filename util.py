import csv
import os.path


def filter_closed(path_in, path_out):
    # noinspection GrazieInspection
    """
        filter out all questions tagged as "CLOSED"

        :param path_in: path of reading file
        :param path_out: path to write
        """
    with open(path_in, "r", encoding="utf-8") as f_in:
        with open(path_out, "w", encoding="utf-8") as f_out:
            read_lines = f_in.readlines()
            for line in read_lines:
                if line.find("CloseDate=") > -1:
                    f_out.write(line)


def xml2csv(read_path: str, write_path: str, question_only: bool):
    """
    convert xml into csv, All attributes but question title will be removed.

    :param question_only: whether ignoring other attributes
    :param read_path: i.e. path of xml file
    :param write_path: i.e. path of csv file
    """
    import xml.etree.ElementTree as ET
    with open(read_path, 'r', encoding='latin1') as f_read:
        read_lines = f_read.readlines()
        line_num = len(read_lines)
        with open(write_path, 'w', encoding='utf-8', newline='') as f_write:
            csv_writer = csv.writer(f_write)
            for i in range(line_num):
                line = read_lines[i]
                post = dict(ET.fromstring(line).attrib)
                if question_only:
                    csv_writer.writerow([i, post['Body']])
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


def csv_split(file_path: str, folder: str, split_lines: int):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        total = len(lines)
        full_split = total // split_lines
        last_lines = total - (full_split * split_lines)
        cursor = 0
        file_name_head = os.path.join(folder, 'split')
        pass
