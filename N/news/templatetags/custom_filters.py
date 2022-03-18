from django import template


register = template.Library()


censor_list = ['сука', 'придурок', 'дебил', 'дурак']


@register.filter(name='censor')
def censor(value):
    for word in censor_list:
        value = value.replace(word, '*****')
    return value

