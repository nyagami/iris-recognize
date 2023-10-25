import requests

from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from login.models import User, LoginHistory

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
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        with open(file_path, 'wb') as f:
            f.write(base64)
        data = {}
        try: 
            response = requests.post(
                'http://domain.com/recognize',
                data = {
                    'base64':  base64
                }
            )
            response.raise_for_status()
            data = response.json()
        except Exception as e:
            print(e)
        print(data)
        if data.get('verify'):
            user_id = data["user_id"]
            verified_user = User.objects.first(id=user_id)
            new_login = LoginHistory.objects.create(user=verified_user)
            new_login.imageUrl = settings.MEDIA_URL + file_name
            new_login.modelId = data['model_id']
            new_login.status = 'success'
            new_login.save()
            return HttpResponse(json.dumps({'success': True}), content_type='application/json')
        else:
            os.remove(file_path)
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
