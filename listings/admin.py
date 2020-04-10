from django.contrib import admin
from .models import Listing

class ListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'category', 'price', 'is_published', 'list_date')
    list_display_links = ('id', 'title')
    list_filter = ('category',)
    search_fields = ('title', 'description', 'address', 'city', 'zipcode', 'state', 'price')
    list_per_page = 30

admin.site.register(Listing, ListAdmin)