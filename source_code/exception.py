# import sys
# from source_code.logger import logging

# def error_message_detail(error,error_detail:sys):
#         _,_,exc_tb=error_detail.exc_info()
#         file_name=exc_tb.tb_frame.f_code.co_filename
        
#         error_message = "Error occured in python script name [{0}] line number [{1}] error message {error}".format(
#              file_name,exc_tb.tb_lineno,str(error)
#         )

#         return error_message
# class CustomException(Exception):

#     def __init__(self, error_message, error_detail:sys):
#         super().__init__(error_message)
#         self.error_message=error_message_detail(error_message,error_detail=error_detail)

#     def __str__(self):
#         return self.error_message

import sys
import traceback
from source_code.logger import logging

def error_message_detail(error, error_detail: sys):
    exc_type, exc_obj, exc_tb = error_detail
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in Python script name [{file_name}] line number [{line_number}] error message: {error}"
    return error_message

class CustomException(Exception):

    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
