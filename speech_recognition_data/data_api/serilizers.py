from rest_framework import serializers
# from data_api.models import Data  


class DataSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
