def filter_nums(nums: str) -> set[int]:
    return {int(n) for n in filter(lambda x: len(x.strip()) > 0, nums.split(' '))}
    
def play_card(card) -> int:
    matches = 0
    card_nums = card.split(' | ')
    win_nums = filter_nums(card_nums[0])
    play_nums = filter_nums(card_nums[1])
    
    for win_num in win_nums:
        if win_num in play_nums:
            matches += 1

    return matches

def part1(game_cards: list[str]) -> int:
    total_points = 0
    for game_card in game_cards:
        matches = play_card(game_card.split(':')[-1].strip())
        if 0 <= matches <= 2: total_points += matches
        else: total_points += 2 ** (matches - 1)
    
    return total_points

def part2(game_cards: list[str]) -> int:
    matches = []
    copies = []
    for game_card in game_cards:
        matches.append(play_card(game_card.split(':')[-1].strip()))
        copies.append(1)
    
    for i, match_res in enumerate(matches):
        for target in range(1, match_res + 1):
            copies[i + target] += copies[i]
    
    return sum(copies)

if __name__ == '__main__':
    TEST = False
    target = 'test' if TEST else 'input'
    # test answer: 13
    # prod answer: 26426
    with open(f'day4/{target}.txt', 'r') as data_f:
        data = data_f.read().strip().split('\n')
        print(part1(data))

    # test answer: 30
    # prod answer: 
    with open(f'day4/{target}.txt', 'r') as data_f:
        data = data_f.read().strip().split('\n')
        print(part2(data))
