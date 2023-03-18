import re 

file = "tweets/tweets_elonmusk_21032.txt"
output = "./data/elonmusk.txt"
# read the file
with open(file, "r") as f:
    line = f.read().replace("\n", " ")
    line = re.sub(r"[\[\]\"”’\'()]", "", line)
    line = re.sub(r'https?://[\n\S]+\b', 'URL', line)
    line = re.sub(r'&amp;', '&', line)
    line = re.sub(r'@', 'user', line)
    line = re.sub(r'_', '', line)

with open(output, "w") as f:
    f.write(line)