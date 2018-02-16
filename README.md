A music recommendation system based on sentiment analysis.

This is a recommendation system based on content filtering. Here, sentiment analysis is performed on lyrics and the songs with matching sentiment values are suggested.

Training process:
1. Identify sentiments from training data.         
2. Remove stop words.
3. Create a bag of words for all songs.
4. Find the frequency distribution of all words.
5. Apply features to a filtered corpus and use an algorithm (in this case, Naive-Bayes) to train the classifier.

The Recommendation is based on the last 5 songs the user listens to (Last_5_Songs.txt).
1. Identify the sentiments of the songs in user's history.
2. Calculate the majority sentiment.
3. Recommended a song (selected at random) of the same sentiment.

