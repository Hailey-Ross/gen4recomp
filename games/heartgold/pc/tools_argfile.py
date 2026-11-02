#!/usr/bin/env python3
"""Runs a Python tool with its long file lists read from files, as "@file" arguments.

Linux limits one shell command to 128 KB, and POST_LINK names every source file
several times over. usage: tools_argfile.py TOOL.py [ARG | @LIST]...
"""
import os
import runpy
import sys

args = []
for a in sys.argv[2:]:
    if a.startswith("@"):
        with open(a[1:]) as f:
            args.extend(f.read().split())
    else:
        args.append(a)
tool = sys.argv[1]
sys.argv = [tool] + args
sys.path.insert(0, os.path.dirname(os.path.abspath(tool)))
runpy.run_path(tool, run_name="__main__")
