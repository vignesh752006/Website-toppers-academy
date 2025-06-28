from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class AdmissionSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return ['admissions:index', 'admissions:success', 'admissions:admission_form']  # Use the correct URL names

    def location(self, item):
        return reverse(item)
