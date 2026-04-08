import json 

def load_example(idx = 0, txt_only=True):
    with open("../Assignment_1_Assets/reviews_devset.json", "r", encoding = "utf-8") as f:
        data = f.read()

    check_split_method_correctness = len(data.split("reviewerID")) == len(data.split("\n"))
    assert check_split_method_correctness

    entries = data.split("\n")

    print(f"There are {len(entries)} reviews in the dataset.")

    sample_review = json.loads(entries[idx])
    
    if txt_only:
        return sample_review["reviewText"]
    else:
        return sample_review

if __name__== "__main__":
    single_review_obj = load_example(3, False)
    print(single_review_obj)
