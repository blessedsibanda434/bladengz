from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','slug', 'updated',)
    search_fields = ('title',)
    list_filter = ('status', 'updated', 'created',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)