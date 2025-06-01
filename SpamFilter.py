from typing import Set
import re
from typing import NamedTuple
from typing import List, Tuple, Dict, Iterable
import math
from collections import defaultdict

def tokenize(text: str) -> set[str]:
    text = text.lower() # convert to lowercase
    all_words = re.findall("[a-z0-9]+", text) # extract the words, and
    return set(all_words) # remove duplicates

assert tokenize("Data Science is science") == {"data", "science", "is"}

class Message(NamedTuple):
    text: str
    is_spam: bool

    class NaiveBayesClassifier:
        def __init__(self, k: float = 0.5) -> None:
            self.k = k # smoothing factor

            self.tokens: set[str] = set()
            self.token_spam_counts: Dict[str, int] = defaultdict(int)
            self.token_ham_counts: Dict[str, int] = defaultdict(int)
            self.spam_messages = self.ham_messages = 0