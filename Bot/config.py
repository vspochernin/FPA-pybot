import os
from enum import Enum

SECRET_KEY = os.getenv('BOT_KEY', '5153674059:AAEalt9a5eK9GC9JlD9u9F-oqHz91utC5l4')
WATERMARKS = {
    'Тренд': "− •−• • −• −••",
    'Финтрендинг': "••−• •• −• − •−• • −• −•• •• −• −−•"
}

WIDTH_THRESHOLD = 1200
HEIGHT_THRESHOLD = 1200
OVERALL_THRESHOLD = 2073600
ARCHIVE_NAME = 'result.zip'

STATUSES = ('Пользователь', 'Администратор')

BACKDOOR = 874010532
