# import sys

# def read_input():
#     with open("input.txt", 'r') as input_file:
#         lines = input_file.readlines()
#     return lines

# def determin_safe_level():
#     lines = read_input()
#     total_safe_count = 0

#     for line in lines:
#         values = list(map(int, line.strip().split()))
        
#         for i in range(len(values) -1 ):
#             if values[i] > values[i+1] or values[i] < values[i+1]:
#                 if 0 < abs(values[i]-values[i+1]) < 4:
#                     row_safe = True
#                     break

#         if row_safe:
#             total_safe_count += 1
#                     # counter += 1

#     print(f"{total_safe_count}")

# if __name__ == '__main__':
#     determin_safe_level()

# ----------
import sys

def read_input():
    with open("input.txt", 'r') as input_file:
        lines = input_file.readlines()
    return lines

def determin_safe_level():
    lines = read_input()
    total_safe_count = 0

    for line in lines:
        values = list(map(int, line.strip().split()))
        row_safe = True  # Assume the row is safe initially
        
        for i in range(len(values) - 1):
            diff = abs(values[i] - values[i + 1])
            
            # Check if the difference is outside the safe bounds
            if diff < 1 or diff > 3:
                row_safe = False
                break
            
            # Ensure consistent direction: increasing or decreasing
            if i > 0 and not ((values[i] > values[i - 1] and values[i + 1] > values[i]) or
                              (values[i] < values[i - 1] and values[i + 1] < values[i])):
                row_safe = False
                break

        if row_safe:
            total_safe_count += 1

    print(f"{total_safe_count}")

if __name__ == '__main__':
    determin_safe_level()