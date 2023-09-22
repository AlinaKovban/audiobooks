from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import (GenericForeignKey,
                                                GenericRelation)
from django.contrib.contenttypes.models import ContentType
from django.db import models


class UserLibrary(models.Model):
    user_id = models.ForeignKey(to=get_user_model(), related_name="user", on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    media = GenericForeignKey('content_type', 'object_id')


class Book(models.Model):

    class BOOK_TYPES(models.IntegerChoices):
        AUDIOBOOK = 0, "Audiobook"
        EBOOK = 1, "Ebook"

    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    publication_date = models.DateField()
    book_type = models.CharField(max_length=10, choices=BOOK_TYPES.choices)

    def __str__(self):
        return f"{self.title} ({self.author})"


class Audiobook(Book):
    audio_file_path = models.FileField(upload_to='audiobooks/')

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.title} ({self.author})"


Audiobook.user_libraries = GenericRelation(UserLibrary)


class Ebook(Book):
    file_path = models.FileField(upload_to='ebooks/')

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.title} ({self.author})"


Ebook.user_libraries = GenericRelation(UserLibrary)


class Podcast(models.Model):
    title = models.CharField(max_length=150)
    host = models.CharField(max_length=150)
    release_date = models.DateField
    audio_url = models.FileField(upload_to='podcasts/')

    def __str__(self):
        return f"{self.title} ({self.host})"


Podcast.user_libraries = GenericRelation(UserLibrary)
