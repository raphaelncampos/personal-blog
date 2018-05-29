#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Raphael Campos'
SITENAME = AUTHOR
SITESUBTITLE = 'Software Engineer'
#SITEURL = 'http://rcampos.rio.br/'
SITELOGO = '//s.gravatar.com/avatar/9d77a848d13cdb876f260d82199f7b57?s=120'
SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

COPYRIGHT_YEAR = 2018

THEME = "/home/rcampos/git/pessoal/pelican-themes/Flex"
PATH = 'content'
TIMEZONE = 'America/Sao_Paulo'

#ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
#if {name}
    #ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{name}/'
#ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'
#if {name}
    #ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{name}/'index.html'

#DIRECT_TEMPLATES = (('index', 'blog', 'tags', 'categories', 'archives', 'authors'))
#PAGINATED_DIRECT_TEMPLATES = (('blog',))
#TEMPLATE_PAGES = {'index.html',}

# Default theme language.
I18N_TEMPLATES_LANG = 'en'
#MAIN_LANG = 'en'
# Your language.
DEFAULT_LANG = 'en'
LOCALE = 'en_US.utf8'
OG_LOCALE = 'en_US.utf8'

MENUITEMS = {
    'Archives': '/archives.html',
    'Categories': '/categories.html',
    'Tags': '/tags.html',
}

I18N_SUBSITES = {
    'br': {
        'SITESUBTITLE': 'Engenheiro de Software',
        'SITEDESCRIPTION': 'Visões e experiências do %s' % AUTHOR,
        'LOCALE' : 'pt_BR.utf8',
        'OG_LOCALE' : 'pt_BR.utf8',
        'MENUITEMS': {
                'Arquivos': '/archives.html',
                'Categorias': '/categories.html',
                'Tags': '/tags.html',
            }
        },
    }

#DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ('Get Pelican', 'http://getpelican.com/'),
        # ('Python.org', 'http://python.org/'),
        # ('Jinja2', 'http://jinja.pocoo.org/'),
        # ('You can modify those links in your config file', '#'),
        )

# Social widget
# SOCIAL = (
#           ('facebook', 'http://facebook.com/yamirhcp', 1),
#           ('telegram', 'https://telegram.me/raphaelncampos', 2),
#           ('github', 'https://github.com/raphaelncampos', 3),
#           ('linkedin', 'https://www.linkedin.com/in/raphael-campos-70b94733/', 2),
#           )

SC_PRIORITY = 2

SOCIAL = (
          ('Facebook', 'facebook', 'http://facebook.com/yamirhcp', 1),
          ('LinkedIn', 'linkedin', 'https://www.linkedin.com/in/raphael-campos-70b94733/', 1),
          ('Telegram','telegram', 'https://telegram.me/raphaelncampos', 1),
          ('Twitter','twitter', 'http://twitter.com/raphaelncampos', 2),
          ('Github','github', 'https://github.com/raphaelncampos', 1),
          ('BitBucket','bitbucket', 'https://bitbucket.org/raphaelncampos', 4),
          ('Gitlab','gitlab', 'https://gitlab.com/raphaelncampos', 4),
          ('Google Play Store','google-play', 'https://play.google.com/store/apps/dev?id=6876456275699695441', 7),
          ('Apple App Store','app-store', '#', 7),
          ('Skype: raphaelncampos','skype', '#', 3),
          ('YouTube','youtube', 'https://www.youtube.com/user/raphaelncampos', 5),
          ('Medium','medium', 'http://medium.com/@raphaelncampos', 4),
          ('Stack Overflow','stack-overflow', 'https://stackoverflow.com/users/9043278/raphael-campos', 4),
          ('DEV','devto', 'https://dev.to/raphaelncampos', 4),
          ('Steam','steam', 'https://steamcommunity.com/id/raphaelncampos', 4),
          ('Xbox Live','xbox', 'http://live.xbox.com/pt-BR/Profile?gamertag=raphaelncampos', 4),
          ('Instagram','instagram', 'http://instagram.com/raphaelncampos', 4),
          ('Google','google', 'https://google.com/+RaphaelCampos', 5),
          ('Spotify','spotify', 'https://open.spotify.com/user/raphaelncampos', 6),
          ('Reddit','reddit', 'https://www.reddit.com/user/raphaelncampos/', 7),
          ('Twitch TV','twitch', 'https://www.twitch.tv/raphaelncampos', 7),
          ('Meetup','meetup', 'https://www.meetup.com/pt-BR/members/249136674/', 7),
          ('Discord: raphaelncampos#6695','discord', '#', 7),
          )


MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

# mapping: language_code -> settings_overrides_dict

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
PLUGINS = ['i18n_subsites','pelican_unity_webgl', 
           'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code']
        #    'liquid_tags.include_code', 'liquid_tags.notebook']
# Enable Jinja2 i18n extension used to parse translations.
JINJA_ENVIRONMENT = {
    'extensions' : ['jinja2.ext.i18n',]
}

def article_trans(article, lang, url):
    for trans in article.translations:
        if trans.lang == lang:
            return trans.url
    return url

def page_trans(page, lang, url):
    if lang != I18N_TEMPLATES_LANG:
        return "/%s/%s" % (lang,getattr(page, lang))
    return "/%s" % getattr(page, lang)

def get_flag(page, lang):
    switcher = {
        "en" : "gb"

    }
    return switcher.get(lang, lang)

JINJA_FILTERS = {'article_trans':article_trans,'page_trans':page_trans, 'get_flag':get_flag}