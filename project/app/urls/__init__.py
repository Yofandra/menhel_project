from .url_auth import urlpatterns as auth
from .url_dashboard import urlpatterns as dashboard

urlpatterns = (
    auth 
    + dashboard
)