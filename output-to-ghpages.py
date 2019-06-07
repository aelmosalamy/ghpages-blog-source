from distutils.dir_util import copy_tree
from shutil import rmtree
import os

# if specified all files will be deleted - except .git - before copying
# otherwise copying will add files if non-existing and overwrite files
# which exists
CLEANUP_BEFORE_COPYING = True

# runs pelican to convert "content" into "output"
os.system("pelican")
print("Pelican site generated to output!")

if CLEANUP_BEFORE_COPYING:
    for filename in os.listdir("gh-pages"):
        if filename != ".git":
            path = "gh-pages/" + filename
            os.remove(path) if os.path.isfile(path) else rmtree(path)
        else:
            pass
    print("Clean up completed!")
    copy_tree("output/", "gh-pages/")
    print("Tree fully copied!")
else:
    copy_tree("output/", "gh-pages/")
    print("Tree fully copied!")
