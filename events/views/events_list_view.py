from django.shortcuts import render


def list_of_events(request):
    context_object = {}
    template_name = "events/events_list.html"
    
    return render(request, template_name=template_name, context=context_object)
