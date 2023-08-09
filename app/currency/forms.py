from currency.models import Rate, Source

from django import forms


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = {
            'buy',
            'sale',
            'source',
            'type'
        }


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = {
            'source_url',
            'name',
            'source_avatar',
        }
