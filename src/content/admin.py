from django.contrib import admin

from content.models import Book, Podcast, UserLibrary

admin.site.register([UserLibrary, Book, Podcast])
