#!/bin/bash

pip install --upgrade pip
pip install --upgrade setuptools
pip install --upgrade wheel
pip install --upgrade twine
pip install --upgrade build

python3 -m build

pip install dist/my_minipack-1.0.0.tar.gz

# ex after import :
# import my_minipack.progressbar
# import my_minipack.logger
# from time import sleep
# for i in my_minipack.progressbar.ft_progress(range(1000)): sleep(0.01)
# machine= my_minipack.logger.CoffeeMachine()