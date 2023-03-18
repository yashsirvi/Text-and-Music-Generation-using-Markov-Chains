import snscrape.modules.twitter as sntwitter
import pandas as pd 

attribute_container = []
user = "elonmusk"
n = 0
year = 2010
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f"from:{user}").get_items()):
    n+=1
    if n % 100 == 0:
        print(n, tweet.date.year, tweet.date.month, tweet.date.day)
    if  tweet.date.year < year:
        break
    attribute_container.append([tweet.rawContent])

tweets_df = pd.DataFrame(attribute_container, columns=["Tweets"])

# export df as csv
tweets_df.to_csv(f"./tweets/tweets_{user}_{n}.txt", index=False)