from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from event import models


def index(request):
    return HttpResponse("Hello, world. You're at the event index.")


def create(request):
    title = request.POST.get("title")
    new_event = models.Event()
    new_event.event_title = title
    new_event.save()  # ここでテーブルにデータが保存される
    return HttpResponseRedirect(reverse("event:index"))  # 画面に登録したデータのidが表示される
