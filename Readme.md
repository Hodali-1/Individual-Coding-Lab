# Lab 2 - The Social Media Data Detective

This is my project for Lab 2. It reads a CSV file of tweets and does a few things with it.
For the sorting and finding the max I wrote my own loops, I did not use `.sort()`, `sorted()` or `max()`.

## Files

- `data-detective.py` - the python program
- `feed-analyzer.sh` - the bash script that shows the top 5 users
- `twitter_dataset.csv` - the data file

## How to run the python program

Put the CSV in the same folder and run:

```
python3 data-detective.py
```

It will:
1. Clean the data and print how many bad rows were fixed or removed.
2. Print the tweet with the most likes.
3. Print the top 10 tweets by likes.
4. Ask you for a word and print the tweets that have that word.

## How to run the bash script

First make it runnable, then run it with the CSV:

```
chmod +x feed-analyzer.sh
./feed-analyzer.sh twitter_dataset.csv
```

It prints the 5 users that appear the most times.

## How my sorting works

My sort is a bubble sort. It keeps going through the list and compares each tweet with the
next one, and if the next one has more likes it swaps them, so the bigger numbers slowly move
to the top. It repeats this until the whole list is sorted from most likes to least likes.
