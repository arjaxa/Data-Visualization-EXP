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

        def train(self, messages: Iterable[Message]) -> None:
            for message in messages:
                # increment message counts
                if message.is_spam:
                    self.spam_messages += 1
                else:
                    self.ham_messages += 1

                # increment word counts
            for token in tokenize(message.text):
                self.tokens.add(token)
                if message.is_spam:
                    self.token_spam_counts[token] += 1
                else:
                    self.token_ham_counts[token] += 1       

        def _probabilities(self, token: str) -> Tuple[float, float]:
            """returns p(token|spam) and p(token|ham)"""
            spam = self.token_spam_counts[token]
            ham = self.token_ham_counts[token]

            p_token_spam = (spam + self.k) / (self.spam_messages + 2 * self.k)
            p_token_ham = (ham + self.k) / (self.ham_messages + 2 * self.k)

            return p_token_spam, p_token_ham                  