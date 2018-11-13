from django import template
from ..models import Article, Category, AdImages
import datetime

register = template.Library()


@register.simple_tag
def get_recent_articles(num=5):
    return Article.objects.all()[:num]


@register.simple_tag
def get_hot_articles(num=5):
    return Article.objects.all().order_by('-views')[:num]


@register.simple_tag
def get_category_list():
    return Category.objects.all()


@register.simple_tag
def get_foot_year():
    return datetime.date.today().year


@register.simple_tag
def get_adImages_tag(num=3):
    return AdImages.objects.all()[:num]

