from oauth2_provider.settings import oauth2_settings
from oauthlib.common import generate_token
from django.http import JsonResponse
from oauth2_provider.models import AccessToken, Application, RefreshToken
from django.utils.timezone import now, timedelta


def get_token_json(access_token):
    #Creates json format of Access Token withe refereshtoken
    token = {
        'access_token': access_token.token,
        'expires_in': oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS,
        'token_type': 'Bearer',
        'refresh_token': access_token.refresh_token.token,
        'scope': access_token.scope,
    }
    return JsonResponse(token)


def get_access_token(user): #,serializer):
    app = Application.objects.get(name="Pharmeasy")

    try:
        old_access_token = AccessToken.objects.get(
            user=user, application=app)
        old_refresh_token = RefreshToken.objects.get(
            user=user, application=app
        )
    except:
        pass
    else:
        old_access_token.delete()
        old_refresh_token.delete()

    access_token = generate_token()
    refresh_token = generate_token()
    oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS = 100000000
    expires = now() + timedelta(seconds=oauth2_settings.
                                ACCESS_TOKEN_EXPIRE_SECONDS)
    scope = "read write"
    access_token = AccessToken.objects. \
        create(user=user,
               application=app,
               expires=expires,
               token=access_token,
               scope=scope)

    RefreshToken.objects. \
        create(user=user,
               application=app,
               token=refresh_token,
               access_token=access_token)
    #serializer.save()
    return get_token_json(access_token)