# a simple script that creates a new article entry at "content/articles/"
# with a customised name and title
def main():
    import string, sys
    from datetime import datetime

    article_metadata = {"Title": '',
                        "Date": '',
                        "Tags": '',
                        "Slug": '',
                        }

    template = ""
    PLACEHOLDER_LINE = "*This is a placeholder, place your content here.*"

    # set title and slug
    while True:
        title = input("Post Title: ").strip().lower()
        if title:
            if confirmed(title):
                title = title.lower().strip()
                article_metadata["Title"] = title.title()
                article_metadata["Slug"] = title.translate(str.maketrans('', '', string.punctuation)).strip().replace(' ', '-')
                break
            else:
                continue
        else:
            print("Retry: empty input!")

    # set tags
    while True:
        tags = input("Post Tags (separated by comma): ").strip().lower()
        if tags:
            if confirmed(tags):
                article_metadata['Tags'] = tags
                break
            else:
                continue
        else:
            print("Retry: empty input!")

    # set cover img location
    while True:
        cover_loc = input("Cover Image Name (must be inside /images/covers/): ")
        if cover_loc:
            if confirmed(cover_loc):
                article_metadata['Cover'] = "/images/covers/" + cover_loc
                break
            else:
                continue
        else:
            if confirmed("Use default cover image"):
                print("Default cover image will be used 'post-bg.jpg'")
                break
            else:
                continue
        
    # set date
    article_metadata['Date'] = datetime.now().strftime("%d-%m-%Y %H:%M")

    # write metadata into text
    for key in article_metadata:
        template += "{}: {}\n".format(key, article_metadata[key])

    while True:
        print(template)
        if confirmed("template above"):
            break
        else:
            sys.exit("Template was NOT saved, try again!")

    # adding a line to be replaced by the user
    template += "\n" + PLACEHOLDER_LINE

    # write metadata to "{slug}.md" as destination
    with open("posts/{}.md".format(article_metadata["Slug"]), 'w') as f:
        f.write(template)

    print('"{}.md" was successfully created in the "posts/" directory'.format(article_metadata['Slug']))
    input("exit...")

def confirmed(user_input):
    while True:
        i = input('Confirm "{}" [yes/no] '.format(user_input)).strip().lower()
        if i in ['yes', 'y']:
            return True
        elif i in ['no', 'n']:
            return False
        else:
            continue

if __name__ == '__main__':
    main()
