from users.models import user
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['id', 'username', 'name', 'creationtime', 'userdescription']

# specific serializer for patch request as we don't want to update username
class UserPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['id', 'username', 'name', 'creationtime', 'userdescription']
        read_only_fields = ['username']
