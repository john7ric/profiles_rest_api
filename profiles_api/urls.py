from django.urls import path , include
from profiles_api import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello_viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.ProfileFeedItemViewSet)

urlpatterns = [
    path('hello/', views.UserAPIView.as_view()),
    path('login/',views.LoginApiView.as_view()),
    path('', include(router.urls))
]

