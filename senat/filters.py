import django_filters
from .models import *



class CourrierFilter(django_filters.FilterSet):
    # code = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Courrier
        fields = ['code', 'objet']