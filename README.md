# Quickly start a project by wx-skeleton :cake::cake::cake:
# Usage
```bash
$ pip install pipenv
$ pipenv install 
$ pipenv shell
(venv)$ pipenv install wx-skeleton
(venv)$ mkskl.py new_project
Successfully run build_skeleton for new_project
Successfully build project new_project!
```

# Start a project the right way?[(reference)](https://raw.githubusercontent.com/WangXin93/My_python_demo/master/skeleton/mkskl.py)

What this script can make is a project directory like that:
```bash
$ tree -a ~/new_project
new_project
├── .gitignore
├── README.md
├── bin
|   └── __init__.py
├── docs
├── new_project
│   └── __init__.py
├── setup.py
└── tests
    ├── __init__.py
        └── setup_tests.py
```

The building process follow this process:

- [x] Make directory for the root
- [x] Make directory with root/project_name
- [x] Make directory root/bin
- [x] Make directory root/docs
- [x] Make directory root/tests
- [x] touch root/project_name/\_\_init\_\_.py
- [x] touch root/tests/\_\_init\_\_.py
- [x] touch root/bin/\_\_init\_\_.py
- [x] touch root/setup.py
- [x] touch root/tests/setup_tests.py
- [x] Add first test to setup_tests.py
- [x] touch root/.gitignore and add default contents
- [x] touch README.md

# How to distribute and publish python project?
<https://docs.djangoproject.com/en/2.0/intro/reusable-apps/>
