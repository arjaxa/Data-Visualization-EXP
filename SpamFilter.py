from typing import Set
import re

def tokenize(text: str) -> set[str]:
    text = text.lower() # convert to lowercase
    all_words = re.findall("[a-z0-9]+", text) # extract the words, and
    return set(all_words) # remove duplicates