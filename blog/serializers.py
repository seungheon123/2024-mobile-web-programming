from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

# class PostSerializer(serializers.HyperlinkedModelSerializer):
#     author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) # add for

#     class Meta:
#         model = Post
#         fields = ('author', 'title', 'text', 'created_date', 'published_date', 'image')
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'