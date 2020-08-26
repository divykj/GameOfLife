#!/usr/bin/env python3

ALIVE = 1
DEAD = 0


def tick_cell(cells, width, height, x, y):
    alive_neighbours = sum(
        cells[j % height][i % width]
        for i in range(x - 1, x + 2)
        for j in range(y - 1, y + 2)
        if (i, j) != (x, y)
    )

    if cells[y][x] == DEAD:
        return ALIVE if alive_neighbours == 3 else DEAD
    return ALIVE if 1 < alive_neighbours < 4 else DEAD


def tick(cells, width, height):
    return [
        [tick_cell(cells, width, height, i, j) for i in range(width)]
        for j in range(height)
    ]


def is_dead(cells):
    return all(cell == DEAD for row in cells for cell in row)


def main():
    print("Run 'python play.py -h'")


if __name__ == "__main__":
    main()
