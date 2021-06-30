from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView Features"""
        an_apiview = [
            'Uses HTTP methods as functions (get,put,post,delete)',
            'Is similar to a traditional django view',
        ]
        return Response({
            "message": "Working For Now",
            "Features": an_apiview
        })
