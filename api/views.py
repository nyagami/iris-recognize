from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from login.models import User

import hashlib
import json
import os

# Create your views here.

@csrf_exempt
def verify(request: HttpRequest):
    if request.method == "POST":
        blob = request.FILES.get('image')
        base64 = blob.read()
        file_name = hashlib.sha1(base64).hexdigest() + '.png'
        with open(os.path.join(settings.MEDIA_ROOT, file_name), 'wb') as f:
            f.write(base64)
        # send request to other server
        isVerify = True
        if isVerify:
            return HttpResponse(json.dumps({'success': True}), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'success': False}), content_type='application/json')
    return HttpResponseBadRequest()

def get_all_users(request):
    users = [{
        'id': user.pk,
        'fullName': user.fullName,
        'room': user.room,
        'role': user.role
    } for user in User.objects.all()]
    return HttpResponse(json.dumps(users), content_type='application/json')