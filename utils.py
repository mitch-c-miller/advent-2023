def read_input(day: int, prod: bool) -> list[str]:
    target = 'test' if prod != True else 'input'
    with open(f'day{day}/{target}.txt', 'r') as data_f:
        data = data_f.read().strip().split('\n')
        return data

