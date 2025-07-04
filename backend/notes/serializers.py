from rest_framework import serializers
from .models import Note

 
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'is_important']
        read_only_fields = ['created_at', 'updated_at'] 