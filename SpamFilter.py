from typing import Set
import re
from typing import NamedTuple

def tokenize(text: str) -> set[str]:
    text = text.lower() # convert to lowercase
    all_words = re.findall("[a-z0-9]+", text) # extract the words, and
    return set(all_words) # remove duplicates

assert tokenize("Data Science is science") == {"data", "science", "is"}

class Message(NamedTuple):
    text: str
    is_spam: bool