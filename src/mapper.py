import re
import sys
from explore_json import load_example
from nonstopword import load_stopwords, process_stopwords

# Tokenization to unigrams, using whitespaces, tabs, digits, 
# and the characters ()[]{}.!?,;:+=-# _"'`~#@&*%€$§\/ as delimiters
pattern = re.compile(r"[\s()\[\]{}.!?,;:+=\-_\"'`~#@&*%€$§\\/]+")

def map_line(line, stopwords, category):
    sanitized_category = category.replace("\t", " ") # since we emit tuples separated by tabs, we want to avoid tabs in the tokens or categories.
    tokens = pattern.split(line.strip())        
    for token in tokens:        
        if token and len(token) > 1 and token.lower() not in stopwords:  # avoid emitting empty strings, single-character tokens and stopwords                
            print(f"{token.lower()}\t{sanitized_category}") # Emit unigrams after case folding, separated by tabs (which were removed by \s as delimiters)

def mapper():
    stopwords = process_stopwords(load_stopwords("../Assignment_1_Assets/stopwords.txt"))
    for line in sys.stdin: # TODO: Hadoop input should actually be stdin       
        map_line(line, stopwords)

if __name__ == "__main__":
    
    x = load_example()
    stopwords = process_stopwords(load_stopwords("../Assignment_1_Assets/stopwords.txt"))
    map_line(x, stopwords)
    