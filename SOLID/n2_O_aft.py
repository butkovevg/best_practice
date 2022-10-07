# import sys
# import time
#
#
# class Logger:
#     def __init__(self):
#         self.format = '%Y-%b-%d %H:%M:%S -->'
#
#     def log(self, message):
#         prefix = time.strftime(self.format, time.localtime())
#         sys.stderr.write(f"{prefix} {message}\n")
#
#
# class CustomerLogger(Logger):
#     def __init__(self):
#         super().__init__()
#         self.format = '%Y-%b-%d ::'
#
#
# logger = Logger()
# logger.log('An error has happened!')
#
# c_logger = CustomerLogger()
# c_logger.log('Custom logged message!')

import sys
import time


class Logger:
    def log(self, message):
        current_time = time.localtime()
        sys.stderr.write(f"{time.strftime('%Y-%b-%d %H:%M:%S', current_time)} --> {message}\n")


logger = Logger()
logger.log('Logger')


class Custom_Logger(Logger):
    def log(self, message):
        current_time = time.localtime()
        sys.stderr.write(f"{time.strftime('%Y-%b-%d', current_time)} --> {message}\n")


custom_logger = Custom_Logger()
custom_logger.log('Custom_Logger')
