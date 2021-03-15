from django.contrib import admin

from .models import Scene, RelatedScene


class RelatedSceneInline(admin.StackedInline):
    model = RelatedScene
    fields = ('scene_id', 'theta')
    extra = 1


class SceneAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'id', 'name', 'image'
            ),
        }),
    )
    inlines = [RelatedSceneInline]
    list_display = ('id', 'name')
    
admin.site.register(Scene, SceneAdmin)
