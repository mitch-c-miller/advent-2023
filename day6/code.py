from sys import path
path.append('../advent2023')

import utils
from functools import reduce

def ways_to_win(times: list[str], dists: list[str]) -> int:
    res = []
    races = [
        {'time': int(t), 'distance': int(d)} for t, d, in zip(times, dists)
    ]

    for race in races:
        race_res = 0
        for i in range(1, race['time'] + 1):
            race_res += race_check(i, race['time'], race['distance'])
        res.append(race_res)

    return reduce(lambda x, y: x * y, res, 1)

def race_check(charging_time: int, total_time: int, record: int) -> int:
    travel_speed = charging_time
    travel_time = total_time - charging_time
    return 1 if travel_speed * travel_time > record else 0

if __name__ == '__main__':
    # test answer: 288
    # prod answer: 500346
    data = utils.read_input(6, False)
    race_times = filter(lambda x: len(x) > 0, data[0].replace('Time:', '').split(' '))
    race_dists = filter(lambda x: len(x) > 0, data[1].replace('Distance:', '').split(' '))
    # print(ways_to_win(race_times, race_dists))

    # test answer: 71503
    # prod answer: 42515755
    data = utils.read_input(6, True)
    race_times = [data[0].split(':')[-1].replace(' ', '')]
    race_dists = [data[1].split(':')[-1].replace(' ', '')]
    print(ways_to_win(race_times, race_dists)) 