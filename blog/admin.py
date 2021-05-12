from django.contrib import admin

from .models import Post, AdditionalImage, Comment


class AdditionalImageInline(admin.TabularInline):
    model = AdditionalImage


class CommentInLine(admin.TabularInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    fields = (
        ('author'), 'title', 'body',
        'image', 'is_active'
    )
    inlines = (AdditionalImageInline,CommentInLine)

admin.site.register(Post, PostAdmin)