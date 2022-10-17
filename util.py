def load_xml(path, encoding="UTF-8"):
    with open(path, "r", encoding=encoding) as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
    return lines
