#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Philipp Eller'
SITENAME = 'Andromediary'
SITEURL = ''

PATH = 'content'
STATIC_PATHS =('notebooks', 'content/spherical_opt')

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
PLUGINS = ['ipynb2pelican', 'render_math', 'figure-ref']             # Name of the plugin
IGNORE_FILES = ['.ipynb_checkpoints']   # Prevent parsing checkpoints files

#IPYNB_USE_METACELL = True
   # Markdown Plugins
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'figureAltCaption':{},
    },
    'output_format': 'html5',
}

THEME = 'theme/'

BIO = 'Articles by Philipp Eller, all material copyrighted, licensed under <a href="(https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>' 


DISQUS_SITENAME = 'https-philippeller-github-io'


GOOGLE_ANALYTICS = "UA-141804640-1"
