import random 
from django import template
register = template.Library()

@register.filter(name='category_random')
def category_random(arg):
    tmp = list(arg)[:10]
    random.shuffle(tmp)
    return tmp

