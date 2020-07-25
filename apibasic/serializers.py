from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharFiled()
    author = serializers.CharFiled()
    email = serializers.EmailFiled()
    date = serializers.DateFiled()

    def create(self, validated_data):
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)
        instance.save()

        return instance
