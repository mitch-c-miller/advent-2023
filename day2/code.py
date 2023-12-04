from functools import reduce

LIMITS = {'red': 12, 'green': 13, 'blue': 14}

def game_scenario(path: str, style: str) -> int:
    res = 0
    with open(path, 'r') as games_f:
        games = games_f.read()
        for game in games.split('\n'):
            game_num, game_data = game.split(':')
            if style == 'max' and play_game(game_data.strip(), style):
                res += int(game_num.replace('Game ', ''))
            elif style == 'min':
                res += play_game(game_data.strip(), 'min')
    return res


def play_game(game: str, style: str) -> bool or int:
    colours = LIMITS.keys()
    colour_counts = {colour: 0 for colour in colours}
    for round in game.split(';'):
        for pull in round.split(','):
            count, colour = pull.strip().split(' ')
            colour_counts[colour] = max(int(count), colour_counts[colour])
            if style == 'max' and colour_counts[colour] > LIMITS[colour]:
                return False
    
    if style == 'max':
        return True
    elif style == 'min':
        return reduce((lambda x, y: x * y), colour_counts.values())


if __name__ == '__main__':
    print(game_scenario('day 2/input.txt', 'max'))
    print(game_scenario('day 2/input.txt', 'min'))
