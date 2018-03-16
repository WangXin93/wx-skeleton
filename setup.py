import setuptools

config = {
    name:'Name',
    version:'0.1',
    packages:setuptools.find_packages(exclude=['tests', 'docs']),
    entry_points:{
        'console_scripts': [
            'mkskl.py = wx_skeleton.bin:mkskl.py'
        ],
    },
    install_requires:['nose>=1.3.7'],
    tests_require:['pytest'],
    package_data:{
        'wx_skeleton':['.gitignore']
    },
    author:'Wang Xin',
    author_email:'wangxin19930411@163.com',
    description:'Quickly build python project skeleton',
    license:'BSD',
    url:'https://github.com/WangXin93/wx_skeleton',
}


if __name__ == "__main__":
    setuptools.setup(**config)
