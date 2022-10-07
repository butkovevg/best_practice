"""
Более высокоуцровневые модули не должны зависеть от низкоуровнывых, а должны зависить все от абстракций.
Абстракции не должны зависеть от деталей(Детали должны зависеть от абстракции)

НЕПРАВИЛЬНО:
класс Logger  зависит от двух класов  TerminalPrinter и FilePrinter, а должен зависеть от абстракции
и методы класса Logger: log_stderr(...) и log_file(...)

ПРАВИЛЬНО переписать эти два метода на:

    def log(self, message, notifier):
        notifier().write(f"{message}")

и вызывать, передавая классы, TerminalPrinter и FilePrinter вместо notifier
"""

import sys
import time


class TerminalPrinter:
    def write(self, msg):
        sys.stderr.write(f"{msg}\n")


class FilePrinter:
    def write(self, msg):
        with open('log.txt', 'a+', encoding='UTF8') as f:
            f.write(f"{msg}\n")


class Logger:
    def __init__(self):
        self.prefix = time.strftime('%Y-%b-%d %H:%M:%S', time.localtime())

    def log_stderr(self, message):
        TerminalPrinter().write(f"{self.prefix} {message}")

    def log_file(self, message):
        FilePrinter().write(f"{self.prefix} {message}")


logger = Logger()
logger.log_file("Starting the program...")
logger.log_stderr("An error!")
