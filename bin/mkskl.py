#!/usr/bin/env python
from argparse import ArgumentParser
from wxskeleton.skutils import build_skeleton
import sys

def main():
    parser = ArgumentParser('Build python project skeleton at this path')
    parser.add_argument('project_name', type=str, help='project name include path')
    args = parser.parse_args()
    build_skeleton(args.project_name)
    print("Successfully build project %s!" % args.project_name)

if __name__ == "__main__":
    main()
