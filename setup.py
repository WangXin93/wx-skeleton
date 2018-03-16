import setuptools

config = {
    'name':'wx-skeleton',
    'version':'0.1',
    'packages':setuptools.find_packages(exclude=['tests', 'docs']),
    'entry_points':{
        'console_scripts': [
            'mkskl.py = bin.mkskl:main'
        ],
    },
    'install_requires':['nose>=1.3.7'],
    'tests_require':['nose'],
    'package_data':{
        'wxskeleton':['.gitignore']
    },
    'author':'Wang Xin',
    'author_email':'wangxin19930411@163.com',
    'description':'Quickly build python project skeleton',
    'license':'BSD',
    'url':'https://github.com/WangXin93/wx_skeleton',
}


if __name__ == "__main__":
    setuptools.setup(**config)
