from django.shortcuts import render, redirect
from .forms import WatchAppForm
from .models import WatchApp
from django.contrib import messages


def add_watch(request):
    form = WatchAppForm()
    if request.method == "POST":
        form = WatchAppForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Watch added successfully !')
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
        form = WatchAppForm(request.POST, request.FILES, instance=watch_obj)
        if form.is_valid():
            form.save()
            messages.warning(request, 'Watch updated successfully !')
            return redirect("display-watch")
    template_name = "watchapp/add_watch.html"
    context = {"form": form}
    return render(request, template_name, context)


def delete_watch(request, id):
    watches = WatchApp.objects.filter(id=id)
    watches.delete()
    messages.error(request, 'Watch deleted successfully !')
    return redirect("display-watch")

def aboutView(request):
    template_name = "watchapp/about.html"
    context = {}
    return render(request, template_name, context)

def contactView(request):
    template_name = "watchapp/contact.html"
    context = {}
    return render(request, template_name, context)

def faqView(request):
    template_name = "watchapp/faq.html"
    context = {}
    return render(request, template_name, context)

def servicesView(request):
    template_name = "watchapp/services.html"
    context = {}
    return render(request, template_name, context)
