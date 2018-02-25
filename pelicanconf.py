#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Monica Chin'
SITENAME = 'monica_chin'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Tijuana'

DEFAULT_LANG = 'en'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites']
THEME = "themes/pelican-bootstrap3"
JINJA_ENVIRONMENT = {
    "extensions": ['jinja2.ext.i18n'],
}

PYGMENTS_STYLE = 'monokai'

CUSTOM_CSS = 'theme/css/custom.css'

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'theme/css/custom.css'},
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Articles
SHOW_ARTICLE_AUTHOR = False

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('blog', '/category/blog.html'),
    ('projects', '/projects'),
    ('cv', '/cv'),
    ('contact', '/contact')
    )

ABOUT_ME = 'Web Development. Bay Area. <strong><3s</strong> learning, my dog, hiking, baking, and traveling.'

# Blogroll
LINKS = (('Tegan & Sara', 'http://teganandsara.com'),
        )

# Social widget
SOCIAL = (('Github', 'https://github.com/mchin'),
          ('Linkedin', 'https://www.linkedin.com/in/monchin'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
