from django.urls import path
from .views import EmployeeListView, EmployeeDetailView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView
from .views import GroupListView, GroupCreateView, GroupUpdateView, GroupDeleteView, UserGroupUpdateView
from .views import PermissionListView, PermissionCreateView, PermissionUpdateView, PermissionDeleteView

app_name = 'employees'

urlpatterns = [
    path('<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('create/', EmployeeCreateView.as_view(), name='employee-create'),
    path('<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee-delete'),

    path('groups/', GroupListView.as_view(), name='group-list'),
    path('groups/create/', GroupCreateView.as_view(), name='group-create'),
    path('groups/<int:pk>/update/', GroupUpdateView.as_view(), name='group-update'),
    path('groups/<int:pk>/delete/', GroupDeleteView.as_view(), name='group-delete'),
    path('users/<int:pk>/groups/', UserGroupUpdateView.as_view(),
         name='user-group-update'),

    path('permissions/', PermissionListView.as_view(), name='permission-list'),
    path('permissions/create/', PermissionCreateView.as_view(),
         name='permission-create'),
    path('permissions/<int:pk>/update/',
         PermissionUpdateView.as_view(), name='permission-update'),
    path('permissions/<int:pk>/delete/',
         PermissionDeleteView.as_view(), name='permission-delete'),


    path('', EmployeeListView.as_view(), name='employee-list'),
]
