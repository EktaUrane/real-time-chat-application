from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import re

def room(request, room_name):

    if not re.match(r'^[a-zA-Z0-9_]+$', room_name):
        return redirect('chat:index')
    
    context = {
        'room_name': room_name,
    }
    return render(request, 'chat/room.html', context)

def index(request):
    """Landing page for choosing a room"""
    return render(request, 'chat/index.html')

@require_http_methods(["POST"])
def join_room(request):
    """API endpoint for joining a room"""
    room_name = request.POST.get('room_name', '').strip()
    username = request.POST.get('username', '').strip()
    
    if not room_name or not re.match(r'^[a-zA-Z0-9_]+$', room_name):
        return JsonResponse({'error': 'Invalid room name'}, status=400)
    
    if not username:
        username = 'Anonymous'
    
 
    request.session['username'] = username
    
    return JsonResponse({
        'redirect_url': f'/chat/{room_name}/',
        'room_name': room_name,
        'username': username
    })