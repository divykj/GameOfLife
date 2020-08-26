#!/usr/bin/env python3

from argparse import ArgumentParser
from json import loads
from os import get_terminal_size
from random import choices
from time import sleep

from game_of_life import ALIVE, DEAD, is_dead, tick

with open("artifacts.json", "r") as atrtifacts_file:
    ARTIFACTS = loads(atrtifacts_file.read())


def draw_cells(cells) -> None:
    print(
        "\n".join(
            "".join("  " if cell == DEAD else "██" for cell in row) for row in cells
        ),
        end="",
    )


def generate_cells(seed, width, height):
    if seed == "random":
        return [
            choices([DEAD, ALIVE], cum_weights=[5, 6], k=width) for _ in range(height)
        ]
    return [
        [ALIVE if [i, j] in ARTIFACTS[seed] else DEAD for i in range(width)]
        for j in range(height)
    ]


def main():
    parser = ArgumentParser(description="Conway's Game of Life - By Divy Jain")
    parser.add_argument(
        "seed",
        nargs="?",
        metavar="SEED",
        action="store",
        default="random",
        choices=["random", *ARTIFACTS.keys()],
        help="Starter seed for game of life",
    )
    parser.add_argument(
        "-t",
        "--tick",
        action="store",
        default=200,
        type=int,
        dest="tick_size",
        help="Time between ticks in ms",
    )
    args = parser.parse_args()

    width, height = get_terminal_size()
    width = width // 2

    cells = generate_cells(args.seed, width, height)

    try:
        while True:
            if is_dead(cells):
                break
            draw_cells(cells)
            sleep(args.tick_size / 1000)
            cells = tick(cells, width, height)
    except KeyboardInterrupt:
        print("\nBye.")
    sleep(0.5)


if __name__ == "__main__":
    main()
