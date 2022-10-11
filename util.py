def filter_closed(path_in, path_out):
    with open(path_in, "r", encoding="utf-8") as f_in:
        with open(path_out, "w", encoding="utf-8") as f_out:
            read_lines = f_in.readlines()
            for line in read_lines:
                if line.find("CloseDate=") > -1:
                    f_out.write(line)


def xml2csv(file):
    pass
