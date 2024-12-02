import sys

def read_input():
    with open("input.txt", 'r') as f:
        lines = [list(map(int, line.split())) for line in f.readlines()]

    left, right = list(map(list,zip(*lines))) 

    return sorted(left), sorted(right)


def main():
    left, right = read_input()
    rem_list = []
    dif = 0
    total = 0

    for i in range(len(left)):
        dif = abs(left[i]-right[i])
        rem_list.append(dif)


    total = sum(rem_list)

    print(total)



if __name__ == '__main__':
    main()
