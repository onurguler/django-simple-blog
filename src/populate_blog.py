import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogproject.settings')

import django
django.setup()

import time
import random
import requests
from faker import Faker
from blog.models import Post
from django.contrib.auth.models import User


fake = Faker()

SENTENCE_NB_WORDS_RANGE = range(6,15)
UNSPLASH_RANDOM_URL = 'https://source.unsplash.com/1600x900/?'
UNSPLASH_QUERY = 'computer,programming,coding,algorithm'
LOREM_MARKDOWN_URL = 'https://jaspervdj.be/lorem-markdownum/markdown.txt'


def unsplash_source_random(query=''):
    r = requests.get(UNSPLASH_RANDOM_URL + query)
    return r.url


def lorem_markdown():
    r = requests.get(LOREM_MARKDOWN_URL)
    return r.text


def populate(N=5):
    """Create N posts
    
    Args:
        N (int, optional): Populate size
    """
    for _ in range(N):
        author = User.objects.get(username='onurguler')
        title = fake.sentence(nb_words=random.choice(SENTENCE_NB_WORDS_RANGE), 
                              variable_nb_words=True, ext_word_list=None)
        subtitle = fake.sentence(nb_words=random.choice(SENTENCE_NB_WORDS_RANGE), 
                                 variable_nb_words=True, ext_word_list=None)
        cover_image = unsplash_source_random(UNSPLASH_QUERY)
        text = lorem_markdown()
        created_at = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None)
        published_at = fake.date_time_between(start_date=created_at, end_date='now', tzinfo=None)
        
        post = Post.objects.get_or_create(author=author, title=title, 
                                          subtitle=subtitle, cover_image=cover_image,
                                          text=text, created_at=created_at,
                                          updated_at=created_at, published_at=published_at)
        time.sleep(2)
        


if __name__ == '__main__':
    populate(20)
