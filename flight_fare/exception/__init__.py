import numbers
import os
import sys

class ProjectException(Exception):

    def __init__(self, error_message:Exception, error_detail:sys):
        super().__init__(error_message)
        # this error message will pass to the __init__() of Exception class.
        # above line equivalent to Exception(error_message)
        self.error_message = ProjectException.get_detailed_error_message(error_message = error_message,
                                                                        error_detail= error_detail)

    # without creating object we can call the function using staticmethod                                                                   
    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_detail:sys) -> str:
        """
            error_message: Exception object
            error_detail: object of sys module
        """
        _,_, exec_tb = error_detail.exc_info()
        '''
            exc_info() will return most recently occurred exception in three values, 
            first 2 values are not needed so mentioned as _
        '''
        exception_block_line_number = exec_tb.tb_frame.f_lineno
        try_block_line_number = exec_tb.tb_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_message = f"""
        Error occured in script: 
            [ {file_name} ] at 
            try block line number: [{try_block_line_number}] and exception block line number: [{exception_block_line_number}] 
            error message: [{error_message}]
        """
        return error_message

    def __str__(self):
        return self.error_message


    def __repr__(self) -> str:
        return ProjectException.__name__.str()



