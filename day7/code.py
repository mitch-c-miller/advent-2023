from sys import path
path.append('../advent2023')

import utils
from functools import reduce
from collections import Counter
from enum import Enum

card_types = Enum('card_types', ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A'])
hand_types = Enum('hand_types', [
    'high card',
    'one pair',
    'two pair',
    'three of a kind',
    'full house',
    'four of a kind',
    'five of a kind',
])


def camel_cards(hands: list[dict[str, int]]):
    for hand in hands:
        hand['hand_value'] = hand_value(hand['cards'])
        hand['card_value'] = card_value(hand['cards'])
    
    hands.sort(key = lambda h: (h['hand_value'], h['card_value']))
    res = 0
    for i, hand in enumerate(hands):
        res += (i + 1) * hand['bid']
    return res


def hand_value(hand: str):
    cards = Counter(hand)
    card_counts = list(cards.values())
    max_card_count = max(card_counts)
    if max_card_count == 5: return hand_types['five of a kind'].value
    elif max_card_count == 4: return hand_types['four of a kind'].value
    elif max_card_count == 3 and card_counts.count(2) == 1: return hand_types['full house'].value
    elif max_card_count == 3 and card_counts.count(2) == 0: return hand_types['three of a kind'].value
    elif max_card_count == 2 and card_counts.count(2) == 2: return hand_types['two pair'].value
    elif max_card_count == 2 and card_counts.count(2) == 1: return hand_types['one pair'].value
    else: return hand_types['high card'].value


def card_value(hand: str):
    card_values = [card_types[card].value for card in hand]
    return card_values


if __name__ == '__main__':
    # test answer: 
    # prod answer: 
    data = utils.read_input(7, True)
    hands = []
    for hand in data:
        cards, bid = hand.split(' ')
        hands.append({'cards': cards, 'bid': int(bid)})
    print(camel_cards(hands))



    # test answer:
    # prod answer: 
    # data = utils.read_input(7, False)