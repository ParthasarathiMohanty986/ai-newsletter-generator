from jinja2 import Environment, FileSystemLoader
from datetime import datetime

def generate_html(articles, title="Weekly Digest"):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('newsletter_template.html')
    return template.render(title=title, date=datetime.now().strftime("%B %d, %Y"), articles=articles)
