from typing import List
from collections import Counter


def raw_majority_votes(labels: list[str]) -> str:
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]
    return winner

assert raw_majority_votes(['a', 'b', 'c', 'd']) == 'b'

def majority_vote(labels: list[str]) -> str:
    """assumes that labels are cordered from nearest to farthest."""
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([Count
                       for count in vote_counts.values()
                       if count == winner_count])
    if num_winners == 1:
        return winner
    else:
        return majority_vote(labels[:1])
    
    assert majority_vote(['a', 'b', 'c', 'b', 'a']) == 'b'