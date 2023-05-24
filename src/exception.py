import sys
from src.logger import logging



def error_message_detail(error,error_deatail:sys):
    _,_,exc_tb=error_deatail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python scirpt name [{0}] line number [{1}] error Message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))

    return error_message 
    


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_deatail=error_detail)
    def __str__(self) -> str:
        return self.error_message
    
# if __name__=="__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("divide by zero")
#         raise CustomException(e,sys)