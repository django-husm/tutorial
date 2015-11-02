from django.contrib import admin

from blog.models import Post, Comment

class CommentInline(admin.StackedInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')
    inlines = [
        CommentInline,
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

# Register your models here.
