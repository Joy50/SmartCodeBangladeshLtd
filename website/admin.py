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


@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('media_type', 'is_active')
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'media_type', 'order', 'is_active')
        }),
        ('Media Content', {
            'fields': ('image', 'video_url', 'description'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')
    fieldsets = (
        (None, {
            'fields': ('name', 'logo', 'order', 'is_active')
        }),
        ('Additional Info', {
            'fields': ('website', 'description'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'description', 'testimonial')
    fieldsets = (
        (None, {
            'fields': ('name', 'logo', 'order', 'is_active')
        }),
        ('Client Details', {
            'fields': ('website', 'description', 'testimonial'),
            'classes': ('collapse',)
        }),
    )