from distutils.dir_util import copy_tree
import os

os.system("pelican")
copy_tree("output/", "gh-pages/")
