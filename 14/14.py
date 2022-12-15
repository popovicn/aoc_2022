import sys


def _safe_add(m, x, y) -> dict:
    if x not in m:
        m[x] = set()
    m[x].add(y)
    return m


def _parse_coordinates(line: str):
    coords = line.split(" -> ")
    for i in range(len(coords[:-1])):
        x1, y1 = [int(x) for x in coords[i].split(",")]
        x2, y2 = [int(x) for x in coords[i+1].split(",")]
        for x in range(min(x1, x2), max(x1, x2)+1):
            yield x, y1
        for y in range(min(y1, y2), max(y1, y2)+1):
            yield x1, y


def _go_down(x, y, terrain):
    while y+1 not in terrain[x]:
        y += 1
    return x, y


def _go_sides(x, y, terrain):
    if x-1 not in terrain or y+1 not in terrain[x-1]:
        return x-1, y+1
    elif x+1 not in terrain or y+1 not in terrain[x+1]:
        return x+1, y+1
    else:
        return x, y


def load_terrain(file_name) -> (dict, int):
    terrain = dict()
    max_y = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            for x, y in _parse_coordinates(line):
                terrain = _safe_add(terrain, x, y)
                max_y = max(max_y, y)
    return terrain, max_y


def fill_sand(terrain, max_y):
    sand_count, x, y = 0, 500, 0
    while y < max_y:
        if x not in terrain or y > max(terrain[x]):
            return sand_count
        nx, ny = _go_down(x, y, terrain)
        nx, ny = _go_sides(nx, ny, terrain)
        if nx == x and ny == y:
            terrain = _safe_add(terrain, nx, ny)
            sand_count += 1
            x, y = 500, 0
        else:
            x, y = nx, ny
    return sand_count


if __name__ == '__main__':
    file_name = sys.argv[1]
    terrain, max_y = load_terrain(file_name)
    sand_count = fill_sand(terrain, max_y)
    print(sand_count)
