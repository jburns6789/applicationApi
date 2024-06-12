from rest_framework import serializers


from application1.models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('name', 'email', 'education', 'accomplishments', 'work_experence', 'certifications')