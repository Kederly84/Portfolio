from django.contrib import admin
from blogapp.models import Blog
from django.utils.html import format_html


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'created_at')
    list_per_page = 10
    list_filter = ('title', 'created_at')
    search_fields = ('title', 'created_at')
    date_hierarchy = 'created_at'

    def slug(self, obj):
        return format_html(
            '<a href="http://127.0.0.1:8000/admin/blogapp/blog/{}/change/">{}</a>',
            obj.pk,
            obj.title
        )

    slug.short_description = 'Запись в блоге'
