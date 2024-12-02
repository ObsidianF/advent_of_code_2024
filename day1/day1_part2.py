import sys
from collections import Counter

def read_input():
    with open("input.txt", 'r') as f:
        lines = [list(map(int, line.split())) for line in f.readlines()]

    left, right = list(map(list,zip(*lines))) 

    return sorted(left), sorted(right)


def main():
    left, right = read_input()
    num_values = {}
    right_counts = Counter(right)
    count = 0

    for values in left:
        num_values[values] = right_counts.get(values, 0)

    for key, value in num_values.items():
        count += key * value

    print(count)


if __name__ == '__main__':
    main()
