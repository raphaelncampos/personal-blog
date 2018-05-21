#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Raphael Campos'
SITENAME = AUTHOR
SITESUBTITLE = 'Software Engineer'
#SITEURL = 'http://rcampos.rio.br/'
SITELOGO = '//s.gravatar.com/avatar/9d77a848d13cdb876f260d82199f7b57?s=120'
SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR
PYGMENTS_STYLE = 'monokai'

THEME = "/home/rcampos/git/pessoal/pelican-themes/Flex"
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
         #('You can modify those links in your config file', '#'),
         )

# Social widget
SOCIAL = (
          ('facebook', 'http://facebook.com/yamirhcp'),
          ('instagram', 'http://instagram.com/raphaelncampos'),
          ('linkedin', 'https://www.linkedin.com/in/raphael-campos-70b94733/'),
          ('twitter', 'http://twitter.com/raphaelncampos'),
          ('medium', 'http://medium.com/@raphaelncampos'),
          ('telegram', 'https://telegram.me/raphaelncampos'),
          ('gitlab', 'https://gitlab.com/raphaelncampos'),
          ('bitbucket', 'https://bitbucket.org/raphaelncampos'),
          ('github', 'https://github.com/raphaelncampos'),
          ('google', 'https://google.com/+RaphaelCampos'),
          )


MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
    'br': {
        'SITESUBTITLE': 'Engenheiro de Software',
        'SITEDESCRIPTION': 'Visões e experiências do %s' % AUTHOR,
        'MENUITEMS': {
                'Arquivos': '/archives.html',
                'Categorias': '/categories.html',
                'Tags': '/tags.html',
            }
        }
    }

TWITTER_USERNAME = 'raphaelncampos'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


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


