#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if len(args) < 2:
    print("none")
else:
    for arg in args[::-1]:
        print(arg)
