from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Event
# Create your views here.

@csrf_exempt

def create_event(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        event = Event.objects.create(
            name=data['name'], description=data['description'],
            location=data['location'], start_date=data['start_date'], end_date=data['end_date']
        )
        return JsonResponse({'id': str(event.id), 'message': 'Event Created!'}, status=201)

@csrf_exempt

def update_event(request, event_id):
    if request.method == 'PATCH':
        event = get_object_or_404(Event, id=event_id)
        data = json.loads(request.body)
        event.name = data.get('name', event.name)
        event.save()
        return JsonResponse({'message': 'Event Updated!'})

def get_all_events(request):
    events = list(Event.objects.values())
    return JsonResponse(events, safe=False)

def get_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return JsonResponse({'id': event.id, 'name': event.name, 'location': event.location})

@csrf_exempt

def delete_event(request, event_id):
    if request.method == 'DELETE':
        event = get_object_or_404(Event, id=event_id)
        event.delete()
        return JsonResponse({'message': 'Event Deleted!'})
