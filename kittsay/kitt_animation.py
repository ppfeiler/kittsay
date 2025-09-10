import asyncio
import os
import sys
import time
from typing import List

from colorama import Fore
from colorama import Style

DEFAULT_DURATION_SEC = 50.0
DEFAULT_TICK_SEC = 1.0 / 40.0
DEFAULT_MAX_SIZE = max(0, min(30, os.get_terminal_size().columns - 2))
DEFAULT_SPEED_CELLS_SEC = 8.0

EYE = [
    Fore.LIGHTRED_EX + "*" + Style.RESET_ALL,
    Fore.RED + Style.BRIGHT + "*" + Style.RESET_ALL,
    Fore.LIGHTRED_EX + "*" + Style.RESET_ALL,
]
LEFT_BRACKET = "["
RIGHT_BRACKET = "]"


def hide_cursor() -> None:
    sys.stdout.write("\x1b[?25l")
    sys.stdout.flush()


def show_cursor() -> None:
    sys.stdout.write("\x1b[?25h")
    sys.stdout.flush()


def _prebuild_spaces(n: int) -> List[str]:
    return [" " * i for i in range(n + 1)]


async def play(
    duration_sec: float = DEFAULT_DURATION_SEC,
    tick_sec: float = DEFAULT_TICK_SEC,
    max_pos: int = DEFAULT_MAX_SIZE,
    speed_cells_per_sec: float = DEFAULT_SPEED_CELLS_SEC,
) -> None:
    write = sys.stdout.write
    flush = sys.stdout.flush
    eye = "".join(EYE)
    lb, rb = LEFT_BRACKET, RIGHT_BRACKET
    spaces = _prebuild_spaces(max_pos)

    pos_f = 0.0
    direction = 1
    start = time.monotonic()
    end_time = start + duration_sec
    next_frame = start
    last_time = start

    hide_cursor()
    try:
        while True:
            now = time.monotonic()
            if now >= end_time:
                break

            dt = now - last_time
            last_time = now
            pos_f += direction * speed_cells_per_sec * dt

            if pos_f <= 0.0:
                pos_f = 0.0
                direction = 1
            elif pos_f >= float(max_pos):
                pos_f = float(max_pos)
                direction = -1

            pos = int(round(pos_f))

            left_pad = spaces[pos]
            right_pad = spaces[max_pos - pos]
            line = lb + left_pad + eye + right_pad + rb
            write("\r" + line)
            flush()

            next_frame += tick_sec
            delay = next_frame - time.monotonic()
            if delay > 0:
                await asyncio.sleep(delay)
            else:
                next_frame = time.monotonic()
    finally:
        write("\n")
        flush()
        show_cursor()
