#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Philipp Eller'
SITENAME = 'Andromediary'
SITEURL = ''

PATH = 'content'
STATIC_PATHS =('notebooks',)

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
        )

# Social widget
SOCIAL = (('github', 'https://github.com/philippeller'),
        ('linkedin', 'https://www.linkedin.com/in/philipp-eller-b541b015b/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')                # Add 'ipynb'
PLUGIN_PATHS = ('pelican-plugins', )       # Ensure your plugin path is in it
#PLUGINS = ['ipynb.markup']             # Name of the plugin
PLUGINS = ['ipynb2pelican']             # Name of the plugin
IGNORE_FILES = ['.ipynb_checkpoints']   # Prevent parsing checkpoints files

#IPYNB_USE_METACELL = True


THEME = 'theme/'

BIO = 'Blah blah'


DISQUS_SITENAME = 'https-philippeller-github-io'


GOOGLE_ANALYTICS = "UA-141804640-1"
