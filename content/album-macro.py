"""
This script scans all images in the given directory (IMAGE_DEST) then
generates a "gallery.md" file which smoothly integrates with my Pelican workflow.

"""

def main():
    import os, platform
    from datetime import datetime

    now = datetime.now()

    # Set this to the destination of your images directory
    IMAGE_DEST = "images/gallery"
    OUTPUT_DEST = "pages/gallery.md"

    TEMPLATE = """Title: Gallery
Date: {}
Slug: gallery

A growing gallery of artistic creations I make from time to time, Enjoy!

---

<section id="photos">
""".format(now.strftime("%d-%m-%Y %H:%M"))

    # collect all images as a list of filenames
    IMAGE_FILENAMES = os.listdir(IMAGE_DEST)

    # the paranthesis will be filled in with customised infromation later
    IMAGE_TEMPLATE = '<img id="gallery" src="/{}/{}">\n'
    # generate supported HTML img tags for each image with colorbox support
    image_tags = ""
    for name in IMAGE_FILENAMES:
        # filling in the blanks using the filenames in our directory
        image_link = IMAGE_TEMPLATE.format(IMAGE_DEST, name, name, IMAGE_DEST, name)
        image_tags += image_link

    TEMPLATE += image_tags
    TEMPLATE += "</section>"
    # writing our generated template to "gallery.md", creating it or overwriting existing files
    with open(OUTPUT_DEST, "w") as f:
        f.write(TEMPLATE)

    print("Gallery code generated!")
    
# can be used for an improved sort by data created generation. (to be added)
# def creation_date(path_to_file):
#     """
#     Try to get the date that a file was created, falling back to when it was
#     last modified if that isn't possible.
#     See http://stackoverflow.com/a/39501288/1709587 for explanation.
#     """
#     if platform.system() == 'Windows':
#         return os.path.getctime(path_to_file)
#     else:
#         stat = os.stat(path_to_file)
#         try:
#             return stat.st_birthtime
#         except AttributeError:
#             # We're probably on Linux. No easy way to get creation dates here,
#             # so we'll settle for when its content was last modified.
#             return stat.st_mtime


if __name__ == "__main__":
    main()
