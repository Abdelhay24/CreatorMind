from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Count
from django.utils import timezone
from .models import Idea, Content, MediaFile
from .forms import IdeaForm, MediaUploadForm
import json

def dashboard(request):
    ideas_count = Idea.objects.count()
    in_progress = Content.objects.exclude(status='PUBLISHED').count()
    scheduled = Content.objects.filter(status='SCHEDULED').count()
    published = Content.objects.filter(status='PUBLISHED').count()
    
    next_to_publish = Content.objects.filter(status='SCHEDULED').order_by('publish_date').first()
    
    context = {
        'ideas_count': ideas_count,
        'in_progress': in_progress,
        'scheduled': scheduled,
        'published': published,
        'next_to_publish': next_to_publish,
    }
    return render(request, 'content/dashboard.html', context)

def idea_list(request):
    ideas = Idea.objects.all().order_by('-priority', '-created_at')
    return render(request, 'content/idea_list.html', {'ideas': ideas})

def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = form.save()
            # Automatically create a Content item for pipeline
            Content.objects.create(idea=idea, status='IDEA')
            return redirect('idea_list')
    else:
        form = IdeaForm()
    return render(request, 'content/idea_form.html', {'form': form, 'title': 'Create Idea'})

def idea_edit(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == 'POST':
        form = IdeaForm(request.POST, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('idea_list')
    else:
        form = IdeaForm(instance=idea)
    return render(request, 'content/idea_form.html', {'form': form, 'title': 'Edit Idea'})

def idea_delete(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == 'POST':
        idea.delete()
        return redirect('idea_list')
    return render(request, 'content/idea_confirm_delete.html', {'idea': idea})

def pipeline(request):
    contents = Content.objects.select_related('idea').all()
    # Group by status
    pipeline_data = {status[0]: [] for status in Content.STATUS_CHOICES}
    for content in contents:
        pipeline_data[content.status].append(content)
        
    context = {
        'pipeline_data': pipeline_data,
        'statuses': Content.STATUS_CHOICES
    }
    return render(request, 'content/pipeline.html', context)

@require_POST
def update_content_status(request):
    try:
        data = json.loads(request.body)
        content_id = data.get('content_id')
        new_status = data.get('new_status')
        
        content = get_object_or_404(Content, pk=content_id)
        valid_statuses = [s[0] for s in Content.STATUS_CHOICES]
        
        if new_status in valid_statuses:
            content.status = new_status
            content.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'error': 'Invalid status'}, status=400)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)

def calendar_view(request):
    # Get all scheduled/published content that has a date
    scheduled_contents = Content.objects.filter(publish_date__isnull=False).order_by('publish_date')
    return render(request, 'content/calendar.html', {'scheduled_contents': scheduled_contents})

def media_library(request):
    media_files = MediaFile.objects.all().order_by('-uploaded_at')
    return render(request, 'content/media_library.html', {'media_files': media_files})

def media_upload(request):
    if request.method == 'POST':
        form = MediaUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('media_library')
    else:
        form = MediaUploadForm()
    return render(request, 'content/media_form.html', {'form': form})
