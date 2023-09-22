from django.contrib import admin

from audiobooks.models import Book, Podcast, UserLibrary

admin.site.register([UserLibrary, Book, Podcast])
