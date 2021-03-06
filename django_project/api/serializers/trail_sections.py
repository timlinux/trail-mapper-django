from rest_framework import serializers
from trail_mapper.models.trail_sections import TrailSections

__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '01/10/2018'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class TrailSectionsSerializer(serializers.ModelSerializer):
    """Serializer class for trail_mapper sections model."""

    class Meta:
        model = TrailSections
        url_field_name = 'guid'
        fields = [
            'trail',
            'trail_section',
            'order'
        ]

