from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class ResultSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return ['results:index', 'results:10th_result', 'results:12th_result']  # Use the correct URL names

    def location(self, item):
        return reverse(item)
