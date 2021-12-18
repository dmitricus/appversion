from datetime import datetime

from django.conf import settings
from django.db import connection
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .serializers import VersionSerializer


class VersionAPIView(APIView):
    renderer_classes = (JSONRenderer,)
    serializer_class = VersionSerializer
    authentication_classes = ()
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        version_data = {
            'version': getattr(settings, 'BUILD_NUMBER', settings.VERSION),
            'build_time': settings.BUILD_TIME,
            'commit': settings.COMMIT,
            'db_datetime': self._get_db_datetime(),
            'server_datetime': datetime.now().isoformat(),
        }

        return Response(status=status.HTTP_200_OK, data=version_data)

    @staticmethod
    def _get_db_datetime():
        with connection.cursor() as cursor:
            cursor.execute('SELECT NOW()')
            row = cursor.fetchone()
        db_datetime = row[0]
        if isinstance(db_datetime, datetime):
            db_datetime = db_datetime.isoformat()
        return db_datetime
