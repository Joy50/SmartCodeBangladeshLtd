from django.shortcuts import render
from .models import *

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