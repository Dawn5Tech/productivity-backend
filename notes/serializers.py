from rest_framework import serializers
from .models import Category, Note


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class NoteSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'category', 'category_name', 'created_at']

    def validate_category(self, value):
        user = self.context['request'].user

        if value and value.owner != user:
            raise serializers.ValidationError("You do not own this category!")

        return value
