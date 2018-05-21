#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Raphael Campos'
SITENAME = u'Raphael Campos dev blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'en'

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
SOCIAL = (('twitter', 'http://twitter.com/raphaelncampos'),
          ('github', 'https://github.com/raphaelncampos'),
          ('facebook', 'http://facebook.com/yamirhcp'),
          )

TWITTER_USERNAME = 'raphaelncampos'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "/home/rcampos/git/pessoal/pelican-themes/Flex"

DEFAULT_CATEGORY = 'General'
USE_FOLDER_AS_CATEGORY = False

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
TYPOGRIFY = True
DATE_FORMATS = {
    'en': ('en_US.utf8','%a, %d %b %Y'),
    'br': ('pt_BR.utf8','%a, %d de %B de %Y'),
}

DISQUS_SITENAME='raphaelncampos'
GITHUB_URL='https://github.com/raphaelncampos'

PLUGIN_PATHS = ['/home/rcampos/git/pessoal/pelican-plugins']
PLUGINS = ['i18n_subsites','pelican_unity_webgl',]

# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
    'br': {
        'SITENAME': 'Dev blog do Raphael Campos',
        }
    }
