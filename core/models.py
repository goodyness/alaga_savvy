from django.db import models

class RecentWork(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='recent_works/')
    description = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Client(models.Model):
    SERVICE_CHOICES = [
        ('alaga', 'Alaga Ìdúró & Ìjòkò'),
        ('letters', 'Proposal & Acceptance Letters'),
        ('consult', 'Consultation for Couples'),
        ('eru', 'Ẹrú Ìyàwó Support'),
    ]

    service_needed = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    marital_status = models.CharField(max_length=20)
    address = models.TextField()
    occupation = models.CharField(max_length=100)
    religion = models.CharField(max_length=50)
    proposed_date = models.DateField()

    bride_name = models.CharField(max_length=150)
    bride_oriki = models.CharField(max_length=255, blank=True)
    bride_occupation = models.CharField(max_length=100, blank=True)
    bride_favorite_artist = models.TextField(blank=True)
    bride_religion = models.CharField(max_length=50, blank=True)
    bride_email = models.EmailField(blank=True)

    bride_father_name = models.CharField(max_length=150, blank=True)
    bride_father_state = models.CharField(max_length=100, blank=True)
    bride_father_hometown = models.CharField(max_length=100, blank=True)
    bride_father_family_compound = models.CharField(max_length=100, blank=True)
    bride_father_occupation = models.CharField(max_length=100, blank=True)
    bride_father_religion = models.CharField(max_length=50, blank=True)
    bride_father_best_songs = models.TextField(blank=True)

    bride_mother_name = models.CharField(max_length=150, blank=True)
    bride_mother_maiden_name = models.CharField(max_length=150, blank=True)
    bride_mother_hometown = models.CharField(max_length=100, blank=True)
    bride_mother_family_compound = models.CharField(max_length=100, blank=True)
    bride_mother_occupation = models.CharField(max_length=100, blank=True)
    bride_mother_religion = models.CharField(max_length=50, blank=True)

    groom_name = models.CharField(max_length=150)
    groom_oriki = models.CharField(max_length=255, blank=True)
    groom_religion = models.CharField(max_length=50, blank=True)
    groom_occupation = models.CharField(max_length=100, blank=True)
    groom_favorite_artist = models.TextField(blank=True)

    groom_father_name = models.CharField(max_length=150, blank=True)
    groom_father_state = models.CharField(max_length=100, blank=True)
    groom_father_hometown = models.CharField(max_length=100, blank=True)
    groom_father_family_compound = models.CharField(max_length=100, blank=True)
    groom_father_occupation = models.CharField(max_length=100, blank=True)
    groom_father_favorite_artist = models.TextField(blank=True)

    groom_mother_name = models.CharField(max_length=150, blank=True)
    groom_mother_maiden_name = models.CharField(max_length=150, blank=True)
    groom_mother_state = models.CharField(max_length=100, blank=True)
    groom_mother_hometown = models.CharField(max_length=100, blank=True)
    groom_mother_family_compound = models.CharField(max_length=100, blank=True)
    groom_mother_religion = models.CharField(max_length=50, blank=True)
    groom_mother_occupation = models.CharField(max_length=100, blank=True)
    groom_mother_favorite_artist = models.TextField(blank=True)

    share_on_social_media = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.service_needed})"



class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"


class RecentWork(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class RecentWorkImage(models.Model):
    work = models.ForeignKey(RecentWork, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='recent_works/')

    def __str__(self):
        return f"Image for {self.work.title}"
    
from django.db import models
from urllib.parse import urlparse, urlunparse

class WorkVideo(models.Model):
    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
        ('tiktok', 'TikTok'),
    ]

    title = models.CharField(max_length=200)
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    video_url = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def clean_url(self):
        """
        Strip query parameters from the video URL.
        """
        parsed = urlparse(self.video_url)
        cleaned = urlunparse(parsed._replace(query=""))
        print("📦 Cleaned URL saved:", cleaned)
        return cleaned

    def save(self, *args, **kwargs):
        self.video_url = self.clean_url()
        super().save(*args, **kwargs)

    @property
    def data_id(self):
        if self.platform == "tiktok" and "video/" in self.video_url:
            try:
                return self.video_url.rstrip('/').split("video/")[-1].split("?")[0]
            except IndexError:
                return ""
        return ""

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
