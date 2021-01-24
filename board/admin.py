from django.contrib import admin
from board.models import Post
# Register your models here.


@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','writer','modify_dt','tag_list','hit')
    list_filter = ('modify_dt',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug':('title',)}

    def get_queryset(self,request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self,obj):
        return ', '.join(o.name for o in obj.tags.all())
