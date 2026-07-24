#!/bin/bash

# feed-analyzer.sh
# quest 2 but in bash - find the top 5 most active users

file=$1

echo "Top 5 Most Active Users:"

# get the username column (field 2), skip the header line,
# count each user, sort by the biggest count, take the top 5
tail -n +2 $file | cut -d',' -f2 | sort | uniq -c | sort -nr | head -5
