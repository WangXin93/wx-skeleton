# Usage

# [Start a project the right way?](https://raw.githubusercontent.com/WangXin93/My_python_demo/master/skeleton/mkskl.py)

What this script can make is a project directory like that:
```bash
$ tree -a ~/proj
proj
├── .gitignore
├── README.md
├── bin
├── docs
├── proj
│   └── __init__.py
├── setup.py
└── tests
    ├── __init__.py
        └── setup_tests.py
```

The building process follow this path:

[x]1. Make directory for the root
[x]2. Make directory with project_name
[x]3. Make directory bin
[x]4. Make directory docs
[x]5. Make directory tests
[x]6. touch root/project_name/__init__.py
[x]7. touch tests/__init__.py
[x]8. touch root/setup.py
[x]9. touch tests/setup_tests.py
[x]10. Add first to setup_tests.py
[ ]11. touch root/.gitignore and add default contents
[x]12. touch README.md
