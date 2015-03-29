# coding: utf-8
"""
Django settings for modelpage project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from decouple import config
from dj_database_url import parse as db_url
from unipath import Path
BASE_DIR = Path(__file__).parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    '.localhost',
    '127.0.0.1',
    '.herokuapp.com',
]


# Application definition

INSTALLED_APPS = (
    'grappelli_extensions',
    'grappelli',
    'filebrowser',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # other apps
    'south',
    'tinymce',
    'sorl.thumbnail',
    'taggit_autosuggest',
    'taggit',
    'bootstrap_pagination',
    'bootstrap3',

    # my apps
    'modelpage.core',
    'modelpage.event',
    'modelpage.blog',
    'modelpage.bid',
    'modelpage.channel',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'modelpage.current_user.CurrentUserMiddleware',
)

ROOT_URLCONF = 'modelpage.urls'

WSGI_APPLICATION = 'modelpage.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='sqlite:///' + BASE_DIR.child('db.sqlite3'),
        cast=db_url),
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Recife'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = BASE_DIR.child('staticfiles')
STATIC_URL = '/static/'

MEDIA_ROOT = BASE_DIR.child('media')
MEDIA_URL = '/media/'


# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
EMAIL_USE_TLS = config('EMAIL_USE_TLS')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT')


# django-tinymce
# TINYMCE_JS_URL = STATIC_URL + 'tiny_mce/tiny_mce.js'
TINYMCE_DEFAULT_CONFIG = {
    # General options
    # 'mode': "textareas",
    'theme': "advanced",
    'height': '400',
    'plugins': "autolink,lists,spellchecker,pagebreak,style,layer,table,save, \
                advhr,advimage,advlink,emotions,iespell,inlinepopups, \
                insertdatetime,preview,media,searchreplace,print,contextmenu, \
                paste,directionality,fullscreen,noneditable,visualchars, \
                nonbreaking,xhtmlxtras,template,syntaxhl",
    'extended_valid_elements': "code[class]",
    'remove_linebreaks': False,
    'forced_root_block': False,
    'force_p_newlines': False,
    'force_br_newlines': False,
    'style_formats': [
        {"title": "BASH", "block": "code", "classes": "bash", },
        {"title": "C#", "block": "code", "classes": "csharp", },
        {"title": "CSS", "block": "code", "classes": "css", },
        {"title": "Go", "block": "code", "classes": "go", },
        {"title": "INI", "block": "code", "classes": "ini", },
        {"title": "Java", "block": "code", "classes": "java", },
        {"title": "JavaScript", "block": "code", "classes": "javascript", },
        {"title": "JSON", "block": "code", "classes": "json", },
        {"title": "HTML/XML", "block": "code", "classes": "xml", },
        {"title": "Ruby", "block": "code", "classes": "ruby", },
        {"title": "PHP", "block": "code", "classes": "php", },
        {"title": "Python", "block": "code", "classes": "python", },
        {"title": "Scala", "block": "code", "classes": "scala", },
        {"title": "SQL", "block": "code", "classes": "sql", },
    ],

    # Theme options
    'theme_advanced_buttons1': "save,newdocument,|,bold,italic,underline, \
        strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull, \
        |,styleselect,formatselect,fontselect,fontsizeselect",
    'theme_advanced_buttons2': "cut,copy,paste,pastetext,pasteword,|,search, \
        replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo, \
        |,link,unlink,anchor,image,cleanup,help,code,|,insertdate,inserttime, \
        preview,|,forecolor,backcolor",
    'theme_advanced_buttons3': "tablecontrols,|,hr,removeformat,visualaid, \
        |,sub,sup,|,charmap,emotions,iespell,media,advhr,|,print,|,ltr, \
        rtl,|,fullscreen",
    'theme_advanced_buttons4': "insertlayer,moveforward,movebackward, \
        absolute,|,styleprops,spellchecker,|,cite,abbr,acronym,del,ins, \
        attribs,|,visualchars,nonbreaking,template,blockquote, \
        pagebreak,|,insertfile,insertimage,syntaxhl",
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_statusbar_location': "bottom",
    'theme_advanced_resizing': "true",
}


# grappelli
GRAPPELLI_ADMIN_TITLE = 'OW7 | CMS'

GRAPPELLI_EXTENSIONS_NAVBAR = 'modelpage.extensions.Navbar'

# GRAPPELLI_EXTENSIONS_SIDEBAR = 'modelpage.extensions.Sidebar'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)


# south {taggit}
SOUTH_MIGRATION_MODULES = {
    'taggit': 'taggit.south_migrations',
}


TAGGIT_AUTOSUGGEST_CSS_FILENAME = 'autoSuggest-grappelli.css'
