from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def web_video_upload(request):
    if request.method == "POST" and request.FILES["video_file"]:
        video_file = request.FILES["video_file"]
        fs = FileSystemStorage()
        filename = fs.save('received/' + video_file.name, video_file)
        video_url = fs.url(filename)
        print(video_url)
        return render(request, "upload.html", {
            "video_url": video_url,
            "video_translation": "This is a dummy video translation"
        })
    return render(request, "upload.html")
    

@csrf_exempt
def rest_video_upload(request):
    if request.method == "POST" and request.FILES["video_file"]:
        video_file = request.FILES["video_file"]
        request_details = request.POST['request_details']
        fs = FileSystemStorage()
        filename = fs.save('received/' + video_file.name, video_file)
        video_url = fs.url(filename)
        print(video_url)
        return JsonResponse({
            "video_stored_at": video_url,
            "request_details": request_details,
            "sign_language_translation": "This is a dummy video translation",
        })
    return JsonResponse({'API_type': 'GET'})


