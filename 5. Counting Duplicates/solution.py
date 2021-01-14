from collections import Counter

def duplicate_count(text):
    my_counter = Counter(text.lower())
    counter = 0
    for x in my_counter.values():
        if x > 1:
            counter += 1
    return counter
     
