from pelican import signals

AUTHOR = 'Isaias, David, Lucas'
SITENAME = 'CodiZen'
SITEURL = ''

PATH = './content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'https://getpelican.com/'),
    ('Python.org', 'https://www.python.org/'),
    ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
    ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (
    ('You can add links in your config file', '#'),
    ('Another social link', '#'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = './output/theme/mediumfox/'

def exclude_nohtml(generator):
    generator.nohtml_articles = [
        article for article in generator.articles if not article.metadata.get('noHTML', '').lower() == 'true'
    ]

    generator.articles = [article for article in generator.articles if not article.metadata.get('noHTML', '').lower() != 'true']
    
def add_nohtml_to_context(generator):
    context = generator.context
    context['nohtml_articles'] = getattr(generator, 'nohtml_articles', [])

signals.article_generator_finalized.connect(exclude_nohtml)
signals.article_generator_finalized.connect(add_nohtml_to_context)