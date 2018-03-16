#!/usr/bin/env python
from argparse import ArgumentParser
from wx_skeleton.skutils import build_skeleton
import sys


if __name__ == "__main__":
    parser = ArgumentParser('Build python project skeleton at this path')
    parser.add_argument('project_name', type=str, help='project name include path')
    args = parser.parse_args()
    build_skeleton(args.project_name)
    print("Successfully build project %s!" % args.project_name)
