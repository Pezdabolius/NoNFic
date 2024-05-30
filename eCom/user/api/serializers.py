from rest_framework import serializers
from django.contrib.auth.forms import User
from rest_framework import validators


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True},
                        'username': {'validators': [
                            validators.UniqueValidator(
                                User.objects.all(), 'The username is already exists.'
                            )
                        ]},
                        'email': {'write_only': True,
                                  'allow_blank': False,
                                  'validators': [
                                      validators.UniqueValidator(
                                          User.objects.all(), 'The email is already exists.'
                                      )
                                  ]}
                        }