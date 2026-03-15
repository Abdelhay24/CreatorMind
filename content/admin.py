from django.contrib import admin
from .models import Idea, Content, MediaFile

@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ('title', 'platform', 'category', 'priority', 'created_at')
    list_filter = ('platform', 'category')
    search_fields = ('title', 'description')

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('get_idea_title', 'status', 'publish_date', 'created_at')
    list_filter = ('status',)
    search_fields = ('idea__title',)

    def get_idea_title(self, obj):
        return obj.idea.title
    get_idea_title.short_description = 'Idea'

@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'file_type', 'uploaded_at')
    list_filter = ('file_type',)
