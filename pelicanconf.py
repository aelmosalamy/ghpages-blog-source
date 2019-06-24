#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Adham Elmosalamy'

HIDE_AUTHORS = False
SITENAME = 'elmosalamy'
# SITESUBTITLE = "Welcome to the blog!"
SITEURL = 'https://aelmosalamy.github.io'

THEME = "pelican-bootstrap3"

LOAD_CONTENT_CACHE = False
CACHE_CONTENT = False

SOCIAL = (('Github', 'https://github.com/aelmosalamy'),
          ('Stackoverflow', 'https://stackoverflow.com/users/8249904/aelmosalamy', 'stack-overflow'))

PATH = 'content'
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images', 'extra']

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
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
ARTICLE_ORDER_BY = 'reversed-date'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

ARCHIVES_SAVE_AS = 'archives.html'

DEFAULT_PAGINATION = 9
DISPLAY_PAGES_ON_MENU = True

# Blogroll
LINKS = ()

GITHUB_URL = "https://github.com/aelmosalamy"

PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-bootstrapify', 'i18n_subsites', 'tag_cloud']

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

BOOTSTRAP_THEME = 'cosmo'

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# Some info about me
ABOUT_ME = "I am a programmer and graphic designer who enjoys teaching and sharing knowledge."
AVATAR = "images/avatar.png"

# Banner settings
# BANNER = 'images/covers/post-bg.jpg'
# BANNER_SUBTITLE = 'Welcome to the blog!'

# Display site hierarchy above each post
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True

# Aqua navigation bar
BOOTSTRAP_NAVBAR_INVERSE = True

DISPLAY_ARTICLE_INFO_ON_INDEX  = True

### Sidebar settings ###
# Tags
DISPLAY_TAGS_ON_SIDEBAR = True
tag_cloud = True
# Recent posts
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
RECENT_POST_COUNT = 5
# GitHub repos
GITHUB_USER = 'aelmosalamy'

#Social and engagement
DISQUS_DISPLAY_COUNTS = False

# Color scheme uses Pygments
PYGMENTS_STYLE = "paraiso-dark"

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
