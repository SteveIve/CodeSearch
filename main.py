import util

lines = util.load_xml("raw-data/posts_java.xml")
for line in lines:
    print(line)
print(len(lines))