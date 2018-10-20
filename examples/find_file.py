#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Last modified: 2018-10-20 11:05:15
"""This is the example module.

This module does stuff.
"""

__version__ = '0.1'
__author__ = 'lsieun'

import os
import os.path
import time


def traverse(root_dir: str, pattern: str) -> list:
    print(root_dir)
    lst = []
    for parent, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(pattern):
                filepath = os.path.join(parent, filename)
                lst.append(filepath)
    return lst


def find_it(path_list: list, keyword: str) -> None:
    print("keyworkd:", keyword)
    for path in path_list:
        line_list = get_file_lines(path)
        for line in line_list:
            if line.find(keyword) > -1:
                print("###")
                print("path", path)
                print("line:", line)
                print()


def get_file_lines(path: str) -> list:
    with open(path, encoding='utf-8') as file:
        lst = []
        for line in file:
            line = line.rstrip()
            lst.append(line)
        return lst


if __name__ == "__main__":
    plist = traverse("/home/liusen/workdir/dummy/idea-jar-src", ".java")
#    plist = traverse("/home/liusen/workdir/dummy/idea-jar-src/com/jetbrains/ls", ".java")
    find_it(plist, "Default.xml")

