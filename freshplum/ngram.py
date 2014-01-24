'''
Write a function to count the number of occurrences of each n-gram in a given input text (see http://en.wikipedia.org/wiki/N-gram for a definition).

ex. for n=2, "to be or not to be" yields
  "to be": 2
  "be or": 1
  "or not": 1
  "not to": 1
'''

from collections import defaultdict

def ngram_count(text, n):
    counts = defaultdict(lambda: 0)
    start, end = 0, n # window used to retrieve n-gram
    text = text.split()
    
    # for n-gram in sliding-window-of-size-n
    for _ in text:
        # stop when window reaches the end
        if end == len(text) + 1: break
    
        # extract ngram
        ngram = " ".join(text[start:end])
        
        # increment ngram count
        if ngram in counts:
            counts[ngram] += 1
        else:
            counts[ngram] = 1
        
        # increment window
        start, end = start+1, end+1
            
    return counts

# test
for ngram, count in ngram_count(text="to be or not to be", n=2).items():
    print "{0}: {1}".format(ngram,count)
''' test output
be or: 1
to be: 2
not to: 1
or not: 1
'''
