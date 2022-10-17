import util

# First of all, you may download the posts_java.zip, unzip it and move it to the /raw-data directory.

lines = util.load_xml("raw-data/posts_java.xml")
print("file loaded.")

# print("filtering")
lines = util.filter_closed_negative(lines)
print("\nfiltered")

util.save_xml(lines, 'processed/filtered.xml')

util.save_as_csv(lines, 'processed/filtered.csv', True)

samples = util.sample_k_from_list(2000, lines)

util.save_as_csv(samples, 'processed/sample.csv', True)
