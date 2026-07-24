import csv

# my lab 2 - data detective

# open the file and read the tweets
def load_raw_data(filename):
    tweets = []
    file = open(filename)
    reader = csv.DictReader(file)
    for row in reader:
        tweets.append(row)
    return tweets


# quest 1 - clean the data
def clean_data(tweets):
    good_tweets = []
    bad = 0
    for t in tweets:
        if t["Text"] == "":
            bad = bad + 1
        else:
            if t["Likes"] == "":
                t["Likes"] = 0
                bad = bad + 1
            else:
                t["Likes"] = int(t["Likes"])
            if t["Retweets"] == "":
                t["Retweets"] = 0
                bad = bad + 1
            else:
                t["Retweets"] = int(t["Retweets"])
            good_tweets.append(t)
    print("bad rows fixed or removed:", bad)
    return good_tweets


# quest 2 - find the tweet with most likes
def find_viral_tweet(tweets):
    best = tweets[0]
    for t in tweets:
        if t["Likes"] > best["Likes"]:
            best = t
    return best


# quest 3 - sort by likes (bubble sort)
def custom_sort_by_likes(tweets):
    n = len(tweets)
    for i in range(n):
        for j in range(n - 1):
            if tweets[j]["Likes"] < tweets[j + 1]["Likes"]:
                a = tweets[j]
                tweets[j] = tweets[j + 1]
                tweets[j + 1] = a
    return tweets


# quest 4 - search for a word
def search_tweets(tweets, word):
    found = []
    for t in tweets:
        if word.lower() in t["Text"].lower():
            found.append(t)
    return found


# main
tweets = load_raw_data("twitter_dataset.csv")
print("loaded", len(tweets), "tweets")

tweets = clean_data(tweets)
print("clean tweets:", len(tweets))

viral = find_viral_tweet(tweets)
print("")
print("most viral tweet:")
print("user:", viral["Username"])
print("likes:", viral["Likes"])
print("text:", viral["Text"])

tweets = custom_sort_by_likes(tweets)
print("")
print("top 10 tweets:")
for t in tweets[:10]:
    print(t["Likes"], "likes -", t["Text"])

print("")
word = input("enter a word to search: ")
found = search_tweets(tweets, word)
print("found", len(found), "tweets")
for t in found:
    print(t["Text"])
