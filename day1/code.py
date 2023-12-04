import requests
from os import listdir, getcwd

DIGITS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
WORDS = {
    'one': '1', 'two': '2', 'three': '3',
    'four': '4', 'five': '5', 'six': '6',
    'seven': '7', 'eight': '8', 'nine': '9',
}

# part 1
def trebuchetDigits(input_str: str) -> int:
    line_nums = []
    for line in input_str.strip().split('\n'):
        line_digits = ''
        len_line = len(line)

        # from the left
        for l_i in range(len_line):
            if line[l_i] in DIGITS:
                line_digits += line[l_i]
                break

        # from the right
        for r_i in range(len_line - 1, -1, -1):
            if line[r_i] in DIGITS:
                line_digits += line[r_i]
                break
        
        line_nums.append(int(line_digits))
    
    return sum(line_nums)

# part 2
def trebuchetWords(input_str: str) -> int:
    line_nums = []
    word_lens = {len(k) for k in WORDS.keys()}

    for line in input_str.strip().split('\n'):
        line_digits = ''
        len_line = len(line)

        # from the left
        l_i, break_left = 0, False
        while l_i < len_line and not break_left:
            if line[l_i] in DIGITS:
                line_digits += line[l_i]
                break

            for word_len in word_lens:
                curr_slice = line[l_i:l_i + word_len]
                if curr_slice in WORDS.keys():
                    line_digits += WORDS[curr_slice]
                    break_left = True
                    break
        
            l_i += 1

        # from the right
        r_i, break_right = len_line - 1, False
        while r_i >= 0 and not break_right:
            if line[r_i] in DIGITS:
                line_digits += line[r_i]
                break

            for word_len in word_lens:
                curr_slice = line[r_i + 1 - word_len:r_i + 1]
                if curr_slice in WORDS.keys():
                    line_digits += WORDS[curr_slice]
                    break_right = True
                    break
            
            r_i -= 1

        line_nums.append(int(line_digits))
    
    return sum(line_nums)

if __name__ == '__main__':
    # with open('day 1/part1_input.txt', 'r') as reader:
    #     print('part 1: ', trebuchetDigits(reader.read()))
    
    with open('day 1/part2_input.txt', 'r') as reader:
        print('part 2: ', trebuchetWords(reader.read()))
