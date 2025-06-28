from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class GallerySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return ['gallery:index']  # Use the correct URL names

    def location(self, item):
        return reverse(item)
