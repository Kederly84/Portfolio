from django.contrib import admin
from django.utils.html import format_html
from portfolioapp.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'created_at', 'deleted')
    list_per_page = 10
    list_filter = ('title', 'created_at', 'updated_at', 'deleted')
    search_fields = ('title', 'created_at')
    date_hierarchy = 'created_at'

    def slug(self, obj):
        return format_html(
            '<a href="http://127.0.0.1:8000/admin/portfolioapp/project/{}/change/">{}</a>',
            obj.pk,
            obj.title
        )

    slug.short_description = 'Название проекта'
