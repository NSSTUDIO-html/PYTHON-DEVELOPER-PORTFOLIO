from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import base64
import os
from datetime import datetime

@csrf_exempt
def home(request):
    return render(request, 'attendance/home.html')

@csrf_exempt
def mark_attendance(request):
    if request.method == 'POST':
        data_url = request.POST.get('image')
        if data_url:
            header, image_data = data_url.split(';base64,')
            image_bytes = base64.b64decode(image_data)

            filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
            filepath = os.path.join('attendance/static/attendance_images', filename)

            with open(filepath, 'wb') as f:
                f.write(image_bytes)

            return JsonResponse({'status': 'success', 'filename': filename})
    return JsonResponse({'status': 'fail'})
