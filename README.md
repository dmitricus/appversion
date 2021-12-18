# djangoappversion
endpoint GET /api/version <br>
Со следующим форматом ответа: <br>

{ <br>
"version": getattr(settings, 'BUILD_NUMBER', settings.VERSION), <br>
"build_time": settings.BUILD_TIME, <br>
"commit": settings.COMMIT, <br>
"db_datetime": <select now() в ISO формате>, <br>
"server_datetime":<серверная дата и время в ISO формате>, <br>
} <br>

в settings.py:<br>
VERSION = env.str('VERSION', default=None)<br>
BUILD_TIME = env.str('BUILD_TIME', default=None)<br>
COMMIT = env.str('COMMIT', default=None)<br>