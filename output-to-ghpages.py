from distutils.dir_util import copy_tree
import os

# if specified all files will be deleted - except .git - before copying
# otherwise copying will add files if non-existing and overwrite files
# which exists
CLEANUP_BEFORE_COPYING = False

# runs pelican to convert "content" into "output"
os.system("pelican")
print("'pelican' called!")

if CLEANUP_BEFORE_COPYING:
    for filename in os.listdir("gh-pages"):
        if filename != ".git"
            os.remove(filename)
        else:
            pass
    print("Clean up completed!")
    copy_tree("output/", "gh-pages/")
    print("Tree fully copied!")
else:
    copy_tree("output/", "gh-pages/")
    print("Tree fully copied!")
