from .url_auth import urlpatterns as auth
from .url_dashboard import urlpatterns as dashboard
from .url_emosi import urlpatterns as emosi
from .url_pemodelan import urlpatterns as pemodelan
from .url_ringkasan import urlpatterns as ringkasan
from .url_pesan import urlpatterns as pesan

urlpatterns = (
    auth 
    + dashboard
    + pesan
    + emosi
    + pemodelan
    + ringkasan
)