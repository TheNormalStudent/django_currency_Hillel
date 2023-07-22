from currency.models import Rate
from currency.resources import RateResource

from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from rangefilter.filters import DateRangeFilter

# Register your models here.


class RateAdmin(ImportExportModelAdmin):
    resource_class = RateResource
    list_display = (
        'id',
        'buy',
        'sale',
        'type',
        'source',
        'created',
    )

    list_filter = (
        'type',
        'source',
        ('created', DateRangeFilter)
    )

    search_fields = (
        'type',
        'source',
    )

    def has_delete_permission(self, request, obj=None) -> bool:
        return False


admin.site.register(Rate, RateAdmin)
