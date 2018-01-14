#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from video_extension import VideoExtension

AUTHOR = 'jim zheng guo'
SITENAME = 'jim.kangaroo.g2.fdis'
#SITESUBTITLE = 'Kangaroo G2 FDIS'

#THEME = 'themes/pelican-elegant-1.3'
THEME = 'themes/attila-1.2'
HEADER_COLOR='green'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'
STATIC_PATHS = {'images'}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

MARKDOWN = {
    'extensions': [VideoExtension()]
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
