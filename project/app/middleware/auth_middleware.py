from django.shortcuts import redirect
from django.conf import settings
from django.urls import resolve
from django.utils.deprecation import MiddlewareMixin

class LoginRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        assert hasattr(request, 'user'), "The Login Required Middleware requires authentication middleware to be installed. Edit your MIDDLEWARE setting to insert 'django.contrib.auth.middleware.AuthenticationMiddleware'."

        if not request.user.is_authenticated:
            current_url_name = resolve(request.path_info).url_name
            current_app_name = resolve(request.path_info).app_name


            if current_url_name not in ['login', 'logout']:
                return redirect('login')
