import re
import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('stopwords')
nltk.download('vader_lexicon')

with open("miracle_in_the_andes.txt", "r", encoding="utf8") as file:
    book = file.read()

print("How many chapters are there?")
print(book.count("Chapter"))
pattern = re.compile("Chapter [0-9]+")
findings = re.findall(pattern, book)
print(len(findings))

print("Which are sentences where 'love' was used?")
pattern = re.compile("[A-Z]{1}[^.]*[^a-zA-Z]+love[^a-zA-Z]+[^.]*.")
findings = re.findall(pattern, book)
print(findings)
print(len(findings))

print("What are the most used words?")
pattern = re.compile("[a-zA-Z]+")
findings = re.findall(pattern, book.lower())
d = {}
for word in findings:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1

d_list = [(value, key) for (key, value) in d.items()]
d_list = sorted(d_list, key=lambda x: x[0], reverse=True)
print(d_list[:10])

print("What are the most used words? (non articles)")
english_stopwords = stopwords.words("english")
filtered_words = []
for count, word in d_list:
    if word not in english_stopwords:
        filtered_words.append((word, count))
print(filtered_words[:5])

print("What is the most positive and the most negative chapter")
analyzer = SentimentIntensityAnalyzer()
pattern = re.compile("Chapter [0-9]+")
chapters = re.split(pattern, book)
for nr, chapter in enumerate(chapters):
    scores = analyzer.polarity_scores(chapter)
    print(nr, scores)
