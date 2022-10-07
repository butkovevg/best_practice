"""Принцип Open-closed (OCP) Можно расширять, но не модифицировать напрямую
Пришла задача изменить вывод логгера (убрать время)
НЕПРАВИЛЬНО: изменить уже реализованный Logger.log(...), так как может вызвать ошибки в зависимостях
ПРАВИЛЬНО: отнаследоваться от Logger для нового CustomerLogger и переопределить функционал
"""
import sys
import time


class Logger:
    def log(self, message):
        current_time = time.localtime()
        sys.stderr.write(f"{time.strftime('%Y-%b-%d %H:%M:%S', current_time)} --> {message}\n")


logger = Logger()
logger.log('An error has happened!')
