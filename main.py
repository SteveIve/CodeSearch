import time
import zipfile
import util

# First, we unzip the posts_java.zip file
start = time.perf_counter()
with zipfile.ZipFile('raw-data/posts_java.zip') as zf:
    zf.extractall('raw-data/')
end = time.perf_counter()
print("done unzipping file")
print("it takes %.2f seconds to unzip the file" % (end-start))

# Filter out posts with negative score
start = time.perf_counter()
util.filter_negative_score("raw-data/posts_java.xml", "raw-data/posts_without_neg.xml")
end = time.perf_counter()
print("done filtering neg")
print("it takes %.2f seconds to filter out posts with negative score" % (end-start))

# Filter out posts with closed tag
start = time.perf_counter()
util.filter_closed('raw-data/posts_without_neg.xml', 'raw-data/posts_without_closed.xml')
end = time.perf_counter()
print("done filtering closed")
print("it takes %.2f seconds to filter out posts with closed tag" % (end-start))

# Convert xml into csv and keep questions only
start = time.perf_counter()
util.xml2csv('raw-data/posts_without_closed.xml', 'raw-data/posts.csv', True)
end = time.perf_counter()
print("done converting into csv")
print("it takes %.2f seconds to convert xml into csv, and keep questions only" % (end-start))

# Split
start = time.perf_counter()
num = util.csv_split('raw-data/posts.csv', 'split/', 10000)
end = time.perf_counter()
print("done splitting")
print("it takes %.2f seconds to split %d files." % ((end-start), num))
