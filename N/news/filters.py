import django_filters
from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {'title': ['icontains'], 'dateCreation': ['gt'], 'author': ['exact'], 'postCategory': ['exact']}

class NewsFilter (FilterSet):
    date = django_filters.DateFilter(field_name='create_time', lookup_expr='gte', label='Дата от')
    date.field.error_messages = {'invalid': 'Введите дату в формате ДД.ММ.ГГГГ. Например: 16.10.1993'}
    date.field.widget.attrs = {'placeholder':'ДД.ММ.ГГГГ.'}
