from currency.models import ContactUs, Rate, Source
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


class SourceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'source_url',
        'name'
    )

    list_filter = (
        'id',
    )

    search_fields = (
        'name',
    )


class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email_to',
        'subject',
        'body',
        'created'
    )

    list_filter = (
        'id',
        'email_to',
        ('created', DateRangeFilter)
    )

    search_fields = (
        'id',
        'email_to',
        'subject'
    )

    def has_delete_permission(self, request, obj=None) -> bool:
        return False

    def has_add_permission(self, request) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False


admin.site.register(Rate, RateAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
