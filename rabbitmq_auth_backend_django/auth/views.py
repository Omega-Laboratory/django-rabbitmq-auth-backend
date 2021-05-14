from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
import logging
import jwt


from decouple import config

RABBIT_LOGIN = config("RABBIT_LOGIN")
RABBIT_PASS = config("RABBIT_PASS")

with open(config("JWT_PUBLIC_KEY_PATH")) as key_file:
    SECRET_JWT_KEY = key_file.read()

logger = logging.getLogger('auth_backend')

@csrf_exempt
def user(request):
    logger.info(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    print(f"user auth: {username}")
    if username == RABBIT_LOGIN and password == RABBIT_PASS:
        return HttpResponse("allow administrator")
    return HttpResponse("allow")

@csrf_exempt
def vhost(request):
    logger.info(request.POST)
    return HttpResponse("allow")

@csrf_exempt
def resource(request):
    logger.info(request.POST)
    token = request.POST['username']
    resource = request.POST['resource']
    name = request.POST['name']
    permission = request.POST['permission']

    if token == RABBIT_LOGIN:
        return HttpResponse("allow")
    try:
        decoded_data = jwt.decode(token, key=SECRET_JWT_KEY, algorithm='RS256')
    except (jwt.DecodeError, jwt.ExpiredSignatureError, AttributeError) as e:
        print(e)
        return HttpResponse("deny")
    print("resource auth")
    if permission != "configure":
        return HttpResponse("allow")
    else:
        return HttpResponse("deny")






@csrf_exempt
def topic(request):
    logger.info(request.POST)
    return HttpResponse("allow")
