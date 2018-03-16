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

The building process follow this process:

- [x] Make directory for the root
- [x] Make directory with project_name
- [x] Make directory bin
- [x] Make directory docs
- [x] Make directory tests
- [x] touch root/project_name/__init__.py
- [x] touch tests/__init__.py
- [x] touch root/setup.py
- [x] touch tests/setup_tests.py
- [x] Add first to setup_tests.py
- [x] touch root/.gitignore and add default contents
- [x] touch README.md
