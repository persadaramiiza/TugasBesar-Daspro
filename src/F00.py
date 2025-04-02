import os
import time
from typing import Iterator, List

def linear_congruential_generator(m: int, a: int, c: int, seed: int) -> Iterator[int]:
    x = seed
    while True:
        yield x
        x = (a * x + c) % m

def random(lower_limit: float, upper_limit: float) -> float:
    global gen, seed_random
    rand = lower_limit + (next(gen) % int((upper_limit - lower_limit) * 100)) / 100
    seed_random = (seed_random * 1103515245 + 12345) & 0x7fffffff
    return rand//1
# Initialize the generator outside the function
seed_random = int(os.getpid() + time.time())
gen = linear_congruential_generator(m=2**31, a=1103515245, c=12345, seed=seed_random)
