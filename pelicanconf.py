#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Adham Elmosalamy'
HIDE_AUTHORS = True
SITENAME = 'aelmosalamy'
SITESUBTITLE = "A passionate learner and a curious creator"
SITEURL = ''

LOAD_CONTENT_CACHE = False
CACHE_CONTENT = False

PATH = 'content'
STATIC_PATHS = ['images', 'pdfs']

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
ARTICLE_URL = '/blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_ORDER_BY = 'reversed-date'

DEFAULT_PAGINATION = 9

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

GITHUB_URL = "https://github.com/aelmosalamy"
DISQUS_SITENAME = "elmosalamy"

PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-bootstrapify', 'pelican_albums']

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

THEME = "alchemy"

SITEIMAGE = "/images/profile.png width=200 height=200"

ICONS = [
    ('github', GITHUB_URL),
    ('instagram', 'https://www.instagram.com/aelmosalam.y/')
]
