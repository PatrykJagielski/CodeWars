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

def is_straight_flush(hole_cards, community_cards):
    return False

def is_pair(hole_cards, community_cards):
    seen = set()
    all_cards = hole_cards + community_cards
    all_cards.sort(key=lambda card: RANK.index(card[0]))
    all_cards_ranks = [x[0] for x in all_cards]
    pairs = [x for x in all_cards_ranks if x in seen or seen.add(x)] 
    pairs.sort(key=lambda card: RANK.index(card[0])) # sort pairs
    all_cards_ranks = [x for x in all_cards_ranks if x not in pairs] # cards without pairs
    if len(pairs) == 2 and pairs[0] == pairs[1]:
        return ("three-of-a-kind", pairs[:1] + all_cards_ranks[:2])
    if len(pairs) == 2:
        return ("two pair", pairs + all_cards_ranks[:1])
    elif len(pairs) == 1:
        return ("pair", pairs + all_cards_ranks[:3])
    else:
        return ("nothing", all_cards_ranks[:5])

def is_straight(hole_cards, community_cards):
    all_cards = hole_cards + community_cards
    all_cards.sort(key=lambda card: RANK.index(card[0]))
    all_cards_ranks = [x[0] for x in all_cards]
    for i in range(3):
        s = "".join(all_cards_ranks[i:i+5])
        if s in RANKS:
            return("straight", all_cards_ranks[i:i+5])

def hand(hole_cards, community_cards):
    match = is_straight_flush(hole_cards, community_cards)
    if match:
        return match
    
    match = is_straight(hole_cards, community_cards)
    if match:
        s, m = match
        return (s, list(map(lambda x: "10" if x == "1" else x, m)))
    
    match = is_pair(hole_cards, community_cards)
    if match:
        return match
    