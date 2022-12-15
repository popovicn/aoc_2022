import re
import sys

M4 = 4000000


def get_f_ranges(x, y, r):
    freq_ranges = []
    for _x in range(max(0, x-r), min(M4, x+r+1)):
        min_y = y - (r - abs(x-_x))
        max_y = min(M4, y + (r - abs(x-_x)))
        min_f = max(0, M4 * _x + min_y)
        max_f = max(0, M4 * _x + max_y)
        freq_ranges.append([min_f, max_f])
    return freq_ranges


def merge_and_sort(ranges: list):
    sorted_ranges = sorted(ranges, key=lambda r: r[0])
    result_ranges = [sorted_ranges[0]]
    for r in sorted_ranges[1:]:
        if r[0] <= result_ranges[-1][1] <= r[1]:
            result_ranges[-1][1] = r[1]
        else:
            result_ranges.append(r)
    return result_ranges


if __name__ == '__main__':
    file_name = sys.argv[1]
    covered_fs = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            xs, ys, xb, yb = [int(x) for x in re.findall('-?\d+', line)]
            r = abs(xs - xb) + abs(ys - yb)
            s_covered_fs = get_f_ranges(xs, ys, r)
            covered_fs = merge_and_sort(covered_fs + s_covered_fs)
    last_r = 0
    for r in covered_fs:
        if last_r + 1 < r[0]:
            exit(f"{last_r + 1}")
        elif r[1] > last_r:
            last_r = r[1]
    print(last_r+1)
