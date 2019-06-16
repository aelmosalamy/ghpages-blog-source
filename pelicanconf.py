#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Adham Elmosalamy'

HIDE_AUTHORS = False
SITENAME = 'Adham Elmosalamy'
SITESUBTITLE = "Welcome to the blog!"
SITEURL = ''

LOAD_CONTENT_CACHE = False
CACHE_CONTENT = False

SOCIAL = (('twitter', 'https://twitter.com/aelmosalamy_'),
          ('github', 'https://github.com/aelmosalamy'),
          ('instagram', 'https://www.instagram.com/aelmosalam.y/'))

PATH = 'content'
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images', 'extra']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Delete the output directory, and all of its contents, before generating new files.
# This can be useful in preventing older, unnecessary files from persisting in your output.
# However, this is a destructive setting and should be handled with extreme care.
DELETE_OUTPUT_DIRECTORY = True

# Articles
ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_ORDER_BY = 'reversed-date'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

DEFAULT_PAGINATION = 9

# Blogroll
LINKS = ()

GITHUB_URL = "https://github.com/aelmosalamy"
DISQUS_SITENAME = "aelmosalamy-github-io"

PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-bootstrapify']

BOOTSTRAPIFY = {
    'table': ['table', 'table-striped', 'table-hover'],
    'img': ['img-fluid'],
    'blockquote': ['blockquote'],
}

TYPOGRIFY = True

USE_FOLDER_AS_CATEGORY = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Theme settings ------------------------------------------------------------

THEME = "attila"

SHOW_SOCIAL_ON_INDEX_PAGE_HEADER = False
DISPLAY_PAGES_ON_MENU = True

# Color scheme uses Pygments
COLOR_SCHEME_CSS = "paraiso-dark"

CSS_OVERRIDE = ["css/custom.css"]

# COVER IMAGES
HOME_COVER = "/images/covers/home-bg.jpg"

# Useful theme settings
# HEADER_COVERS_BY_TAG
# HEADER_COVERS_BY_CATEGORY

AUTHORS_BIO = {
  "adham elmosalamy": {
    "name": "Adham Elmosalamy",
    "cover": "/images/covers/post-bg.jpg",
    "image": "/images/avatar.png",
    "github": "aelmosalamy",
    "twitter": "aelmosalamy_",
    "location": "Alexandria",
    "bio": "I like reading, mathematics, coding and teaching stuff."
  }
}
