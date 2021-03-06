# coding=utf-8
"""Model definitions for a trail_mapper"""
import os
import uuid as uuid_lib

from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf.global_settings import MEDIA_ROOT


__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '01/09/2018'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class Trail(models.Model):
    """Model definition of a Trail."""

    guid = models.UUIDField(
        _('GUID'),
        db_index = False,
        null = False,
        default=uuid_lib.uuid4,
        editable=False
    )

    name = models.CharField(
        _('Name of Trail'),
        max_length=255,
        help_text=_('Enter name of the Trail.')
    )

    notes = models.TextField(
        _("Notes on named Trail"),
        max_length = 300,
        null = True,
        blank = True,
        help_text = _('Enter some notes regarding the above named trail_mapper')
    )

    image = models.ImageField(
        _('Image file'),
        null=True,
        blank=True,
        upload_to=os.path.join(MEDIA_ROOT, 'images/trail_mapper'),
        help_text=_(
            'An image of the trail_mapper. '
            'Most browsers support dragging the image directly on to the '
            '"Choose File" button above.')
    )

    colour = models.CharField(
        _("Colour"),
        max_length = 255,
        null=True,
        blank = True,
        help_text = _('Enter colour hex of the trail_mapper.')
    )

    offset = models.IntegerField(
        _("Offset"),
        default=0,
        null=True,
        blank=True,
        help_text=_('Enter offset value i.e -2')
    )

    geom = models.PointField(
        dim=3,
        geography=True,
        blank=True,
        null=True,
        srid=4326
    )

    slug = models.SlugField()
    objects = models.Manager()


    def _str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return '%s' % (self.name)
