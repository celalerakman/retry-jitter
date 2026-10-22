"""Bounded exponential retry delay with an injected jitter source."""
import random


def delay(attempt, rng=random):
    if type(attempt) is not int or attempt < 0:
        raise ValueError('Non-negative integer attempt required')
    return rng.uniform(0, min(300, 2 ** min(attempt, 9)))


if __name__ == '__main__':
    print([round(delay(i, random.Random(i)), 3) for i in range(7)])
