from django.db import models

# Create your models here.
from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from colorfield.fields import ColorField

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='site/')
    favicon = models.ImageField(upload_to='site/')
    primary_color = ColorField(default='#4e73df')
    secondary_color = ColorField(default='#1cc88a')
    dark_color = ColorField(default='#5a5c69')
    light_color = ColorField(default='#f8f9fc')
    
    def __str__(self):
        return self.site_name

class HomePage(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    background_image = models.ImageField(upload_to='home/')
    button_text = models.CharField(max_length=50)
    button_link = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class Service(models.Model):
    icon_class = models.CharField(max_length=100, help_text="Use Font Awesome or Bootstrap Icons class names")
    title = models.CharField(max_length=200)
    description = models.TextField()
    color = ColorField(default='#4e73df')
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

class Feature(models.Model):
    icon_class = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    show_on_homepage = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class Testimonial(models.Model):
    client_name = models.CharField(max_length=200)
    client_position = models.CharField(max_length=200)
    content = models.TextField()
    client_image = models.ImageField(upload_to='testimonials/')
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    
    def __str__(self):
        return self.client_name

class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    bio = models.TextField()
    image = models.ImageField(upload_to='team/')
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.name

class PageSection(models.Model):
    SECTION_CHOICES = [
    ('about', 'About Section'),
    ('services', 'Services Section'),
    ('projects', 'Projects Section'),
    ('news', 'News Section'),
    ('career', 'Career Section'),
    ('contact', 'Contact Section'),
    ('team', 'Team Section'),
    ]
    
    section_name = models.CharField(max_length=50, choices=SECTION_CHOICES, unique=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    background_color = ColorField(default='#ffffff')
    show_section = models.BooleanField(default=True)
    
    def __str__(self):
        return self.get_section_name_display()
    
class Project(models.Model):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('upcoming', 'Upcoming'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='news/')
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Career(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=100)
    posted_at = models.DateTimeField(auto_now_add=True)
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.title
