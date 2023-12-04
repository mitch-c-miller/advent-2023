from string import digits
punctuation = '/+#-%=*&@$'

def engine(schematic: list[str], gear: bool = False) -> int:
    def __get_adjacent(i: int, j: int, searchable: str) -> list[tuple[int, int]]:
        possible_adjacent_coords = [
            (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
            (i, j - 1), (i, j + 1),
            (i + 1, j - 1), (i + 1, j), (i + 1, j + 1),
        ]
        valid_adjacent_coords = list(filter(
            (lambda coord: 0 <= coord[0] < m and 0 <= coord[1] < n),
            possible_adjacent_coords
        ))
        
        return set(filter(
            (lambda coord: schematic[coord[0]][coord[1]] in searchable),
            valid_adjacent_coords
        ))


    def __get_number(init_i: int, init_j: int) -> (list[tuple[int, int]], int):
        coords, val = [], ''

        # traverse left
        i, j = init_i, init_j
        while 0 <= j < n and schematic[i][j] in digits:
            if (i,j) not in coords:
                coords.insert(0, (i, j))
                val = schematic[i][j] + val
            j -= 1
        
        # traverse right
        i, j = init_i, init_j
        while 0 <= j < n and schematic[i][j] in digits:
            if (i,j) not in coords:
                coords.append((i, j))
                val += schematic[i][j]
            j += 1
        return (coords, int(val))


    def __part1():
        i, res = 0, 0
        while i < m:
            j = 0
            while j < n:
                if schematic[i][j] in digits:
                    coords, val = __get_number(i, j)
                    for num_i, num_j in coords:
                        if len(__get_adjacent(num_i, num_j, punctuation)) > 0:
                            res += val
                            break
                    i, j = coords[-1]
                j += 1
            i += 1
        return res


    def __part2():
        i, res = 0, 0
        while i < m:
            j = 0
            while j < n:
                if schematic[i][j] == '*':
                    adjacent_to_gear = __get_adjacent(i, j, digits)
                    adjacent_num_coords = set()
                    adjacent_num_vals = []
                    for adjacent_i, adjacent_j in adjacent_to_gear:
                        num_coords, num_val = __get_number(adjacent_i, adjacent_j)
                        if tuple(num_coords) not in adjacent_num_coords:
                            adjacent_num_coords.add(tuple(num_coords))
                            adjacent_num_vals.append(num_val)
                    if len(adjacent_num_coords) == 2:
                        temp_val = adjacent_num_vals[0] * adjacent_num_vals[1]
                        res += (temp_val)
                j += 1
            i += 1
        return res


    m, n = len(schematic), len(schematic[0])
    if not gear: return __part1()
    else: return __part2()


if __name__ == '__main__':
    TEST = False
    target = 'test' if TEST else 'input'
    # test answer: 4361
    # prod answer: 527369
    with open(f'day 3/{target}.txt', 'r') as schematic_f:
        schematic = schematic_f.read().strip().split('\n')
        print(engine(schematic))
       
    # test answer: 467835
    # prod answer: 73074886
    with open(f'day 3/{target}.txt', 'r') as schematic_f:
        schematic = schematic_f.read().strip().split('\n')
        print(engine(schematic, True))
