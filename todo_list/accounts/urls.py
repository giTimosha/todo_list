from django.urls import path

from accounts.views import login_view, logout_view, register_view, UserListView, UserDetailView, \
    UserPersonalInfoChangeView, UserPasswordChangeView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', register_view, name='create'),
    path('users/', UserListView.as_view(), name='user'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('<int:pk>/update', UserPersonalInfoChangeView.as_view(), name='update'),
    path('<int:pk>/pass_change', UserPasswordChangeView.as_view(), name='password_change')
]

app_name = 'accounts'
