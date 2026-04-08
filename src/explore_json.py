import json 

def load_example(idx = 0):
    with open("../Assignment_1_Assets/reviews_devset.json", "r", encoding = "utf-8") as f:
        data = f.read()

    check_split_method_correctness = len(data.split("reviewerID")) == len(data.split("\n"))
    assert check_split_method_correctness

    entries = data.split("\n")

    print(f"There are {len(entries)} reviews in the dataset.")

    sample_review = json.loads(entries[0])
    
    return sample_review["reviewText"]
