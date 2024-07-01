from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import StudentClassBaseView, StudentMixinBaseView, StudentGenericBaseView, StudentViewSet, LoginView, LogoutView
from rest_framework.routers import DefaultRouter              # model view set

from rest_framework.authtoken.views import obtain_auth_token              # Token Authentication

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView         # jwt token


router = DefaultRouter()                            # model view set
router.register('studentapi', views.StudentViewSet, basename='student')            # model view set

# router.register(r'product', ProductViewSet, basename='Product')
# router.register(r'image', ImageViewSet, basename= 'Image')

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    ##################################################################################
                                # API View   CLASS BASE VIEW URL_PATH

    path('list/<int:id>/',views.StudentClassBaseView.as_view()),
    path('post/',views.StudentClassBaseView.as_view()),
    # path('delete/<int:id>/',views.StudentClassBaseView.as_view()),
    # path('put/<int:id>/',views.StudentClassBaseView.as_view()),
    # path('patch/<int:id>/',views.StudentClassBaseView.as_view()),
    # path('get_object/<int:id>/',views.StudentClassBaseView.as_view()),


    ##################################################################################
                                #    MIXIN BASE VIEW URL_PATH

    # path('list_mixin/',views.StudentMixinBaseView.as_view()),
    # path('post_mixin/',views.StudentMixinBaseView.as_view()),
    # path('delete_mixin/<int:pk>/',views.StudentMixinBaseView.as_view()),
    # path('put_mixin/<int:pk>/',views.StudentMixinBaseView.as_view()),


    ##################################################################################
                                #    GENERIC BASE VIEW URL_PATH

    path('list_generics/', views.StudentGenericBaseView.as_view()),
    path('post_generics/', views.StudentGenericBaseView.as_view()),
    # path('delete_generics/<int:pk>/', views.StudentGenericBaseView.as_view()),
    # path('put_generics/<int:pk>/', views.StudentGenericBaseView.as_view()),
    # path('get_generics/<int:pk>/', views.StudentGenericBaseView.as_view()),



    ##################################################################################
                                # MODEL VIEW SET URL_PATH
    
    # path('', include(router.urls)),

    ###############################################################################
                                  # TOKEN AUTHENTICATION

    path('auth/login/', obtain_auth_token, name = 'create token'),


    ###############################################################################
                                  # JWT TOKEN
    
    path('api/jwt_token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/jwt_token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    

    # path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    ####################################################################################################################################
                                  # FUNCTION BASE URL_PATH
    
    # path('list/',views.show_list),
    # path('create/',views.create),
    path('id_data/<int:id>/',views.get_id_data),
    path('delete/<int:id>/',views.remove_id),
    path('update/<int:id>/',views.update),
    path('partial_update/<int:id>/',views.partial_update),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)