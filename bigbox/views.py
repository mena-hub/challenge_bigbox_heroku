from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Box, Activity

def home(request):
    return render(request, "bigbox/challenge.html")

def boxes(request):
    box_list = get_list_or_404(Box)
    return render(request, "bigbox/box_list.html", {'boxes': box_list})

def box_detail(request, box_id):
    box_information = get_object_or_404(Box, id=box_id)
    return render(request, "bigbox/box_detail.html", {'box_detail': box_information})

def activities(request, box_id):
    boxes = get_list_or_404(Box, id=box_id)
    #----
    identification_number = get_object_or_404(Box, id=box_id)
    activity_list =  identification_number.activities.all().order_by("name")
    #----
    page = request.GET.get('page', 1)
    paginator = Paginator(activity_list, 20)
    try:
        activities = paginator.page(page)
    except PageNotAnInteger:
        activities = paginator.page(1)
    except EmptyPage:
        activities = paginator.page(paginator.num_pages)
    return render(request, "bigbox/activity_list.html", {'activities': activities, 'box_data': boxes})

def activity_detail(request, box_id, activity_id):
    activity_information = get_object_or_404(Activity, id=activity_id)
    return render(request, "bigbox/activity_detail.html", {'activity_detail': activity_information})

def box_detail_tag(request, slug):
    tag_information = get_list_or_404(Box)
    return render(request, "bigbox/sample.html", {'tag': tag_information})