from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('posts.urls')),
  path('profile/', include('accounts.urls')),
  path('register/', accounts_views.register, name='register'),
  path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
  path('register/', accounts_views.register, name='register'),
  path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
  path('profile-follow/', accounts_views.ProfileFollowToggle.as_view(), name='follow')
] 

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
