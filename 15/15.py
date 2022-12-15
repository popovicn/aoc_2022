import re
import sys


if __name__ == '__main__':
    file_name, y = sys.argv[1], int(sys.argv[2])
    forbidden_x = set()
    beacons_x = set()
    with open(file_name, 'r') as f:
        for line in f.readlines():
            xs, ys, xb, yb = [int(x) for x in re.findall('-?\d+', line)]
            r = abs(xs - xb) + abs(ys - yb)
            y_diff = abs(ys - y)
            if y_diff <= r:
                for x in range(xs - r + y_diff, xs + r - y_diff + 1):
                    forbidden_x.add(x)
            if yb == y:
                beacons_x.add(xb)
    print(len(forbidden_x.difference(beacons_x)))
