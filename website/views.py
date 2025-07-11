from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

def home(request):
    context = {
        'settings': SiteSetting.objects.first(),
        'home_page': HomePage.objects.first(),
        'services': Service.objects.all().order_by('order'),
        'features': Feature.objects.filter(show_on_homepage=True),
        'testimonials': Testimonial.objects.all(),
        'team': TeamMember.objects.all().order_by('order'),
        'projects': Project.objects.all(),
        'news_list': News.objects.order_by('-published_at')[:5],
        'careers': Career.objects.filter(is_open=True),
        'sections': {section.section_name: section for section in PageSection.objects.all()},
        'media_items': MediaItem.objects.filter(is_active=True).order_by('order'),
        'partners': Partner.objects.filter(is_active=True).order_by('order'),
        'clients': Client.objects.filter(is_active=True).order_by('order'),
    }
    return render(request, 'index.html', context)

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    context = {
        'settings': SiteSetting.objects.first(),
        'project': project,
        'sections': {section.section_name: section for section in PageSection.objects.all()},
    }
    return render(request, 'project_detail.html', context)

def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    context = {
        'settings': SiteSetting.objects.first(),
        'service': service,
        'sections': {section.section_name: section for section in PageSection.objects.all()},
    }
    return render(request, 'service_detail.html', context)

def team_member_detail(request, member_id):
    member = get_object_or_404(TeamMember, id=member_id)
    context = {
        'settings': SiteSetting.objects.first(),
        'member': member,
        'sections': {section.section_name: section for section in PageSection.objects.all()},
    }
    return render(request, 'team_member_detail.html', context)

def news_detail(request, news_id):
    news_item = get_object_or_404(News, id=news_id)
    recent_news = News.objects.exclude(id=news_id).order_by('-published_at')[:5]
    context = {
        'settings': SiteSetting.objects.first(),
        'news': news_item,
        'recent_news': recent_news,
        'sections': {section.section_name: section for section in PageSection.objects.all()},
    }
    return render(request, 'news_detail.html', context)

def career_detail(request, career_id):
    career = get_object_or_404(Career, id=career_id)
    open_positions = Career.objects.filter(is_open=True).exclude(id=career_id)
    context = {
        'settings': SiteSetting.objects.first(),
        'career': career,
        'open_positions': open_positions,
        'sections': {section.section_name: section for section in PageSection.objects.all()},
    }
    return render(request, 'career_detail.html', context)

def career_detail(request, career_id):
    career = get_object_or_404(Career, id=career_id)
    open_positions = Career.objects.filter(is_open=True).exclude(id=career_id)
    
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.career = career
            application.save()
            return redirect('application_success', career_id=career.id)
    else:
        form = ApplicationForm()
    
    context = {
        'career': career,
        'open_positions': open_positions,
        'form': form,
    }
    return render(request, 'career_detail.html', context)

def application_success(request, career_id):
    career = get_object_or_404(Career, id=career_id)
    return render(request, 'application_success.html', {'career': career})