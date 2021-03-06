import numpy.testing as npt
import sys
import os
import pkg_resources

from pymatbridge import messenger

ROOT = __file__
CONFIG = os.path.realpath(os.path.join(ROOT, '../../../../config.ini'))
print(CONFIG)
BIN    = messenger.get_matlab_bin(config=CONFIG)

def test_config():
    npt.assert_equal(os.path.isfile(CONFIG), True)

@npt.decorators.skipif(BIN==None, 'No Matlab Installed')
def test_matlab_bin():
    npt.assert_equal(os.path.isdir(BIN), True)

    mexext = any(m for m in os.listdir(BIN) if m == 'mexext' or m == 'mexext.exe')
    mex    = any(m for m in os.listdir(BIN) if m == 'mex' or m == 'mex.exe')

    npt.assert_equal(mexext, True)
    npt.assert_equal(mex, True)

@npt.decorators.skipif(BIN==None, 'No Matlab Installed')
def test_matlab_env():
    matlab    = os.path.join(messenger.get_matlab_bin(config=CONFIG), 'matlab')
    env       = messenger.get_matlab_env(matlab=matlab)
    arch = env['ARCH']

    npt.assert_equal(arch.endswith(messenger.get_messenger_dir()[-2:]), True)

