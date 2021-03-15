from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic

from .models import Scene, RelatedScene

class HomeView(generic.TemplateView):
    template_name = 'streetview/home.html'


def scene_view(request):
    context = {}
    return render(request, 'streetview/view.html', context)


def ajax_transition(request):
    scene_id = request.GET.get('id')
    scene = Scene.objects.get(id=scene_id)
    scene_image_url = scene.image.url

    relatedscene_list = RelatedScene.objects.all().filter(parent_scene=scene)
    relatedscene_id = [relatedscene.scene_id for relatedscene in relatedscene_list]
    relatedscene_theta = [relatedscene.theta for relatedscene in relatedscene_list]

    d = {
        'scene_id': scene_id,
        'scene_image_url': scene_image_url,
        'relatedscene_id': relatedscene_id,
        'relatedscene_theta': relatedscene_theta,
    }
    return JsonResponse(d)
