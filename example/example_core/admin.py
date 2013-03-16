from django.contrib import admin
from brillixy.panels import AllModelsPanel
from example_core.models import Post, PostFile


class MyModelsPanel(AllModelsPanel):
    def app_groups(self):
        return (
            # You cal also define empty title for group
            (u"Blog", ('example_core',)),

            # With title for group
            (u"Auth & Sites", ('auth', 'sites')),
        )


class PostFileInline(admin.TabularInline):
    model = PostFile
    extra = 1

    def title(self):
        return self.instance


class PostAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'published_at', 'is_published')
    list_filter = ('is_published',)
    list_editable = ('is_published',)
    list_per_page = 20
    save_on_top = True
    date_hierarchy = 'published_at'
    inlines = [PostFileInline]

admin.site.register(Post, PostAdmin)
