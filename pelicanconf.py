AUTHOR = 'The National Archives'
SITENAME = 'Judiciary guidance for the Find Case Law service from The National Archives'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Switch off feeds, we don't use them
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'theme'
THEME_STATIC_DIR = ''

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}.html'

# Pull the file's slug from the filename
FILENAME_METADATA = r'(?P<slug>.*)'

# These all disable category/author/archive/tag/article functions
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
TAG_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
ARTICLE_SAVE_AS = ''
ARTICLE_URL = ''

DIRECT_TEMPLATES = [] # Removes index.html, archives, etc.

PAGE_PATHS = [''] # Look for pages in the root of the content folder
ARTICLE_PATHS = [] # Don't look for articles anywhere

NAV_STRUCTURE = [
    {"title": "Home", "slug": "index", "children": []},
    {"title": "About this guidance", "slug": "about_this_guidance", "children": []},
    {"title": "Front page formatting", "collapse_id": "Frontpage", "children": [
        {"title": "Headers &amp; footers", "slug": "headers_and_footers"},
        {"title": "Court crest &amp; court details", "slug": "court_crest_and_details"},
        {"title": "NCN", "slug": "ncn"},
        {"title": "Parties", "slug": "parties"},
        {"title": "Rubric &amp; content warnings", "slug": "rubric_and_content_warnings"}
    ]},
    {"title": "Body formatting", "collapse_id": "Bodyformat", "children": [
        {"title": "Fonts", "slug": "fonts"},
        {"title": "Headings", "slug": "headings"},
        {"title": "Paragraphs", "slug": "paragraphs"},
        {"title": "Quotations", "slug": "quotations"},
        {"title": "Images", "slug": "images"},
        {"title": "Tables", "slug": "tables"},
        {"title": "Redactions", "slug": "redactions"},
        {"title": "Footnotes", "slug": "footnotes"}
    ]},
    {"title": "General styling tips", "collapse_id": "General", "children": [
        {"title": "Using web view in Word", "slug": "word_web_view"},
        {"title": "Alignment", "slug": "alignment"},
        {"title": "Indentation", "slug": "indentation"}
    ]},
    {"title": "Supplementary documents", "slug": "supplementary_documents", "children": []},
    {"title": "Accessibility", "collapse_id": "Accessibility", "children": [
        {"title": "Alternative text", "slug": "alternative_text"},
        {"title": "Table headers", "slug": "table_headers"},
        {"title": "Table captions", "slug": "table_captions"}
    ]}
]
