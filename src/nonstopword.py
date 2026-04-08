
# Stopword filtering: use the stop word list [on TUWEL] (stopwords.txt) . In addition, filter out all
# tokens consisting of only one character

def load_stopwords(path):
    with open(path, "r", encoding = "utf-8") as f:
        data = f.read()
    
    return data

def process_stopwords(data):
    stopwords = []
    for line in data.split("\n"):
        if line.strip():
            stopwords.append(line.strip().lower())
    
    return set(stopwords)

if __name__ == "__main__":
    rel_path = "../Assignment_1_Assets/stopwords.txt"
    data = load_stopwords(rel_path)
    data = process_stopwords(data)
    print(data)
