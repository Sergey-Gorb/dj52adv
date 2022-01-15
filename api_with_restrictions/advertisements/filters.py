from django_filters import FilterSet, filters

from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(FilterSet):
    """Фильтры для объявлений."""

    #status = filters.ChoiceFilter(choices=AdvertisementStatusChoices, null_value=None)
    status = filters.CharFilter()
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['status', 'created_at']
