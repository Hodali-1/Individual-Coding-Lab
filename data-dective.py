import csv
import sys
import os

def load_raw_data(filename):
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    raw_tweets = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            raw_tweets.append(row)
    return raw_tweets

def clean_data(tweets):
    cleaned_tweets = []
    for tweet in tweets:
        if not tweet.get('Text'):
            continue
        if not tweet.get('Likes'):
            tweet['Likes'] = 0
        else:
            tweet['Likes'] = int(tweet['Likes'])
        if not tweet.get('Retweets'):
            tweet['Retweets'] = 0
        else:
            tweet['Retweets'] = int(tweet['Retweets'])
        cleaned_tweets.append(tweet)
    return cleaned_tweets

def find_viral_tweet(tweets):
    if not tweets:
        return None
    best_tweet = tweets[0]
    for tweet in tweets:
        if tweet['Likes'] > best_tweet['Likes']:
            best_tweet = tweet
    return best_tweet

def custom_sort_by_likes(tweets):
    n = len(tweets)
    for i in range(n):
        for j in range(0, n - i - 1):
            if tweets[j]['Likes'] < tweets[j + 1]['Likes']:
                tweets[j], tweets[j + 1] = tweets[j + 1], tweets[j]
    return tweets

def search_tweets(tweets, keyword):
    matching_tweets = []
    keyword_lower = keyword.lower()
    for tweet in tweets:
        if keyword_lower in tweet['Text'].lower():
            matching_tweets.append(tweet)
    return matching_tweets

if __name__ == "__main__":
    dataset = load_raw_data("twitter_dataset.csv")
    print(f"Loaded {len(dataset)} raw tweets.\n")
    clean_dataset = clean_data(dataset)
    print(f"Cleaned dataset has {len(clean_dataset)} tweets.\n")
    viral = find_viral_tweet(clean_dataset)
    print(f"Most viral tweet: {viral}\n")
    sorted_tweets = custom_sort_by_likes(clean_dataset)
    print("Top 3 tweets by likes:")
    for t in sorted_tweets[:3]:
        print(t)
    keyword = input("\nEnter a keyword to search for: ")
    results = search_tweets(clean_dataset, keyword)
    print(f"\nFound {len(results)} tweets matching '{keyword}':")
    for t in results:
        print(t)
