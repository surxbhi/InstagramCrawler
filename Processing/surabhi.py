import nltk
import string
from nltk.corpus import stopwords 
from nltk.stem import WordNetLemmatizer 
import pandas as pd
# import the inflect library 
import inflect 
# Tokenize version 2
from nltk.tokenize import TweetTokenizer

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
def tokenizewordsTweet(areview):
  tknzr = TweetTokenizer()
  review_tokenized = tknzr.tokenize(areview)
  return review_tokenized
def text_lowercase(text): 
    return text.lower()

p = inflect.engine() 

# convert number into words 
def convert_number(text): 
	# split string into list of words 
	temp_str = text.split() 
	# initialise empty list 
	new_string = [] 

	for word in temp_str: 
		# if word is a digit, convert the digit 
		# to numbers and append into the new_string list 
		if word.isdigit(): 
			temp = p.number_to_words(word) 
			new_string.append(temp) 

		# append the word as it is 
		else: 
			new_string.append(word) 

	# join the words of new_string to form a string 
	temp_str = ' '.join(new_string) 
	return temp_str 

# remove punctuation 
def remove_punctuation(text): 
	translator = str.maketrans('', '', string.punctuation) 
	return text.translate(translator) 

# remove whitespace from text 
def remove_whitespace(text): 
	return " ".join(text.split())


# remove stopwords function 
def remove_stopwords(text): 
  stop_words = set(stopwords.words("english"))
  word_tokens = tokenizewordsTweet(text)
  print(word_tokens)
  word_tokens = [word for word in word_tokens if word.isalpha()]
  filtered_text = [word for word in word_tokens if word not in stop_words]
  filtered_text = " ".join(filtered_text)

  return filtered_text

lemmatizer = WordNetLemmatizer() 
# lemmatize string 
def lemmatize_word(text):
	word_tokens = tokenizewordsTweet(text)
	lemmas = [lemmatizer.lemmatize(word, pos ='v') for word in word_tokens]
	return lemmas 

# Simply call this to do all the data pre-processing
def NewPreProcessing(text):
  new_text = text_lowercase(text)
  new_text = convert_number(new_text)
  new_text = remove_punctuation(new_text)
  new_text = remove_whitespace(new_text)
  new_text = remove_stopwords(new_text)
  new_text = lemmatize_word(new_text)
  replacement_review=" ".join(new_text)
  
  return replacement_review

abc_news = pd.read_csv("final_abc_news_comment.csv")

#au_news["comment"]

listt = abc_news["comment"].tolist()
# listt //list form
#au_news['processed comments'] = process_comments
without_micro_text = listt
with_micro_text = listt
i = 0
for row in listt:
  with_micro_text[i] = NewPreProcessing(row)
  i = i + 1
  print(i)

#Convert list of tuples to dataframe and set column names and indexes
with_micro_text_df = pd.DataFrame(with_micro_text, columns = ['processed_comments_without_microtext']) 
abc_news['processed_comments_without_microtext'] = with_micro_text_df['processed_comments_without_microtext']
abc_news.to_csv('final_abc_news_processed_comment.csv')