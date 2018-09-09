#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Last modified: 2018-09-01 20:33:15
"""This is the example module.

This module compare file text.

"""

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'lsieun'

import sys
import difflib
import argparse

def get_lines(filename: str) -> list:
    line_list: list = []
    with open(filename, "r") as f:
        for line in f.readlines():
            line_list.append(line.rstrip())

    return line_list


def main():
    parser = argparse.ArgumentParser(description="compare two files line by line.")
    parser.add_argument("first", action="store", type=str, help="first filename")
    parser.add_argument("second", action="store", type=str, help="second filename")
    args = parser.parse_args()
    filename1 = args.first
    filename2 = args.second
    line_list1 = get_lines(filename1)
    line_list2 = get_lines(filename2)
    diff = difflib.ndiff(line_list1, line_list2)
    print("\n".join(diff))
    return 0

if __name__ == '__main__':
    sys.exit(main())  
