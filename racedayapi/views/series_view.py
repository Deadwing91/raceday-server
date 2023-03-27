"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from racedayapi.models import Series, Track



class SeriesView(ViewSet):
    """Level up series view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single series

        Returns:
            Response -- JSON serialized series
        """
        series = Series.objects.get(pk=pk)
        serializer = SeriesSerializer(series)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all series

        Returns:
            Response -- JSON serialized list of series
        """
        series = Series.objects.all()

        # if "track" in request.query_params:
        #     filteredby = request.query_params['track'][0]
        #     series = series.filter(track=filteredby)

        # for series in series:
        #     user = User.objects.get(user=request.auth.user)
        #     # Check to see if the gamer is in the attendees list on the series
        #     series.joined = user in series.name.all()

        series = Series.objects.all().order_by('name')
        serializer = SeriesSerializer(series, many=True)
        return Response(serializer.data)


            
        # serializer = SeriesSerializer(series, many=True)
        # return Response(serializer.data)
    

class SeriesSerializer(serializers.ModelSerializer):
    """JSON serializer for series
    """
    class Meta:
        model = Series
        fields = ('id', 'name', 'image')