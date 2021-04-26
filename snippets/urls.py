from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
	path('snippets/', views.SnippetList.as_view(), name='list'),
	path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='detial'),
	path('user/', views.UserList.as_view(), name='user'),
	path('user/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
	path('', views.api_root),
	path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
]


urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]


urlpatterns = format_suffix_patterns([
	path('', views.api_root),
	path('snippets/', views.SnippetList.as_view(), 
		name='snippet-list'),
	path('snippets<int:pk>/', views.SnippetDetail.as_view(),
		name='snippet-detail'),
	path('snippets/<int:pk>/highlight/', 
		views.SnippetHighlight.as_view(),
		name='snippet-highlight'),
	path('users/', views.UserList.as_view(), 
		name='user-list'),
	path('users/<int:pk>/', views.UserDetail.as_view(),
		name='user-detail'),	
])
