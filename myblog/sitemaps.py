from django.contrib.sitemaps import Sitemap
from board.models import Post
from django.urls import reverse

class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.create_dt
