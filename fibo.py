#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import time
import argparse


def main_recursive(max_iter_number):
    for x in range(max_iter_number):
        print("fibonacci({}) = {}".format(x, str(fibonacci(x))))

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main_generator():
    f = fiboyield()
    for x in range(60):
        print("fibonacci: {}".format(f.next()))

# GENERATOR
def fiboyield():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--count',
        dest='fib_count',
        action='store',
        type=int,
        default=0,
        help='30 + count will get fibonacci last iteration number')
    args = parser.parse_args()
    start_time = time.time()
    main_recursive(args.fib_count + 31)
    print(time.time() - start_time, "seconds")
