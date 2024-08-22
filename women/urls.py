from django.urls import path, include
from .views import woman, woman_tag, category

app_name = 'women'

woman_urls = [
    path('', woman.WomanListView.as_view(), name='woman-list'),
    path('create/', woman.WomanCreateView.as_view(), name='woman-create'),
    path('<int:pk>/', woman.WomanDetailView.as_view(), name='woman_detail'),
]

woman_tag_urls = [
    path('<int:pk>/', woman_tag.DetailTagView.as_view(), name='woman-tag-detail'),
]

woman_category_urls = [
    path('<int:pk>/', category.ShowCategoryView.as_view(), name='woman-category-detail'),
]

urlpatterns = [
    path('', include(woman_urls)),
    path('tag/', include(woman_tag_urls)),
    path('category/', include(woman_category_urls)),
]
