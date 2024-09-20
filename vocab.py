import pandas as pd
import nltk
from nltk.corpus import stopwords
import time
porter = nltk.PorterStemmer()
stopwords = nltk.corpus.stopwords.words('english')

# reading the data file to variable osdr
try:
    f = open('osdr_short.json')
    osdr = pd.read_json(f)
except Exception as e:
    print("Sorry, there was an error. Data file osdr_short.json is needed")
    print(e)
    
# variable for full text content
osdr_full_text = ""

# fetching the text content from osdr to osdr_full_text and testing for unwanted values
for ind in osdr.index:
    test_name = isinstance(osdr['name'][ind], str)
    test_descr = isinstance(osdr['description'][ind], str)
    if test_name and test_descr:
        osdr_full_text = osdr_full_text + osdr['name'][ind] + " " + osdr['description'][ind] + " "
    else:
        print("Bad values in data file index", ind)

print("\nFull text length", len(osdr_full_text))

# tokenizing full text, not everything is used
tokens = nltk.wordpunct_tokenize(osdr_full_text)
tokens_text = nltk.Text(tokens)
words = [w.lower for w in tokens_text]
vocabulary = sorted(set([word.lower() for word in tokens if word.isalpha()]))

# something unfinished
#fdist = nltk.FreqDist(osdr_full_text)
#print("Freqdist")
#print(fdist)

# creating trimmed vocabulary using stopwords
trimmed_vocabulary = []

for word in vocabulary:
    #print(word)
    if word not in stopwords:
        trimmed_vocabulary.append(word)

# stemming and tagging the trimmed vocabulary
stemmed_vocabulary = [porter.stem(t) for t in trimmed_vocabulary]
tagged_vocabulary = nltk.pos_tag(trimmed_vocabulary)

# printing vocabularies and some data

print("\nVocabulary")
print(vocabulary)

print("\nTrimmed vocabulary")
print(trimmed_vocabulary)

print("\nStemmed vocabulary")
print(stemmed_vocabulary)

print("\nTagged vocabulary")
print(tagged_vocabulary)

print(f"\nLength of the trimmed vocabulary: {len(trimmed_vocabulary)}")
print(f"Length of the original vocabulary {len(vocabulary)}")

print(f"Content fraction of trimmed / original vocabulary: {len(trimmed_vocabulary)/len(vocabulary)}")

# function for saving vocabulary files
def save_file(name, content):
    try:  
        f = open(f"{name}_{time.time()}.txt", "x")
        f.write("[")
        for index, word in enumerate(content):
            #len(content)
            if index < len(content)-1:
                f.write(f"'{word}', ")
            else:
                f.write(f"'{word}'")
        f.write("]")
        f.close()
        print(f"saved {name}_{time.time()}.txt")
    except Exception as e:
        print("Sorry, there was an error")
        print(e)

# prompting for saving vocabulary to a text file
print(f"\nSave vocabulary to text file? (y - Yes, anything else - No):")
inputcommand = input("")
if inputcommand == "y":
    save_file("vocabulary", vocabulary)

# prompting for saving trimmed vocabulary to a text file
print(f"\nSave trimmed vocabulary to text file? (y - Yes, anything else - No):")
inputcommand = input("")
if inputcommand == "y":
    save_file("trimmed_vocabulary", trimmed_vocabulary)

# prompting for saving stemmed vocabulary to a text file
print(f"\nSave stemmed vocabulary to text file? (y - Yes, anything else - No):")
inputcommand = input("")
if inputcommand == "y":
    save_file("stemmed_vocabulary", stemmed_vocabulary)

# prompting for saving tagged vocabulary to a text file
print(f"\nSave tagged vocabulary to text file? (y - Yes, anything else - No):")
inputcommand = input("")
if inputcommand == "y":
    save_file("tagged_vocabulary", tagged_vocabulary)

print("End of program")