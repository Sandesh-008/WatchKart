from django.shortcuts import render, redirect
from .forms import WatchAppForm
from .models import WatchApp


def add_watch(request):
    form = WatchAppForm()
    if request.method == "POST":
        form = WatchAppForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("display-watch")
    template_name = "watchapp/add_watch.html"
    context = {"form": form}
    return render(request, template_name, context)

def display_watch(request):
    watches = WatchApp.objects.all()
    template_name = "watchapp/display_watch.html"
    context = {"watches": watches}
    return render(request, template_name, context)

def update_watch(request, id):
    watch_obj = WatchApp.objects.get(id=id)
    form = WatchAppForm(instance=watch_obj)
    if request.method == "POST":
        form = WatchAppForm(request.POST, instance=watch_obj)
        if form.is_valid():
            form.save()
            return redirect("display-watch")
    template_name = "watchapp/add_watch.html"
    context = {"form": form}
    return render(request, template_name, context)


def delete_watch(request, id):
    watches = WatchApp.objects.filter(id=id)
    watches.delete()
    return redirect("display-watch")
