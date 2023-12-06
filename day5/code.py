from sys import path
path.append('../advent2023')

from string import digits, ascii_lowercase
import utils

def seeds(mappings: list[str], part: int = 1) -> dict[int, int]:
    res, nums = {}, []
    if part == 1:
        res = {
            int(seed): int(seed) for seed in mappings[0].replace('seeds: ', '').split(' ')
        }
    elif part == 2:
        seeds = [int(s) for s in mappings[0].replace('seeds: ', '').split(' ')]
        for i in list(range(0, len(seeds), 2)):
            res = {**res, **{s: s for s in range(seeds[i], seeds[i] + seeds[i + 1])}}

    for m in mappings[2:]:
        if len(m) == 0:
            res = translate(nums, res)
            nums = []
        elif m[0] in ascii_lowercase:
            names = parse_names(m)
            pass
        elif m[0] in digits:
            nums.append(parse_nums(m))
    else:
        if len(nums) > 0:
            res = translate(nums, res)
    return min(res.values())


def parse_names(mapping_line: str) -> dict[str, str]:
    src, _, dest = mapping_line.split(' ')[0].split('-')
    return {src: dest}

def parse_nums(mapping_line: str) -> dict[int, int]:
    dest, src, incr = [int(v) for v in mapping_line.split(' ')]
    return {'dest': dest, 'src': src, 'incr': incr}

def translate(mapping_dict: list[dict[str, int]], prev_state: dict[int, int]) -> dict[int, int]:
    new_state = {}
    for mapping in mapping_dict:
        for o_seed, u_seed in prev_state.items():
            if mapping['src'] <= u_seed < (mapping['src'] + mapping['incr']):
                new_state[o_seed] = u_seed + (mapping['dest'] - mapping['src'])
    return {**prev_state, **new_state}


if __name__ == '__main__':
    # test answer: 35
    # prod answer: 535088217
    # print(seeds(utils.read_input(5, True)))

    # test answer: 46
    # prod answer: 
    print(seeds(utils.read_input(5, False), 2))
