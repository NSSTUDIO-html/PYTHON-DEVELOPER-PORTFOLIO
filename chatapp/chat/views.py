from django.shortcuts import render, redirect

def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
def home(request):
    return render(request, 'chat/home.html')