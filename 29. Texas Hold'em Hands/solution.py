from collections import Counter

RANK = [
    "A",
    "K",
    "Q",
    "J",
    "1", #10
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2",
]

SUITS = '♦♥♠♣'
RANKS = 'AKQJ198765432'

def is_straight_flush(all_cards):
    f = is_flush(all_cards)
    s = is_straight(all_cards)
    if f and s:
        return ("straight-flush", f[1])

def is_pair(all_cards):
    seen = set()
    all_cards_ranks = [x[0] for x in all_cards]
    all_cards_copy = all_cards_ranks.copy()
    c = Counter(all_cards_ranks)
    pairs = [x for x in all_cards_ranks if x in seen or seen.add(x)] 
    pairs.sort(key=lambda card: RANK.index(card[0])) # sort pairs
    all_cards_ranks = [x for x in all_cards_ranks if x not in pairs] # cards without pairs
    
    if c.most_common(1)[0][1] == 4:
        return ("four-of-a-kind", [c.most_common(1)[0][0], list(filter(lambda x: x != c.most_common(1)[0][0], all_cards_copy))[0]])
    if c.most_common(2)[0][1] + c.most_common(2)[1][1] == 5:
        return ("full house", [c.most_common(2)[0][0], c.most_common(2)[1][0]])
    if len(pairs) == 2 and pairs[0] == pairs[1]:
        return ("three-of-a-kind", pairs[:1] + all_cards_ranks[:2])
    if len(pairs) == 2:
        return ("two pair", pairs + all_cards_ranks[:1])
    elif len(pairs) == 1:
        return ("pair", pairs + all_cards_ranks[:3])
    else:
        return ("nothing", all_cards_ranks[:5])

def is_straight(all_cards):
    all_cards_ranks = [x[0] for x in all_cards]
    for i in range(3):
        s = "".join(all_cards_ranks[i:i+5])
        if s in RANKS:
            return("straight", all_cards_ranks[i:i+5])

def is_flush(all_cards):
    all_cards_suits = [x[-1] for x in all_cards]
    all_cards_ranks = [x[0] for x in all_cards]
    c = Counter(all_cards_suits)
    if c.most_common(1)[0][1] >= 5:
        return ("flush", list(map(lambda x: x[0:-1],list(filter(lambda x: x[-1] in c.most_common(1)[0][0], all_cards))[:5])) )

def hand(hole_cards, community_cards):
    list_of_functions = [is_straight_flush, is_flush, is_straight, is_pair]
    all_cards = hole_cards + community_cards
    all_cards.sort(key=lambda card: RANK.index(card[0]))

    for f in list_of_functions:
        match = f(all_cards)
        if match:
            s, m = match
            return (s, list(map(lambda x: "10" if x == "1" else x, m)))
    