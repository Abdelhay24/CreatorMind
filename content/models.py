from django.db import models
from django.utils import timezone

class Idea(models.Model):
    PLATFORM_CHOICES = [
        ('TikTok', 'TikTok'),
        ('YouTube Shorts', 'YouTube Shorts'),
        ('Instagram Reels', 'Instagram Reels'),
        ('Facebook', 'Facebook'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    priority = models.IntegerField(default=0, help_text="Higher number = higher priority")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} ({self.platform})"

class Content(models.Model):
    STATUS_CHOICES = [
        ('IDEA', 'Idea'),
        ('SCRIPT', 'Script'),
        ('RECORDED', 'Recorded'),
        ('EDITED', 'Edited'),
        ('SCHEDULED', 'Scheduled'),
        ('PUBLISHED', 'Published'),
    ]

    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name='contents')
    script_text = models.TextField(blank=True)
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='IDEA')
    publish_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Content for: {self.idea.title} - {self.status}"

class MediaFile(models.Model):
    FILE_TYPE_CHOICES = [
        ('VIDEO', 'Video'),
        ('IMAGE', 'Image/Thumbnail'),
    ]

    file = models.FileField(upload_to='media_library/')
    file_type = models.CharField(max_length=20, choices=FILE_TYPE_CHOICES)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.file.name)
