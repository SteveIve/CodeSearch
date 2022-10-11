import csv


def filter_closed(path_in, path_out):
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


def xml2csv(read_path, write_path):
    """
    convert xml into csv, All attributes but question title will be removed.

    :param read_path: i.e. path of xml file
    :param write_path: i.e. path of csv file
    """
    import xml.etree.ElementTree as ET
    with open(read_path, 'r', encoding='latin1') as f_read:
        read_lines = f_read.readlines()
        line_num = len(read_lines)
        with open(write_path, 'w', encoding='utf-8', newline='') as f_write:
            csv_writer = csv.writer(f_write)
            keys = list(dict(ET.fromstring(read_lines[0]).attrib).keys())
            for i in range(line_num):
                line = read_lines[i]
                post = dict(ET.fromstring(line).attrib)
                csv_writer.writerow([i, post['Body']])
                f_write.flush()


def csv_split(backups: int):
    # TODO
    pass
