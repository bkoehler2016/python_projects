words = []

with open("words.txt") as f:
    for w in f:
        w = w.strip()
        words.append(w)
        
def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

#print(sorted(words.keys()))

from pprint import pprint

def anagrams():
    result = {}
    results_by_len = {}

    longest_sig = None
    longest_len = -1

    for w in words:  # O(n) over the number of words
        signature = "".join(sorted(w))

        if signature not in result:
            result[signature] = []

        result[signature].append(w)

        if len(result[signature]) >= longest_len:
            longest_len = len(result[signature])
            longest_sig = signature
 
    """
    for sigs in result:  # O(n) over the number of sigs
        l = len(result[sigs])
​
        if l not in results_by_len:
            results_by_len[l] = []
​
        results_by_len[l].append(result[sigs])
​
    for i in range(3,7):
        pprint(results_by_len[i])
    """

    return result[longest_sig]

pprint(anagrams())  # [listen, silent, ... ]