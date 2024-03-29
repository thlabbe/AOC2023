import os
from functools import cache


def get_input(name="input12.txt"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')

    return input_file


@cache
def get_num_filled_blanks(block):
    num_blanks = block.count('?')
    num_filled = block.count('#')
    return num_filled, num_blanks


@cache
def get_num_perm_block(block, nums):
    num_filled, num_blanks = get_num_filled_blanks(block)
    total_filled = sum(nums)
    total_blank = max(len(nums) - 1, 0)
    if ((total_filled > num_filled + num_blanks)
            or (total_blank > num_blanks)
            or (total_filled + total_blank > len(block))
            or (num_filled > total_filled)):
        return 0

    if (total_filled == num_filled) and "?" not in block:
        return 1

    total = 0
    for i, char in enumerate(block):
        if char == '?':
            total += get_num_perm(block[:i] + " " + block[i + 1:], nums)
            total += get_num_perm(block[:i] + "#" + block[i + 1:], nums)
            break
    return total


@cache
def get_num_perm(config, nums):
    config = config.split(' ', 1)
    if len(config) == 1:
        out = get_num_perm_block(config[0], nums)
        return out

    return sum(get_num_perm(config[0], nums[:i]) * get_num_perm(config[1], nums[i:]) for i in range(len(nums) + 1))


def main():
    input_file = get_input()

    total = 0
    for line in input_file:
        config, nums = line.split(' ')
        config = "?".join([config] * 5)
        nums = ",".join([nums] * 5)
        config = ' '.join(config.replace('.', ' ').split())
        nums = tuple(int(i) for i in nums.split(','))
        total += get_num_perm(config, nums)

    print(total)


if __name__ == "__main__":
    main()