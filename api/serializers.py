from rest_framework import serializers
class FacebookSerializer(serializers.Serializer):
 id = serializers.IntegerField()
 user = serializers.CharField(max_length=100)
 followers = serializers.IntegerField()
 following = serializers.IntegerField()
 bio = serializers.CharField(max_length=200)
 likes = serializers.CharField(max_length=100)