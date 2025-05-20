# exception.py

import sys
import traceback
from logger import get_logger

logger = get_logger(__name__)

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = CustomException.get_detailed_error_message(error_message, error_detail)
        logger.error(self.error_message)

    @staticmethod
    def get_detailed_error_message(error_message, error_detail: sys):
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown"
        line_number = exc_tb.tb_lineno if exc_tb else "Unknown"
        return f"Error occurred in file '{file_name}' at line {line_number}: {error_message}"

    def __str__(self):
        return self.error_message
