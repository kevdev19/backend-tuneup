#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

__author__ = "Kevin Blount"

import cProfile
import pstats
import functools
import io
import timeit


def profile(func):
    """A cProfile decorator function that can be used to
    measure performance.
    """
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retrv = func(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retrv

    return inner


def read_movies(src):
    """Returns a list of movie titles."""
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Returns True if title is within movies list."""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list."""
    movies = read_movies(src)
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


# TODO - use timeit to test the main() function. Replace stmt with needed statment
def timeit_helper():
    """Part A: Obtain some profiling measurements using timeit."""
    avg_results = []
    t = timeit.Timer(stmt='pass', setup='pass')
    result = sorted(t.repeat(repeat=7, number=3))
    for float_num in result:
        avg_result = float_num / 3
        avg_results.append(avg_result)
    print('Best time across 7 repeats of 5 runs per repeat: {:.11} sec'.format(
        min(avg_results)))


@profile
def main():
    """Computes a list of duplicate movie entries."""
    timeit_helper()
    result = find_duplicate_movies('movies.txt')
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))


if __name__ == '__main__':
    main()
