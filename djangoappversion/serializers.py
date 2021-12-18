from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class VersionSerializer(serializers.Serializer):
    version = serializers.CharField(label=_('Версия'))
    build_time = serializers.DateTimeField(
        required=False,
        help_text="Дата и время создания билда.",
    )
    commit = serializers.CharField()
    db_datetime = serializers.DateTimeField(
        required=False,
        help_text="Дата и время в базе данных. Формат - ISO.",
    )
    server_datetime = serializers.DateTimeField(
        required=False,
        help_text="Серверная дата и время. Формат - ISO",
    )
