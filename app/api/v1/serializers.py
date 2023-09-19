from rest_framework import serializers
from currency.models import Rate, Source, ContactUs
from currency.tasks import contact_us

class RateSourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sale',
            'type',
        )

class SourceSerializer(serializers.ModelSerializer):
    rate_set = RateSourceSerializer(many=True, read_only=True)

    class Meta:
        model = Source
        fields = [
            'id',
            'name',
            'rate_set'
        ]

class RateSerializer(serializers.ModelSerializer):
    source_obj = SourceSerializer(source='source', read_only=True)

    class Meta:
        model = Rate
        fields = [
            'id',
            'buy',
            'sale',
            'type',
            'source_obj',
            'source',
            'created'
        ]
        extra_kwargs = {
            'source': {'write_only': True}
        }

class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = (
        'email_to',
        'subject',
        'body',
        'created',
        )

    def create(self, validated_data):
        print(validated_data)

        subject = validated_data['subject']
        body = validated_data['body']
        email_to = validated_data['email_to']

        full_email_body = f'''
        Email from: {email_to}
        Body: {body}
        '''

        contact_us.apply_async(args=(subject, ), kwargs={'body': full_email_body})

        return ContactUs.objects.create(**validated_data)