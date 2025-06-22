from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'primary_color', 'secondary_color')
    
@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')
    
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_class', 'color', 'order')
    list_editable = ('order',)
    
admin.site.register(Service, ServiceAdmin)
admin.site.register(Feature)
admin.site.register(Testimonial)

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'order')
    list_editable = ('order',)
    
admin.site.register(TeamMember, TeamMemberAdmin)

@admin.register(PageSection)
class PageSectionAdmin(admin.ModelAdmin):
    list_display = ('section_name', 'title', 'show_section')
    list_editable = ('show_section',)

admin.site.register(Project)
admin.site.register(News)
admin.site.register(Career)
