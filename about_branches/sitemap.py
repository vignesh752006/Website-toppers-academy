from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class AboutBranchesSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return ['about_branches:dattanagar', 'about_branches:ambegoan', 'about_branches:narhe']  # Use the correct URL names

    def location(self, item):
        return reverse(item)
