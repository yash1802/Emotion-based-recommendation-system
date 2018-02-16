import ast
import nltk
from nltk.corpus import stopwords
from collections import Counter 
from random import randint

def create_tuples( fileName ):
	file_open = open(fileName)
	file_read = file_open.read()
	collection = ast.literal_eval(file_read)
	result = []
	for i in collection:
		record = (i["lyric"], i["sentiment"])
		result.append(record)
	return result
	
def stop_words_removal(lyrics):
	array = []
	for i in lyrics:
		sentiment = i[1]
		stop = set(stopwords.words('english')) 
		filtered_words = [word for word in i[0].split() if word not in stop]
		combine = (filtered_words , sentiment)
		array.append(combine)
	return array 

def get_words(lyrics):
	all_words = []
	for(words, sentiment) in lyrics:
		all_words.extend(words)
	return all_words

def word_features(List_word):
	List_word = nltk.FreqDist(List_word)
	word_features = List_word.keys()
	return word_features

def extract_features(doc):
	doc_words = set(doc)
	features = {}
	for word in word_features: 
		features['contains(%s)' %word] = (word in doc_words)
	return features 
 
def stop_word_removal1(lyrics):
    stop = set(stopwords.words('english'))
    filtered_words = [word for word in lyrics.split() if word not in stop]
    return filtered_words
    
def user_sentiment(file):
    file_open = open(file)
    file_read = file_open.read()
    file_split=file_read.split("|")
    result_list=[]
    for lyrics in file_split:
        filtered_lyrics=stop_word_removal1(lyrics)
        output = classifier.classify(extract_features(filtered_lyrics))
        result_list.append(output)
    return result_list

def recommendedSong(history):
    c= Counter(history)
    file_open = open("/home/yash/Desktop/project_lyrics/code/training.txt")
    file_read = file_open.read()
    collection = ast.literal_eval(file_read)
    if c['P']>=c['N']:
        songs_positive=[i for i in collection if i["sentiment"]=='P']
        return songs_positive[randint(0,len(songs_positive)-1)]["name"]
    else:
        songs_negative=[i for i in collection if i["sentiment"]=='N']
        return songs_negative[randint(0,len(songs_negative)-1)]["name"]
        
lyrics = create_tuples("/home/yash/Desktop/project_lyrics/code/training.txt")
filtered_corpus = stop_words_removal(lyrics)
word_features = word_features(get_words(filtered_corpus))
training_set = nltk.classify.apply_features(extract_features,filtered_corpus)
classifier = nltk.NaiveBayesClassifier.train(training_set)

lyrics_test = create_tuples("/home/yash/Desktop/project_lyrics/code/testing.txt")
test_corpus = stop_words_removal(lyrics_test)
test_set = nltk.classify.apply_features(extract_features,test_corpus)

print "\t" + "Accuracy:" + str(nltk.classify.accuracy(classifier, test_set))

def sentiment(output):
    if str(output) == "P":
        return "Positive"
    if str(output) == "N":
        return "Negative"
    if str(output) == "A":
        return "Sentiment not defined"

        
lyrics = "Gotta take my chance tonight"
output = classifier.classify(extract_features(lyrics.split()))
print sentiment(output)

file_open = open("/home/yash/Desktop/project_lyrics/code/Last_5_Songs.txt")
file_read = file_open.read()
file_split=file_read.split("|")
result_list=[]

sentiment_history= user_sentiment("/home/yash/Desktop/project_lyrics/code/Last_5_Songs.txt") 
print "recommended: " + recommendedSong(sentiment_history)      