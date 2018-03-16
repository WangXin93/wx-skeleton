#!/usr/bin/env python3
import sys
import os
import shutil

gitignore_path = os.path.join(os.path.dirname(os.path.abspath((__file__))),
                              '.gitignore')

def touch(path):
    '''Create a file if it doesn't exist, otherwise update its mtime
    
    Args:
        path: string, path of file to be touched

    raise:
        NameError: if base directory doesn't exist
    '''
    assert path, "path can't be empty"
    path = os.path.expanduser(path)
    with open(path, 'a'):
        # Update mtime in case file exists
        os.utime(path, None)


def build_skeleton(project):
    # Assume project is string like "d1/a1"
    assert not os.path.exists(project), "Project path already exists"
    # Get base directory "d1"
    project_path = os.path.dirname(project)
    # Get project name "a1"
    project_name = os.path.basename(project)
    # Make project root
    os.makedirs(project)
    # mkdir bin
    os.makedirs(os.path.join(project, "bin"))
    # mkdir NAME
    os.makedirs(os.path.join(project, project_name))
    # mkdir docs
    os.makedirs(os.path.join(project, "docs"))
    # mkdir tests
    os.makedirs(os.path.join(project, "tests"))
    # touch d1/a1/a1/__init__.py
    touch(os.path.join(project, project_name, "__init__.py"))
    # touch d1/a1/tests/__init__.py
    touch(os.path.join(project, "tests", "__init__.py"))
    # touch d1/a1/bin/__init__.py
    touch(os.path.join(project, "bin", "__init__.py"))
    # touch d1/a1/setup.py
    touch(os.path.join(project, "setup.py"))
    # touch d1/a1/tests/setup_tests.py
    touch(os.path.join(project, "tests", "setup_tests.py"))
    setup_tests="""from nose.tools import *
def setup_tests():
    print("SETUP!")
"""
    with open(os.path.join(project, "tests", "setup_tests.py"), "w") as f:
        f.write(setup_tests)

    # Add .gitignore from skutils package path
    shutil.copy(gitignore_path, os.path.join(project, '.gitignore'))

    # touch d1/a1/README.md
    touch(os.path.join(project, 'README.md'))
    # Print done.
    print("Successfully run build_skeleton for %s" % project)


