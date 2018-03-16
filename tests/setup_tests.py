from nose.tools import *
from wx_skeleton.skutils import *
import os
import shutil


def setup_tests():
    print("SETUP!")


def touch_tests():
    # Test touch a file
    path = './test_touch'
    touch(path)
    path = os.path.expanduser(path)
    print("Create file at %s ..." % path)
    assert_true(os.path.exists(path))
    os.remove(path)
    print("Remove file at %s ..." % path)

    # Test raise NameError while directory doesn't exist
    path = './not_dir/test_touch'
    with assert_raises(IOError) as cm:
        touch(path)


def build_skeleton_tests():
    build_skeleton('./test_skeleton')
    assert_equal((os.path.exists('./test_skeleton')), True)
    shutil.rmtree('./test_skeleton')

