"""View module for handling requests about track types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from racedayapi.models import Track_Type


class TrackTypeView(ViewSet):
    """Level up track types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single track type

        Returns:
            Response -- JSON serialized track type
        """
        tracktype = Track_Type.objects.get(pk=pk)
        serializer = TrackTypeSerializer(tracktype)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all track types

        Returns:
            Response -- JSON serialized list of track types
        """
        tracktypes = Track_Type.objects.all()
        serializer = TrackTypeSerializer(tracktypes, many=True)
        return Response(serializer.data)
    

class TrackTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for track types
    """
    class Meta:
            model = Track_Type
            fields = ('id', 'label')