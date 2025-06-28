from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class EventSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return ['events:index', 'events:career_guidance', 'events:annualFunction','events:sports_day','events:mock_test']  # Use the correct URL names

    def location(self, item):
        return reverse(item)
