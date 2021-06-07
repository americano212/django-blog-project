from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Post(models.Model):
    title = models.CharField(verbose_name='제목',max_length=50)
    writer = models.ForeignKey('accounts.Account', verbose_name = "WRITER", on_delete = models.CASCADE, null=True)
    slug = models.SlugField('SLUG',unique=True,allow_unicode=True)
    description = models.CharField('설명',max_length=100,blank=True)
    content = RichTextUploadingField('')
    create_dt = models.DateTimeField('CREATE DATE',auto_now_add = True)
    modify_dt = models.DateTimeField('MODIFY DATE',auto_now = True)
    tags = TaggableManager(blank=True,help_text=False)
    hit = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'
        ordering = ('-create_dt',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('board:post_detail',args=(self.slug,))

    def get_previous(self):
        return self.get_previous_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()

    @property
    def update_counter(self):
        self.hit = self.hit + 1
        self.save()
        return ''
