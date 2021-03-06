# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class chatSession(models.Model):
    title = models.CharField(max_length=128, help_text="Session title")
    profile_name = models.CharField(max_length=128, help_text="The person's name")
    profile_url = models.URLField(help_text="The Url of the person's website")
    description = models.TextField(max_length=512, help_text="Session details")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    register_url = models.URLField(help_text="URL for the event registration")

    def __str__(self):
        return self.title
