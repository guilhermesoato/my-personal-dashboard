from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),  
    
    #endpoints de autenticação
    path('api/auth/', include('accounts.urls')), # Inclui a URL de registro
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # Login
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Refresh
]
