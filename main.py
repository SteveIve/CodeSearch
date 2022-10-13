import zipfile

import util

# First, we unzip the posts_java.zip file
with zipfile.ZipFile('raw-data/posts_java.zip') as zf:
    zf.extractall('raw-data/')

# Filter out posts with negative score
util.filter_negative_score("raw-data/posts_java.xml", "raw-data/posts_without_neg.xml")
print("done filtering neg")

# Filter out posts with closed tag
util.filter_closed('raw-data/posts_without_neg.xml', 'raw-data/posts_without_closed.xml')
print("done filtering closed")

# Convert xml into csv and keep questions only
util.xml2csv('raw-data/posts_without_closed.xml', 'raw-data/posts.csv', True)
print("done converting into csv")

# Split
util.csv_split('raw-data/posts.csv', 'split/', 10000)
print("done splitting")
