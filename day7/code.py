from sys import path
path.append('../advent2023')

import utils
from collections import Counter
from enum import Enum

std_card_types = Enum('card_types', ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'])
jokers_card_types = Enum('card_types', ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A'])
hand_types = Enum('hand_types', [
    'high card',
    'one pair',
    'two pair',
    'three of a kind',
    'full house',
    'four of a kind',
    'five of a kind',
])


def camel_cards(hands: list[dict[str, int]], jokers=False):
    for hand in hands:
        hand_value = jokers_hand_value if jokers else std_hand_value
        hand['hand_value'] = hand_value(hand['cards']).value
        hand['card_value'] = card_value(hand['cards'], jokers)
    
    hands.sort(key = lambda h: (h['hand_value'], h['card_value']))

    res = 0
    for i, hand in enumerate(hands):
        res += (i + 1) * hand['bid']
    return res


def std_hand_value(hand: str) -> hand_types:
    cards = Counter(hand)
    card_counts = list(cards.values())
    max_card_count = max(card_counts)
    if max_card_count == 5: return hand_types['five of a kind']
    elif max_card_count == 4: return hand_types['four of a kind']
    elif max_card_count == 3 and card_counts.count(2) == 1: return hand_types['full house']
    elif max_card_count == 3 and card_counts.count(2) == 0: return hand_types['three of a kind']
    elif max_card_count == 2 and card_counts.count(2) == 2: return hand_types['two pair']
    elif max_card_count == 2 and card_counts.count(2) == 1: return hand_types['one pair']
    else: return hand_types['high card']


def jokers_hand_value(hand: str) -> int:
    sub_j_hand = hand.replace('J', '')
    num_j = 5 - len(sub_j_hand)
    
    if num_j == 5: return hand_types['five of a kind']
    
    cards = Counter(sub_j_hand)
    card_counts = list(cards.values())
    max_card_count = max(card_counts)
    max_card = list(filter(
        lambda x: x[1] == max_card_count,
        cards.items()
    ))[0][0]
    
    new_hand = sub_j_hand + (max_card * num_j)
    return std_hand_value(new_hand)


def card_value(hand: str, jokers=False) -> list[int]:
    if jokers: return [jokers_card_types[card].value for card in hand]
    else: return [std_card_types[card].value for card in hand]


if __name__ == '__main__':
    data = utils.read_input(7, True)
    hands = []
    for hand in data:
        cards, bid = hand.split(' ')
        hands.append({'cards': cards, 'bid': int(bid)})

    # test answer: 6440
    # prod answer: 253910319
    print(camel_cards(hands))

    # test answer: 5905
    # prod answer: 254083736
    print(camel_cards(hands, True))