from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from racedayapi.models import Track, Track_Type, Series


class TrackView(ViewSet):
    """Race Day track view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single track type

        Returns:
            Response -- JSON serialized track type
        """
        try:
            tracks = Track.objects.get(pk=pk)
            serializer = TrackSerializer(tracks)
            return Response(serializer.data)
            # this is more specificvv for tests
        except Track.DoesNotExist as ex:
            #  Exception
            return Response({"Message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Handle GET requests to get all tracks

        Returns:
            Response -- JSON serialized list of tracks
        """
        tracks = Track.objects.all()
        serializer = TrackSerializer(tracks, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized track instance
        """
        tracktype = Track_Type.objects.get(pk=request.data["tracktype"])

        track = Track.objects.create(
            name=request.data["name"],
            location=request.data["location"],
            length=request.data["length"],
            turns = request.data["turns"],
            seating_capacity=request.data["seating_capacity"],
            image=request.data["image"],
            user=request.auth.user,
            tracktype=tracktype
        )
        serializer = TrackSerializer(track)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a track

        Returns:
            Response -- Empty body with 204 status code
        """

        track = Track.objects.get(pk=pk)
        track.name = request.data["name"]
        track.location = request.data["location"]
        track.length = request.data["length"]
        track.turns = request.data["turns"]
        track.seating_capacity = request.data["seating_capacity"]
        track.image = request.data["image"]
        
        tracktype = Track_Type.objects.get(pk=request.data["tracktype"])
        track.tracktype = tracktype
        track.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        track = Track.objects.get(pk=pk)
        track.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    

class TrackTrackTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track_Type
        fields = ('id', 'label', )

# class SeriesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Series
#         fields = ('id', 'name', )
    

class TrackSerializer(serializers.ModelSerializer):
    """JSON serializer for tracks
    """
    tracktype = TrackTrackTypeSerializer(many=False)

    class Meta:
        model = Track
        fields = ( 'id', 'user', 'tracktype', 'name', 'location', 'length', 'turns', 'seating_capacity', 'image' )