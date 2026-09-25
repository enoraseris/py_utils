from collections.abc import Iterable
from itertools import chain
from typing import cast


def iterable_with_previous[T, S](
    iterable: Iterable[T], sentinel: S
) -> Iterable[tuple[T | S, T]]:
    previous: T | S = sentinel
    for current in iterable:
        yield (previous, current)
        previous = current


def iterable_with_next[T, S](
    iterable: Iterable[T], sentinel: S
) -> Iterable[tuple[T, T | S]]:
    iterator = iter(iterable)
    try:
        current = next(iterator)
    except StopIteration:
        return

    for next_item in chain(iterator, [sentinel]):
        yield current, cast(T | S, next_item)
        current = cast(T, next_item)


def iterable_with_previous_and_next[T, S](
    iterable: Iterable[T], sentinel: S
) -> Iterable[tuple[T | S, T, T | S]]:
    iterator = iter(iterable)
    try:
        current = next(iterator)
    except StopIteration:
        return
    previous: T | S = sentinel
    for next_item in chain(iterator, [sentinel]):
        yield (previous, current, cast(T | S, next_item))
        previous = current
        current = cast(T, next_item)
