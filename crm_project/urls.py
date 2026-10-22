
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Django標準の認証URL（login, logoutなど）を 'accounts/' というパスで読み込む
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('crm_app.urls')),
]